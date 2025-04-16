import datetime
import os

class Logger:

    log_dir = 'СЮДА ВСТАВИТЬ ПУТЬ ДО СОЗДАННОЙ ДИРЕКТОРИИ logs'
    file_name = f'log_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
    file_path = os.path.join(log_dir, file_name)

    @classmethod
    def _ensure_log_dir_exists(cls):
        """создает директорию для логов, если её нет"""
        os.makedirs(cls.log_dir, exist_ok=True)

    @classmethod
    def write_log_to_file(cls, data: str):
        try:
            cls._ensure_log_dir_exists()
            with open(cls.file_path, 'a', encoding='utf-8') as logger_file:
                logger_file.write(data)
        except Exception as e:
            print(f"ошибка записи в лог: {e}")

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = (
            "\n-----\n"
            f"тест: {test_name}\n"
            f"время начала теста: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"название начального метода: {method}\n"
            '\n'
        )

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):

            data_to_add = (
                f"время конца теста: {str(datetime.datetime.now())}\n"
                f"название конечного метода: {method}\n"
                f"URL: {url}\n"
                "\n-----\n"
            )

            cls.write_log_to_file(data_to_add)