import PySimpleGUI as sg  # Part 1 - The import
from text_to_speech import *

sg.theme('DarkPurple')


def input_win():
    # Define the window's contents
    layout = [[sg.Text("Enter the receivers mail address")],  # Part 2 - The Layout
              [sg.Input()],
              [sg.Button('Ok')]]

    # Create the window
    window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True)  # Part 3 - Window Defintion

    # Display and interact with the Window
    event, values = window.read()  # Part 4 - Event loop or Window.read call
    window.close()
    return values[0]
    # Finish up by removing from the screen


def disp_win(val):
    text(sg.Popup(val, no_titlebar=True, button_type=5, any_key_closes=True, grab_anywhere=True))
