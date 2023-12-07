from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def number_button():
    n1 = KeyboardButton(text='Filial 📍')
    n2 = KeyboardButton(text='Start ✅')
    n4 = KeyboardButton(text='NewPost')
    n3 = KeyboardButton(text='🔙 back')

    design = [
        [n1, n2],
        [n4, n3],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def start_button():
    n1 = KeyboardButton(text="Woman 🧍‍♀️")
    n2 = KeyboardButton(text="Men 🧍‍♂️")
    n3 = KeyboardButton(text="🔙 back")

    design = [
        [n1, n2],
        [n3],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def men_or_women_button():
    n1 = KeyboardButton(text="1 - oy")
    n2 = KeyboardButton(text="2 - oy")
    n3 = KeyboardButton(text="3 - oy")
    n4 = KeyboardButton(text="4 - oy")
    n5 = KeyboardButton(text="🔙 back")

    design = [
        [n1, n2],
        [n3, n4],
        [n5]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def training():
    n1 = KeyboardButton(text="Dushanba")
    n2 = KeyboardButton(text="Seshanba")
    n3 = KeyboardButton(text="Chorshanba")
    n4 = KeyboardButton(text="Payshanba")
    n5 = KeyboardButton(text="Juma")
    n6 = KeyboardButton(text="Shanba")
    n7 = KeyboardButton(text="🔙 back")

    design = [
        [n1, n2, n3],
        [n4, n5, n6],
        [n7]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm
