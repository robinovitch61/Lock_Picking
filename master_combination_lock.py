print("Let's pick your Master lock!", "\n")

count = 0
lefts = []
rights = []
possibilities = []
numTexts = ['first', 'second', 'third',
            'fourth', 'fifth', 'sixth',
            'seventh', 'eighth', 'ninth',
            'tenth', 'eleventh', 'twelth and final']
while count < 12 and len(possibilities) < 5:
    left = None
    right = None
    try:
        left, right = map(float, input("Enter the " + numTexts[count] + \
                                       " sticking point boundaries, separated by a space: ").split())
        print('\n')
        
        if left >= right or left == None or right == None:
            raise Exception('Please ensure you enter the smaller boundary, then the larger, separated by a space.')
            
        if count != 0 and rights[count - 1] >= left:
            raise Exception('Ensure your left boundary is larger than ' + str(rights[count - 1]) + '.')
        
        lefts.append(left)
        rights.append(right)
        if ((left + right) / 2.0).is_integer():
            possibilities.append((left + right) / 2.0)
        count += 1
    
    except Exception as ex:
        print(ex.args[0])
        
if len(possibilities) == 5 and count < 12:
    print("That's all we'll need!")
    
while len(possibilities) != 5 and count == 12:
    print('It seems like you need to correct one or more of these entries...\n')
    print('You only have', str(len(possibilities)), 'possibilities for your third number but there should be 5.', '\n')
    print('Your possibilities are:')
    print(possibilities, '\n')
    try:
        index = int(input('Which sticking boundary entry would you like to correct? Enter a number from 1 - 12: '))
        index -= 1
        if index > 11 or index < 0:
            raise Exception('Please enter an integer between 1 and 12')
    except Exception as ex:
        print(ex.args[0])
          
    try:
        left, right = map(float, input("Correct the " + numTexts[index] + \
                                       " sticking point boundaries, separated by a space: ").split())
        print('\n')

        if left >= right or left == None or right == None:
            raise Exception('Please ensure you enter the smaller boundary, then the larger, separated by a space.')

        if index != 0 and rights[index - 1] >= left:
            raise Exception('Ensure your left boundary is larger than ' + str(rights[index - 1]) + '.')

        lefts[index] = left
        rights[index] = right
        if ((left + right) / 2.0).is_integer() and ((left + right) / 2.0) not in possibilities:
            possibilities.append((left + right) / 2)
            possibilites.sort()
        elif ((left + right) / 2.0) in possibilities:
            print("Sorry, this doesn't add any new information.")
                
    except Exception as ex:
        print(ex.args[0])

correct = 'Y'
while correct == 'Y':
    print("Your current possibilities for the Third number are:")
    print(possibilities, '\n')
    correct = input('Would you like to correct any of these entries? If so, type <Y>: ')
    if correct != 'Y':
        break
    correction = float(input("Enter the possibility you'd like to correct: "))
    try:
        if correction in possibilities:
            possibilities = list(filter(lambda a: a != correction, possibilities))
        else:
            raise Exception('That value is not a possibility.')
    except Exception as ex:
        print(ex.args[0])
