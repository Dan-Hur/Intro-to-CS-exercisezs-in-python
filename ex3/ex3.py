###############################################################################
# FILE: ex3.py
# WRITER:Daniel
# EXCERCISE: intro2cs2 ex3
# functions that calculate different things
###############################################################################

def input_list():
    """a function that takes input from the user and
     returns a list of numbers with their sum at the end"""
    input_list = []
    num_sum = 0
    user_input = input()
    # the next loop will append and sum numbers until a blank is entered
    while user_input != "":
        number = float(user_input)
        input_list.append(number)
        num_sum += number
        user_input = input()

    input_list.append(num_sum)
    return input_list

def inner_product(vec_1,vec_2):
    """a function that calculates an inner product of 2 vectors"""
    inner_prod = 0
    if len(vec_1) != len(vec_2):
        return None
    for i in range(len(vec_1)):
        inner_prod += vec_1[i] * vec_2[i]
    return inner_prod

def is_increasing(sequence):
    """checks for monotonic increase"""
    validity = True
    for i in range(len(sequence)-1):
        validity = sequence[i] <= sequence[i+1]
        if validity == False:
            break
    return validity

def is_strictly_increasing(sequence):
    """checks for strict monotonic increase"""
    validity = True
    for i in range(len(sequence)-1):
        validity = sequence[i] < sequence[i+1]
        if validity == False:
            break
    return validity

def is_decreasing(sequence):
    """checks for monotonic decrease"""
    validity = True
    for i in range(len(sequence) - 1):
        validity = sequence[i] >= sequence[i + 1]
        if validity == False:
            break
    return validity

def is_strictly_decreasing(sequence):
    """checks for strict monotonic decrease"""
    validity = True
    for i in range(len(sequence) - 1):
        validity = sequence[i] > sequence[i + 1]
        if validity == False:
            break
    return validity

def sequence_monotonicity(sequence):
    """checks for monotonicity type, returns a list of booleans of the form:
    [increasing, strictly increasing, decreasing, strictly decreasing]"""
    return [is_increasing(sequence), is_strictly_increasing(sequence), \
            is_decreasing(sequence), is_strictly_decreasing(sequence)]

def check_bool_input(def_bool):
    """a function that checks that the boolean list is possible"""
    condition_counter = 0
    for i in def_bool:
        if i == True:
            condition_counter += 1
    if condition_counter > 2 or condition_counter == 0:
        return False
    if def_bool[0] == False and def_bool[1] == True:
        return False
    if def_bool[2] == False and def_bool[3] == True:
        return False

    return True

def monotonicity_inverse(def_bool):
    """a function that inverses a boolean string to a sequence"""
    INCREASE_LIST = [1,2,2,3]
    STRICT_INCREASE_LIST = [1,2,3,4]
    DECREASE_LIST = [4,3,3,2]
    STRICT_DECREASE_LIST = [4,3,2,1]
    MONOTONIC_NON_STRICT = [1,1,1,1]
    # a check to see if the input has a possible sequence
    if not(check_bool_input(def_bool)):
        return None
    # conditionals for returning the correct sequence
    if def_bool[0] == True and def_bool[2] == True:
        return MONOTONIC_NON_STRICT
    if def_bool[0] and def_bool[1]:
        return STRICT_INCREASE_LIST
    if def_bool[0] == True and def_bool[1] == False:
        return INCREASE_LIST
    if def_bool[2] and def_bool[3]:
        return STRICT_DECREASE_LIST
    if def_bool[2] == True and def_bool[3] == False:
        return DECREASE_LIST

def is_prime(n):
    """checks if a number is prime"""
    if n == 1:
        return False
    if n == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_for_asafi(n):
    """returns a list of 'n' prime numbers"""
    prime_list = []
    counter = 0
    while len(prime_list) < n:
        if is_prime(counter):
            prime_list.append(counter)
        counter += 1
    return prime_list

def sum_of_2_vectors(vec1,vec2):
    summed_vec = []
    for i in range(len(vec1)):
        summed_vec.append(vec1[i] + vec2[i])
    return summed_vec

def sum_of_vectors(vec_lst):
    if vec_lst == []:
        return None
    summed_vecs = vec_lst[0]
    for i in range(1,len(vec_lst)):
       summed_vecs = sum_of_2_vectors(summed_vecs,vec_lst[i])
    return summed_vecs

def num_of_orthogonal(vector):
    """a function that checks for orthogonality"""
    num_of_orthogonals = 0
    for i in vector:
        for j in vector: # I run over the same list twice
            if inner_product(i,j) == 0:
                num_of_orthogonals += 1
        # I substract a count if the vector is orthogonal to itself
        if inner_product(i,i) == 0:
            num_of_orthogonals -= 1
    return num_of_orthogonals//2
