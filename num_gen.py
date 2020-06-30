import string
    # ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # ascii_lowercase = 'abcdefghijklm nopqrstuvwxyz'
    # ascii_uppercase = 'ABCDEFGHIJKLM NOPQRSTUVWXYZ'

def gotest(f, t,*num):
    filename = str(f)+'_'+str(t)
    if str(f) == f and str(t) == t:
        if f in string.ascii_lowercase and t in string.ascii_lowercase:
            with open(filename+".lbx","w+") as file:
                print("deleted {} strings".format(len(file.readlines())))
                del file.readlines()[:]
                file.write("\n")
                if num == 1:
                    for letter in list(map(chr, range(ord(f), ord(t)+1))):
                        file.write(letter + '\n')
                else:
                    newstring = ""
                    for lettera in list(map(chr, range(ord(f), ord(t)+1))):
                        for letterb in list(map(chr, range(ord('a'), ord('z')+1))):
                            file.write(lettera+letterb+'\n')
        else:
            with open(filename+".lbx","w+") as file:
                print("deleted {} strings".format(len(file.readlines())))
                del file.readlines()[:]
                file.write("\n")
                if num == 1:
                    for letter in list(map(chr, range(ord(f), ord(t)+1))):
                        file.write(letter + '\n')
                else:
                    newstring = ""
                    for lettera in list(map(chr, range(ord(f), ord(t)+1))):
                        for letterb in list(map(chr, range(ord('A'), ord('Z')+1))):
                            file.write(lettera+letterb+'\n')
    elif int(f) == f and int(t) == t:
        with open(filename+".lbx", "w+") as file:  # для чтения и записи
            print("deleted {} strings".format(len(file.readlines())))
            del file.readlines()[:]
            file.write("\n")
            for number in range(1, t+1):
                file.write(str(number) + '\n')
    print("end")
        

def ui():
    print("from (includes):")
    from_ = input()
    # from_ = 1
    print("to number (including last):")
    to_ = input()
    if from_ in string.ascii_letters:
        print("1 or 2 letters:")
        num_ = int(input())
        gotest(from_,to_,num_)
    else:
        gotest(int(from_),int(to_))
# def connect(): TODO
#     filename1 = str(f)+'_'+str(t)
#     filename2 = str(f)+'_'+str(t)
    # to_ = 10
# for inc in range(5515, 5530):
#     gotest(1, inc)
ui()
