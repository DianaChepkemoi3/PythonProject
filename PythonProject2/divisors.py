import sys


def eval_bool():
    return False

def main():
    joint_divisors=list() #append,join, ...
    other=list()
    for number in range(100): # for each number from 0 to 99

        if number % 2 == 0 and number % 11 ==0:
            joint_divisors.append(number)
        else:
            other.append(number)

            print(f"{joint_divisors = }")
            print()
            print(f"{other= }")

            return 0

        if __name__=="__main__":
            sys.exit(main())