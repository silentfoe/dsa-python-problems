# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# my first solution: 

def sort_array(source_array):
    
    odds = []
    count = 0
    answer = []
    
    for num in source_array:
        if num % 2 != 0:
            odds.append(num)
            
    odds.sort()
            
    for num in source_array:
        if num % 2 == 0:
            answer.append(num)
        else:
            answer.append(odds[count])
            count += 1
    
    return answer

# clever solution I found on the code wars solutions page: 

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]