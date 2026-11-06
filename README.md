# Практическая работа: Python + SQLite + SQLAlchemy

## Что находится в проекте
- `main.py` — готовая программа.
- `pyproject.toml` — настройки проекта и зависимость SQLAlchemy.
- `test.db` — создастся автоматически при первом запуске.

## Запуск на Linux

1. Распакуй архив.
2. Открой терминал в папке `pythonDB`.
3. Проверь, что установлен Python 3.10 или новее и `uv`.

Если `uv` уже установлен, выполни:

```bash
uv sync
uv run main.py
```

Если `uv` ещё нет, можно запустить без него:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install sqlalchemy
python main.py
```

## Запуск на Windows

Открой терминал в папке проекта и выполни:

```powershell
uv sync
uv run main.py
```

Либо без uv:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install sqlalchemy
python main.py
```

## Что должно появиться

Сначала будет выведен список 4 групп, затем список 12 студентов с названиями их групп.
Файл `test.db` создаётся автоматически рядом с `main.py`.

Повторный запуск не добавляет дубликаты данных.
