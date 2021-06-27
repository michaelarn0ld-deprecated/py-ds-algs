# Given an array of strings, print all possible permutations of the array

def permuteArrayHelper(stringList, chosen):
    if not stringList:
        print(chosen)
    else:
        for i in range(len(stringList)):
            #  choose
            choice = stringList[i]
            chosen.append(choice)
            stringList.remove(choice)

            # explore
            permuteArrayHelper(stringList, chosen)

            # unchoose
            chosen.pop()
            stringList.insert(i, choice)
#  ----------------------------------------------------------

def permuteArray(stringList):
    chosen = []
    permuteArrayHelper(stringList, chosen)
#  ----------------------------------------------------------


# test case
test = ['a','b','c']
permuteArray(test)