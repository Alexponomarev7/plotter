def writingcode(commands, path):
    f_w = open('w', path + "output.pl")
    
    print('pencilUp()', file=f_w)
    for i in commands:
        print(str(i), file=f_w)
    
    f_w.close()
    