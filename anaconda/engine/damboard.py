from anaconda.engine.damtypes import BoardSize, BoardSquareStatus


class Position:
    """Сохраняет номера полей, занятых фигурами
    """
    def __init__(self) -> None:
        self.white_squares = set()
        self.black_squares = set()
    
    def append_piece(self, piece: BoardSquareStatus) -> None:
        """Добавляет в set номер поля, занятого фигурой 
        """
        