import random

def generate_list(size=50, min_val=10, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]
