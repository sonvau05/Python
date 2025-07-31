import random

with open('data.txt', 'w') as f:
    for _ in range(10):
        name = random.choice(['Aptech', 'FPT', 'NIIT', 'Viettel', 'VinTech'])
        score = random.randint(1, 100)
        f.write(f'{name} score: {score}\n')

with open('data.txt', 'r') as f:
    for line in f:
        if 'Aptech' in line:
            print(line.strip())