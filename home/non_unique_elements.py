def f(x):
    def g(y):
        return y + y
    return g(x+1)

f(3)

def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  
    
    # direct Scheme copy
    #def iter(lst, result):
        #if len(lst) == 0:
        #    return result
        #else:
        #    if lst[0] in result + lst[1:]:
        #        return iter(lst[1:], result + [lst[0]])
        #    else:
        #        return iter(lst[1:], result)
        
    result = []
    input = data
    
    for i in range(len(data)):
        print(input)
        if input[0] in result + input[1:]:
            result.append(input[0])
        input = input[1:]
    
    #replace this for solution
    return result
