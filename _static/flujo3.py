from random import choice

if __name__ == '__main__':
    (pos,nil,neg) = (0,0,0)
    while pos<10 and nil<10 and neg<10:
        num = choice([-1,0,1])
        if num == 0:
            nil += 1
        elif num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            print 'Something impossible just happened!'

    print 'Positive:',pos,'Zero:',nil,'Negative:',neg

