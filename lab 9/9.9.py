def most_popular_number(votes):
    count = {}
    max_count = 0
    min_number = float('inf')
    result = None

    for number in votes:
        count[number] = count.get(number, 0) + 1
        if count[number] > max_count or (count[number] == max_count and number < min_number):
            max_count = count[number]
            min_number = number
            result = number

    return result


test_cases = int(input())

for _ in range(test_cases):
    v = int(input())  
    votes = [int(input()) for _ in range(v)]  

    popular_number = most_popular_number(votes)  
    print(popular_number)
