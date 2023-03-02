import math

n = int(input())

p_list = map(int, input().split())

def is_prime_number(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

error = 0

for num in p_list:
    if is_prime_number(num):
        error += 1
    
print(error)
