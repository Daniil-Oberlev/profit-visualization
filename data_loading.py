import pandas as pd


def load_dataset(file_path):
    """Функция загрузки датасета из Excel файла."""
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл '{file_path}' пуст.")
        return None
    except pd.errors.ParserError:
        print(f"Ошибка: Не удалось разобрать файл '{file_path}'.")
        return None
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None
