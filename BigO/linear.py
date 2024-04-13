#Linear O Notation

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']

def findNemo(array):
    for i in array:
        if i == 'nemo':
            print("Found nemo!")

findNemo(everyone) #O(n)