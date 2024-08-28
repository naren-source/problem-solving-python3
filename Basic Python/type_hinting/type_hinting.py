def calc_avg(items: list) -> int:
    return int(sum(items)/len(items))


avg: int = calc_avg([1, 3, 5])
print(avg)
