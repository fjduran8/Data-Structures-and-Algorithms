#Big O Rules

#Rule 1: Worst Case
'''
Always think of the worst case inputs
Example: even if you add a break to a 
loop after searching for an item, what
if the item you were searching for was still at the last of the list
'''

#Rule 2: Remove Constants
'''
Remove the constants to simplify function
Example: O(544 + 20n) = O(n)
'''
#Rule 3: Different terms for inputs
'''
The following function would have O(n + m), not O(n) or O(n + n)
function printFirstItemThenFirstHalfThenSayHi100Times(items) {
    console.log(items[0]);

    var middleIndex = Math.floor(items.length / 2);
    var index = 0;

    while (index < middleIndex) {
        console.log(items[index]);
        index++;
    }

    for (var i = 0; i < 100; i++) {
        console.log('hi');
    }
}

'''
#Rule 4: Drop Non-Dominants
'''
If we get something like O(n^2 + 100 + n + n) 
we only consider the dominant term and get O(n^2)
'''
