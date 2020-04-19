import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
iris = pd.read_csv('C:\\Users\\Duddupuditeja\\Desktop\\iris.csv')
iris.head()
iris.corr()
iris_corr_data = iris.corr()
ax = sns.heatmap(iris_corr_data,annot=True) #annot will gve vals in cells
ax = sns.heatmap(iris_corr_data, vmin=0, vmax=1)

ax = sns.heatmap(iris_corr_data, center=0)

from string import ascii_letters

sns.set(style="white")

# Compute the correlation matrix
corr = iris.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})






