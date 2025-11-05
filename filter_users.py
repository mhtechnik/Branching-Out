import json

def load_users(path="users.json"):
    """Lädt die Benutzerliste aus der JSON-Datei."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def filter_users_by_name(name):
    users = load_users()
    filtered_users = [user for user in users if str(user.get("name", "")).lower() == name.lower()]
    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    """Filtert alle Nutzer mit genau diesem Alter (int)."""
    users = load_users()
    filtered_users = [user for user in users if int(user.get("age", -1)) == age]
    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('name' or 'age'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_input = input("Enter an age (number): ").strip()
        try:
            age_to_search = int(age_input)
        except ValueError:
            print("Please enter a valid number for age.")
        else:
            filter_users_by_age(age_to_search)

    else:
        print("Filtering by that option is not yet supported.")

