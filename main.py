#imports
import os
import webbrowser


def say(text_command):
    funcs = ['Открой браузер', 'Запустить команду', 'посчитать']
    
    if text_command == 'погуглить':
        os.system('clear')
        url = input('google: ')
        webbrowser.open_new('google.com/search?q=' + url)

    elif text_command == 'запустить команду':
        os.system('clear')
        while True:
            cmd = input('>>> ')
            os.system(cmd)

            if cmd == 'exit':
                break
    
    elif text_command == 'посчитать':
        os.system('clear')
        print('calculator:')

        culc = eval(input())
        print(culc)
        
    elif text_command == 'выйти':
        print("Пока!")
        quit()
    else:
        print('Я не понимаю')






while True:
    funcs = ['Погуглить', 'Запустить команду', 'Посчитать']
    for i in funcs:
        print('-------------------------------')
        print(i)

    text_command = input().lower()
    say(text_command)
