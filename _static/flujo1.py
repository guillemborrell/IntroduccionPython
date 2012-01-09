from random import choice

if __name__ == '__main__':
    guess = choice([True,False])
    if guess:
        print 'Cara'
    else:
        print 'Cruz'
