import math
from scipy.stats import norm

s_0, k, r, sigma, t = 0, 0, 0, 0, 0


def init():
    global s_0, k, r, sigma, t
    s_0 = int(input("Enter current stock price: "))
    k = int(input("Enter strike price: "))
    r = int(input("Enter interest rate (e.g. enter 4 for 4%) : "))/100
    sigma = float(input("Enter standard deviation of stock return: "))
    t = int(input("Enter maturity time in months: "))/12


def d1_d2():
    d1 = (math.log(s_0/k) + (r + sigma**2/2) * t)/(sigma * (t**0.5))
    d2 = d1 - sigma*(t**0.5)
    return d1, d2


def call(d1, d2):
    return s_0 * norm.cdf(d1) - k * (math.e ** (-r*t)) * norm.cdf(d2)


def put(d1, d2):
    return k * (math.e ** (-r * t)) * norm.cdf(-d2) - s_0 * norm.cdf(-d1)


def main():
    init()
    d1, d2 = d1_d2()
    call_price = call(d1, d2)
    print("Call price: " + str(call_price))
    put_price = put(d1, d2)
    print("Put price: " + str(put_price))


if __name__ == '__main__':
    main()
