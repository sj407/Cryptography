def encrypt(txt):

    split_txt = txt.split()
    cipher_key = len(split_txt)

    lower_letters = 'abcdefghijklmnopqrstuvxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_key = {}
    upper_key = {}
    lower_cnt = 0
    upper_cnt = 0

    for i in lower_letters:
        lower_key[i] = lower_letters[(lower_cnt + cipher_key) % len(lower_letters)]
        lower_cnt += 1

    for i in upper_letters:
        upper_key[i] = upper_letters[(upper_cnt + cipher_key) % len(upper_letters)]
        upper_cnt += 1 

    
    caesar_result = ''

    for i in txt:
        if i.isupper():
            if i in upper_key:
                caesar_result += upper_key[i]
            else:
                caesar_result += i 
        else:
            if i in lower_key:
                caesar_result += lower_key[i]
            else:
                caesar_result += i

    ghp_result = ''

    codes = {
        'a': 'z','b': 'y','c': 'x','d': 'w',
        'e': 'v','f': 'u','g': 't','h': 's','i': 'r','j': 'q','k': 'p','l': 'o','m': 'n','n': 'm','o': 'l',
        'p': 'k','q': 'j','r': 'i','s': 'h','t': 'g','u': 'f','v': 'e','w': 'd','x': 'c','y': 'b','z': 'a',
    }

    for i in caesar_result:
        if i.isupper():
            ghp_result += codes[i.lower()].upper() 
        elif i.islower():
            ghp_result += codes[i]
        else:
            ghp_result += i

    ascii_result = []

    for i in ghp_result:
        ascii_result.append(str(ord(i)))

    return "-".join(ascii_result)

def decrypt(txt):

    split_txt = txt.split('-')
    ascii_result = []

    for i in split_txt:
        ascii_result.append(chr(int(i)))

    ghp_result = ''

    codes = {
        'a': 'z','b': 'y','c': 'x','d': 'w',
        'e': 'v','f': 'u','g': 't','h': 's','i': 'r','j': 'q','k': 'p','l': 'o','m': 'n','n': 'm','o': 'l',
        'p': 'k','q': 'j','r': 'i','s': 'h','t': 'g','u': 'f','v': 'e','w': 'd','x': 'c','y': 'b','z': 'a',
    }

    for i in "".join(ascii_result):
        if i.isupper():
            ghp_result += codes[i.lower()].upper()
        elif i.islower():
            ghp_result += codes[i]
        else:
            ghp_result += i

    cipher_key = len(ghp_result.split())

    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_key = {}
    upper_key = {}
    lower_cnt = 0
    upper_cnt = 0

    for i in lower_letters:
        lower_key[i] = lower_letters[(lower_cnt + cipher_key) % len(lower_letters)]
        lower_cnt += 1 

    for i in upper_letters:
        upper_key[i] = upper_letters[(upper_cnt + cipher_key) % len(upper_letters)]
        upper_cnt += 1

    lower_dec = {}
    upper_dec = {}

    for i in lower_key:
        lower_dec[lower_key[i]] = i 

    for i in upper_key:
        upper_dec[upper_key[i]] = i 

    caesar_result = ''

    for i in ghp_result:
        if i.isupper():
            if i in upper_dec:
                caesar_result += upper_dec[i] 
            else:
                caesar_result += i 
        else:
            if i in lower_dec:
                caesar_result += lower_dec[i]
            else:
                caesar_result += i 

    return caesar_result 

if __name__ == '__main__':

    text = input('Enter the text:')
    option = input('Encryption or decryption:').lower()

    if option == 'encrypt' or option == 'encryption':
        print(encrypt(text))
    elif option == 'decrypt' or option == 'decryption':
        print(decrypt(text))
    else:
        print('Option not available')