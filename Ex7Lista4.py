print("Fahrenheit   Centígrados")

for fahrenheit in range(50, 151):
    centigrados = (5/9) * (fahrenheit - 32)
    print(f"{fahrenheit}           {centigrados:.2f}")