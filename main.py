# Sample JAMB profile system in Python

# Dictionary to store user profiles
profiles = {}

def create_profile():
    """Create a new JAMB profile"""
    name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    profile = {
        "Name": name,
        "Email": email,
        "Phone": phone
    }
    profiles[email] = profile
    print(f"Profile for {name} created successfully!\n")

def view_profiles():
    """View all JAMB profiles"""
    if not profiles:
        print("No profiles available.\n")
        return
    
    for email, profile in profiles.items():
        print(f"Profile for {profile['Name']}:")
        print(f"Email: {profile['Email']}")
        print(f"Phone: {profile['Phone']}\n")

def update_profile():
    """Update an existing profile"""
    email = input("Enter the email of the profile you want to update: ")
    if email in profiles:
        print("Current details:")
        print(f"Name: {profiles[email]['Name']}")
        print(f"Phone: {profiles[email]['Phone']}")
        new_name = input("Enter new name (or press Enter to skip): ")
        new_phone = input("Enter new phone number (or press Enter to skip): ")
        
        if new_name:
            profiles[email]['Name'] = new_name
        if new_phone:
            profiles[email]['Phone'] = new_phone
            
        print("Profile updated successfully!\n")
    else:
        print("Profile not found.\n")

def menu():
    """Display the menu options"""
    while True:
        print("1. Create JAMB Profile")
        print("2. View All Profiles")
        print("3. Update Profile")
        print("4. Exit")
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            create_profile()
        elif choice == '2':
            view_profiles()
        elif choice == '3':
            update_profile()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
