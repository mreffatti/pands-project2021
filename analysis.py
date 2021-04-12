#Author: Marcelo Reffatti


#analysis iris.csv
import pandas as pd
import numpy as np
import collections as cl
import matplotlib.pyplot as plt

# load data file
data_file = pd.read_csv('iris.csv')

# calculate
avg = str(np.mean(data_file))
cnt = str(cl.Counter(data_file['species']))

#saving txt file
filetxt = open('summary.txt', 'w')
filetxt.write("\n" + cnt + "\n")
filetxt.write("Averages:" + "\n")
filetxt.write(avg)
filetxt.close()

#species filter
setosa = data_file.loc[data_file['species'] == 'setosa']
versicolor = data_file.loc[data_file['species'] == 'versicolor']
virginica = data_file.loc[data_file['species'] == 'virginica']

#histogram
setosa.hist()
plt.suptitle('Setosa', fontsize=20,fontweight="bold")
plt.savefig('histogram_setosa.png')
versicolor.hist()
plt.suptitle('Versicolor', fontsize=20,fontweight="bold")
plt.savefig('histogram_versicolor.png')
virginica.hist()
plt.suptitle('Virginica', fontsize=20,fontweight="bold")
plt.savefig('histogram_virginica.png')
data_file.hist()
plt.savefig('histogram.png')

# scatter plot
data_file.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset - SEPALS')
data_file.plot.scatter(x='petal_length', y='petal_width', title='Iris Dataset - PETALS')
plt.show()

