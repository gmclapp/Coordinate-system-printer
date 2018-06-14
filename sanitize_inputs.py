def get_real_number(prompt=None, positive=True, negative=True):
# Gets a real number from the user with an optional prompt. Whether positive
# or negative values should be allowed can be specified with those arguments.

    num_flag = False
    while(not num_flag):
        try:
            number = float(input(prompt))
            if (number >= 0 and positive) or (number <= 0 and negative):
                num_flag = True
            elif(not positive and not negative):
                print("You must allow either positive or negative or both.")
            else:
                pass
            
        except ValueError:
            print("Enter a real number.")
            num_flag = False
            
    return(number)

def get_letter(prompt=None, accept=None):
# Gets a single alpha character that is included in the list 'accept'
# Optionally include a prompt to the user
# omitting the accept list allows all alpha characters.

    flag = False
    while(not flag):
        letter = str(input(prompt))
        if(letter.isalpha() and len(letter) == 1):
            if accept != None:
                for i in accept:
                    if letter == i or accept==None:
                        flag = True
                        break
                    else:
                        pass
            else:
                flag = True

        else:
            pass

    return(letter)
