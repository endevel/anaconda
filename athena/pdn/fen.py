from athena.core.board_square import BoardSquare
from athena.core.player import Player


class Fen:
    def __init__(self):
        self._start_color = Player.WHITE
        self._pieces: dict[int, BoardSquare] = {}

    def _parse_pieces(self, fen: str):
        piece: BoardSquare = BoardSquare.empty
        if fen[0].upper() == "W":
            piece = BoardSquare.white_piece
        elif fen[0].upper() == "B":
            piece = BoardSquare.black_piece
        fen = fen.replace(fen[0], "")
        last_char = fen[-1]
        if last_char == ".":
            fen = fen[:-1]

        pieces: list[str] = fen.split(",")
        for piece_str in pieces:
            if piece_str[0].upper() == "K":
                piece = piece.promote()
                piece_str = piece_str.replace(piece_str[0], "")
            square_ndx = int(piece_str)
            self._pieces[square_ndx] = piece

    def parse(self, position: str):
        items: list[str] = position.split(":")
        self._start_color = Player.WHITE if items[0].upper() == "W" else Player.BLACK
        for item in items[1:]:
            self._parse_pieces(item)

    @property
    def start_color(self) -> Player:
        return self._start_color

    @property
    def pieces(self) -> dict[int, BoardSquare]:
        return self._pieces
