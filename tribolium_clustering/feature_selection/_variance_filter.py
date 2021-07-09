def variance_filter(df_regprops, threshold = 0.01, print_variances = False):
    from sklearn.feature_selection import VarianceThreshold
    import pandas as pd
    
    keys = df_regprops.keys().tolist()
    
    selector = VarianceThreshold(threshold = threshold)
    
    filtered = selector.fit_transform(df_regprops)
    
    variances = selector.variances_
    filtered_keys_and_idx = [(key,i) for i, key in enumerate(keys) if variances[i] < threshold]
    
    if print_variances:
        for i, key in enumerate(keys):
            print(key + ' has var: {}'.format(variances[i]))
    
    for fkey,i in filtered_keys_and_idx:
        print(fkey + ' was filtered out with a variance of {}'.format(variances[i]))
        keys.remove(fkey)   
    
    
    return pd.DataFrame(filtered,columns = keys)