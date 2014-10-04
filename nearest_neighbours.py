import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import NearestCentroid
import pandas as pd
from pandas import read_table


# import some data to play with

data = read_table('fractals.csv',sep=',')
names = data.type.tolist()

X = data.ix[0:19,"Voltage(V)":"Concentration(M)"].astype(float)
h = .1  # step size in the mesh
y = []
for value in names:
    if value == 'dense':
        y.append(0)
    if value == 'dendritic':
        y.append(1)
    if value == 'branch':
        y.append(2)
    if value == 'spikey':
        y.append(3)
Y = np.array(y)
print y


# Create color maps
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets


h = .005  # step size in the mesh

logreg = linear_model.LogisticRegression(C=1e5)

# we create an instance of Neighbours Classifier and fit the data.
logreg.fit(X, Y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = 0,26
y_min, y_max = 0,1.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
print xx
X = pd.DataFrame(X)
# Plot also the training points

plt.scatter( X['Voltage(V)'],X['Concentration(M)'], c=Y, edgecolors='k', cmap=plt.cm.Paired,s = 200,zorder = 10)
plt.xlabel('Voltage (V)')
plt.ylabel('Concentration (M)')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())


plt.savefig('classes',bbox_inches='tight')