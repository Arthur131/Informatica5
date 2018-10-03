invoer1 = input('wat doet speler1:')
invoer2 = input('wat doet speler2:')

if invoer1 == 'schaar' and invoer2 == 'blad':
    print('speler 1 wint')
elif invoer1 == 'steen' and invoer2 == 'schaar':
    print('speler 1 wint')
elif invoer1 == 'blad' and invoer2 == 'steen':
    print('speler 1 wint')
elif invoer1 == 'blad' and invoer2 == 'schaar':
    print('speler 2 wint')
elif invoer1 == 'schaar' and invoer2 == 'steen':
    print('speler 2 wint')
elif invoer1 == 'steen' and invoer2 == 'blad':
    print('speler 2 wint')
else:
    print('onbeslist')


