import PySimpleGUI as sg
from constant import *
import math

width = 800
height = 600

DefaultWindowProps = dict(
    title=TITLE,
    size=(width, height),
    font=("Helvetica", 14),
    margins=(16, 16),
    element_padding=(10, 10),
    background_color="#6FCAC1"
)


def GUItitle(text):
    return sg.Text(text, size=(width, 4), font=("Helvetica", 25), justification='center')


def GUIButton(text):
    return sg.Button(text, size=(100, 2), font=("Helvetica", 14))


def showStartWindow():
    sg.theme('LightGreen')

    layout = [[GUItitle(WELCOME)], [GUIButton(START)], ]

    result, events = sg.Window(
        layout=layout,
        **DefaultWindowProps,
    ).read(close=True)

    print(result)
    return result != None
