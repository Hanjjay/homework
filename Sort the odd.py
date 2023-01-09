def sort_array(source_array):
    even_list = []
    odd_list = []
    result = []
    
    for i in source_array:
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
            
    odd_list.sort()
    
    even_list.reverse()
    odd_list.reverse()
    
    for i in source_array:
        if i%2 == 0:
            result.append(even_list.pop())
        else:
            result.append(odd_list.pop())
    return result