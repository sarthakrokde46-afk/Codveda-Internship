from cryptography.fernet import Fernet
import os

def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()

        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    return key

def encrypt_file(filename, fernet):

    try:
        with open(filename, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        encrypted_filename = filename + ".encrypted"

        with open(encrypted_filename, "wb") as file:
            file.write(encrypted_data)

        print("\nFile encrypted successfully!")
        print("Encrypted file:", encrypted_filename)

    except FileNotFoundError:
        print("\nError: File not found.")

    except Exception as e:
        print("\nError:", e)


def decrypt_file(filename, fernet):

    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        if filename.endswith(".encrypted"):
            decrypted_filename = filename[:-10]
        else:
            decrypted_filename = filename + ".decrypted"

        with open(decrypted_filename, "wb") as file:
            file.write(decrypted_data)

        print("\nFile decrypted successfully!")
        print("Decrypted file:", decrypted_filename)

    except FileNotFoundError:
        print("\nError: File not found.")

    except Exception:
        print("\nError: Unable to decrypt the file.")
        print("Make sure the file was encrypted using the correct secret key.")


def main():

    key = load_key()

    fernet = Fernet(key)

    while True:

        print("\n==============================")
        print("     FILE ENCRYPTION TOOL")
        print("==============================")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            filename = input("Enter the file name to encrypt: ")

            encrypt_file(filename, fernet)

        elif choice == "2":

            filename = input("Enter the file name to decrypt: ")

            decrypt_file(filename, fernet)

        elif choice == "3":

            print("\nThank you for using the File Encryption Tool!")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()