for number in range(100, 401):
    is_only_even = True
    for a in str(number):
        if int(a) % 2 != 0:
            is_only_even = False
            break
    if is_only_even:
        print(number)