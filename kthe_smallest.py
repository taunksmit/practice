  ''' 
  Given an array (or list) find the kth smallest integer from the array
  '''
arr = [7,10,15,6,9,4,2,5]
k = 3
for i in range(0,k-1):
    arr.remove(min(arr))
return min(arr)