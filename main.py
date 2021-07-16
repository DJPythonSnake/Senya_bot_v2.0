#imports
import os
import time
import webbrowser
import server
import client


from time import sleep


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
            os.system("clear")
            break

def num_count():
    os.system('clear')
    print('калькулятор:')

    culc = eval(input())
    print(culc)

def enable_server():
    print("Доступные Wi-Fi сети:")
    os.system("nmcli dev wifi")
    time.sleep(0.5)

    ask_to_connect = input("Подключиться? ('да' или 'нет'): ")

    if ask_to_connect == "да":
        os.system("clear")
        server.init_server()
    else:
        pass

def enable_client():
    os.system("clear")
    print("Поиск сервера...")
    time.sleep(1)

    while True:
        client.client()





print("Приветсвую! Чем я могу помочь?")
time.sleep(2)

while True:
    funcs = ['погуглить', 'запустить команду', 'посчитать', 'запустить сервер', 'найти сервер']
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
    elif text_command == funcs[3]:
        enable_server()
    elif text_command == funcs[4]:
        enable_client()
    elif text_command == 'выйти':
        break
    else:
        print("Я не понимаю") 
