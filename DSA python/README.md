# DSA Python

This workspace contains simple Python programs demonstrating array operations.

## Files

- `array.py` - Consolidated module with reusable functions:
  - `count_even(nums)` - count even numbers
  - `find_largest(nums)` - find largest number
  - `count_positive(nums)` - count positive numbers
  - `find_smallest(nums)` - find smallest number
  - `sum_list(nums)` - compute sum of numbers
- `count.py` - standalone script to count even numbers in a predefined list.
- `largest.py` - standalone script to find the largest number in a predefined list.
- `positivenum.py` - standalone script to count positive numbers in a predefined list.
- `smallest.py` - standalone script to find the smallest number in a predefined list.
- `sum.py` - standalone script to sum the numbers in a predefined list.

## Usage

Run the consolidated module:

```bash
python3 array.py
```

Or import functions from `array.py` in your own scripts:

```python
from array import find_largest, sum_list

nums = [12, 34, 56, 78, 90]
print(find_largest(nums))
print(sum_list(nums))
```
