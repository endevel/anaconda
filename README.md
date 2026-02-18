# Anaconda

Программная реализация игры в шашки (draughts) на Python.

## Обзор

Anaconda — это библиотека для работы с игровой логикой шашек, включающая:

- **Игровая логика** — представление доски, фигур и ходов
- **Генерация ходов** — алгоритмы для нахождения допустимых ходов
- **Парсинг позиций** — поддержка FEN/PDN форматов
- **Графический интерфейс** — PyQt6 GUI для игры
- **Игровой движок** — в разработке

## Требования

- Python 3.12 или выше

## Установка

### Клонирование репозитория

```bash
git clone <repository-url>
cd anaconda
```

### Установка зависимостей

```bash
pip install -e .
```

## Использование

### Запуск приложения

```bash
python -m anaconda
```

### Использование библиотеки

```python
from athena.damboard.damboard import Damboard
from athena.movegen.movegen import MoveGen
from athena.core.player import Player
from athena.core.move import Move

# Создание доски
board = Damboard()
board.setup("start")  # Начальная позиция

# Генерация ходов
movegen = MoveGen(board, Player.WHITE)
moves: list[Move] = []
movegen(moves)

for move in moves:
    print(f"{move.from_square} -> {move.to_square}")
```

## Тестирование

### Запуск всех тестов

```bash
pytest
```

### Запуск тестов с покрытием кода

```bash
pytest --cov=athena
```

### Запуск тестов с отладочным выводом

```bash
pytest -v -s
```

## Разработка

### Линтинг и форматирование

Проверка кода:

```bash
ruff check .
```

Форматирование кода:

```bash
ruff format .
```

### Проверка типов

```bash
mypy athena/
```

## Структура проекта

```
.
├── anaconda/            # Точка входа приложения
├── athena/              # Основная библиотека
│   ├── core/            # Базовые типы данных
│   ├── damboard/        # Представление доски
│   ├── movegen/         # Генерация ходов
│   ├── pdn/             # Парсинг PDN/FEN
│   └── engine/          # Игровой движок (в разработке)
├── gui/                 # Графический интерфейс (PyQt6)
├── tests/               # Модульные тесты
├── pyproject.toml       # Конфигурация проекта
└── README.md            # Документация
```

## Лицензия



## Вклад


