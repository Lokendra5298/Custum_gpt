# yourscript.py

def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

def create_personalized_message(name, age):
    message = f"Hello, {name}! "
    if age.isdigit():
        age = int(age)
        if age < 18:
            message += "You are underage."
        else:
            message += f"You are {age} years old."
    else:
        message += "Age should be a numeric value."
    return message

def main():
    print("Welcome to Your Script!")

    # Get user input
    user_name, user_age = get_user_input()

    # Create and display personalized message
    personalized_message = create_personalized_message(user_name, user_age)
    print(personalized_message)

if __name__ == "__main__":
    main()
