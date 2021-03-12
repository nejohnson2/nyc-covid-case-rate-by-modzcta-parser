''' Parse git history to get historical case-rate data

This code is intended to be run inside a Jupyter Notebook.  I'm not
sure if running !git rev-list master will work outside of a notebook.

by Nicholas Johnson
'''
import re
import glob
import pandas as pd

def search_folder(date):
    """Search current diretory for data-by-modzcta file"""
    fpath = glob.glob('**/data-by-modzcta.csv', recursive=True)[0]
    print(fpath)
    df = pd.read_csv(fpath)
    df['date'] = pd.to_datetime(date).strftime('%Y-%m-%d')[0]
    return df
  
# -- get all commits
commit_history = !git rev-list master

current_date = ''
data = []
for commit in commit_history:
    
    # -- List all commit messages
    message = !git log --format=%B -n 1 {commit}

    # -- find dates in messages
    result = re.findall('(\d{1,}[\/]\d{1,})', message[0])

    #
    if len(result) > 0:
        if (result[0] != current_date) & (result[0] != '12/09'):
            current_date = result[0]
                
            #print(result[0], current_date, commit, message)

            # -- go to previous commit
            !git checkout {commit}

            # -- get date of commit
            datestamp = !git show -s --format=%ci {commit}

            if pd.to_datetime(datestamp).date[0] >= pd.to_datetime(['2020-05-18']).date[0]:

                # -- search for data-by-modzcta file
                df = search_folder(datestamp)

                !git checkout master
            else:
                !git checkout master
                break

            if df.shape[0] == 177:
                data.append(df)
            else:
                print('BAD DATAFRAME')
                
data = pd.concat(data)
