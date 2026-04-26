from athena.core.board_size import BoardSize
from athena.core.player import Player


class MoveDir:
    def __init__(self, player: Player, board_size: BoardSize):
        self.player = player
        if player == Player.WHITE:
            self.__man_move_dirs: tuple[int, ...] = (
                -board_size.width - 1,
                -board_size.width - 3,
            )
        elif player == Player.BLACK:
            self.__man_move_dirs: tuple[int, ...] = (
                board_size.width + 1,
                board_size.width + 3,
            )
            self.__king_move_dirs: tuple[int, ...] = (
                -board_size.width - 1,
                -board_size.width - 3,
                board_size.width + 1,
                board_size.width + 3,
            )
        self.__reflect_dirs: dict[int, int] = {
            -board_size.width - 1: board_size.width + 3,
            -board_size.width - 3: board_size.width + 1,
            board_size.width + 1: -board_size.width - 3,
            board_size.width + 3: -board_size.width - 1,
        }
        self.__capture_dirs: tuple[int, ...] = (
            -board_size.width - 1,
            -board_size.width - 3,
            board_size.width + 1,
            board_size.width + 3,
        )

        self.__king_move_dirs: tuple[int, ...] = (
            -board_size.width - 1,
            -board_size.width - 3,
            board_size.width + 1,
            board_size.width + 3,
        )

    def man_move_dirs(self) -> tuple[int, ...]:
        return self.__man_move_dirs

    def king_move_dirs(self) -> tuple[int, ...]:
        return self.__king_move_dirs

    def capture_dirs(self) -> tuple[int, ...]:
        return self.__capture_dirs

    def reflect_dir(self, dir: int) -> int:
        return self.__reflect_dirs[dir]
