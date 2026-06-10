def square(number):
    # Validation: A chessboard only has squares 1 through 64
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
        
    # Since square 1 has 1 grain (2^0), square 2 has 2 grains (2^1), etc.
    # The formula for any square 'n' is 2^(n-1)
    return 2 ** (number - 1)


def total():
    # The total number of grains on a 64-square board is (2^64) - 1
    return (2 ** 64) - 1