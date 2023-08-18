import marshal

try:
    while(True):
        myfile = input("Write python file : ")
        if(myfile == 'arret'): break
        open_file = open(myfile, 'r').read()
        compile_file = compile(open_file, '', 'exec')
        encrypt = marshal.dumps(compile_file)
        code = open('New_'+str(myfile), 'w')
        code.write("import marshal\n")
        code.write('exec(marshal.loads('+repr(encrypt)+'))')
        print("The file Encrypted : "+str(myfile))
except IOError:
    print("Unable to open or read the data inthe file.")