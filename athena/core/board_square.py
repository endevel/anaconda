from enum import Enum

from athena.core.player import Player


class BoardSquare(Enum):
    """Represents the state of a square on the draughts board.

    Each square can be empty, contain a piece (man or king), or have a special state
    like taken or out of bounds.
    """

    EMPTY = 0
    WHITE_PIECE = 1
    WHITE_KING = 2
    BLACK_PIECE = 3
    BLACK_KING = 4
    TAKEN = 5
    OUT_OF_BOUNDS = 6

    def promote(self):
        """Promote a man piece to a king piece.

        Returns:
            BoardSquare: The king variant of the piece (WHITE_KING or BLACK_KING).

        Raises:
            ValueError: If the square does not contain a man piece that can be promoted.
        """
        if self == BoardSquare.WHITE_PIECE:
            return BoardSquare.WHITE_KING
        elif self == BoardSquare.BLACK_PIECE:
            return BoardSquare.BLACK_KING
        else:
            raise ValueError("Only man pieces can be promoted")

    @property
    def is_white(self) -> bool:
        """Check if the square contains a white piece.

        Returns:
            bool: True if the square contains a white piece (man or king), False otherwise.
        """
        return (
            True
            if self == BoardSquare.WHITE_PIECE or self == BoardSquare.WHITE_KING
            else False
        )

    @property
    def is_black(self) -> bool:
        """Check if the square contains a black piece.

        Returns:
            bool: True if the square contains a black piece (man or king), False otherwise.
        """
        return (
            True
            if self == BoardSquare.BLACK_PIECE or self == BoardSquare.BLACK_KING
            else False
        )

    @property
    def is_empty(self) -> bool:
        """Check if the square is empty.

        Returns:
            bool: True if the square is empty, False otherwise.
        """
        return self == BoardSquare.EMPTY

    @property
    def is_man(self) -> bool:
        """Check if the square contains a man piece (not a king).

        Returns:
            bool: True if the square contains a man piece (white or black), False otherwise.
        """
        return self == BoardSquare.WHITE_PIECE or self == BoardSquare.BLACK_PIECE

    @property
    def is_king(self) -> bool:
        """Check if the square contains a king piece.

        Returns:
            bool: True if the square contains a king piece (white or black), False otherwise.
        """
        return self == BoardSquare.WHITE_KING or self == BoardSquare.BLACK_KING

    @property
    def owner(self) -> Player:
        """Get the player who owns the piece on this square.

        Returns:
            Player: The player who owns the piece (Player.WHITE or Player.BLACK).

        Raises:
            ValueError: If the square does not contain a piece that can have an owner.
        """
        if self.is_white:
            return Player.WHITE
        elif self.is_black:
            return Player.BLACK
        else:
            raise ValueError("Invalid square")

    def is_opponent(self, player: Player) -> bool:
        """Check if the square contains an opponent piece.

        Args:
            player (Player): The player to check against.

        Returns:
            bool: True if the square contains an opponent piece, False otherwise.
        """
        return self.owner != player
