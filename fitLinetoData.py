# import libraries

import numpy as np

from scipy.stats import linregress

import matplotlib.pyplot as plt

#----------

# obtain data and fit it using linear regression

# request data from user
dataList = []
while True:
	userInput = raw_input('enter coordinate pair (comma-separated); type "stop" when finished: ')
	if userInput == 'stop':
		break

	dataList.append([float(i) for i in userInput.split(',')])

# transform list of data into array
dataArr = np.array(dataList)

# fit the data
fitResults = linregress(dataArr)
print '\nFIT RESULTS'
print 'function: Ax + By = C'
print 'fit parameters: A = %.3f, B = 1.0, C = %.3f' % (-fitResults[0], fitResults[1])
print 'Pearson coefficient: %.3f' % (fitResults[2])

#----------

# plot the data and the fit

fig = plt.figure()
ax1 = plt.subplot(111)

# data
ax1.scatter(dataArr[:, 0], dataArr[:, 1], c = 'k', zorder = 2)

# fit
y_fit = fitResults[0] * dataArr[:, 0] + fitResults[1]
ax1.plot(dataArr[:, 0], y_fit, zorder = 1)

# include fitted parameters
text = 'fit: %.3fx + y = %.3f' % (-fitResults[0], fitResults[1])
x = ax1.get_xlim()[0] + 0.05 * (ax1.get_xlim()[1] - ax1.get_xlim()[0])
y = ax1.get_ylim()[1] - 0.1 * (ax1.get_ylim()[1] - ax1.get_ylim()[0])
ax1.text(x, y, text)

plt.show()
