import PySimpleGUI as sg

def getCaesar(PLAIN):
# 秘密鍵
    KEY = 3

    # 以下に、記述してください。
    enc = ""

    for char in list(PLAIN):
        ASCII = ord(char)
        num = ASCII - 97
        num = (num + KEY) % 26
        ASCII = num + 97
        enc += chr(ASCII)

    return enc

def showGUI():
    sg.theme('DarkAmber')   # デザインテーマの設定
    # ウィンドウに配置するコンポーネント
    layout = [  [sg.Text('暗号にしたい文章を入れてください'), sg.InputText()],
                [sg.Button('OK'), sg.Button('キャンセル')] ]

    # ウィンドウの生成
    window = sg.Window('シーザー暗号', layout)

    # イベントループ
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'キャンセル':
            break
        elif event == 'OK':
            print('暗号： ', getCaesar(values[0]))

    window.close()