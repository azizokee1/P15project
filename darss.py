# from dars import create_table_user,insert_user, login

# n = input("""
# 1.regiter
# 2.login
# >>>""")
# if n=='1':
#     data = dict(
#         first_name = input("Firstname:"),
#         last_name = input("Lastname:"),
#         email = input("Email:"),
#         username = input("Username:"),
#         password = input("Password:"),
#         password1 = input("Confirm Password:"),
#     )
#     res = insert_user(data)
#     if res == 201:
#         print("Success")
# elif n=='2':
#     user = dict(
#         username = input("Username: "),
#         password = input("Password: ")
#     )
#     response = login(user)
#     if response:
#         print("Welcome to our website")
#     else:
#         print("Invalid username or password!")

# if __name__ == '__main__':
#     create_table_user()