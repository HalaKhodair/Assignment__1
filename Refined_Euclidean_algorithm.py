#creating a class
class Euclidean_Algo:
#initialising instance of the class
    def __init__(self, Num1, Num2):
# ensuring Num1 is greater than Num2 
        if Num2 > Num1:
 # swapping if Num2 is greater than Num1
            Num1, Num2 = Num2, Num1 
# setting the initial values when a new object of the class is created
        self._Num1 = Num1
        self._Num2 = Num2
# defining a method to calculate the greatest common divisor
    def calculate_gcd(self):
# Using the while loop to iterate until the remainder is equal 0
        while self._Num2 != 0:
# calculating the remainder using MOD operation
            remainder = self._Num1 % self._Num2
# swapping and updating the variables
            self._Num1, self._Num2 = self._Num2, remainder 
        return self._Num1


# defining a function to validate input that only accepts positive integers
def only_positive(prompt):
#using a while loop to iterate until a positive integer is inputted
    while True:
#using the try and except blocks to handle errors
        try:
            num = int(input(prompt))
#using the if statament to check if the num is less than or equal to 0
            if num <= 0 :
                print("Enter a positive integer.")
            else:
                return num
#printing a message when an error is found
        except ValueError:
            print("Invalid input, enter a positive integer.")

# inputting 2 integer numbers
Num1 = only_positive("Enter an integer number: ")
Num2 = only_positive("Enter another integer number: ")

# creating an instance of the class
gcd = Euclidean_Algo(Num1, Num2)

# outputting the Greatest Common Divisor
print("The Greatest Common Divisor is =", gcd.calculate_gcd())
