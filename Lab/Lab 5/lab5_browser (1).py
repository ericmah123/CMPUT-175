#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from final.stack import Stack

def getAction():
    '''
    Take users input and decides whether the input is valid, based on the four designated entries.
    If the input is not valid then an invalid message is raised.
    '''
    user_url = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    if user_url == '=' or user_url == '<' or user_url == '>' or user_url == 'q':
        return user_url
    else:
        raise print('Invalid entry')



def goToNewSite(current, bck, fwd):
    '''
    This will give the user an option to input a desired site they want to go to.
    '''   
    #delete pass and write your code here
    current_address = input('URL: ')
    # Will clear the fwd list so it does not allow users to go forward if they should not be able to
    fwd.clear()
    # Appends the current site to the bck list so that this can enable the back functionality
    bck.push(current)
    return current_address

def goBack(current, bck, fwd):
    '''
    Write docstring to describe function
    Allows the user to travel back to their previous website
    '''    
    #delete pass and write your code here

    try:
        # Assign this function to a variable
        y = bck.peek()
        # This will remove the currently viewed element in the list, so that when peek
        # is returned it will show the previous website
        bck.pop()
        # Append the current site to forward so that we can enable forward functionality
        fwd.push(current)
        return y
    except Exception:
        print('Cannot go back!')
        return current


def goForward(current, bck, fwd):
    '''
    Allows user to move forward towards a site they were visiting
    '''    
    #delete pass and write your code here
    try:
        # Assign variable to peek
        x = fwd.peek()
        # Will pop the highest index element and returns it
        fwd.pop()
        # Appends to the bck list to enable back functionality
        bck.push(current)
        return x
    except Exception:
        print('Cannot go forward!')
        return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            # print(actionException.args[0])
            pass



        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            #TO DO: add code for the other valid actions ('<', '>', 'q')
            #HINT: LOOK AT LAB 4
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
