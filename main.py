#imports
import os
import webbrowser


def google_search():
    os.system('clear')
    url = input('google: ')
    webbrowser.open_new('google.com/search?q=' + url)

def cmd_run():
    os.system('clear')
    while True:
        cmd = input('>>> ')
        os.system(cmd)

        if cmd == 'exit':
            break

def num_count():
    os.system('clear')
    print('calculator:')

    culc = eval(input())
    print(culc)






while True:
    funcs = ['погуглить', 'запустить команду', 'посчитать']
    for i in funcs:
        print('-------------------------------')
        print(i)

    text_command = input().lower()
    
    if text_command == funcs[0]:
        google_search()
    elif text_command == funcs[1]:
        cmd_run()
    elif text_command == funcs[2]:
        num_count()
    elif text_command == 'выйти':
        break
    else:
        print("Я не понимаю") 
