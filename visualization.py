import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def plot_histogram(data, column, bins=30):
    # гистограмма для указанного столбца
    try:
        plt.figure(figsize=(10, 6))
        plt.hist(data[column], bins=bins, color='blue', edgecolor='black')
        plt.title(f'Гистограмма для {column}')
        plt.xlabel(column)
        plt.ylabel('Частота')
        plt.show()
        logging.info(f"Гистограмма для {column} успешно построена.")
    except Exception as e:
        logging.error(f"Ошибка при построении гистограммы: {e}")
        raise

def plot_scatter(data, x_col, y_col):
    #диаграмма рассеяния между двумя столбцами
    try:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data[x_col], y=data[y_col])
        plt.title(f'Диаграмма рассеяния: {x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()
        logging.info(f"Диаграмма рассеяния между {x_col} и {y_col} построена.")
    except Exception as e:
        logging.error(f"Ошибка при построении диаграммы рассеяния: {e}")
        raise