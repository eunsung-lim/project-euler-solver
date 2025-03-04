"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

The diagonals are:
Bottom right: 1,9,25,49 (odd squares)
Top right: 1,3,13,31
Top left: 1,5,17,37
Bottom left: 1,7,21,43

For each new layer:
- Bottom right increases by (2n)^2 where n is layer number
- Top right increases by 2n-1 each time
- Top left increases by 2n each time 
- Bottom left increases by 2n+1 each time
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

side_length = 1
total_diagonals = 1
total_primes = 0
n = 0

while True:
    n += 1
    side_length += 2
    
    # Calculate the 4 new diagonal numbers
    bottom_right = (2*n + 1)**2
    top_right = bottom_right - 6*n
    top_left = bottom_right - 4*n
    bottom_left = bottom_right - 2*n
    
    # Check if they're prime
    if is_prime(top_right): total_primes += 1
    if is_prime(top_left): total_primes += 1
    if is_prime(bottom_left): total_primes += 1
    # bottom_right is always a square number, so never prime
    
    total_diagonals += 4
    
    if total_diagonals > 1 and total_primes/total_diagonals < 0.1:
        break

print(side_length)
