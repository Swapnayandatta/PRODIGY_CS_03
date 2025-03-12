import re
def strenght_checker(password):
    if len(password) < 8 :
        return "weak password : Password must be at least 8 character."
    
    if not any(char.isdigit() for char in password):
        return "weak password : Password must containt a digit."
    
    if not any(char.isupper() for char in password):
        return "weak password : Password must containt a Upper case."
    
    if not any(char.islower() for char in password):
        return "weak password : Password must containt a Lower case."
    
    if not re.search(r'[!@#$%^&*(){}<>.?]', password):
        return "Medium password : your password need at least one special character."
    
    return "Your password is strong and secure. "


def pass_check():
    print("Check your password strength with this tool now!")
    while True:
        password = input("Enter your password (if you want to quit then press exit): ")
        if password.lower() == 'exit':
            print("Thanks for using this tool")
            break
        result = strenght_checker(password)
        print(result)

pass_check()