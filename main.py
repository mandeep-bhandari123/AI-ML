import matplotlib.pyplot as plt
import numpy as np
# Use your custom style
plt.style.use("./deeplearning.mplstyle")

x_train = np.array([1.0, 2.0])
y_train = np.array([300, 500])
m = len(x_train)
print(f"Number of traning example is: {m}")