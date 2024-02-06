from utilities.csv import to_matrix
import random
import numpy as np


class Neuron:
    def __init__(self, csv_path, eta, tolerance, iterations):
        self.eta = eta,
        self.tolerance = tolerance
        self.iterations = iterations
        self.csv_path = csv_path

    def training(self):
        dataset = to_matrix(self.csv_path)
        matrix = np.insert(np.array(dataset), 0, 1, axis=1)
        print(matrix)
        yd = np.array(matrix[:, -1]).reshape(-1, 1).astype(int)
        w = generate_w(matrix)
        errors = []
        w_by_iterations = [w]

        for _ in range(self.iterations):
            u = get_u(w, matrix)
            yc = activation_function(u)
            e = calculate_error(yd, yc)
            delta_w = calculate_delta_w(self.eta, e, matrix)
            errors.append(calculate_norm(e))
            w = update_w(w, delta_w)
            w_by_iterations.append(w)

        return errors, w_by_iterations


def generate_w(matrix):
    return np.random.random((1, matrix.shape[1] - 1))


def get_u(w, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    return np.dot(x, w.T)


def activation_function(u):
    return np.where(u >= 0, 1, 0).astype(int)


def calculate_error(yd, yc):
    return yd - yc


def calculate_norm(e):
    return np.linalg.norm(e)


def calculate_delta_w(eta, e, matrix):
    x = matrix[:, :(matrix.shape[1] - 1)]
    # return (-eta) * np.dot(e.T, x)
    return eta * np.dot(e.T, x)


def update_w(w, delta_w):
    return w + delta_w


