"""
Simple but useful GUI application telling user to never hard
reset not committed repo
"""
import PySimpleGUI as sg
import pyttsx3 as speech
from PySimpleGUI import Window


def get_window(window_type: str) -> Window:
    """returns a window object basing on the desired type"""
    if window_type == 'choice':
        layout = get_layout('choice')
        window = sg.Window('Enter your choice', layout)
    elif window_type == 'wrong_choice':
        layout = get_layout('wrong_choice')
        window = sg.Window('Wrong choice.', layout)
    else:
        layout = get_layout('do_not_reset!')
        window = sg.Window('Do not reset!', layout)
    return window


def get_layout(layout_type: str) -> list:
    """returns a layout schema for window creation"""
    if layout_type == 'choice':
        layout = \
            [
                [
                    sg.Text('How would you like to be told not to reset '
                            'never committed repo?\n'
                            '1 - with text\n'
                            '2 - with speech:\n')
                ],
                [sg.Input()],
                [sg.Button('OK')]
            ]
    elif layout_type == 'wrong_choice':
        layout = \
            [
                [
                    sg.Text('Wrong choice, please enter again.')
                ],
                [sg.Button('OK')]
            ]
    else:
        layout = \
            [
                [
                    sg.Text('Do not ever make a hard reset on '
                            'never committed repo!')
                ],
                [sg.Button('OK')]
            ]
    return layout


def ask_for_decision() -> str:
    """asks user on how they would like to be informed"""
    while True:
        choice_window = get_window('choice')
        event, decision = choice_window.read()
        if decision[0] in ('1', '2'):
            return decision[0]
        choice_window.close()
        window_wrong_choice = get_window('wrong_choice')
        window_wrong_choice.read()
        window_wrong_choice.close()


if __name__ == '__main__':
    final_decision = ask_for_decision()
    if final_decision == '1':
        get_window('do_not_reset').read()
    if final_decision == '2':
        engine = speech.init()
        engine.say('Do not ever make a hard reset on never committed repo!')
        engine.runAndWait()
