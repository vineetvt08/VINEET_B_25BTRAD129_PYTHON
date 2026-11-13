class ContactBook:
    def __init__(self):
        # List to store multiple contact dictionaries
        self.contacts = []

    def add_contact(self, name, phone, email, category="Personal"):
        """Add a new contact to the contact book."""
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print(f"\n[Error] Contact '{name}' already exists.")
                return False
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'category': category
        }
        self.contacts.append(new_contact)
        print(f"\n[Success] Contact '{name}' added successfully.")
        return True

    def search_contact(self, query):
        """Search for contacts by name or phone number."""
        results = [
            c for c in self.contacts
            if query.lower() in c['name'].lower() or query in c['phone']
        ]
        return results

    def update_contact(self, name, phone=None, email=None, category=None):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                if phone:
                    contact['phone'] = phone
                if email:
                    contact['email'] = email
                if category:
                    contact['category'] = category
                print(f"\n[Success] Contact '{name}' updated successfully.")
                return True
        print(f"\n[Error] Contact '{name}' not found.")
        return False

    def delete_contact(self, name):
        """Delete a contact by name."""
        for i, contact in enumerate(self.contacts):
            if contact['name'].lower() == name.lower():
                deleted = self.contacts.pop(i)
                print(f"\n[Success] Contact '{deleted['name']}' deleted successfully.")
                return True
        print(f"\n[Error] Contact '{name}' not found.")
        return False

    def display_contacts(self):
        """Display all stored contacts in a tabular format."""
        if not self.contacts:
            print("\n[Info] The contact book is currently empty.")
            return
        print("\n" + "=" * 65)
        print(f"{'NAME':<15} | {'PHONE':<12} | {'EMAIL':<22} | {'CATEGORY':<10}")
        print("=" * 65)
        for c in self.contacts:
            print(f"{c['name']:<15} | {c['phone']:<12} | {c['email']:<22} | {c['category']:<10}")
        print("=" * 65 + "\n")

def main():
    book = ContactBook()
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone: ").strip()
            email = input("Enter Email: ").strip()
            category = input("Enter Category (Personal/Client/Internal/Vendor): ").strip() or "Personal"
            book.add_contact(name, phone, email, category)
            
        elif choice == '2':
            query = input("Enter name or phone number to search: ").strip()
            results = book.search_contact(query)
            if results:
                print(f"\nFound {len(results)} matching contact(s):")
                for c in results:
                    print(f"-> {c['name']} | Phone: {c['phone']} | Email: {c['email']} | Category: {c['category']}")
            else:
                print("\n[Info] No matching contacts found.")
                
        elif choice == '3':
            name = input("Enter the name of the contact to update: ").strip()
            print("Leave blank if you do not want to change a field.")
            phone = input("Enter new phone (optional): ").strip() or None
            email = input("Enter new email (optional): ").strip() or None
            category = input("Enter new category (optional): ").strip() or None
            book.update_contact(name, phone=phone, email=email, category=category)
            
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ").strip()
            book.delete_contact(name)
            
        elif choice == '5':
            book.display_contacts()
            
        elif choice == '6':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
