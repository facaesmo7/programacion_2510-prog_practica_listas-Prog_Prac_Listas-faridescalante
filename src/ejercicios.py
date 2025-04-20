# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        resultado.append(nueva_fila)
    return resultado

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    contador = 0
    palabras = frase.split()
    for palabra in palabras:
        contador += 1
    return contador

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
    cont = 1
    tabla = []
    while cont <= 10:
        tabla.append(n * cont)
        cont += 1
    return tabla

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    texto = texto.lower()
    cifrado = ""
    for i in texto:
        if i.isalpha():  # Solo ciframos letras
            base = ord('a')
            texto_nuevo = (ord(i) - base + desplazamiento) % 26 + base
            cifrado += chr(texto_nuevo)
        else:
            cifrado += i  # No alteramos los caracteres no alfabéticos
    return cifrado

# Aquí comienza el programa principal. No modifiques el código debajo de esta línea.
def main():
    pass

if __name__ == "__main__":
    main()
