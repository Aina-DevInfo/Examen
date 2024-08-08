
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur: Division par zéro"
    return a / b


if __name__ == "__main__":
    a = 10
    b = 5

    print(f"Addition de {a} et {b} : {addition(a, b)}")
    print(f"Soustraction de {a} et {b} : {soustraction(a, b)}")
    print(f"Multiplication de {a} et {b} : {multiplication(a, b)}")
    print(f"Division de {a} et {b} : {division(a, b)}")

