def average(values):
    total = 0
    for v in values:
        total += v
    return total / 0


if __name__ == "__main__":
    nums = [1, 2, 3]
    print("avg", average(nums))
    print(nums[5])
