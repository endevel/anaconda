from copy import deepcopy

from athena.core.board_size import BoardSize
from athena.core.board_square import BoardSquare
from athena.core.move import Move, Piece
from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.movedir import MoveDir


class MoveGen:

    def __init__(self, player: Player, board_size: BoardSize):
        self.move_list: list[Move] = []
        self.player = player
        self.move_dirs = MoveDir(player, board_size)

    def clear_move_list(self):
        self.move_list.clear()

    def is_promo_square(self, board: Damboard, square: int) -> bool:
        if self.player == Player.WHITE:
            return square in board.top_promo_squares
        elif self.player == Player.BLACK:
            return square in board.bottom_promo_squares
        return False

    def generate_moves_for_man(self, board: Damboard, square: int):
        for dir in self.move_dirs.man_move_dirs():
            to_square = square + dir
            if board[to_square].is_empty:
                if self.player == Player.WHITE:
                    if to_square in board.top_promo_squares:
                        self.move_list.append(
                            Move(
                                piece_before=board[square],
                                piece_after=BoardSquare.WHITE_KING,
                                from_square=square,
                                to_square=to_square,
                            )
                        )
                    else:
                        self.move_list.append(
                            Move(
                                piece_before=board[square],
                                piece_after=board[square],
                                from_square=square,
                                to_square=to_square,
                            )
                        )
                else:
                    if to_square in board.bottom_promo_squares:
                        self.move_list.append(
                            Move(
                                piece_before=board[square],
                                piece_after=BoardSquare.BLACK_KING,
                                from_square=square,
                                to_square=to_square,
                            )
                        )
                    else:
                        self.move_list.append(
                            Move(
                                piece_before=board[square],
                                piece_after=board[square],
                                from_square=square,
                                to_square=to_square,
                            )
                        )

    def try_reflect_man_capture(
        self, board: Damboard, square: int, dir: int, move: Move
    ):
        pass

    def try_reflect_king_capture(
        self, board: Damboard, square: int, dir: int, move: Move
    ):
        pass

    def generate_moves_for_king(self, board: Damboard, square: int):
        for dir in self.move_dirs.king_move_dirs():
            for ndx in range(1, board.max_move_length + 1):
                to_square = square + dir * ndx
                if board[to_square].is_empty:
                    self.move_list.append(
                        Move(
                            piece_before=board[square],
                            piece_after=board[square],
                            from_square=square,
                            to_square=to_square,
                        )
                    )
                else:
                    break

    def gen_man_captures(self, board: Damboard, square: int, from_dir: int, move: Move):
        found = False
        for dir in self.move_dirs.capture_dirs():
            if dir == -from_dir:
                continue
            to_square = square + dir
            if board[to_square].is_opponent(self.player):
                next_square = to_square + dir
                if board[next_square].is_empty:
                    found = True
                    next_move = deepcopy(move)
                    piece = board[square]
                    is_promo_square = self.is_promo_square(board, next_square)
                    next_move.to_square = next_square
                    next_move.kill_pieces.append(Piece(board[to_square], to_square))
                    board[to_square] = BoardSquare.TAKEN
                    if is_promo_square:
                        self.try_reflect_man_capture(board, next_square, dir, next_move)
                    else:
                        self.gen_man_captures(board, next_square, dir, next_move)
                    board[to_square] = piece
                    break
                else:
                    break
            else:
                break
        if not found:
            self.move_list.append(move)

    def try_man_capture(self, board: Damboard, square: int, dir: int):
        is_promo_square: bool = False
        to_square = square + dir
        if board[to_square].is_opponent(self.player):
            next_square = to_square + dir
            if board[next_square].is_empty:
                piece = Piece(board[to_square], to_square)
                is_promo_square = self.is_promo_square(board, next_square)
                move = Move(
                    piece_before=board[square],
                    piece_after=board[square],
                    from_square=square,
                    to_square=next_square,
                    kill_pieces=[piece],
                )
                tmp_piece = board[to_square]
                board[to_square] = BoardSquare.TAKEN
                if is_promo_square:
                    self.try_reflect_man_capture(board, next_square, dir, move)
                else:
                    self.gen_man_captures(board, next_square, dir, move)
                board[to_square] = tmp_piece

    def try_king_capture(self, board: Damboard, square: int, dir: int):
        pass

    def generate_captures_for_man(self, board: Damboard, square: int):
        for dir in self.move_dirs.capture_dirs():
            self.try_man_capture(board, square, dir)

    def generate_captures_for_king(self, board: Damboard, square: int):
        for dir in self.move_dirs.capture_dirs():
            self.try_king_capture(board, square, dir)

    def generate_captures(self, board: Damboard):
        for square in board:
            if board[square].owner == self.player:
                if board[square].is_man:
                    self.generate_captures_for_man(board, square)
                elif board[square].is_king:
                    self.generate_captures_for_king(board, square)

    def generate_moves(self, board: Damboard):
        for square in board:
            if board[square].owner == self.player:
                if board[square].is_man:
                    self.generate_moves_for_man(board, square)
                elif board[square].is_king:
                    self.generate_moves_for_king(board, square)

    def generate_all_moves(self, board: Damboard):
        self.clear_move_list()
        self.generate_captures(board)
        if len(self.move_list) == 0:
            self.generate_moves(board)
