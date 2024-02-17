import os
from dotenv import load_dotenv


load_dotenv()


class Data:                             # тут храним данные в скрытом формате

    # логин
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    # регистрация
    R_LOGIN = os.getenv("R_LOGIN")
    R_PASSWORD = os.getenv("R_PASSWORD")
    R_REPEAT_PASSWORD = os.getenv("R_REPEAT_PASSWORD")

    PHOTO_1 = os.getenv("PHOTO1")
    PHOTO_2 = os.getenv("PHOTO2")
    PHOTO_3 = os.getenv("PHOTO3")
