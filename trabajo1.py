print('******************************************')  
print('******************************************')
print('*******UNIVERSIDAD TECNICA ISRAEL*********')
print('********SANTIAGO SALAS GUERRA*************')
print('********7mo SEMESTRE PARALELO B***********')
print('******************************************')
print('******************************************')
print('PROGRAMA PARA ESCOGER EL NUMERO DE DATOS A ' )
print('INGRESAR Y CALCULAR LA SUMA DE TODOS Y LO '  )
print('DIVIDE PARA EL VALOR INGRESADO INICIALMENTE ')


def sumaDigitos(num) :
    s = 0 #suma de los digitos
    while num > 0:
            s = s + num % 10
            num = num // 10
            return s
            
n = int (input("Cantidad de numeros a calcular:   "))  # cantidad de numeros
sumaT = 0 #el total de la suma a calcular
while n > 0:
        num = int(input("Numero:  "))
        sumaT = sumaT + sumaDigitos(num)
        n = n - 1

print(sumaT)
