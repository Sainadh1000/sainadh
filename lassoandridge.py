from sklearn.linear_model import Lasso,Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt


x = np.array([10,20,30,40,50,56,78,89,102,145]).reshape(-1,1)
y = np.array([103,345,455,500,678,900,1423,1678,2021,2761])

scaler=StandardScaler()
x_scale=scaler.fit_transform(x)
ridge=Ridge(alpha=10)
ridge.fit(x_scale,y)

y_pred_ridge=ridge.predict(x_scale)
print("ridgecoffecient:", ridge.coef_)
print("ridge intercept:", ridge.intercept_)
print("Ridge MSE:", mean_squared_error(y, y_pred_ridge))
plt.scatter(x, y, label="Actual")
plt.plot(x, y_pred_ridge, label="Ridge")
plt.legend()
plt.title("Ridge Regression")
plt.show()


lasso=Lasso(alpha=10)
lasso.fit(x_scale,y)
y_pred_lasso=lasso.predict(x_scale)
print("Lasso Coefficient:", lasso.coef_)
print("Lasso Intercept:", lasso.intercept_)
print("Lasso MSE:", mean_squared_error(y, y_pred_lasso))

plt.scatter(x, y, label="Actual")
plt.plot(x, y_pred_lasso, label="Lasso")
plt.legend()
plt.title("Lasso Regression")
plt.show()
