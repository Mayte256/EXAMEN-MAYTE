def sumar(a, b):
    return a - b 

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print("Calculadora MAYTE")
    print(f"4 + 4 = {sumar(4, 4)}")
    print(f"10 - 3 = {restar(10, 3)}")
    print(f"5 * 3 = {multiplicar(5, 3)}")
    print(f"10 / 2 = {dividir(10, 2)}")