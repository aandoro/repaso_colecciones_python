def final_comun_mayor(word1, word2):
    str1 = list(reversed(word1))
    str2 = list(reversed(word2))
    result = ''
    for index,letter1 in enumerate(str1):
        if letter1 == str2[index]:
            result += letter1
        else:
            result = ''.join(list(reversed(result)))
            return result
    #return result

print(final_comun_mayor('camión', 'ración'))
print(final_comun_mayor('Python', 'PyCon'))
print(final_comun_mayor('Teclado', 'Mezclado'))
print(final_comun_mayor('Harina', 'Arroz'))