print("Welcome to the Password Generator App")
passwordChar = int(input("Choose how many characters would you like to have in your password: "))

if passwordChar < 5:
    print("Error, minimum password's characters is 5")


if passwordChar > 5:
    print(f"The amount of characters you chose for your password: {passwordChar}")
