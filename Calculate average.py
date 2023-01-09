def find_average(numbers):
    count = 0
    sum = 0

    for i in range(len(numbers)):
        sum += numbers[i]
        count += 1
    
    return sum / count