import os

def generate_custom_vigenere_table(keyword):
    keyword = keyword.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere_table = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            vigenere_table[i][j] = alphabet[(i + j) % 26]
    custom_table = []
    for char in keyword:
        char_index = ord(char) - ord('A')
        custom_table.append(vigenere_table[char_index])
    
    print("Custom Vigenere Table:")
    for row in custom_table:
        print(' '.join(row))
    
    return custom_table

def generate_default_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere_table = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            vigenere_table[i][j] = alphabet[(i + j) % 26]
    return vigenere_table

def vigenere_encrypt(plaintext, keyword, vigenere_table):
    plaintext = plaintext.replace(" ", "").upper()
    keyword = keyword.upper()
    ciphertext = ''
    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            encrypted_char = vigenere_table[keyword_index % len(keyword)][ord(char) - ord('A')]
            ciphertext += encrypted_char
            keyword_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, keyword, vigenere_table):
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    plaintext = ''
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            for i in range(26):
                if vigenere_table[keyword_index % len(keyword)][i] == char:
                    plaintext += chr(i + ord('A'))
                    break
            keyword_index += 1
        else:
            plaintext += char
    return plaintext

def display_ascii():
    print("\033[38;2;0;255;0m ██▓███ ▓██   ██▓ ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓")
    print("▓██░  ██▒▒██  ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒")
    print("▓██░ ██▓▒ ▒██ ██░▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░")
    print("▒██▄█▓▒ ▒ ░ ▐██▓░▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ")
    print("▒██▒ ░  ░ ░ ██▒▓░▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ")
    print("▒▓▒░ ░  ░  ██▒▒▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ")
    print("░▒ ░     ▓██ ░▒░   ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░    ")
    print("▒ ░░ ░  ░  ██▒▓░ ░ ░  ░ ░   ░░   ░ ▒ ▒ ░░  ░░         ░      ")
    print("░ ░░       ▒ ▒ ░░ ░            ░░   ░ ░                       ")
    print("░           ░ ░     ░ ░         ░     ░ ░                       ")
    print("            ░ ░     ░                 ░ ░                       ")

def main():
    os.system('clear')
    display_ascii()
    print("Vigenere-table-master\n")
    print("1. Default Vigenere Table")
    print("2. Custom Vigenere Table")
    choice = input("Choose an option: ")
    if choice == '1':
        vigenere_table = generate_default_vigenere_table()
        keyword = ""  # Define an empty keyword for default table
    elif choice == '2':
        keyword = input("Enter a word to generate custom Vigenere table: ")
        vigenere_table = generate_custom_vigenere_table(keyword)
    else:
        print("Invalid choice!")
        return
    while True:
        choice = input("\n1. Encrypt\n2. Decrypt\n3. Change Vigenere Table\n4. Exit\nEnter: ")
        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            keyword = input("Enter keyword: ")  # Ask for keyword input here
            encrypted_text = vigenere_encrypt(plaintext, keyword, vigenere_table)
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            ciphertext = input("Enter the encrypted text: ")
            keyword = input("Enter keyword: ")  # Ask for keyword input here
            decrypted_text = vigenere_decrypt(ciphertext, keyword, vigenere_table)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            choice = input("1. Default Vigenere Table\n2. Custom Vigenere Table\nChoose an option: ")
            if choice == '1':
                vigenere_table = generate_default_vigenere_table()
                keyword = ""  # Define an empty keyword for default table
            elif choice == '2':
                keyword = input("Enter a new word to generate custom Vigenere table: ")
                vigenere_table = generate_custom_vigenere_table(keyword)
            else:
                print("Invalid choice!")
        elif choice == '4':
            print("Bye you sneaky butthole!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
