import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        # layer_sizes e.g. [3, 4, 2] = 3 inputs, 4 hidden, 2 outputs
        self.weights = []
        self.biases = []
        for i in range(len(layer_sizes) - 1):
            W = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * 0.1
            b = np.zeros((1, layer_sizes[i+1]))
            self.weights.append(W)
            self.biases.append(b)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        s = self.sigmoid(x)
        return s * (1 - s)

    def forward(self, X):
        self.activations = [X]
        self.z_values = []

        for W, b in zip(self.weights, self.biases):
            z = self.activations[-1] @ W + b   # weighted sum
            self.z_values.append(z)
            self.activations.append(self.sigmoid(z))  # activation

        return self.activations[-1]

    def loss(self, y_pred, y_true):
        # Mean squared error
        return np.mean((y_pred - y_true) ** 2)

    def backward(self, X, y_true, learning_rate=0.1):
        m = X.shape[0]
        y_pred = self.activations[-1]

        # Start with output layer error
        delta = 2 * (y_pred - y_true) / m * self.sigmoid_derivative(self.z_values[-1])

        # Walk backwards through layers
        for i in reversed(range(len(self.weights))):
            dW = self.activations[i].T @ delta
            db = np.sum(delta, axis=0, keepdims=True)

            if i > 0:
                delta = delta @ self.weights[i].T * self.sigmoid_derivative(self.z_values[i-1])

            # Update weights and biases
            self.weights[i] -= learning_rate * dW
            self.biases[i]  -= learning_rate * db

    def train(self, X, y, epochs=1000, learning_rate=0.1):
        for epoch in range(epochs):
            y_pred = self.forward(X)
            self.backward(X, y, learning_rate)

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {self.loss(y_pred, y):.4f}")


# --- Try it on XOR (the classic test) ---
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0],   [1],   [1],   [0]])   # XOR output

nn = NeuralNetwork([2, 4, 1])   # 2 inputs → 4 hidden → 1 output
nn.train(X, y, epochs=5000, learning_rate=1.0)

print("\nPredictions:")
print(nn.forward(X).round(2))