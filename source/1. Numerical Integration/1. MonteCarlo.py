import math
import random
import time

def monte_carlo():
    n = 100000
    count = 0

    # Initialize the random number generator only once
    random.seed(time.time())

    for _ in range(n):
        # Generate a random number from 0 to 3
        random_x = random.uniform(0, 3.0)
        # Generate a random number from 0 to 0.12
        random_y = random.uniform(0, 0.12)

        if random_y < (math.sin(random_x)**2) / (13 - 12 * math.cos(random_x)):
            count += 1

    # Calculate the area
    area = count / n * 3.0 * 0.12

    return area

def main():
    k = 20
    sumS1 = 0.0
    sumS2 = 0.0

    for _ in range(k):
        a = monte_carlo()
        print(f"{a:.5f}")
        sumS1 += a
        sumS2 += a**2

    sumS2 /= k
    sumS1 = (sumS1 / k)**2

    sigma = math.sqrt(sumS2 - sumS1)
    print(f"Sigma: {sigma:.5f}")

if __name__ == "__main__":
    main()
