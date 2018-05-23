import time

def TS(str):
    for letter in str:
        print(letter,end='')
        time.sleep(0.1)

TS("Hi !\nToday I'm gonna show you how to simulate typing in Python\nTyping...\n")
time.sleep(2)
x = input('Do you want to learn ?(y,n):')
if(x == 'y'):
    TS("#Just Follow Me#\nimport time\ndef Type_Slow(str):\n    for letter in str:\n        print(letter,end='')\n        time.sleep(0.05)\nType_Slow('Your Text')")
elif(x == 'n'):
    quit()
    
