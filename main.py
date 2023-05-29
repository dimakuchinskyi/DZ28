def average_closure():
    total_sum = 0
    count = 0
    def add_number(number):
        nonlocal total_sum, count
        total_sum += number
        count += 1
    def get_average():
        return total_sum / count if count > 0 else 0
    return add_number, get_average
add_func, avg_func = average_closure()
add_func(10)
add_func(20)
add_func(30)
average = avg_func()
print(average)