import os
from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        function_name = old_function.__name__
        arguments = f"Аргументы: {args}, {kwargs}"

        try:
            with open("main.log", 'a', encoding='cp1251') as log_file:
                log_file.write(f"Дата и время вызова функции: {current_time}\n")
                log_file.write(f"Имя функции: {function_name}\n")
                log_file.write(f"{arguments}\n")

                result = old_function(*args, **kwargs)

                log_file.write(f"Результат вызова функции: {result}\n")
                log_file.write("\n")

            return result

        except Exception as e:
            with open("main.log", 'a', encoding='cp1251') as log_file:
                log_file.write(f"Ошибка в функции {function_name}: {str(e)}\n")
                log_file.write("\n")

            raise

    return new_function


def logger_1(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            function_name = old_function.__name__
            arguments = f"Аргументы: {args}, {kwargs}"

            try:
                abs_path = os.path.abspath(path)

                dir_path = os.path.dirname(abs_path)
                if dir_path and not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                with open(abs_path, 'a', encoding='cp1251') as log_file:
                    log_file.write(f"Дата и время вызова функции: {current_time}\n")
                    log_file.write(f"Имя функции: {function_name}\n")
                    log_file.write(f"{arguments}\n")

                    result = old_function(*args, **kwargs)

                    log_file.write(f"Результат вызова функции: {result}\n")
                    log_file.write("\n")

                return result

            except Exception as e:
                with open(abs_path, 'a',encoding='cp1251') as log_file:
                    log_file.write(f"Ошибка в функции {function_name}: {str(e)}\n")
                    log_file.write("\n")

                raise

        return new_function

    return __logger


@logger_1('main.log')
def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item