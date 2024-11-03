class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.items[-1]
    
    def print_pila(self):
        print(self.items)

def evaluar_expresion(expresion, orden):
    pila = Pila()
    tokens = expresion.split()
    if orden == "POST":
        for token in tokens:
            if token.isdigit():
                pila.apilar(int(token))
            else:
                operando2 = pila.desapilar()
                operando1 = pila.desapilar()
                if token == '+':
                    pila.apilar(operando1 + operando2)
                elif token == '-':
                    pila.apilar(operando1 - operando2)
                elif token == '*':
                    pila.apilar(operando1 * operando2)
                elif token == '/':
                    pila.apilar(operando1 / operando2)
        return pila.desapilar()
    elif orden == "PRE":
        for token in tokens[::-1]:
            if token.isdigit():
                pila.apilar(int(token))
            else:
                operando1 = pila.desapilar()
                operando2 = pila.desapilar()
                if token == '+':
                    pila.apilar(operando1 + operando2)
                elif token == '-':
                    pila.apilar(operando1 - operando2)
                elif token == '*':
                    pila.apilar(operando1 * operando2)
                elif token == '/':
                    pila.apilar(operando1 / operando2)
        return pila.desapilar()
    
def mostrar_infijo(expresion, orden):
    i = 0
    j = 0
    pila = Pila()
    tokens = expresion.split()
    if orden == "POST":
        for token in tokens:
            if token.isdigit():
                pila.apilar(token)
            else:
                if token == '+':
                    operando2 = pila.desapilar()
                    operando1 = pila.desapilar()
                    pila.apilar(f"{operando1} {token} {operando2}")
                elif token == '-':
                    operando2 = pila.desapilar()
                    operando1 = pila.desapilar()
                    lengthOp1 = len(operando1.split())
                    lengthOp2 = len(operando2.split())
                    splitOp1 = operando1.split()
                    splitOp2 = operando2.split()
                    k = 0
                    while k < lengthOp2:
                        if splitOp2[k] == '(':
                            i += 1
                        elif splitOp2[k] == ')':
                            i -= 1
                        elif i == 0 and (splitOp2[k] == '*' or splitOp2[k] == '/'):
                            i = k
                        if i == 0 and k > 0:
                            i = k +1
                            break
                        k += 1
                    k = 0
                    while k < lengthOp1:
                        if splitOp1[k] == '(':
                            j += 1
                        elif splitOp1[k] == ')':
                            j -= 1
                        elif j == 0 and (splitOp1[k] == '*' or splitOp1[k] == '/'):
                            j = k
                        if j == 0 and k > 0:
                            break
                        k += 1
                    k = 0
                    if lengthOp1 > 1:
                        if (splitOp1[j] == '*' or splitOp1[j] == '/') and (splitOp2[i] == '*' or splitOp2[i] == '/'):
                            pila.apilar(f"{operando1} {token} {operando2}")
                        elif splitOp2[i] == '*' or splitOp2[i] == '/':
                            pila.apilar(f"{"("} {operando1} {")"} {token} {operando2}")
                        else:
                            pila.apilar(f" {operando1} {token} {"("} {operando2} {")"} ")
                    else:
                        pila.apilar(f"{operando1} {token} {operando2}")
                elif token == '*' or token == '/':
                    operando2 = pila.desapilar()
                    operando1 = pila.desapilar()
                    lengthOp1 = len(operando1.split())
                    lengthOp2 = len(operando2.split())
                    splitOp1 = operando1.split()
                    splitOp2 = operando2.split()
                    k = 0
                    while k < lengthOp1:
                        if splitOp1[k] == '(':
                            i += 1
                        elif splitOp1[k] == ')':
                            i -= 1
                        elif i == 0 and (splitOp1[k] == '*' or splitOp1[k] == '/'):
                            i = k
                            break
                        if i == 0 and k > 0:
                            i = k
                            break
                        k += 1
                    k = 0
                    while k < lengthOp2:
                        if splitOp2[k] == '(':
                            j += 1
                        elif splitOp2[k] == ')':
                            j -= 1
                        elif j == 0 and (splitOp2[k] == '*' or splitOp2[k] == '/'):
                            j = k
                            break
                        if j == 0 and k > 0:
                            j = k
                            break
                        k += 1
                    k = 0
                    if lengthOp1 > 1 and lengthOp2 > 1:
                        if (splitOp1[i] == '*' or splitOp1[i] == '/') and (splitOp2[j] == '*' or splitOp2[j] == '/'):
                            pila.apilar(f"{"("} {operando1} {")"} {token} {"("} {operando2} {")"}")
                        elif splitOp1[i] == '*' or splitOp1[i] == '/':
                            pila.apilar(f"{operando1} {token} {"("} {operando2} {")"}")
                        elif splitOp2[j] == '*' or splitOp2[j] == '/':
                            pila.apilar(f"{"("} {operando1} {")"} {token} {operando2}")
                        else:
                            pila.apilar(f"{"("} {operando1} {")"} {token} {"("} {operando2} {")"}")
                    elif lengthOp1 > 1:
                        if splitOp1[i] == '*' or splitOp1[i] == '/':
                            pila.apilar(f"{operando1} {token} {operando2}")
                        else:
                            pila.apilar(f"{"("} {operando1} {")"} {token} {operando2}")
                    elif lengthOp2 > 1:
                        if splitOp2[j] == '*' or splitOp2[j] == '/':
                            pila.apilar(f"{operando1} {token} {operando2}")
                        else:
                            pila.apilar(f"{operando1} {token} {"("} {operando2} {")"}")
                    else:
                        pila.apilar(f"{operando1} {token} {operando2}")
            i = 0; j = 0
        return pila.desapilar()
    elif orden == "PRE":
        for token in tokens[::-1]:
            if token.isdigit():
                pila.apilar(token)
            else:
                if token == '+':
                    operando1 = pila.desapilar()
                    operando2 = pila.desapilar()
                    pila.apilar(f"{operando1} {token} {operando2}")
                elif token == '-':
                    operando1 = pila.desapilar()
                    operando2 = pila.desapilar()
                    lengthOp1 = len(operando1.split())
                    lengthOp2 = len(operando2.split())
                    splitOp1 = operando1.split()
                    splitOp2 = operando2.split()
                    if lengthOp2 > 1:
                        k = 0
                        while k < lengthOp2:
                            if splitOp2[k] == '(':
                                i += 1
                            elif splitOp2[k] == ')':
                                i -= 1
                            elif i == 0 and (splitOp2[k] == '*' or splitOp2[k] == '/'):
                                i = k
                                break
                            if i == 0 and k > 0:
                                i = k +1
                                break
                            k += 1
                        k = 0
                        while k < lengthOp1:
                            if splitOp1[k] == '(':
                                j += 1
                            elif splitOp1[k] == ')':
                                j -= 1
                            elif j == 0 and (splitOp1[k] == '*' or splitOp1[k] == '/'):
                                j = k
                                break
                            if j == 0 and k > 0:
                                break
                            k += 1
                        k = 0
                        if (splitOp2[i] == '*' or splitOp2[i] == '/') and (splitOp1[j] == '*' or splitOp1[j] == '/'):
                            pila.apilar(f"{operando1} {token} {operando2}")
                            i = 0; j = 0
                        else:
                            pila.apilar(f"{operando1} {token} {"("} {operando2} {")"}")
                            i = 0; j = 0
                    else:
                        pila.apilar(f"{operando1} {token} {operando2}")
                elif token == '*' or token == '/':
                    operando1 = pila.desapilar()
                    operando2 = pila.desapilar()
                    lengthOp1 = len(operando1.split())
                    lengthOp2 = len(operando2.split())
                    splitOp1 = operando1.split()
                    splitOp2 = operando2.split()
                    k = 0
                    while k < lengthOp1:
                        if splitOp1[k] == '(':
                            i += 1
                        elif splitOp1[k] == ')':
                            i -= 1
                        elif i == 0 and (splitOp1[k] == '*' or splitOp1[k] == '/'):
                            i = k
                            break
                        if i == 0 and k > 0:
                            i = k + 1
                            break
                        k += 1
                    k = 0
                    while k < lengthOp2:
                        if splitOp2[k] == '(':
                            j += 1
                        elif splitOp2[k] == ')':
                            j -= 1
                        elif j == 0 and (splitOp2[k] == '*' or splitOp2[k] == '/'):
                            j = k
                            break
                        if j == 0 and k > 0:
                            j = k
                            break
                        k += 1
                    k = 0
                    if lengthOp1 > 1 and lengthOp2 > 1:
                        if (splitOp1[i] == '*' or splitOp1[i] == '/') and (splitOp2[j] == '*' or splitOp2[j] == '/'):
                            pila.apilar(f"{operando1} {token} {operando2}")
                            i = 0; j = 0
                        elif splitOp1[i] == '*' or splitOp1[i] == '/':
                            pila.apilar(f"{operando1} {token} {"("} {operando2} {")"}")
                            i = 0; j = 0
                        elif splitOp2[j] == '*' or splitOp2[j] == '/':
                            pila.apilar(f"{"("} {operando1} {")"} {token} {operando2}")
                            i = 0; j = 0
                        else:
                            pila.apilar(f"{"("} {operando1} {")"} {token} {"("} {operando2} {")"}")
                    elif lengthOp1 > 1:
                        if splitOp1[i] == '*' or splitOp1[i] == '/':
                            pila.apilar(f"{operando1} {token} {operando2}")
                            i = 0; j = 0
                        else:
                            pila.apilar(f"{"("} {operando1} {")"} {token} {operando2}")
                    elif lengthOp2 > 1:
                        if splitOp2[j] == '*' or splitOp2[j] == '/':
                            pila.apilar(f"{operando1} {token} {operando2}")
                            i = 0; j = 0
                        else:
                            pila.apilar(f"{operando1} {token} {"("} {operando2} {")"}")
                    else:
                        pila.apilar(f"{operando1} {token} {operando2}")
                else:
                    print("Operador incorrecto")
            i = 0; j = 0
    return pila.desapilar()

def main():
    boolean = True
    while boolean:
        print("$> ", end="")
        entrada = input().split()
        numeros = 0
        operadores = 0
        if entrada[0] == "SALIR":
            boolean = False
            break
        else:
            for i in ' '.join(entrada[2:]):
                if i.isdigit():
                    numeros += 1
                elif i in ['+', '-', '*', '/']:
                    operadores += 1
            if operadores >= numeros:
                print("Expresion incorrecta")
            else:
                if entrada[0] == "EVAL":
                    orden = entrada[1]
                    expresion = ' '.join(entrada[2:])
                    print(expresion)
                    if orden == "POST" or orden == "PRE":
                        print(evaluar_expresion(expresion, orden))
                    else:
                        print("Orden incorrecto")
                elif entrada[0] == "MOSTRAR":
                    orden = entrada[1]
                    expresion = ' '.join(entrada[2:])
                    if orden == "POST" or orden == "PRE":
                        print(mostrar_infijo(expresion, orden))
                    else:
                        print("Orden incorrecto")
                else:
                    print("Comando incorrecto")

if __name__ == "__main__":
    main()