import numpy as np
import matplotlib.pyplot as plt
from preprocessing.polynomial_features import PolynomialFeatures

x = np.array([i*np.pi/180 for i in range(60,300,4)])
np.random.seed(10)  #Setting seed for reproducibility
y = 4*x + 7 + np.random.normal(0,3,len(x))

x = np.array([i*np.pi/180 for i in range(60,300,4)])
np.random.seed(10)  #Setting seed for reproducibility
y = 4*x + 7 + np.random.normal(0,3,len(x))

print(y)
X = [7,4]

regX = PolynomialFeatures()

REG_X = regX.transform(y)

print(REG_X)

REG_Y = REG_X[0] + REG_X[1]*x

style.use('ggplot') 
plt.plot(x,y,'g',label='original',linewidth=5)
plt.plot(x,REG_Y,'c',label='fitted',linewidth=5)
plt.title('Data')
plt.xlabel('Degree')
plt.ylabel('Theta')

plt.legend()
plt.grid(True,color='k')

plt.show()
