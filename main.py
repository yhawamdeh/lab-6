#Yazan Al-Hawamdeh
def encode(password):
    return ''.join(str((int(digit) + 3) % 10) for digit in password)

#Completed by Conner Layne
def decode(password):
    return ''.join(str((int(digit) - 3)%10)for digit in password)

def main():
    stored_encoded_password = ''
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                stored_encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please ensure your password is 8 digits long and only contains numbers.")

        elif choice == '2':
            #Conner Layne
            print(f'The encoded password is {stored_encoded_password}, and the original password is {decode(stored_encoded_password)}.')

        elif choice == '3':
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
