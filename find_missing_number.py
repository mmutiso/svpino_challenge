import random
def data_generator():
    array = [i for i in range(1,101)]

    random_number  = random.randint(1,100)
    array.remove(random_number)

    random.shuffle(array)

    return (array, random_number)

def solution(arr):
    '''
    create a visited array initialized with all False. 
    The size of the visited array is the length of 100 + 1
    Iterate first time on arr to set visitation 
    Iterate second time on visited to check unvisited
    '''
    N = len(arr)
    visited_array = [False] * (100+1)
    for i in range(N):
        element = arr[i]
        visited_array[element]  = True

    for i in range(1, len(visited_array)):
        if visited_array[i] == False:
            return i 

    #For the scenario in question we will never get here

if __name__ == "__main__":
    (arr, missing_element) = data_generator()
    result = solution(arr)
    assert result == missing_element
    (arr, missing_element) = data_generator()
    result = solution(arr)
    assert result == missing_element
    
    
