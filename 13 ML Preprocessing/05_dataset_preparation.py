import numpy as np 

data = np.array([10, 20, np.nan, 40, 50])

#Fill missing value with the mean
data[np.isnan(data)] = np.nanmean(data)

#Normalize
data = (data - data.min())/(data.max() - data.min())

print(data)


# np.nanmean()
# np.nansum()
# np.nanmin()
# np.nanmax()
# np.nanstd()
# np.nanvar()
# These functions ignore np.nan values.