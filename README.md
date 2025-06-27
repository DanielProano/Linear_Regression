![Linear_Regression_Algorithm](https://github.com/user-attachments/assets/f2260097-8f01-4b04-983b-a7c5eb3e95b1)

# Linear Regression from Scratch

In this project, I recreated linear regression from scratch, calculating the line of best fit from training data

and applying that to a graph of points. The line of best fit is calculated by solving the least squares problem.

## Setup

The load_file, str_to_float, and train_test_split functions act as a setup, taking in a file with

data coordinates and turning them into two lists: one of training data and the next of test data.

## Problem

Usually, a line of best fit can be eye-balled and guessed visually. But to programmatically and mathematically 

find the line of best fit, it's not so easy. To solve, we need to solve the least squares problem.

## Calculations

The line of best fit is some line: y = mx + b. We need to find the line that minimizes the total

squared distance between the y values and their predicted ones. We can accomplish this

by solving for the optimal slope and y intercepts. To do this, we need the mean, variance, and

covariance to then plug into our equation.

$$ m = covariance / variance $$

$$ b = \text{y axis average} - m * \text{x axis average} $$

## Data Visualization

I then visualized the data using MatPlotLib to show the results of the line of best fit

against the rest of the data, color coding to visualize the training versus the test data.
