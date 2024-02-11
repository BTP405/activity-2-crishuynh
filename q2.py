import matplotlib.pyplot as plt

def graphSnowFall(t): 
    with open(t, 'r') as f:
        ranges = f.readlines()
        for each in range(len(ranges)): 
            ranges[each] = int(ranges[each])
            
        range_0_10 = range_11_20 = range_21_30 = range_31_40 = range_41_50 = 0

        for i in range(len(ranges)):
            if ranges[i] <= 10: range_0_10 += 1
            elif ranges[i] >= 11 and ranges[i] <= 20:  range_11_20 += 1
            elif ranges[i] >=21 and ranges[i] <= 30:  range_21_30 += 1
            elif ranges[i] >= 31 and ranges[i] <= 40:  range_41_50 += 1
            else: range_41_50 += 1

        x = ['0 - 10', '11 - 20', '21 - 30', '31 - 40', '41 - 50']
        y = [range_0_10, range_11_20, range_21_30, range_31_40, range_41_50]; 
        plt.bar(x, y)
        plt.title('Snowfall')
        plt.xlabel('Range (cm)')
        plt.ylabel('Amount')
        plt.yticks([0, 1, 2, 3])
        plt.show() 

graphSnowFall('q2.txt')