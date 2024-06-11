import numpy as np


def demonstrate_numpy():
    # Create a 1D array
    array_1d = np.array([1, 2, 3, 4, 5])
    print("1D Array:", array_1d)

    # Create a 2D array
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D Array:\n", array_2d)

    # Basic operations
    array_sum = array_1d + 5
    print("1D Array after adding 5:", array_sum)

    # Matrix multiplication
    matrix_mult = np.dot(array_2d, array_2d.T)
    print("Matrix multiplication result:\n", matrix_mult)

    # Generating random data
    random_data = np.random.rand(5, 5)
    print("Random data:\n", random_data)

    # Mean and standard deviation
    mean_value = np.mean(random_data)
    std_deviation = np.std(random_data)
    print("Mean of random data:", mean_value)
    print("Standard deviation of random data:", std_deviation)

    # Reshaping arrays
    reshaped_array = random_data.reshape((25,))
    print("Reshaped array:", reshaped_array)

    # Broadcasting
    broadcast_array = array_1d + np.array([10])
    print("Broadcasted addition result:", broadcast_array)

    # Element-wise operations
    elementwise_mult = array_1d * array_1d
    print("Element-wise multiplication:", elementwise_mult)

    # Using NumPy for a simple AI-related task: normalizing data
    data = np.array([15, 20, 35, 40, 50])
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    print("Original data:", data)
    print("Normalized data:", normalized_data)

if __name__ == "__main__":
    demonstrate_numpy()
