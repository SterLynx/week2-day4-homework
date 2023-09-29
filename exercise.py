from IPython.display import clear_output

while True:
    ask = input('input something: ')
    if ask == 'quit':
        break
    elif ask == 'clear':
        clear_output()