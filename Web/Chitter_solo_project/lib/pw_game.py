import hashlib

COACH_PASSWORD_HASH = 'cb93b9e2a8713d622ec3f44c646dfe16b84f41f115ce933d0600771b7943b417'

def check_password(password):
    binary_password = password.encode("utf-8")
    hashed_password = hashlib.sha256(binary_password).hexdigest() # This part does the magic
    return hashed_password == COACH_PASSWORD_HASH

while True:
    guess = input("Enter password: ")
    print(f"Trying {guess}...")
    if check_password(guess):
        print("What! You guessed my password!")
        break
    else:
        print("Ha, nice try!")
