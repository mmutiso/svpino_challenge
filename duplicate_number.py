import random
def data_generator():
    array = [i for i in range(1,101)]

    random_number  = random.randint(1,100)
    array.append(random_number)
    random.shuffle(array)

    return (array, random_number)

def solution(arr):
    '''
    Initialize a visited array whose length is 100 + 1 since we have 100 elements
    Go through arr assigning number of visitations
    go through visitation checking occurrences
    '''
    visitations = [0] * 101
    for i in range(1,101):
        element = arr[i]
        visitations[element] += 1

    for i in range(1, len(visitations)+1):
        if visitations[i] > 1:
            return i

if __name__ == "__main__":
    
    arr, duplicate_number = data_generator()
    
    assert duplicate_number == solution(arr)

