password = "secure3p@ss"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 18:
    strength = "medium"
else:
    strength = "strong"

print("password strengthh is: ", strength)
