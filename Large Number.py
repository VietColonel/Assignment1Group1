def menu(a,b,c):

    def add(a,b):
        if len(a) < len(b) :
            a,b = b,a
        elif len(a) == len(b) and a < b :
            a,b = b,a
        b = '0'*(len(a)-len(b)) + b
        c1 = len(a)-1
        sum = ''
        c4 = 0
        while c1 >= 0 :
            c3 = int(a[c1]) + int(b[c1]) + c4
            if c3 >= 10 and c1 != 0:
                c4 = 1
                c3 = str(c3%10)
            elif c1 == 0 :
                sum = str(c3) + sum
                break
            else:
                c4 = 0
                c3 = str(c3)
            sum = c3 + sum
            c1 -= 1
        return sum

    def sub(a,b):
        if len(a) < len(b) :
            a,b = b,a
        elif len(a) == len(b) and a < b :
            a,b = b,a
        b = '0'*(len(a)-len(b)) + b
        c1 = len(a)-1
        minus = ''
        c4 = 0
        while c1 >= 0 :
            c3 = int(a[c1]) - int(b[c1]) - c4 
            if c3 < 0:
                c3 = str(10+c3)
                c4 = 1
            else: 
                c4 = 0
                c3 = str(c3)
            minus = c3 + minus
            c1 -= 1
        return minus

    def mul(a,b):
        c1 = len(b)-1
        c2 = 0
        keep1 = '0'
        while c1 >= 0 :
            x = 0
            keep = '0'
            while x < int(b[c1]):
                keep =  add(keep,a)
                x += 1
            if x == 0 :
                keep = '0'
            else :
                keep = keep + '0'*c2
            keep1 = add(keep1,keep) 
            c1 -= 1
            c2 += 1
        return keep1


    if c == '1':
        print('Sum of a and b:',add(a,b))
    elif c == '2':
        print('Subtract of a and b:',sub(a,b))
    else: 
        print('Multiple of a and b:',mul(a,b))
if __name__=='__main__':
    while True:    
        try:
            while True:
                print('*'*40)
                print('a)Adding two digit number, choose 1.')
                print('b)Subtracting two digit number, choose 2.')
                print('c)Multiplying two digit number, choose 3.')
                print('d)Exit program, choose 4.')
                c = input('Enter your choice: ')
                if c == '4' : 
                    print('Exiting program. Have a good day!')
                    break
                else:
                    a = input('Enter number a: ')
                    b = input('Enter number b: ')
                    menu(a,b,c)
            break
        except:
            print('Wrong datatype. Go back to the beginning.')

        

            
            

