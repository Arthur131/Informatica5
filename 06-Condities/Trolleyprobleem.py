invoer = input('trek je aan de hendel:')
invoer2 = input('duw je de man:')

if invoer == 'ja' and invoer2 == 'ja':
    print(2)

elif invoer == 'nee' and invoer2 == 'ja':
    print(1)

elif invoer == 'ja' and invoer2 == 'nee':
    print(1)

elif invoer == 'nee' and invoer2 == 'nee':
    print(5)


