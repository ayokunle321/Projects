from importlib import invalidate_caches
from importlib import import_module


def write_py(name, parameters, statements):
    
    '''
    Description: opens and writes out a python file named based on name and  content based on statements/parameters
    Input: name as a str,  parameter (function arguments) as a list, statements as a list
    Return: None
    
    '''
    
    indent_space = ' ' * 4
    namepy = name + '.py'
    parameterstr = ', '.join(parameters)
    with open(namepy, 'w') as outfile:
        outfile.write('def {}({}):'.format(name, parameterstr))
        for statement in statements:
            outfile.write('\n' + indent_space + statement)



def fixed_bubble(size):
    
    '''
    Description: outputs a file that contains a function that uses bubble sort to sort lists of length size
    Input: size (length of list) as an int
    Return: None
    
    '''
        
    nameb = 'bubble' + str(size)
    parameterb = []
    statementb = []
    parameterb.append('a_list')
    sizeb = size - 1

    while sizeb >= 0:
        for i in range(0, sizeb):
            current = i
            nextindex = i + 1
            statementb.append(str('if a_list[{}] > a_list[{}]:'.format(current,nextindex)))
            statementb.append(str('    a_list[{}], a_list[{}] = a_list[{}], a_list[{}]'.format(current, nextindex, nextindex, current)))

        sizeb -= 1

    statementb.append('return a_list')
    write_py(nameb, parameterb, statementb)
    


def load_function(name):
    '''
    load_function - imports a module recently created by name
        and returns the function of the same name from inside of it
    name - a string name of the module (not including .py at the end)
    '''
    # invalidate_caches is necessary to import any files created after this file started!
    invalidate_caches()
    print(f"    Attempting to import {name}...")
    module = import_module(name)
    print(f"    Imported!")
    assert hasattr(module, name), f"{name} is missing from {name}.py"
    function = getattr(module, name)
    assert type(function) is type(load_function)
    return function


def flip(sign):
    
    '''
    Description: takes a single argument, either ">" or "<" and flips it
    Input: sign (either '>' or '<' as a a str
    Return: either '>' or '<' as a str
    
    '''
        
    if sign == '>':
        return '<'
    elif sign == '<':
        return '>'


def greatest_power_of_two_less_than(ant):
    
    '''
    Description: obtains the greatest power of two that’s less than that ant
    Input: ant as an int (ant>=1)
    Return: (greatest power of 2)<ant as an int
    
    '''
        
    assert ant >= 1
    firstpower = 1
    nextpower = 2
    while nextpower < ant:
        firstpower = nextpower
        nextpower *= 2

    return firstpower


def bitonic_merge(a_list,start,end,direction,statement=None):
    
    '''
    Description: recursively sorts a bitonic sequence in ascending order
    Input: a_list (list), start index (int), end index (int), direction: > or < (str), statement
    as a list (to keep track of the order of operations in each direction)
    Return: None
    
    '''
        
    length = int(end) - int(start)

    if length == 1:
        return
    
    else:
        distance = greatest_power_of_two_less_than(length)
        middle = int(end) - int(distance)

        for index in range(start, middle):
            
            #adding the order of operations (str) to statement; these statements will be later utilized in the fixed bitonic function when writing the ouput file

            if direction == '>':
                if statement != None:
                    statement.append(f"if a_list[{index}] > a_list[{index + distance}]:")
                    statement.append(f"    a_list[{index}], a_list[{index + distance}] = a_list[{index + distance}], a_list[{index}]")
                if a_list[index] > a_list[index + distance]:
                    (a_list[index], a_list[index + distance]) = (a_list[index + distance], a_list[index])
                    
            
            if direction == '<':
                if statement != None:
                    statement.append(f"if a_list[{index}] < a_list[{index + distance}]:")
                    statement.append(f"    a_list[{index}], a_list[{index + distance}] = a_list[{index + distance}], a_list[{index}]")
                if a_list[index] < a_list[index + distance]:
                    (a_list[index], a_list[index + distance]) = (a_list[index + distance], a_list[index])
                
                    
                

        bitonic_merge(a_list, start, middle, direction,statement)
        bitonic_merge(a_list, middle, end, direction,statement)
        


def bitonic_sort(a_list,start,end,direction,statement=None):
   
    '''
    Description: produces a bitonic sequence by recursively sorting its two halves in opposite sorting orders, and then
    calls bitonic_merge to make them in the same order
    Input: a_list (list), start index (int), end index (int), direction: > or < (str), statement
    as a list (to keep track of the order of operations in each direction)
    Return: None
    
    '''
        
    length = int(end) - int(start)

    if length == 1:
        return
    
    else:

        middle = start + length // 2

        bitonic_sort(a_list, start, middle, direction,statement)
        bitonic_sort(a_list, middle, end, flip(direction),statement)
        bitonic_merge(a_list, start, end, direction,statement)


def bitonic(a_list,statement=None):
    
    '''
    Description: caller of bitonic_sort for sorting the entire array of length N in ascending order
    Input: Some random list a_list, statement as a list (to keep track of the order of operations in each direction)
    Return: None
    
    '''
        
    start = 0
    end = len(a_list)
    direction = '>'
    bitonic_sort(a_list, start, end, direction,statement)

    
def fixed_bitonic(size):
    
    '''
    Description: outputs a file that contains a function that uses bitonic sort to sort lists of length size
    Input: size as int (length of list)
    Return: None
    
    '''
        
    nameb = 'bitonic' + str(size)
    statementb = []
    parameterb = [] 
    
    
    a_list = [0]*size
    bitonic(a_list,statementb)
    
    parameterb.append('a_list')
    
    statementb.append('return a_list')
    write_py(nameb, parameterb, statementb)    
    
    


if __name__ == '__main__':
    
    #Task 1.5 testing write_py function with a recursive factorial function
    
    write_py("factorial", ["n"], ["if n == 1:", "    return n", "else:", "    return n*factorial(n-1)"])
    factorial = load_function("factorial")
    assert factorial(4) == 24    




    
    

