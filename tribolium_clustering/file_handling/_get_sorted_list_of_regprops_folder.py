# get list of saved regionprops with time index at the end
def get_sorted_list_of_regprops_folder(folderpath, filename_prefix, n_timepoints):
    import pandas as pd
    filelist = [folderpath+filename_prefix+str(i)+'.csv' for i in range(n_timepoints)]
    
    regpropslist = []

    for propname in filelist:
        try:
            regpropslist.append(pd.read_csv(propname))
        except FileNotFoundError:
            pass

    regpropslist = [pd.read_csv(i) for i in filelist]
    try:
        regpropslist = [i.drop('Unnamed: 0', axis = 1) for i in regpropslist]
    except:
        print('No Labels in Regionprops of {}'.format(folderpath))
    try:
        regpropslist = [i.drop('prediction', axis = 1) for i in regpropslist]
    except:
        print('No Predictions in Regionprops of {}'.format(folderpath))
    
    if regpropslist == []:
        print('No FIles Opened')
    
    else:
        return regpropslist