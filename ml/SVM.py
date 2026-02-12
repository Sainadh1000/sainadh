import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris

data = load_iris()
x = data.data[:, :2]
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train SVM model
svm_clf = SVC(kernel="rbf", gamma=0.5, C=1)
svm_clf.fit(x_train, y_train)

# Create meshgrid
xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 300),
    np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 300)
)

# Predict on meshgrid
z = svm_clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, z, alpha=0.3, cmap="coolwarm")
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="coolwarm", edgecolors="k")
plt.title("SVM Decision Boundary (RBF Kernel) on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris

data = load_iris()
x = data.data[:, :2]
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train SVM model
svm_clf = SVC(kernel="poly", gamma=0.5, C=1)
svm_clf.fit(x_train, y_train)

# Create meshgrid
xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 300),
    np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 300)
)

# Predict on meshgrid
z = svm_clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, z, alpha=0.3, cmap="coolwarm")
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="coolwarm", edgecolors="k")
plt.title("SVM Decision Boundary (RBF Kernel) on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()




import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris

data = load_iris()
x = data.data[:, :2]
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train SVM model
svm_clf = SVC(kernel="linear", gamma=0.5, C=1)
svm_clf.fit(x_train, y_train)

# Create meshgrid
xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 300),
    np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 300)
)

# Predict on meshgrid
z = svm_clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, z, alpha=0.3, cmap="coolwarm")
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="coolwarm", edgecolors="k")
plt.title("SVM Decision Boundary (RBF Kernel) on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris

data = load_iris()
x = data.data[:, :2]
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train SVM model
svm_clf = SVC(kernel="rbf", gamma=0.5, C=2)
svm_clf.fit(x_train, y_train)

# Create meshgrid
xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 300),
    np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 300)
)

# Predict on meshgrid
z = svm_clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, z, alpha=0.3, cmap="coolwarm")
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="coolwarm", edgecolors="k")
plt.title("SVM Decision Boundary (RBF Kernel) on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris

data = load_iris()
x = data.data[:, :2]
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train SVM model
svm_clf = SVC(kernel="rbf", gamma=0.5, C=3)
svm_clf.fit(x_train, y_train)

# Create meshgrid
xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min() - 1, x[:, 0].max() + 1, 300),
    np.linspace(x[:, 1].min() - 1, x[:, 1].max() + 1, 300)
)

# Predict on meshgrid
z = svm_clf.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, z, alpha=0.3, cmap="coolwarm")
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="coolwarm", edgecolors="k")
plt.title("SVM Decision Boundary (RBF Kernel) on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()