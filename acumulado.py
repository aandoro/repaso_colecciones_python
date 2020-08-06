def acumulado(list):
    return [ sum(list[:index+1]) for index in range(len(list))]

print(acumulado([1,5,7]))
print(acumulado([1,0,1,0,1]))
print(acumulado([]))