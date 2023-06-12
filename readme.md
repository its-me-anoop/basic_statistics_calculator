# Basic Statistics Calculator

This Python script allows users to input a list of numbers, separated by space or comma, and performs basic statistical calculations on it. The script calculates the minimum value, maximum value, mean, median, mode, sample variance, sample standard deviation, variance, standard deviation, first quartile (Q1), third quartile (Q3), and the interquartile range (IQR) of the numbers.

## Prerequisites

To use this script, you need to have Python installed on your machine along with the `statistics` library.

## Usage

To use the script, follow the steps below:

1. Run the script using Python.

2. You'll be prompted to input a list of numbers. Enter the numbers separated by spaces or commas. For example: `1 2 3 4 5 6 7 8 9` or `1,2,3,4,5,6,7,8,9`.

3. After the data has been entered, the script will perform the statistical calculations and print the results.

## Error Handling

This script comes with built-in error handling. If an invalid input is detected, such as a non-numeric value, you will be notified with the message "Invalid input. Please enter a list of numbers separated by space or comma". The script will then prompt you to re-enter the list of numbers.

There are also error handling mechanisms for statistics-related errors and general exceptions. If a statistics-related error occurs, you'll see "Error in statistical calculation. Check if the input data is sufficient". For other types of errors, you'll see "An error occurred: ", followed by the error message.

## Features

The script is capable of calculating the following statistical measures:

- Minimum value
- Maximum value
- Mean
- Median
- Mode
- Sample Variance
- Sample Standard Deviation
- Variance
- Standard Deviation
- Q1 (First Quartile)
- Q3 (Third Quartile)
- IQR (Interquartile Range)

## Contributions

Your contributions are always welcome. If you have any ideas for improvements, feel free to open an issue or create a pull request.

## License

This project is open-source and available under the MIT License.
