# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_value = [[c/t,t] for c,t in zip(values, weights)]
    unit_value = sorted(unit_value,reverse=True)
    for i in range(len(unit_value)):
        if capacity==0:
            return value
        take = min(capacity,unit_value[i][1])
        value += take * unit_value[i][0]
        capacity-=take
    # print(unit_value)
    # write your code here
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # capacity = 50
    # weights=[20,50,30]
    # values = [60,100,120]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
