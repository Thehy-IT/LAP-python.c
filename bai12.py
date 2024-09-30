'''12: Một phần mềm yêu cầu người dùng nhập username và password để đăng ký. Hãy
viết chương trình yêu cầu người dùng nhập vào username và password sau đó kiểm tra tính
hợp lệ của chúng như sau:
- Username có 6 ký tự bao gồm các ký tự thường và số.
- Password sẽ bao gồm: chữ cái thường, chữ cái in hoa, số, ký tự đặc biệt(!, @, #, $,
%, ^, &, *). Độ dài của password sẽ nằm trong khoảng từ 6 đến 12.'''
import re

def kiem_tra_username(username):
    # Kiểm tra username có độ dài 6 và chỉ chứa ký tự thường và số
    if len(username) == 6 and re.match("^[a-z0-9]+$", username):
        return True
    return False

def kiem_tra_password(password):
    # Kiểm tra độ dài của password từ 6 đến 12 ký tự
    if not (6 <= len(password) <= 12):
        return False

    # Kiểm tra password có ít nhất 1 chữ cái thường
    if not re.search("[a-z]", password):
        return False

    # Kiểm tra password có ít nhất 1 chữ cái in hoa
    if not re.search("[A-Z]", password):
        return False

    # Kiểm tra password có ít nhất 1 số
    if not re.search("[0-9]", password):
        return False

    # Kiểm tra password có ít nhất 1 ký tự đặc biệt
    if not re.search("[!@#$%^&*]", password):
        return False

    return True

# Yêu cầu người dùng nhập vào username và password
username = input("Nhập username (6 ký tự thường hoặc số): ")
password = input("Nhập password (6-12 ký tự, bao gồm chữ thường, chữ hoa, số, ký tự đặc biệt): ")

# Kiểm tra tính hợp lệ của username
if kiem_tra_username(username):
    print("Username hợp lệ.")
else:
    print("Username không hợp lệ. Username phải có 6 ký tự thường hoặc số.")

# Kiểm tra tính hợp lệ của password
if kiem_tra_password(password):
    print("Password hợp lệ.")
else:
    print("Password không hợp lệ. Password phải chứa 6-12 ký tự bao gồm ít nhất 1 chữ cái thường, 1 chữ cái in hoa, 1 số và 1 ký tự đặc biệt (!, @, #, $, %, ^, &, *).")
