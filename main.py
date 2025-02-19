from data_loader import load_spambase_data
from data_processing import count_missing_values, fill_missing_values
from reporting import generate_missing_value_report
from visualization import plot_histogram, plot_scatter

def main():
    # Загрузка данных
    try:
        X, y = load_spambase_data()
    except FileNotFoundError as e:
        print(e)
        return

    # Предобработка данных
    missing_values = count_missing_values(X)
    print(generate_missing_value_report(missing_values))

    # Заполнение пропущенных значений
    X_filled = fill_missing_values(X, strategy='median')

    # Визуализация
    plot_histogram(X, column=X.columns[0])
    plot_scatter(X, x_col=X.columns[0], y_col=X.columns[1])

if __name__ == "__main__":
    main()