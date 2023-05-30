from faker import Faker
import string
import random
import os

from dotenv import load_dotenv

load_dotenv()

base_url = "https://" + "b2c.passport.rt.ru"

"""валидные данные"""
valid_name = 'Андрей'
valid_lastname = 'Данилюк'
valid_email = os.getenv('valid_email')
valid_password_phone = os.getenv('valid_password_phone')
valid_password_email = os.getenv('valid_password_email')
valid_password_log = os.getenv('valid_password_log')
valid_phone = os.getenv('valid_phone')
valid_log = os.getenv('valid_log')

"""невалидные данные"""
fake = Faker()
name = "Вальдемар"
lastname = 'Спиридонов'
fake_email = 'And@yandex.ru'
fake_password = 'Aa-123!'
email_without_domain = 'And@yandex.ru'
email_without_dog = 'And@yandex.ru.ru'
invalid_code = '321654'
invalid_phone1 = '+7900239910'
invalid_login = 'Test'
invalid_ls = '12345678910'

def russian_chars(num):
    text = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def english_chars(num):
    text = 'abcdefghijklmnopqrstuvwxyz'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def number_chars(num):
    text = '0123456789'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def chinese_chars(num):
    text = '的一是不了人我在有他这为之大来以个中上们'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def special_chars(num):
    text = '|/!@#$%^&*()-_=+`~?"№;:[]{}'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string


def password_random(num): # т.к. в пароле обязаны быть строчнаяб заглавная и спецсимвол/число, прибавляем их в начало. Остаток символов выбирается рандомно
    text = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    text1 = 'abcdefghijklmnopqrstuvwxyz'
    text2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text3 = '+-/*!&$#?=@<>1234567890'
    rand_string =  ''.join(random.choice(text1) for i in range(1)) + ''.join(random.choice(text2) for i in range(1)) + ''.join(random.choice(text3) for i in range(1)) + ''.join(random.choice(text) for i in range(num-3))
    return rand_string
    return 'x' * n


def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'


def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'



def special_chars():
    return f'{string.punctuation}'