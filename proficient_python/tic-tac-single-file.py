import random

USERS = {
    'Alice123': 35,
    'BobSmith': 8,
    'Charlie789': 25,
    'Diana007': 12,
    'Ethan2020': 42,
    'Fiona_22': 19,
    'GeorgeH': 5,
    'Hannah_M': 30,
    'Ivan99': 2,
    'JackieQ': 15,
    'Kevin_T': 22,
    'Laura_44': 10,
    'MikeN': 37,
    'NancyT': 17,
    'OscarP': 28,
    'PaulaR': 13,
    'Quincy_56': 44,
    'RebeccaW': 7,
    'SteveH': 3,
    'TinaV': 27,
    'Tommy_87': 31,
    'UrsulaD': 16,
    'Victor_X': 9,
    'Wendy_J': 24,
    'XanderQ': 38,
    'YasminF': 11,
    'ZachT': 45,
    'Ava_28': 29,
    'Ben_J': 18,
    'CarlaS': 33,
    'DanP': 14,
    'EricaK': 21,
    'FrankieM': 39,
    'GinaH': 4,
    'HenryL': 26,
    'IsabelZ': 34,
    'JakeR': 20,
    'KendallC': 40,
    'LiamV': 6
}


def add_user_to_storage(username):
    if username in USERS:
        print(f"User '{username}' already exists.")
    else:
        USERS[username] = 0
        print(f"User '{username}' added.")


def delete_user_from_storage(username):
    if username in USERS:
        del USERS[username]
        print(f"User '{username}' deleted.")
    else:
        print(f"User '{username}' not found.")


def get_all_users_from_storage():
    return USERS


def update_score_to_storage(username):
    if username in USERS:
        USERS[username] += 1
    else:
        print(f"User '{username}' not found. Cannot update score.")


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2 - i] for i in range(3)].count(player) == 3:
        return True
    return False


def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells


def computer_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)


def player_move(board):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if (row, col) in get_empty_cells(board):
            return row, col
        print("Invalid move. Please try again.")


def play(username1, username2):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player, next_player = username1, username2
    player_symbol = {"X": username1, "O": username2}

    while get_empty_cells(board):
        print_board(board)
        if current_player == "computer":
            row, col = computer_move(board)
        else:
            row, col = player_move(board)

        symbol = "X" if current_player == player_symbol["X"] else "O"
        board[row][col] = symbol

        if is_winner(board, symbol):
            print_board(board)
            return current_player

        current_player, next_player = next_player, current_player

    print_board(board)
    print("It's a draw!")
    return None



def welcome_message():
    print("Welcome to Tic Tac Toe!")

def print_menu():
    print("\nMenu:")
    print("1. Add a user")
    print("2. Delete a user")
    print("3. Show all users")
    print("4. Play against the computer")
    print("5. Play against another player")
    print("6. Quit")


def add_user():
    username = input("Enter a username: ")
    add_user_to_storage(username)


def delete_user():
    username = input("Enter a username to delete: ")
    delete_user_from_storage(username)


def show_all_users():
    all_users = get_all_users_from_storage()
    print("\nUsers:")
    for username, score in all_users.items():
        print(f"{username}: {score}")


def play_game(opponent):
    username1 = input("Enter the username of Player 1: ")
    if opponent == "computer":
        username2 = "computer"
    else:
        username2 = input("Enter the username of Player 2: ")

    winner = play(username1, username2)
    if winner:
        print(f"\n{winner} wins!")
        update_score_to_storage(winner)


def main():
    welcome_message()
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            show_all_users()
        elif choice == "4":
            play_game("computer")
        elif choice == "5":
            play_game("player")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
