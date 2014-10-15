def checkio(data):
    '''Returns the median of the given list'''
    
    size = len(data)

    midpoint = size // 2

    data = sorted(data)
    if size % 2 == 1:
        return data[midpoint]
    else:
        return 0.5 * (data[midpoint-1] + data[midpoint])
