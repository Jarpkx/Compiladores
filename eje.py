fichero = open ('ejemplo.txt')

fichero.readline();
fichero.readline();

for linea in fichero:
    print(linea, ' ** longitud:', len(linea));