# WAP using function to convert fahrenheit to celsius.

def fah_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

a = int(input("Enter a temperature in Fahrenheit: "))

c = fah_to_cel(a)           # round banane k liye c use kiya.
print(f"{round(c,2)} °C")   # --> round means point k baad k kitne no. show honge.