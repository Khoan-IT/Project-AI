from reversi import Reversi, Coord
from reversiai import ReversiAI
from aihelper import AIHelper, FormatConverter


def attack():

    # 1- Piece difference, frontier disks and disk squares
    # 2 - calculates the difference between current colored tiles
    # 3- calculates the blank Spaces around my tiles
    # 4 - Corner occupancy
    # 5 - CORNER CLOSENESS
    # 6 - Mobility
    player_white = ReversiAI(6)         #white player is 0
    player_black = ReversiAI(2)         #black player is 1
    game = Reversi()
    current_player = 1
    count = 0
    while True:
        board = FormatConverter.game_to_ai_board(game.board)
        if current_player == 1:
            move_b = player_black.get_next_move(board,'b')
            if move_b is not None:
                game.play(move_b)
            current_player = 0
        else :
            move_w = player_white.get_next_move(board,'w')
            if move_w is not None:
                game.play(move_w)
            current_player = 1
        if game.game_state!='In progress':
            print(game.print_board())
            print(game.game_state)
            break
        print(game.print_board())
        print("------------------------------------")
        # if count==1:
        #     break
        # count +=1



if __name__ == '__main__':
    attack()






