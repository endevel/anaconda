from athena.core.board_square import BoardSquare
from athena.core.move import Move, Piece
from athena.core.player import Player
from athena.damboard.damboard import Damboard


class MoveGen:

    def __init__(self, player: Player):
        self.move_list: list[Move] = []
        self.player = player
        if player == Player.WHITE:
            self.move_dirs = (-1, -3)
        else:
            self.move_dirs = (1, 3)
        self.dirs = (-1, 1, -3, 3)

    def calc_dist(self, dir: int, board: Damboard) -> int:
        return dir // abs(dir) * board.width + dir

    def try_man_captures(self, board: Damboard, square: int):
        for dir in self.dirs:
            dist = self.calc_dist(dir, board)
            next_square: int = square + dist
            if board[next_square].is_opponent(self.player):
                dest_square = next_square + dist
                if board[dest_square].is_empty:
                    kill_piece: Piece = Piece(
                        value=board[next_square], index=next_square
                    )
                    move: Move = Move(
                        from_square=square,
                        to_square=dest_square,
                        piece_before=board[square],
                        piece_after=board[square],
                        kill_pieces=[kill_piece],
                    )
                    save_piece = board[next_square]
                    board[next_square] = BoardSquare.TAKEN
                    self.generate_man_captures(board, square, dir, move)
                    board[next_square] = save_piece

    def generate_man_captures(
        self, board: Damboard, square: int, from_dir: int, move: Move
    ):
        for dir in self.dirs:
            dist = self.calc_dist(dir, board)
            if dist == -from_dir:
                continue
            next_square: int = square + dist
            if board[next_square].is_opponent(self.player):
                dest_square = next_square + dist
                if board[dest_square].is_empty:
                    kill_piece: Piece = Piece(
                        value=board[next_square], index=next_square
                    )
                    move.kill_pieces.append(kill_piece)
                    move.to_square = dest_square
                    save_piece = board[next_square]
                    board[next_square] = BoardSquare.TAKEN
                    self.generate_man_captures(board, next_square, dir, move)
                    board[next_square] = save_piece
                else:
                    break
            else:
                break

    def try_king_captures(self, board: Damboard, square: int):
        pass

    def generate_man_moves(self, board: Damboard, square: int):
        for dir in self.move_dirs:
            dist = self.calc_dist(dir, board)
            next_square: int = square + dist
            if board[next_square].is_empty:
                piece_after = board[square]
                if piece_after.is_white and next_square in board.top_promo_squares:
                    piece_after = piece_after.promote()
                elif piece_after.is_black and next_square in board.bottom_promo_squares:
                    piece_after = piece_after.promote()
                move: Move = Move(
                    from_square=square,
                    to_square=next_square,
                    piece_before=board[square],
                    piece_after=piece_after,
                )
                self.move_list.append(move)

    def generate_king_moves(self, board: Damboard, square: int):
        for dir in self.dirs:
            dist = self.calc_dist(dir, board)
            for ndx in range(1, board.max_move_length):
                next_square: int = square + dist * ndx
                if board[next_square].is_empty:
                    move: Move = Move(
                        from_square=square,
                        to_square=next_square,
                        piece_before=board[square],
                        piece_after=board[square],
                    )
                    self.move_list.append(move)
                else:
                    break

    def generate_captures(self, board: Damboard):
        for square in board:
            piece: BoardSquare = board[square]
            if piece.is_empty or piece.owner != self.player:
                continue
            if piece.is_man:
                self.try_man_captures(board, square)
            else:
                self.try_king_captures(board, square)

    def generate_moves(self, board: Damboard):
        for square in board:
            piece: BoardSquare = board[square]
            if piece.is_empty or piece.owner != self.player:
                continue
            if piece.is_man:
                self.generate_man_moves(board, square)
            else:
                self.generate_king_moves(board, square)

    def generate_all_moves(self, board: Damboard):
        self.move_list.clear()
        self.generate_captures(board)
        if len(self.move_list) == 0:
            self.generate_moves(board)
