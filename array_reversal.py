def solution(arr):
    '''
    Go through the array upto the mid index swapping element at 
    index i with element at index N-1-i
    '''
    N = len(arr)
    half_way = N//2
    for i in range(half_way):
        arr[i],arr[N-1-i]  = arr[N-1-i],arr[i]

    return arr



if __name__ == "__main__":
    result = solution([1,2,3,4,5])
    print(result)
    assert result == [5,4,3,2,1]
  