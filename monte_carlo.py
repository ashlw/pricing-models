import math
import numpy as np

s_0, k, r, sigma, t = 0, 0, 0, 0, 0


def init():
    global s_0, k, r, sigma, t
    s_0 = int(input("Enter current stock price: "))
    k = int(input("Enter strike price: "))
    r = int(input("Enter interest rate (e.g. enter 4 for 4%) : "))/100
    sigma = float(input("Enter standard deviation of stock return: "))
    t = int(input("Enter maturity time in months: "))/12


def calculate_mean():
    return math.log(s_0) + (r - (sigma**2)/2) * t


def calculate_std():
    return sigma * t**0.5


def main():
    init()
    mean = calculate_mean()
    std = calculate_std()
    # draw 1000 samples
    samples = np.random.lognormal(mean, std, 1000)
    payoff = []
    for s_i in samples:
        payoff.append(max(s_i-k, 0))

    # call price
    payoff = np.array(payoff)
    avg = np.mean(payoff)
    call_price = math.e ** (-r*t) * avg
    print("Call_price is:", call_price)


if __name__ == '__main__':
    main()

