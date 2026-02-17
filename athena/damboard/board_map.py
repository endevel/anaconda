from athena.core.board_size import BoardSize
from athena.core.board_square import BoardSquare


class BoardMap:
    """
    Машинное представление игрового поля
    Представляет все поля обычной доски плюс дополнитнльный ряд полей
    с каждой из четырех строн которые играют роль полей-ограничителей.

    В данной реализации считается, что белые поля играют роль ограничителей,
    т.е. недоступны для размещения фигур и перемещения.
    В дальнейшем это может быть изменено.
    """

    def __init__(self, size: BoardSize = BoardSize.STANDARD):
        self.__height = size.height + 2
        self.__width = size.width + 2
        self.__board_map: list[BoardSquare] = [
            BoardSquare.OUT_OF_BOUNDS for _ in range(self.__height * self.__width)
        ]
        self.__fill_board_map()

    def __fill_board_map(self):
        for row in range(1, self.height - 1):
            self.__fill_board_row(row)

    def __fill_board_row(self, row_ndx: int):
        for col in range(1, self.width - 1):
            if (col + row_ndx) % 2 != 0:
                ndx = self.__width * row_ndx + col
                self.__board_map[ndx] = BoardSquare.EMPTY

    def __getitem__(self, key: int) -> BoardSquare:
        return self.__board_map[key]

    def __setitem__(self, key: int, value: BoardSquare) -> None:
        self.__board_map[key] = value

    def clear(self) -> None:
        self.__fill_board_map()

    def add_piece(self, piece: BoardSquare, square: int) -> None:
        self.__board_map[square] = piece

    def remove_piece(self, square: int) -> None:
        self.__board_map[square] = BoardSquare.EMPTY

    def move_piece(self, from_square: int, to_square: int) -> None:
        self.__board_map[to_square] = self.__board_map[from_square]
        self.__board_map[from_square] = BoardSquare.EMPTY

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width
