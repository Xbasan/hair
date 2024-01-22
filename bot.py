from flask import Flask, render_template, request

import json
import telebot

app = Flask(__name__)


def footer():
    with open('./templates/test.html') as file:
        response = file.read( )
    return response

