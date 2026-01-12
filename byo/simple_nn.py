# %%
import numpy as np
import matplotlib.pyplot as plt


# Sigmoid activation function
def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


x = np.linspace(-10, 10, 400)
y = [nonlin(xi) for xi in x]

plt.plot(x, y)
plt.title("Sigmoid Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# %%

# Input dataset
X = np.array(
    [
        inputs0 := [0, 0, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
)

# Output dataset
y = np.array([[0, 0, 1, 1]]).T

# Seed random numbers to make calculation deterministic (just a good practice)
np.random.seed(1)

# Initialize weights randomly with mean 0
syn0 = 2 * np.random.random((len(inputs0), 1)) - 1

for iter in range(10000):
    # Forward propagation
    l0 = X  # First layer: input layer
    l1 = nonlin(np.dot(l0, syn0))  # Second layer: hidden layer

    # Calculate the error
    l1_error = y - l1

    if iter % 1000 == 0:
        print("Error:" + str(np.mean(np.abs(l1_error))))

    # Backpropagation
    l1_delta = l1_error * nonlin(l1, deriv=True)

    # Update weights
    syn0 += np.dot(l0.T, l1_delta)

print("Output after training:")
print(l1)

print("Error after training:")
print(l1_error)

print("Weights after training:")
print(syn0)

print("Input to Output")
for i in range(len(X)):
    print(f"{X[i]} -> {y[i]}")

print(
    "The first neuron (input) is strongly correlated with the output. Hence, the first weight syn0[0] has the highest magnitude."
)
