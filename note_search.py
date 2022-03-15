import os
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('location', help='directorio en el están tus notas')
    parser.add_argument('word', help='palabra a buscar')

    args = parser.parse_args()

    folderpath = args.location
    filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
    all_files = []

    for file in filepaths:
        with open(file, 'r') as f:
            note = f.read()
            if args.word.lower() in note.lower():
                all_files.append(file)
            f.close()

    answer = ''

    while answer != 'exit':

        print('\n')

        for iteration, each in enumerate(all_files):
            print(str(iteration) + " " + each)

        answer = input('\n¿Qué nota querés ver? - Escribí "exit" para salir del script.\n\n')

        if answer.isnumeric() == True:

            with open(all_files[int(answer)], 'r') as f:
                note = f.read()
                print(note)
                print('\n---------------------')
                f.close()

        elif answer != 'exit':
            print('\nError. Ingresá el número de nota que querés ver o "exit" para salir')
            print('--------------------------------------------------------------------')

        else:
            print('\nAdiós. Muchas gracias por usar este script.\n')

if __name__ == "__main__":
    main()
