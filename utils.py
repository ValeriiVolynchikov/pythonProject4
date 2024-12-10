import json
import os


def load_transactions(file_path):
    """Загрузить транзакции из JSON-файла."""
    if not os.path.isfile(file_path):
        return []  # Если файл не существует, вернуть пустой список

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)  # Попытка загрузить данные из файла
            if isinstance(data, list):  # Проверка, является ли загруженные данные списком
                return data
            return []  # Если данные не список, вернуть пустой список
        except json.JSONDecodeError:
            return []  # Если ошибка при декодировании JSON, вернуть пустой список


# Тестирование функции
def test_load_transactions():
    file_path = "data/operations.json"
    transactions = load_transactions(file_path)
    print("Loaded transactions:", transactions)


# Запустите тест
if __name__ == "__main__":
    test_load_transactions()
