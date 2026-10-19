import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    if strategy == "mean":
        idx = np.isnan(data)
        data = np.where(idx==True, [np.nanmean(data, axis=0) for _ in range(len(data))], data)

    if strategy == "mode":
        for i in range(data.shape[1]):
            clean = data[:,i][~np.isnan(data[:,i])]
            vals, counts = np.unique(clean, return_counts=True)
            data[:,i][np.isnan(data[:,i])] = vals[np.argmax(counts)]

    else:
        for i in range(data.shape[1]):
            col = data[:,i]
            clean = col[~np.isnan(col)]
            col[np.isnan(col)] = np.median(clean)
            
    return data