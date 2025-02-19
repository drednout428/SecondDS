import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_missing_value_report(missing_values):
    try:
        report = f"Отчет о пропущенных значениях:\n{missing_values}"
        logging.info("Отчет о пропущенных значениях сгенерирован.")
        return report
    except Exception as e:
        logging.error(f"Ошибка при создании отчета: {e}")
        raise