#Agglomerative кластеризация
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=200,
                  noise=0.05,
                  random_state=0)
db = DBSCAN(eps=0.2,
            min_samples=5,metric='euclidean')
y_db = db.fit_predict(X)
plt.scatter(X[y_db==0,0],
            X[y_db==0,1],
            c='lightblue',
            marker='o',
            s=40,
            edgecolors='black',
            label='кластер 1')
plt.scatter(X[y_db==1,0],
            X[y_db==1,1],
            c='red',
            marker='s',
            s=40,
            edgecolors='black',
            label='кластер 2')
plt.legend()
plt.show()