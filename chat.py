import sys
import time

# Recibir el nombre del contacto como argumento (sys.argv)
if len(sys.argv) < 2:
    print("Error: No contact name provided")
    sys.exit(1)

contact_name = sys.argv[1]

# Imprimir prompt: "Richard, you have a new message from CONTACTO. Reply? [y/n]:"
print(f"Richard, you have a new message from {contact_name}.")

# Leer respuesta de usuario y/n
while True: 
    response = input("Reply? [y/n]:").strip().lower()
    if response == "y":
        print("You chose to reply.")
        break
    elif response == "n":
        print("You chose not to reply.")
        for i in range (3, 0, -1):
            print(f"Exiting in {i} seconds...")
            time.sleep(1)
        sys.exit(0)
    else:
        print("Invalid response. Please enter 'y' or 'n'.")
