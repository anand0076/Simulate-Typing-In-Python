import time

def TS(str):
    for letter in str:
        print(letter,end='')
        time.sleep(0.1)

TS("Hi !\nThis is the Typing Simulator\nTyping...\n")
time.sleep(2)
