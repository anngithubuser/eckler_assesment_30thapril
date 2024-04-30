"""
Simple Calculator
"""
# Provide your solution here
a=int(input(""))
b=int(input(""))
x=input("")

def calculate(a, b, x):
    if x== "+":
        return a+b
    elif x == "-":
        return a-b
    elif x== "*":
        return a*b
    elif x== "/":
        return a%b
        if b== "0":
            print("Division by 0 is not allowed.")
    else:
        print("Invalid operator")

result=(calculate(a,b,x))
print(result)



"""
result = add(5, 6)
print(result)
"""
"""
Reverse Word
"""
# Provide your solution here
"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

word=input("")
def reverse_word(word):
  return word[::-1]
cap=reverse_word(word).capitalize()
print(cap)
"""
