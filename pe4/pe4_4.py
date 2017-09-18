#als het nieuwewachtwoord aan de eisen voldoet dan print die true anders false.
def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    return False

password = input("Type hier je oude wachtwoord in: ")
password2 = input("Type hier je nieuwe wachtwoord in: ")
print(new_password(password, password2))
