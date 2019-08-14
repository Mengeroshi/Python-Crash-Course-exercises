print("Enter two numbers and the program will add them")

try:
                
    number_1 = input("Enter number 1: ")
    number_1 = int(number_1)

    number_2 = input("Enter number 2: " )
    number_2 = int(number_2)

except ValueError:
     print("Don't enter letters, just numbers")
else:    
    suma = number_1+number_2           
    print(suma)