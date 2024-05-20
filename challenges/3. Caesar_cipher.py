"""
One of the first known examples of encryption was used by Julius Caesar.
Read more about here: https://en.wikipedia.org/wiki/Caesar_cipher
Create a program that implements a Caesar cipher.
Allow the user to supply the message and the shift amount, and then display the shifted message.
Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift
values so that it can be used both to encode messages and decode messages.

# When you have done the code, try to decrypt the following:
ldl ndj zcdl wdl id iwxcz ndj wpkt xbegdkts ndjg eniwdc hzxaah rdcvgpijapixdch
"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = input('Enter a word: ')
word = word.lower()
shifts = int(input('How shifts you want?: '))


def Julius(word, shifts, letters):
    encript = ''
    for i in word:
        if i in letters:
            pos = letters.index(i)
            new = (pos+shifts) % len(letters)
            encript += letters[new]
        else:
            encript += i
    return encript


print(f'Encrypt: {Julius(word, shifts, letters)}')


def Julius_reverse(word, shifts, letters):
    return Julius(word, -shifts, letters)


word_encript = input('Enter the word you want to decrypt: ')
decrypt = Julius_reverse(word_encript, shifts, letters)
print(f'Decript: {decrypt}')

