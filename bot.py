#!/usr/bin/python3
import telebot
from Constants import Token, receiver_id
import pyscreenshot as ImageGrab
from PIL import Image
import os

os.environ['DISPLAY'] = ':0'
bot = telebot.TeleBot(Token)
filename = '/home/vladimir/PycharmProjects/screen_bot/screen.png'

def make_screenshot():
    image = ImageGrab.grab()
    image.save(filename)


def send_image(user_id):
    image = open(filename, 'rb')
    bot.send_document(user_id, image)
    image.close()


if __name__ == '__main__':
    make_screenshot()
    send_image(receiver_id)

