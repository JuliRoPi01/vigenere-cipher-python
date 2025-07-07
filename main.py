ABC = "abcdefghijklmnopqrstuvwxyz"

def main() -> None:
    message: str = get_message()
    key: str = get_key()
    activity: str = get_activity()
    print(vigenere_cipher(message, key, activity))

def get_message() -> str:
    usr_message: str = input("Message: ")
    return usr_message

def get_key() -> str:
    usr_key: str = input("Key: ")
    return usr_key

def get_activity() -> str:
    while True:
        usr_activity: str = input("Encode or Decode (e - d): ").lower()
        if usr_activity == "e" or usr_activity == "d":
            return usr_activity
    

def vigenere_cipher(message, key, activity) -> str:
    code: str = str()
    key_len = len(key)
    j = 0
    upper = False

    for i in range(len(message)):
        char = message[i]
        if char not in ABC and char.lower() in ABC:
            char.lower()
            upper = True

        if char in ABC:
            char_i = ABC.index(char)
            key_char = key[j%key_len]
            key_char_i = ABC.index(key_char)
            if activity == "d":
                key_char_i *= -1
            new_char_i = (char_i + key_char_i)%26
            new_char = ABC[new_char_i]
            if upper:
                new_char.upper()
            code += new_char
            j += 1
        else:
            code += char 

        upper = False
    return code

if __name__ == "__main__":
    main()