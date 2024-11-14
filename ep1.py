while True:
    opt = (input('>')).lower()
    if opt == 'help':
        print("1.Start")
        print("2.Stop")
        print("3.Quit")
    elif opt == 'start':
        print('Engine has started')
    elif opt == 'stop':
        print('Engine has stopped')
    elif opt == 'quit':
        break
    else:
        print("i dont understard")