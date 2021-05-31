#imports
import webbrowser
import os



def say(text_command):
    funcs = ['Открой браузер', 'Запустить команду', 'посчитать']
    
    if text_command == 'погуглить':
        os.system('clear')
        url = input('google: ')
        webbrowser.open_new('google.com/search?q=' + url)

    elif text_command == 'запустить команду':
        os.system('clear')
        cmd = input('>>> ')
        os.system(cmd)
    
    elif text_command == 'посчитать':
        os.system('clear')
        print('calculator:')

        culc = input()
        list(culc)
        x = int(culc[0])
        y = int(culc[4])
        z = culc[2]

        if z == "+":
            print(x + y)
        elif z == "-":
            print(x - y)
        elif z == "/":
            print(x / y)
        elif z == "*":
            print(x * y)

    else:
        print('Я не понимаю')






while True:
    funcs = ['погуглить', 'Запустить команду', 'посчитать']
    for i in funcs:
        print('-------------------------------')
        print(i)

    text_command = input()
    say(text_command)
