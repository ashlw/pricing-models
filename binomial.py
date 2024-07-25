import math

init = 50
strike = 50
# probability of going up
p_up = 0.5073
rate = 0.1
# number of steps
n = 5
# up and down step sizes
u = 1.1224
d = 0.8909


def combination(m, r):
    return math.factorial(m) / (math.factorial(r) * math.factorial(m-r))


def main():
    total = []
    for j in range(n):
        jj = n-j
        val = combination(n, j)*(p_up**j)*((1-p_up)**jj) * max(0, init*(u**j)*(d**jj) - strike)
        total.append(val)

    res = sum(total)/(1+rate)
    print(res)


if __name__ == '__main__':
    main()
