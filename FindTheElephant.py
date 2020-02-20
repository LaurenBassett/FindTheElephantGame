# supply program prolog  
#   Name: Lauren Bassett
#   email: lauren.bassett@uky.edu 
# partner: Benton Girdler bgi229@uky.edu
'''purpose to play games of "Find the Elephant" with the user
pre-conditions: user gives difficulty, test or normal mode, clicks to play the game and to say whether they want to play again or not
post-conditions: prompts for difficulty, test or normal mode, feedback to user when they find the elephant, their score, low score, prompt for playing again or not'''
#import libraries
from math import sqrt
from graphics import *
from random import *

def main():
    #start drawing the screen (title)
    win = GraphWin("Find The Elephant", 500,500)
    #ask if they want test mode or normal mode
    
    #ask level of difficulty 1-10
    #clear screen, draw playing screen
    clear_screen = Rectangle(Point(0,0),Point(500,500))
    clear_screen.setFill("white")
    clear_screen.draw(win)
    #call get_test to decide if running in test mode
    test_mode = get_test(win)
    #do the same thing for difficulty
    difficulty = get_difficulty(win)
    #set the low score to an obscenely high number
    low_score = 99999999
    #set play to true so program runs
    play = True
    #enter the loop
    while play == True:
        #display title
        title = Text(Point(250,50), "Find the Elephant!")
        title.draw(win)
        #create the elephant image and make it random
        elephantX = randrange(5,490)
        elephantY= randrange(5,490)
        pic = Image(Point(elephantX, elephantY), "elephant.gif")
	
        
        #if in test mode draw elephant gif
        if test_mode == True:
            pic.draw(win)
         
        
        #get another click
        #get distance
        #win or you dont
        #if you do, change color
        #if test mode, show distance
        click = win.getMouse()
	
	
	
	
	
	
        click_count = 1
        elephant_center = pic.getAnchor()
        dist = distance(click, elephant_center)
        #the adjusted distance changes distance based on difficulty
        Adj_dist = getAdjustedDistance(difficulty, dist)
        while Adj_dist >= 1.5:
            Adj_dist = getAdjustedDistance(difficulty, dist)
            hint_text = Text(Point(250,475),"ELEPHANT")
            hint_text.setSize(20)
            if Adj_dist < 2:
                hint_text.setTextColor("red")
            elif 2 < Adj_dist <= 4:
                hint_text.setTextColor("pink")
            elif 4 < Adj_dist <=6 :
                hint_text.setTextColor("dark grey")
            elif 6 < Adj_dist <= 9:
                hint_text.setTextColor("light blue")
            else:
                hint_text.setTextColor("blue")
            #draw the click 
            hint_text.draw(win)
            click_circle = Circle(click,5)
            click_circle.setFill("red")
            click_circle.draw(win) 
            #if the test mode is true , show the distance
            if test_mode == True:
                tell_dist = Text(Point(250,400), dist)
                tell_dist.draw(win)            
            click = win.getMouse()
            #increase click counter
            click_count += 1
            elephant_center = pic.getAnchor()
            dist = distance(click, elephant_center)
            if test_mode == True:
                tell_dist.undraw()
            hint_text.undraw()
        #user wins
        win_text = Text(Point(250,460),"You found the elephant!\n Click to Continue")
        win_text.setTextColor("Red")
        win_text.draw(win)
        #draw the elephant
        if test_mode == False:
            pic.draw(win)
            #show the click counter
        if click_count < low_score:
            low_score_result = Text(Point(250,490),"CONGRATS! You have a new low score")
            low_score_result.draw(win)
            low_score = click_count
        #close out    
        win.getMouse()
        clear2 = clear_screen.clone()
        clear2.draw(win)
 
         #ask if the user wants to play again or not       
        play = yes_or_no(win)
    #leave the game
    goodbye = Text(Point(250,250),"Thanks for playing!!!\nclick to close")
    goodbye.setSize(20)
    goodbye.draw(win)
    #close window
    win.getMouse()
    win.close() 
def distance(x,y):
    '''purpose: find the distance between two points
    preconditions: two coordinates
    post conditions: the distance between point x and point y'''
    #seperate into x and y
    x1 = x.getX()
    x2 = y.getX()
    y1 = x.getY()
    y2 = y.getY()
    # plug numbers into formula
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance
def yes_or_no(win):
    '''purpose: get user input on if they want to play again or not
    preconditions: the window is set up
    postconditions: play is set to true or false'''
    #create yes and no boxes and draw them
    yes_box = Rectangle(Point(200,200), Point(250,250))
    no_box = Rectangle(Point(250, 200), Point(300,250))
    yes_box.draw(win)
    no_box.draw(win)
    #assume play again is false
    play_again_flag = False
    play_again_text = Text(Point(250,100), "Play again?")
    play_again_text.draw(win)
    yes_text = Text(Point(225,225), "Yes")
    no_text = Text(Point(275,225), "No")
    yes_text.draw(win)
    no_text.draw(win)
    #get a click and then use the function in_between to get an answer
    answer = win.getMouse()
    clicked_in_box = in_between(Point(200,200), Point(250,250), answer) or in_between(Point(250,200), Point(300,250), answer)
    
    while not clicked_in_box:
        #when they didn't click in the box, loop until they do
        answer = win.getMouse()
        clicked_in_box = in_between(Point(200,200), Point(250,250), answer) or in_between(Point(250,200), Point(300,250), answer)
    #if they clicked into the yes box, set it to true
    if in_between(Point(200,200), Point(250,250),answer) == True:
        play_again_flag = True
    #reset the game
    another_blank_screen = Rectangle(Point(0,0),Point(500,500))
    another_blank_screen.setFill("White")
    another_blank_screen.draw(win)
    return play_again_flag
def in_between(pt1,pt2,user_point):
    ''' purpose: to determine if a user click is between two points
    pre-conditions: two points and a user generated point
    post-conditions: a flag indicating if the point is between the two other points or not'''
    #set flag to false
    flag = False
    #seperate points into x and y
    pt1_x = pt1.getX()
    pt1_y = pt1.getY()
    pt2_x = pt2.getX()
    pt2_y = pt2.getY()
    user_x = user_point.getX()
    user_y = user_point.getY()
	#if the user is between the two x and the two y then set the value to true
    if ((pt1_x < user_x < pt2_x) and (pt1_y < user_y < pt2_y)):
        flag = True

    return flag
def get_test(win):
    '''purpose: to determine if the game will be played in test mode
    Preconditions: the window
    Postconditons: a flag indicating test mode or regular mode'''
    #create entry box and ask if they want it to be in test
    get_test_text = Text(Point(250,50), "Test Mode?\n Type T to enter test mode")
    get_test_text.draw(win)
    input_box = Entry(Point(250,250), 1)
    
    input_box.draw(win)
    #set flag to spot
    test_flag = False
    win.getMouse()
    answer = input_box.getText()
    #if they say t or T then they want it in test mode
    if answer == "T" or answer == "t":
        test_flag = True
    #undraw the boxes and return the result
    input_box.undraw()
    get_test_text.undraw()
    return test_flag
    
def get_difficulty(win):
    '''Purpose: allows user to determine the difficulty
    preconditions: the window
    post conditions: a difficulty value from 1-10'''
    #ask user for difficulty
    text_difficulty = Text(Point(250,50), "Please enter your difficulty from 1-10\n 1 is hardest, 10 is easiest")
    text_difficulty.draw(win)
    input_box = Entry(Point(250,250),2)
    input_box.draw(win)
    win.getMouse()
    #check to make sure its a real number
    difficulty = int(input_box.getText())
    while difficulty < 1 or difficulty > 10:
        invalid_input = Text(Point(250,100), "Super invalid input. Pick 1-10")
        invalid_input.draw(win)
        win.getMouse()
        difficulty = int(input_box.getText())
        invalid_input.undraw()
    #delete the boxes
    input_box.undraw()
    text_difficulty.undraw()
    #return the difficulty value
    return difficulty
def getAdjustedDistance(difficulty, distance):
    '''purpose: get the adjusted distance
    pre-conditions: the difficulty and distance
    post-conditions: the adjusted distance'''
    #take the difficulty and multiply it by 10
    divisor = difficulty*10
    #take the actual distance and divide it by the divisor that they just calculated
    new_distance = distance/ divisor
    
    return new_distance
        
main()
