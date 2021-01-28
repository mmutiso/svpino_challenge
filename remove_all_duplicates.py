import random
import copy


def data_generator():

    min_val = 5
    max_val = 11
    array = [i for i in range(1,random.randint(min_val, max_val))]

    # numbers to duplicate
    n_duplicates = random.randint(1,2)
    duplicates = []

    for _ in range(n_duplicates):
        # duplicate frequency
        duplicate_freq = random.randint(1,4)
        # number to duplicate 
        duplication_candidate = random.randint(1, len(array))
        for _ in range(duplicate_freq):
            duplicates.append(duplication_candidate)

    clean_array = copy.deepcopy(array)
    array += duplicates
    random.shuffle(array)

    return (array, clean_array)

def solution(arr):
    '''
    We assume that this array could have negative values even if the data does not. 
    So using a counting array may not work. We will use a dictionary to achieve the same 
    purpose of counting occurences. The occurence count wont matter though since we are trying to remove duplicates
    '''
    counting_dict = {}
    for element in arr:
        if element not in counting_dict:
            counting_dict[element] = 1
        else:
            counting_dict[element] += 1
        
    return list(counting_dict.keys())


if __name__ == "__main__":
    array, clean_array = data_generator()
    print(array)
    print(clean_array)
    result = solution(array)
    print(result)
