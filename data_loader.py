import pandas as pd
import logging
from ucimlrepo import fetch_ucirepo

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
def load_spambase_data():
    #Загружает датасет spambase из UCIMLRepo.
    try:
        logging.info("Загрузка датасета spambase...")
        spambase = fetch_ucirepo(id=94)
        X = spambase.data.features
        y = spambase.data.targets
        logging.info("Датасет успешно загружен!")
        return X, y
    except Exception as e:
        logging.error(f"Ошибка загрузки датасета: {e}")
        raise FileNotFoundError("Не удалось загрузить датасет.")
def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        logging.error(f"Файл {file_path} не найден.")
        raise

def load_json(file_path):
    try:
        return pd.read_json(file_path)
    except ValueError:
        logging.error(f"Ошибка при чтении JSON файла {file_path}.")
        raise