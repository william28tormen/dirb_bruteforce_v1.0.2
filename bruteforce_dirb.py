import requests
import sys

def brute(url, wordlist):

    for word in wordlist:
        try:
            url_final = '{}/{}'.format(url, word.strip())
            response = requests.get(url_final)
            code = response.status_code

            if code != 404:
                print('{} -- {}'.format(url_final, code))

        except KeyboardInterrupt:
            sys.exit(0)

        except Exception as error:
            print(error)

if __name__ == "__main__":

    print('-------------------------------------------------------------')
    print('Brute Force Dirb - n0body v1.0.2')
    print('-------------------------------------------------------------')

    url = sys.argv[1]
    wordlist = sys.argv[2]

    with open(wordlist, 'r') as file:
        wordlist = file.readlines()

    print('-------------------------------------------------------------')
    print('Brute Force Dirb - n0body v1.0.2')
    print('-------------------------------------------------------------')
    brute(url, wordlist)
    print('-------------------------------------------------------------')
    print('Brute Force finalizado!')
    print('-------------------------------------------------------------')