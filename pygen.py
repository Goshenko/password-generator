import string
import random
import hashlib
from argon2 import PasswordHasher

ph = PasswordHasher()


def password_hash_generator(generated_password):
    hash = ph.hash(generated_password)
    print(f"GENERATED HASH: {hash}")

    print("==== ARGON2 VERIFICATION ====")
    if (ph.verify(hash,generated_password)):
        print("==== VERIFICATION SUCCESSFUL ====")
    else:
        print("==== VERIFICATION UNSUCCESSFUL ====")



def program():
    
    while True:
        try:
            password_length  = int(input("ENTER PASSWORD LENGTH: "))
            break
        except ValueError:
            print("\n!! ERROR, INPROPER INPUT !!\n")

    print("|| ENTER CHARACTER SET CHOICE ||")
    print("[1]. Character-Only")
    print("[2]. Numeric-Only")
    print("[3]. Symbolic-Only")
    print("[4]. Character + Numeric")
    print("[5]. Character + Symbolic")
    print("[6]. Numeric + Symbolic")
    print("[7]. Exit")

    character_set = ""

    while True:
        try:
            user_input = int(input("Option Selection: "))
            if user_input == 1:
                character_set += string.ascii_letters
                break
            elif user_input == 2:
                character_set += string.digits
                break
            elif user_input == 3:
                character_set += string.punctuation
                break
            elif user_input == 4:
                character_set += string.ascii_letters + string.digits
                break
            elif user_input == 5:
                character_set += string.ascii_letters + string.punctuation
                break
            elif user_input == 6:
                character_set += string.digits + string.punctuation
                break
            elif user_input == 7:
                break
            else:
                print("\n|| CRITICAL ERROR, TRY AGAIN ||\n")
        except ValueError:
            print("\n!! ERROR, INPROPER INPUT !!\n")

        

    password = []

    for i in range(password_length):
        random_char = random.choice(character_set)
        password.append(random_char)

    print("GENERATED PASSWORD: " + "".join(password))
    password_hash_generator("".join(password))







program()