def find_pearson_correlation(x, y):
    if len(x) != len(y) or len(x) == 0:
        return None

    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))

    std_dev_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
    std_dev_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5

    denominator = std_dev_x * std_dev_y

    return 0 if denominator == 0 else numerator / denominator


if __name__ == "__main__":
    nums_1 = [1, 2, 3, 4, 5]
    nums_2 = [2, 3, 5, 70, 95]
    result = find_pearson_correlation(nums_1, nums_2)
    print(f"Коэффициент корреляции Пирсона: {result}")
