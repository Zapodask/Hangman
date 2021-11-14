from os import system
import random


def startGame():
    word = ''
    display = ''
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    missed = 0
    choices = ''

    with open('words.txt', 'r') as f:
        words = f.read()

        word = random.choice(words.split())

    l = len(word)
    while l > 0:
        display = display + '_ '
        l -= 1

    while missed < 10:
        print(display)

        res = ''

        while True:
            res = input('Choose a letter: ')

            if len(res) > 1:
                print('Just one letter')

            elif len(res) < 1:
                pass

            elif res not in list(validLetters):
                print('just letters')
            
            elif res in list(choices):
                print('Already chosen letter')

            else:
                choices = choices + res
                break

        system('cls')

        splittedChoices = list(choices)
        splittedWord = list(word)
        if res in splittedWord:
            for c in splittedChoices:
                t = 0

                for wl in splittedWord:
                    if c == wl:
                        d = list(display)

                        d[t*2] = c

                        display = ''.join(d)

                    t += 1
            
            if '_' not in display:
                return 'You win'

        else:
            missed += 1

        if missed == 1:
            print(
                '       |       ',
                '               ',
                '               ',
                '               ',
                '               ',
                sep='\n'
            )
        elif missed == 2:
            print(
                '       |       ',
                '       O       ',
                '               ',
                '               ',
                '               ',
                sep='\n'
            )
        elif missed == 3:
            print(
                '       |       ',
                '       O       ',
                '       |       ',
                '               ',
                '               ',
                sep='\n'
            )
        elif missed == 4:
            print(
                '       |       ',
                '       O       ',
                '      \|       ',
                '               ',
                '               ',
                sep='\n'
            )
        elif missed == 5:
            print(
                '       |       ',
                '       O       ',
                '      \|/      ',
                '               ',
                '               ',
                sep='\n'
            )
        elif missed == 6:
            print(
                '       |       ',
                '       O       ',
                '      \|/      ',
                '       |       ',
                '               ',
                sep='\n'
            )
        elif missed == 7:
            print(
                '       |       ',
                '       O       ',
                '      \|/      ',
                '       |       ',
                '      /        ',
                sep='\n'
            )
        elif missed == 8:
            print(
                '       |       ',
                '       O       ',
                '      \|/      ',
                '       |       ',
                '      / \      ',
                sep='\n'
            )
        elif missed == 9:
            print(
                '       |       ',
                '     \ O       ',
                '      \|/      ',
                '       |       ',
                '      / \      ',
                sep='\n'
            )
        elif missed == 10:
            print(
                '       |       ',
                '     \ O /     ',
                '      \|/      ',
                '       |       ',
                '      / \      ',
                sep='\n'
            )

            return 'You lose'


def main():
    while True:
        system('cls')
        
        print('Hangman')

        input('Press enter to start')

        response = startGame()

        print(response)

        again = input('Play again?(y/n): ')

        if again != 'y':
            break


if __name__ == '__main__':
    main()
