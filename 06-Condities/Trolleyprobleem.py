invoer = input('trek je aan de hendel:')
invoer2 = input('duw je de man:')

if invoer == 'ja' and invoer2 == 'ja':
    print(2)

if invoer == 'nee' and invoer2 == 'ja':
    print(1)

if invoer == 'ja' and invoer2 == 'nee':
    print(1)

if invoer == 'nee' and invoer2 == 'nee':
    print(5)


