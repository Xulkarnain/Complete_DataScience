import os
#injestion of data
def details():
    kwargs = {}
    for i in range(1):
        key = f"Name{i+1}"
        value = input(f"Enter {key}: ")
        kwargs[key] = value
        
        key = f"phone_no{i+1}"
        value = input(f"Enter {key}: ")
        kwargs[key] = value
        
        key = f"email{i+1}"
        value = input(f"Enter {key}: ")
        kwargs[key] = value
        
        key = f"group{i+1}"
        value = input(f"Enter {key}: ")
        kwargs[key] = value
        
        print("\n")

    return kwargs

#Function for searching by name and group

def search_by_name(name, **kwargs):
    for key, value in kwargs.items():
        if name.lower() in value.lower():
            for key, value in kwargs.items():
                print(f"{key} : {value}")
            break
    else:
        print("Name not found.")

def search_by_grp(group, **kwargs):
    for key, value in kwargs.items():
        if group.lower() in value.lower():
            for key, value in kwargs.items():
                print(f"{key} : {value}")
            break
    else:
        print("Group not found.")

# ==== Main Program ====
path = os.path.join(os.getcwd(), 'database.txt')
with open(path , 'a+') as f:
    ans = input("Do you want to add a new entry? (yes/no): ")
    while ans.lower() == 'yes':
        if ans.lower() == 'yes' :
            data = details()
            for key, value in data.items():
                f.write(f"{key} : {value}\n")
                f.write("\n")
        else:
            print("No new entry added.")
            exit()
        ans = input("Do you want to add a new entry? (yes/no): ")
  
# Part 3: Searching
data_dict = {}
with open(path, "a+") as file:
    lines = file.readlines()
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            data_dict[key.strip()] = value.strip()

    src = input("Do you want to search by name or group? (name/group): ")
    if src.lower() == "name":
        search_by_name(input("Enter name to search: "), **data_dict)
    elif src.lower() == "group":
        search_by_grp(input("Enter group to search: "), **data_dict)
    else:
        print("Invalid option. Please enter 'name' or 'group'.")
        exit()
  