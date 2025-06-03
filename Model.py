from math import sqrt
from csv import reader
from random import randrange
import matplotlib.pyplot as plt

def plot(train, test, predicted):
    train_x = [row[0] for row in train]
    train_y = [row[1] for row in train]

    test_x = [row[0] for row in test]
    test_y = [row[1] for row in test]

    B0, B1 = coefficients(train)
    x_line = sorted([row[0] for row in train + test])
    y_line = [B0 + B1 * x for x in x_line]

    plt.scatter(train_x, train_y, color='Blue', label='Training')
    plt.scatter(test_x, test_y, color='Green', label='Test')
    plt.scatter(test_x, predicted, color='Purple', marker='x', label='Predicted')
    plt.plot(x_line, y_line, color='Red', label='Regression Line', linestyle='dashed')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()

def load_file(filename):
    dataset = list()
    with open(filename, "r") as file:
        csv = reader(file)
        for row in csv:
            if not row:
                continue
            dataset.append(row)
    return dataset

def str_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def train_test_split(dataset, split):
    train = list()
    train_size = split * len(dataset)
    dataset_cpy = list(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_cpy))
        train.append(dataset_cpy.pop(index))
    return train, dataset_cpy

def mean(values):
    return sum(values) / len(values)

def variance(values, ave):
    return sum((x - ave)**2 for x in values)

def covariance(x_list, x_ave, y_list, y_ave):
    return sum((x - x_ave) * (y - y_ave) for x, y in zip(x_list, y_list))

def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_ave = mean(x)
    y_ave = mean(y)
    B1 = covariance(x, x_ave, y, y_ave) / variance(x, x_ave)
    B0 = y_ave - B1 * x_ave
    return [B0, B1]

def linear_regression(train, test):
    predictions = list()
    B0, B1 = coefficients(train)
    for row in test:
        predicted_y = B0 + B1 * row[0]
        predictions.append(predicted_y)
    return predictions

def rmse(actual, predicted):
    sum_total = 0.0
    for i in range(len(actual)):
        diff = predicted[i] - actual[i]
        sum_total += (diff ** 2)
    mean_error = sum_total / float(len(actual))
    return sqrt(mean_error)

def evaluate(dataset, algorithm, split):
    train, test = train_test_split(dataset, split)
    predicted = linear_regression(train, test)
    actual = [row[1] for row in test]
    error = rmse(actual, predicted)
    print(f"predict: {predicted}")
    print(f"actual: {actual}")
    plot(train, test, predicted)
    return error


def main():
    dataset = load_file("dataset.csv")
    for i in range(len(dataset[0])):
        str_to_float(dataset, i)
    split = 0.6
    rmse = evaluate(dataset, linear_regression, split)
    print(f"RMSE: {rmse:.3f}")

if __name__ == "__main__":
    main()

