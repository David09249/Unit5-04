# Created by: David Wang
# Created on: 20-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit5-04
# This program finds the smallest value in an array

import ui
from numpy import random

my_numbers = []
count = 0

def calculate_average_touch_up_inside(sender):
    global my_numbers
    global count
    user_input = view['input_textfield'].text
    try:
        user_input = int(user_input)
        if user_input >= 0 and user_input <= 100:
            my_numbers.append(user_input)
            view['display_textview'].text = view['display_textview'].text + str(my_numbers[count]) + "\n"
            count = count + 1
            average = 0
            for index in my_numbers:
                average = average + index
            average = average / len(my_numbers)
            view['average_label'].text = "The average of the numbers is: " + str(average)
            view['error_label'].text = ""
        else:
            view['error_label'].text = "Please enter a number between 0 and 100."
    except:
        view['error_label'].text = "Please enter a number. " + str(user_input) + " is not a number."

view = ui.load_view()
view.present('fullscreen')
