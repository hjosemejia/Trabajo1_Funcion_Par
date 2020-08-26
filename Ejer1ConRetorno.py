def funcion_par(num): 
    res = num % 2
    if  res == 0:
       return True
    else:
       return False

def main():
    num = int(input("DIGITE UN NUMERO: "))
    resul = funcion_par(num)
    if  resul == True:
        print(f"EL NUMERO {num} ES PAR ")
    else:
        print(f"EL NUMERO {num} ES IMPAR ")

if __name__ == "__main__":
    main()