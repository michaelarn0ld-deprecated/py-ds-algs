

def target_sum(arr, target):
    dict = {}
    for i, ele in enumerate(arr):
        dict[ele] = i
        if (target - ele) in dict:
            return (dict[target - ele], i)

print (target_sum([1,4,5,9,12],9))
print (target_sum([1,9,4,5,12],9))
