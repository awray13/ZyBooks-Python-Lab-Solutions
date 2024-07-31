"""
Using the template code provided, fix the code that is vulnerable to least privilege. You will need to change the permission level appropriately for each level of users as follows:

    Admin should have permission to Read, Write, and Execute

    Users should have permission to Read

You will need to fix the grant permission method.

"""
import os
import stat

def admin(filename):
    # Admins get full permissions: read, write, execute
    os.chmod(filename, stat.S_IRWXU)
    

def user(filename):
    # Users get read permissions only
    os.chmod(filename, stat.S_IRUSR)
    

def grant_permission(is_admin, filename):
    if is_admin:
        admin(filename)
    else:
        user(filename)

    check_permission(filename)

def check_permission(filename):
    # Check if file path exists
    path_exists = os.access(filename, os.F_OK)
    print("The path exists:", path_exists)
    
    # Check if User has Read Access
    read_access = os.access(filename, os.R_OK)
    print("Access to read the file:", read_access)
    
    # Check if User has Write Access
    write_access = os.access(filename, os.W_OK)
    print("Access to write the file:", write_access)
    
    # Check if User has Execute Permission
    execute_access = os.access(filename, os.X_OK)
    print("Check if path can be executed:", execute_access)

    if read_access:
        # Open and read the file
        with open(filename) as file:
            file.read()
    else:        
        # In case can't access the file    
        print("Cannot access the file")

    with open("output_file.txt", 'w') as f:
        if write_access:
            f.write("I have write privilege.\n")

if __name__ == '__main__':
    filename = input()
    name = input()
    user_list = []

    with open(filename) as f:
        for line in f:
            fields = line.split()
            user_list.append(fields[0])
            
        is_admin = name in user_list

    grant_permission(is_admin, filename)
