# python3

# Given an integer 1 ≤ money ≤ 103, find the minimum number 
# of coins with denominations 1, 5, and 10 that changes money.

# In this problem, you will implement a simple greedy 
# algorithm used by cashiers all over the world. We assume 
# that a cashier has unlimited number of coins of each denomination.

def money_change(money):
    count = 0
    denom = [10, 5, 1]

    # greedy chioce will be the largest denomination
    while money > 0:
        for val in denom:
            if money >= val:
                number = (money - money % val) // val
                count += number
                money = money - number * val
                break

    return count


def main():
    input_money = int(input())
    print(money_change(input_money))

if __name__ == '__main__':
    main()
