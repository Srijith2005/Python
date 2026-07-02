def count_even(nums):
    """Return the number of even values in nums."""
    return sum(1 for num in nums if num % 2 == 0)


def find_largest(nums):
    """Return the largest value in nums."""
    if not nums:
        raise ValueError("nums must not be empty")
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest


def count_positive(nums):
    """Return the number of positive values in nums."""
    return sum(1 for num in nums if num > 0)


def find_smallest(nums):
    """Return the smallest value in nums."""
    if not nums:
        raise ValueError("nums must not be empty")
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest


def sum_list(nums):
    """Return the sum of values in nums."""
    total = 0
    for num in nums:
        total += num
    return total


if __name__ == "__main__":
    sample_nums = [15, 58, 84, 23, 67, -12, -6, 83, 45, -9, 0, 23, -1]
    print("numbers:", sample_nums)
    print("even count:", count_even(sample_nums))
    print("largest:", find_largest(sample_nums))
    print("positive count:", count_positive(sample_nums))
    print("smallest:", find_smallest(sample_nums))
    print("sum:", sum_list(sample_nums))
