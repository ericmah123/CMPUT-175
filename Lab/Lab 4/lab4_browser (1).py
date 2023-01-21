#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

def getAction():
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''
    # TO DO: delete pass and write your code here
    user = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    if user == '=' or user == '<' or user == '>' or user == 'q':
        return user
    while user != '=' or '<' or '>' or 'q':
        print('Invalid entry.')
        user = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
        if user == '=' or user == '<' or user == '>' or user == 'q':
            return user


def goToNewSite(currentIndex, websites):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''   
    # TO DO: delete pass and write your code here
    user_url = input("URL: ")
    for i in range(currentIndex + 1, len(websites)):
        websites.pop()
    websites.append(user_url)
    return currentIndex + 1





    
def goBack(currentIndex, websites):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''
    # TO DO: delete pass and write your code here
    if currentIndex == 0:
        print('Cannot go back.')
        return currentIndex
    else:
        subtract = currentIndex - 1
        return subtract




def goForward(currentIndex, websites):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    # TO DO: delete pass and write your code here
    if len(websites) > currentIndex + 1:
        addition = currentIndex + 1
        return addition
    else:
        print('Cannot go forward.')
        return currentIndex



def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
