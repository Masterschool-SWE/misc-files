import json

USER_CHOICE = """
Welcome to the shopping list app!
Enter:
- 'a' to add a new product
- 'l' to list all products
- 'b' to mark a product as bought
- 'd' to delete a product
- 'q' to quit
Your choice: """

GROCERIES_FILE = 'groceries.json'


def menu():
    """
    Show the main menu, get user choice and call the wanted function
    Stops only when user quits
    """
    create_file()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_product()
        elif user_input == 'l':
            list_products()
        elif user_input == 'b':
            prompt_bought_product()
        elif user_input == 'd':
            prompt_delete_product()

        user_input = input(USER_CHOICE)


def create_file():
    """
    Creates the json file. If it already exists, do nothing!
    """
    try:
        with open(GROCERIES_FILE, 'x') as file:
            json.dump([], file)  # initialize file as empty list
    except FileExistsError:
        pass


def save_file(products):
    """
    Saves the given product dict to the file, overwriting what's in the file.
    """
    with open(GROCERIES_FILE, 'w') as file:
        json.dump(products, file)


def load_from_file():
    """
    Loads the product dict from the file.
    """
    with open(GROCERIES_FILE, 'r') as json_file:
        return json.load(json_file)


def prompt_add_product():
    """
    Ask the user which product to add and call the insert function
    """
    name = input('Enter the new product name: ')
    quantity = input('Enter the new product quantity: ')
    insert_product(name, quantity)


def insert_product(name, quantity):
    """
    Gets a product name and quantity to add.
    Loads the current file, adds to the dict and re-saves the file.
    """
    products = load_from_file()
    products.append({'name': name, 'quantity': quantity, 'bought': False})
    save_file(products)


def list_products():
    """
    Loads the current file and prints all products to the screen.
    """
    for product in load_from_file():
        bought = 'YES' if product['bought'] == True else 'NO'  # product[3] will be a falsy value (0) if not bought
        print(f"{product['name']} ({product['quantity']} — Bought: {bought}")


def prompt_bought_product():
    """
    Asks the user what product he bought and calls the update function
    """
    name = input('Enter the name of the product you just bought: ')
    mark_product_as_bought(name)


def mark_product_as_bought(name):
    """
    Gets a product name to mark as bought.
    Loads the product file, updates the bought product and re-saves the file.
    """
    products = load_from_file()
    for product in products:
        if product['name'] == name:
            product['bought'] = True
    save_file(products)


def prompt_delete_product():
    """
    Asks the user what product he wants to delete calls the delete function
    """
    name = input('Enter the name of the product you wish to delete: ')
    delete_product(name)


def delete_product(name):
    """
    Gets a product name to remove.
    Loads the product file, removes the wanted product and re-saves the file.
    """
    products = load_from_file()
    products = [product for product in products if product['name'] != name]
    save_file(products)


def main():
    menu()


if __name__ == "__main__":
    main()
