def print_author():
    # Импорт load_dotenv.
    from dotenv import load_dotenv 

    # Импорт библиотеки для работы с окружением.
    import os  

    # Загрузка переменных из .env
    load_dotenv(dotenv_path='/Users/yury/ООП/tema_4/tema_4_3/data.env')

    # Теперь переменные доступны через os.environ
    author = os.getenv('AUTHOR')

    print(f"Автор проекта: {author}")

# Вызов функции
print_author()