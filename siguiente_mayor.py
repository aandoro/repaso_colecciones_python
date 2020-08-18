def siguiente_mayor(list):
    
    contador = 0
    i = 0
    #for i in range(len(list)):
    while contador < len(list):
        temp_list = list[i+1:]
        for j in range(len(temp_list)):
            if list[i] < temp_list[j]:
                index_next = list.index(temp_list[j])
                next_item = list.pop(index_next)
                temp = list.pop(i)
                list.insert(i,next_item)
                list.insert(index_next,temp)
                i += 1
        i+=1
        contador +=1
    list.pop()
    list.append(-1)
    return list

print(f'{siguiente_mayor([5, 7, 3, 2, 8])}')
print(f'{siguiente_mayor([2, 3, 4, 5])}')
print(f'{siguiente_mayor([1, 0, -1, 8, -72])}')