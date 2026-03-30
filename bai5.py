# Sample input: role: admin, action: delete
# role: user, action: write

permissions =  {"admin": ["read", "write", "delete"], "user": ["read"]}

input = input("Nhập role và action của bạn: ")

def action_checker(role_permission):
    parts = role_permission.split(',')

    role = parts[0].split(':')[1].strip().lower()
    action = parts[1].split(':')[1].strip().lower()

    if role in permissions:
        if action in permissions[role]:
            print("Được phép")
        else:
            print("Không được phép")
    else:
        print("Không được phép")

action_checker(input)