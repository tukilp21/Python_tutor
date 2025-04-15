'''
Engineering smart systems Exam 2024
Author: Rasmus V. Jensen
Date: 05-11-2024
This program checke the input from the user. Certain criterias should be
fulfilled: No numbers, spaces or symbols.
'''


def identify_sentence_freq():
    ''' 
    This function evaluates the input from the user. If input is valied, it determines the 
    frequency of all the letters. This information is then printed to the user.
    Parameters: None 
    Returns: None
    '''
    infoList = []
    numberOfLetters = []
    keepTrackOfLetters = ""
    while True:
        try:
            inputValue = input("Enter something: ")
            inputValue = int(inputValue)

        except ValueError:
            flag = False

            if inputValue.isalpha() == True:  # https://www.w3schools.com/python/ref_string_isalpha.asp
                # The isalpha() is found from here.
                flag = True
                for char in inputValue:
                    if char == char.lower():
                        flag = True
                    else:
                        flag = False
                        break

            if flag == True:
                infoList.append(inputValue)
                for currentLetter in inputValue:
                    count = 0
                    for letter in inputValue:
                        if currentLetter == letter:
                            count += 1
                            keepTrackOfLetters += currentLetter + " "
                    if currentLetter not in keepTrackOfLetters:
                        numberOfLetters.append(count)
        except KeyboardInterrupt:
            print(keepTrackOfLetters)
            print(numberOfLetters)
            print(infoList)


identify_sentence_freq()
