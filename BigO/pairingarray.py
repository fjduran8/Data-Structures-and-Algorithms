array = [1,2,3,4,5]


def pairingNumbers(arr):
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            print(arr[i],arr[j])

pairingNumbers(array)

#O(n^2)