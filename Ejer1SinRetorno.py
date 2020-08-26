def funcion_par(num): 
    res = num % 2
    if  res == 0:
       print(f"EL NUMERO {num} ES PAR ")
    else:
       print(f"EL NUMERO {num} ES IMPAR ")

def main():
    num = int(input("DIGITE UN NUMERO: "))
    funcion_par(num)

if __name__ == "__main__":
    main()