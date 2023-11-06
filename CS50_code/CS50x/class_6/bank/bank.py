#return $100 if user does not enter 'hello', $20 if word starts with 'h', $100 if else

#request greeting
greeting = input('enter greeting: ')

#eliminate any unnecessary spaces
greeting = greeting.strip()

#get only lower cases
greeting = greeting.lower()

#chech if greeting is 'hello'

##print('[0,5]: ', greeting[0:5])

if greeting[0:5] == 'hello':
    print('$0')
elif greeting[0] =='h':
    print('$20')
else:
    print('$100')
