import statistics


def get_data():
    """
    Prompt the user for a list of numbers separated by space or comma.
    Returns a list of those numbers.

    Invalid inputs are handled by re-prompting the user.
    """
    while True:
        try:
            numbers_input = input(
                "Enter a list of numbers (separated by space or comma): "
            )
            numbers_input = numbers_input.replace(
                ",", " "
            )  # Replace commas with spaces
            numbers_list = numbers_input.split()
            data = [int(num) for num in numbers_list]
            return data
        except ValueError:
            print(
                "Invalid input. Please enter a list of numbers separated by space or comma."
            )


# Get data from the user
data = get_data()

# Sort the data for accurate statistics calculation
data.sort()

try:
    # Calculate various statistical values from the data
    minimum_value = data[0]
    maximum_value = data[-1]
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.multimode(data)
    sample_variance = statistics.variance(data)
    sample_standard_deviation = statistics.stdev(data)
    variance = statistics.pvariance(data)
    standard_deviation = statistics.pstdev(data)

    # Calculate quartiles
    if len(data) % 2 == 0:
        q1 = statistics.median(data[: int(len(data) / 2)])
        q3 = statistics.median(data[int(len(data) / 2) :])
    else:
        q1 = statistics.median(data[: int(len(data) / 2)])
        q3 = statistics.median(data[int(len(data) / 2) + 1 :])

    iqr = q3 - q1

    # Print the results
    print("\n" + "*" * 45)
    print(f"sorted data: {data}")
    print(f"minumum value: {minimum_value}")
    print(f"maximum value: {maximum_value}")
    print(f"mean: {mean}")
    print(f"median: {median}")
    print(f"mode: {mode}")
    print(f"sample variance: {sample_variance}")
    print(f"sample standard deviation: {sample_standard_deviation}")
    print(f"variance: {variance}")
    print(f"standard deviation: {standard_deviation}")
    print(f"q1: {q1}")
    print(f"q3: {q3}")
    print(f"IQR: {iqr}")
    print("*" * 45 + "\n")

except statistics.StatisticsError:
    # Handle statistical errors
    print("Error in statistical calculation. Check if the input data is sufficient.")
except Exception as e:
    # Handle any other errors
    print(f"An error occurred: {str(e)}")
