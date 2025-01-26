#creating a class
class Euclidean_Algo:
#initialising instance of the class
    def __init__(self, Num1, Num2):
#ensuring Num1 is greater than Num2 right at the initialization
        if Num2 > Num1:
            Num1, Num2 = Num2, Num1  # Swap if Num2 is greater than Num1
#setting the initial values when a new object of the class is created
        self._Num1 = Num1
        self._Num2 = Num2
    
    def calculate_gcd(self):
 # Using the while loop to iterate until the remainder is equal 0
        while self._Num2 != 0:
#calculating the remainder using MOD operation
            remainder = self._Num1 % self._Num2
#swapping and updating the variables
            self._Num1, self._Num2 = self._Num2, remainder
        
        return self._Num1


#inputting 2 integer numbers
Num1 = int(input("Enter an integer number: "))
Num2 = int(input("Enter another integer number: "))

#creating an instance of the class
gcd_calculator = Euclidean_Algo(Num1, Num2)

#outputting the Greatest Common Divisor
print("The Greatest Common Divisor is =", gcd_calculator.calculate_gcd())
