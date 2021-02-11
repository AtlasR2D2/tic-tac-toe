dimensions = 3

game_board = [["" for i in range(dimensions)] for x in range(dimensions)]
board_ords = [["" for i in range(dimensions)] for x in range(dimensions)]
k=0
CROSS = "x"
KNOT = "o"

def set_winner(p1_ind, p2_ind, p1_count,p2_count,dimension_x):
    if p1_count == dimension_x:
        return p1_ind
    elif p2_count == dimension_x:
        return p2_ind
    else:
        return None


def check_game_over_condition(game_board_x, player_1, player_2, avail_moves):
    game_over_condition = False
    winner = None
    # Horizontal Win
    for i in range(len(game_board_x)):
        p1_count = 0
        p2_count = 0
        dimension = len(game_board_x[i])
        for j in range(len(game_board_x[i])):
            if game_board_x[i][j] == player_1:
                p1_count += 1
            elif game_board_x[i][j] == player_2:
                p2_count += 1
            else:
                pass
        # Check Game Over Condition
        game_over_condition = (p1_count == dimension or p2_count == dimension)
        if game_over_condition:
            winner = set_winner(player_1, player_2, p1_count, p2_count, dimension)
            # print("Exit condition H")
            break
    if not game_over_condition:
        # Vertical Win
        for j in range(len(game_board_x)):
            p1_count = 0
            p2_count = 0
            dimension = len(game_board_x)
            for i in range(len(game_board_x)):
                if game_board_x[i][j] == player_1:
                    p1_count += 1
                elif game_board_x[i][j] == player_2:
                    p2_count += 1
                else:
                    pass
            # Check Game Over Condition
            game_over_condition = (p1_count == dimension or p2_count == dimension)
            if game_over_condition:
                winner = set_winner(player_1, player_2, p1_count, p2_count, dimension)
                # print("Exit condition V")
                break
        if not game_over_condition:
            # Diagonal Win
            coords=[]
            # Top left down Scenario
            starting_x_cor = 0
            scenario = []
            for row in range(len(game_board_x)):
                scenario.append([row, starting_x_cor+row])
            coords.append(scenario)
            #Bottom left up Scenario
            starting_x_cor = len(game_board_x)-1
            scenario = []
            for row in range(len(game_board_x)):
                scenario.append([row, starting_x_cor-row])
            coords.append(scenario)
            # print(coords)
            dimension = len(game_board_x)
            for scenario in coords:
                p1_count = 0
                p2_count = 0
                for coord in scenario:
                    if game_board_x[coord[0]][coord[1]] == player_1:
                        p1_count += 1
                    elif game_board_x[coord[0]][coord[1]] == player_2:
                        p2_count += 1
                    else:
                        pass
                    # Check Game Over Condition
                    game_over_condition = (p1_count == dimension or p2_count == dimension)
                if game_over_condition:
                    winner = set_winner(player_1, player_2, p1_count, p2_count, dimension)
                    # print("Exit condition D")
                    break
        else:
            pass
    else:
        pass
    if not game_over_condition:
        # Check if there are still available moves
        if len(avail_moves) == 0:
            # No more moves available | Declare Cat's Game.
            game_over_condition = True
            winner = "Cat's Game."
    # RETURN GAME OVER CONDITION
    return {"game_over": game_over_condition, "winner": winner}

#Populate initial board_ords
for i in range(len(board_ords)):
    for j in range(len(board_ords[i])):
        k += 1
        board_ords[i][j] = k


def show_game_board(game_board_x):
    """Prints the game board to console"""
    print("Game Board")
    for row in range(len(game_board_x)):
        print(f"Row {row}: {game_board_x[row]}")

def show_avail_moves(board_ords_x):
    """Prints the game board to console"""
    print("Available Moves")
    for row in range(len(board_ords_x)):
        print(f"Row {row}: {board_ords_x[row]}")

def determine_available_moves(board_ords):
    """returns a one dimensional list of available moves"""
    moves_list = []
    for row in range(len(board_ords)):
        for col in range(len(board_ords[row])):
            if str(board_ords[row][col]).isnumeric():
                moves_list.append(board_ords[row][col])
    return moves_list


def process_move_gb(player_choice, move, board_ords_x, game_board_x):

    """marks the move on the game board and returns the updated game board"""
    for i in range(len(board_ords_x)):
        for j in range(len(board_ords_x[i])):
            if board_ords_x[i][j] == move:
                # Mark move on game board
                game_board_x[i][j] = player_choice
    return game_board_x


def process_move_bo(move, board_ords_x):
    """Removes the choice from board ords and returns the updated board ords"""
    for i in range(len(board_ords_x)):
        for j in range(len(board_ords_x[i])):
            if board_ords_x[i][j] == move:
                # Clear board ordinal
                board_ords_x[i][j] = ""
    return board_ords_x


# game_board[0][0] = CROSS
# game_board[1][0] = CROSS
# game_board[2][0] = CROSS

# print(check_win_condition(game_board))

Players = [
    {"player_name": "Player 1",
     "player_choice": None
     },
    {"player_name": "Player 2",
     "player_choice": None
     }
]

print("Welcome to Tic Tac Toe Game!\n")

# Ask Player 1 to Select knots or crosses
valid_choice = False
while not valid_choice:
    Player_1_Choice = input(f"Player 1: Choose either Knots or Crosses ({KNOT},{CROSS}): ").lower()
    if Player_1_Choice in [KNOT, CROSS]:
        valid_choice = True
    else:
        print("Please enter a valid choice.")

# Log Player Choices
Players[0]["player_choice"] = Player_1_Choice
if Player_1_Choice == KNOT:
    Players[1]["player_choice"] = CROSS
else:
    Players[1]["player_choice"] = KNOT

#Notify players of what they are playing with
print(f"\n{Players[0]['player_name']} will play {Players[0]['player_choice']}. {Players[1]['player_name']} will play {Players[1]['player_choice']}")

# Commence Game
print("\nLet's Play!")
game_over = False
active_player_ord = 0
while not game_over:
    show_game_board(game_board)
    available_moves = determine_available_moves(board_ords)
    show_avail_moves(board_ords)
    # Player_x to play
    valid_move = False
    while not valid_move:
        try:
            move_x = int(input(f"{Players[active_player_ord]['player_name']}, state your next move (Available Moves {available_moves}): "))
            if move_x in available_moves:
                game_board = process_move_gb(Players[active_player_ord]["player_choice"], move_x, board_ords, game_board)
                board_ords = process_move_bo(move_x, board_ords)
                valid_move = True
            else:
                print("Please select a valid move.")
        except:
            print("Please select a valid move.")
        finally:
            pass

    available_moves = determine_available_moves(board_ords)
    # Check game_status | Process Move
    game_status = check_game_over_condition(game_board_x=game_board, player_1=Players[0]["player_choice"], player_2=Players[1]["player_choice"],avail_moves=available_moves)
    if game_status["game_over"]:
        game_over = True
    else:
        # Switch Players
        active_player_ord = int(not bool(active_player_ord))

# Determine Winner Message
if game_status["winner"] == Player_1_Choice:
    winner_msg = f"{Players[0]['player_name']} Wins!"
elif game_status["winner"] in [KNOT, CROSS]:
    winner_msg = f"{Players[1]['player_name']} Wins!"
else:
    winner_msg = game_status["winner"]


# Show Players Game Outcome
show_game_board(game_board)
print(f"Game Over. Result: {winner_msg}")