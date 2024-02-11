def decoratorFunc(func):
    def wrapper(line):
        func(line)
        nums = line.split()
        for i in range(0, len(nums)):
            nums[i] = int(nums[i])
        print("The numbers read: ", nums)
        print("The count of the numbers read: ", len(nums))
        print("The average of the numbers: ", sum(nums) / len(nums))
        print("The maximum of the numbers: ", max(nums))
        return func(nums)
    return wrapper

@decoratorFunc
def process_line(line):
    print("--------")

def printStats(t):
    with open(t, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            print("Line: " + str(i + 1))
            process_line(lines[i])

def main():
    printStats("q4.txt")


if __name__ == "__main__":
    main()


