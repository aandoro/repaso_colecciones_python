def cuenta_subcadenas_ax(cadena):
    num =  i = 0
    str_upper = cadena.upper()
    while i < len(str_upper):
        if str_upper[i] == 'A':
            num += str_upper[i:].count('X')
        i+=1
    return num

print(cuenta_subcadenas_ax('CAXAAYXZA'))
print(cuenta_subcadenas_ax('AAXOXXA'))
print(cuenta_subcadenas_ax('AXAXAXAXAX'))