""" Assignment of 12th Feb """

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior citizen"

print("\nHello", name + "!")
print("You are", age, "years old and you are", category + ".")
print("It's nice that you enjoy", hobby + ". Keep doing what you love!")