import pandas as pd
import numpy as np
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def count_missing_values(df):
    try:
        missing_count = df.isnull().sum()
        logging.info("Подсчет пропущенных значений завершен.")
        return missing_count
    except Exception as e:
        logging.error(f"Ошибка при подсчете пропущенных значений: {e}")
        raise

def fill_missing_values(df, strategy='mean'):
#Заполняет пропущенные значения в DataFrame в зависимости от выбранной стратегии.
    try:
        if strategy == 'mean':
            df = df.fillna(df.mean())
        elif strategy == 'median':
            df = df.fillna(df.median())
        elif strategy == 'mode':
            df = df.fillna(df.mode().iloc[0])
        else:
            raise ValueError("Ошибка в выборе стратегии заполнения.")
        logging.info(f"Пропущенные значения заполнены с использованием : {strategy}")
        return df
    except Exception as e:
        logging.error(f"Ошибка при заполнении пропущенных значений: {e}")
        raise