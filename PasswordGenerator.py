from random import choice

print("\n*Welcome in the Password Generator Application!*\n")

def generatePassword(length, lowercase, uppercase, digits, specialChars):
     # Define character sets based on user preferences
     chars = specialChars
     if lowercase:
          chars += "qwertyuiopasdfghjklzxcvbnm"
     if uppercase:
          chars += "QWERTYUIOPASDFGHJKLZXCVBNM"
     if digits:
          chars += "0123456789"

     # Check if at least one character set is selected
     if not chars:
          print("Please select at least one character set.")
          return None
     else:
          # Generate the password
          password = ''.join(choice(chars) for _ in range(length))
          return password

while True:
     try:
          length = int(input("\nEnter the length of the password: "))
     except Exception as e:
          print(e,"Try again.")
          continue
     print("\nPlease select your preferences for strong password.\n")
     useLowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
     useUppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
     useDigits = input("Include digits? (y/n): ").lower() == 'y'
     while True:
          useSpecialChars = input("Enter special characters you want to use: ")
          c = ord(useSpecialChars)
          if(33<=c<=47 or 58<=c<=64 or 91<=c<=96 or 123<=c<=126):
               break
          else:
               print("This is not a special character type again.\n")
               continue

     password = generatePassword(length, useLowercase, useUppercase, useDigits, useSpecialChars)

     if password:
          print("\nGenerated Password:", password)
          
     if input("Type 'exit' for quit and press 'Enter' button for continue : ").lower()=='exit':
          exit("Thanks for using Password Generator Application.")