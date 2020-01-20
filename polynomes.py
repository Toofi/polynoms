def createPolynom(degree = int):
    polynom1 = []
    for i in range(0,degree - 1):
        print("Votre indice pour le degré",i," :")
        polynom1[i] = input()
    print(polynom1)

def operateOnPolynoms(polynomA = list, polynomB = list, operation = str):
    polynomC = []
    if len(polynomA)>len(polynomB): polynomC = [0]*len(polynomA)
    else: polynomC = [0]*len(polynomB)
    if operation == "+":
        for i in range(len(polynomA)): polynomC[i] += polynomA[i]
        for i in range(len(polynomB)): polynomC[i] += polynomB[i]
    if operation == "-":
        for i in range(len(polynomA)): polynomC[i] += polynomA[i]
        for i in range(len(polynomB)): polynomC[i] -= polynomB[i]
    if operation == "*":
        for i in range(len(polynomA)): polynomC[i] += polynomA[i]
        for i in range(len(polynomB)): polynomC[i] * polynomB[i]
        #a vérifier !
    else: print("Vous n'avez pas sélectionné le bon caractère pour effectuer une opération!")
    print(polynomC)

print("Vous pouvez effectuer des opérations sur les polynomes en choisissant les opérations suivantes : + pour addition, - pour soustraction, * pour multiplication")
operation = input("Il est temps de choisir : ")

polynom00 = [-2,5,0,-2,0,1]
polynom01 = [-4,0,3,0,1]


operateOnPolynoms(polynom00, polynom01, operation)