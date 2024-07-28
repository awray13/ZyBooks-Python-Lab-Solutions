"""
Using the template code provided, fix the code that is vulnerable to least privilege. You will need to change the permission level appropriately for each level of users as follows:

    Admin should have permission to Read, Write, and Execute

    Users should have permission to Read

You will need to fix the grant permission method.

"""
import os
import stat

def admin(filename, admin):
    return admin
    
def user(filename, user):
    return user    
    
def grant_permission(name_list, filename):
    # FIXME - Fix the permission level for each user
    for name in name_list:
        if admin(filename, name):
            os.chmod(filename, stat.S_IRWXU)
        elif user(filename, name):
            os.chmod(filename, stat.S_IRUSR)

    check_permission(filename)

    return True

def check_permission(filename):
    # Check if file path exists
    path1 = os.access(filename, os.F_OK)
    print("The path exists:", path1)
    # Check if User has Read Access
    path2 = os.access(filename, os.R_OK)
    print("Access to read the file:", path2)
    # Check if User has Write Access
    path3 = os.access(filename, os.W_OK)
    print("Access to write the file:", path3)
    # Check if User has Execute Permission
    path4 = os.access(filename, os.X_OK)
    print("Check if path can be executed:", path4)

    if os.access(filename, os.R_OK):
    	# open txt file as file
    	with open(filename) as file:
    		file.read()
            
    else:
        #in case can't access the file	
        print("Cannot access the file")
        with open("output_file.txt", 'w') as f:
            if os.access(filename, os.W_OK):
                f.write("I have write privilege.\n")
    
if __name__ == '__main__':
    filename = input()
    name = input()
    k = []
    result = False

    with open(filename) as f:
        for line in f:
            fields = line.split()
            k.append(fields[0])
            
        for lineNum in range(len(k)):
            if name in k[lineNum]:
                result = True
                name_result = name
                
        if result:
            admin(filename, name)
        else:
            user(filename, name)

    grant_permission(k, filename)