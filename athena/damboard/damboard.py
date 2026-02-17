from athena.core.board_size import BoardSize
from athena.core.board_square import BoardSquare
from athena.damboard.board_map import BoardMap
from athena.pdn.fen import Fen


class Damboard:

    def __init__(self, size: BoardSize = BoardSize.STANDARD):
        self.__top_promo_squares: set[int] = set()
        self.__bottom_promo_squares: set[int] = set()
        self.__board_map = BoardMap(size)
        self.__squares_map: list = [-1 for _ in range(size.height * size.width // 2)]
        self.__init_squares_map()
        self.__init_promote_squares()
        self.setup(size.start_position)

    def __getitem__(self, key: int) -> BoardSquare:
        return self.__board_map[key]

    def __setitem__(self, key: int, value: BoardSquare) -> None:
        self.__board_map[key] = value

    def __init_squares_map(self):
        pos = 0
        for ndx in range(self.__board_map.height * self.__board_map.width):
            if self.__board_map[ndx] == BoardSquare.EMPTY:
                self.__squares_map[pos] = ndx
                pos += 1

    def __init_promote_squares(self):
        for ndx in range(self.__board_map.width // 2 - 1):
            self.__top_promo_squares.add(self.__squares_map[ndx])

        start: int = len(self.__squares_map) - self.__board_map.width // 2 + 1
        for ndx in range(start, start + self.__board_map.width // 2 - 1):
            self.__bottom_promo_squares.add(self.__squares_map[ndx])

    def setup(self, position: str) -> None:
        fen = Fen()
        self.clear()
        fen.parse(position)
        for square_ndx, piece in fen.pieces.items():
            self.add_piece(piece, self.__squares_map[square_ndx - 1])

    def clear(self) -> None:
        self.__board_map.clear()

    def add_piece(self, piece: BoardSquare, square: int) -> None:
        self.__board_map.add_piece(piece, square)

    def remove_piece(self, square: int) -> None:
        # piece: BoardSquare = self.__board_map[square]
        self.__board_map.remove_piece(square)

    def move_piece(self, from_square: int, to_square: int) -> None:
        # piece: BoardSquare = self.__board_map[from_square]
        self.__board_map.move_piece(from_square, to_square)

    @property
    def height(self):
        return self.__board_map.height - 2

    @property
    def width(self):
        return self.__board_map.width - 2

    @property
    def top_promo_squares(self):
        return self.__top_promo_squares

    @property
    def bottom_promo_squares(self):
        return self.__bottom_promo_squares

    @property
    def max_move_length(self):
        return self.__board_map.height - 2
