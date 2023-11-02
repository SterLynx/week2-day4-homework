address_book = {}

def add_to_address_book():
    while True:
        name = input("Enter a name (or 'quit' to exit): ")
        
        if name == 'quit':
            break
        
        if name == 'clear':
            address_book.clear()
            print("Address book cleared.")
            continue
        
        address = input("Enter the address: ")
        address_book[name] = address

add_to_address_book()

print("Address Book:")
for name, address in address_book.items():
    print(f"Name: {name}, Address: {address}")