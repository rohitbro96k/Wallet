def is_armstrong_number(number):
    number_str = str(number)
    power = len(number_str)
    
    get_sum = sum(int(digit) ** power for digit in number_str)

    return get_sum == number