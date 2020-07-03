while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        import random
        keys = ['abruptly', 'bagpipes', 'croquet', 'dizzying', 'espionage', 'fixable',
                'gizmo', 'jelly', 'khaki', 'lucky', 'microwave', 'nightclub', 'ovary',
                'psyche', 'quiz', 'rhythm', 'stronghold', 'transcript', 'unworthy',
                'vaporize', 'waltz', 'xylophone', 'yummy', 'zodiac']
        key = random.choice(keys)
        dashes = len(key)
        w = list(key)
        dash = '-' * dashes
        res = list(dash)
        g = []
        print('H A N G M A N')
        i = 8
        while i > 0:
            if w == res:
                break
            truth = True
            boo = False
            print('\n')
            print(''.join(res))
            l = input("Input a letter: ")
            if len(l) != 1:
                print('You should input a single letter')
            elif not l.islower():
                print('It is not an ASCII lowercase letter')
            else:
                for z in g:
                    if z == l:
                        boo = True
                if boo:
                    print('You already typed this letter')
                    continue
                g.append(l)
                for d in range(dashes):
                    if l == w[d]:
                        res[d] = l
                        truth = False
                if truth:
                    print('No such letter in the word')
                    i -= 1
        if i == 0:
            print('You are hanged!')
            print('The word was {}\n'.format(key))
        else:
            print('You guessed the word!\nYou survived!\n')
    elif menu == 'exit':
        break
    else:
        continue
