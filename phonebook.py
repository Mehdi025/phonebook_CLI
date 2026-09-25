import json 

# ---------- Load contacts from file ----------
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}


# ---------- Show menu ----------
def show_menu():
    print("\n--- Phonebook ---")
    print("1. Add contact")
    print("2. Search contacts")
    print("3. Delete contacts")
    print("4. Show all")
    print("5. Save & Exit")


# ---------- Main loop ----------
while True:
    show_menu()
    choice = input("Choose: ")

    # ---------- Add contact ----------
    if choice in ("1", "۱"):
        name = input("Name of contact: ").strip()
        if not name:
            print("❌ Name cannot be empty.")
            continue

        while True:
            phone = input("Phone (7-15 digits): ").strip()
            cleaned = phone.replace("+", "").replace(" ", "").replace("-", "")
            
            if not cleaned.isdigit():
                print("❌ Phone must contain only digits. Try again.")
            elif not (7 <= len(cleaned) <= 15):
                print("❌ Phone must be between 7 and 15 digits. Try again.")
            else:
                break

        contacts[name] = phone
        print("✅ Contact added.")

    # ---------- Search ----------
    elif choice in ("2", "۲"):
        name = input("Name to search: ").strip()
        if name in contacts:
            print(f"📞 {name}: {contacts[name]}")
        else:
            print("❌ Contact not found.")

    # ---------- Delete ----------
    elif choice in ("3", "۳"):
        name = input("Name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("🗑️ Contact deleted.")
        else:
            print("❌ Contact not found.")

    # ---------- Show all ----------
    elif choice in ("4", "۴"):
        if not contacts:
            print("📭 No contacts yet.")
        else:
            for name in sorted(contacts):
                print(f"📞 {name}: {contacts[name]}")

    # ---------- Save & Exit ----------
    elif choice in ("5", "۵"):
        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
        print("💾 Saved!")
        print("👋 Bye!")
        break

    # ---------- Invalid option ----------
    else:
        print("❌ Not ready yet.")