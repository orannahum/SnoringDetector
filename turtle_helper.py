# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 01:56:08 2022

@author: Oran Nahum
"""

import turtle
turtle.hideturtle()
s = turtle.getscreen()
turtle.title("Snoring Detector")
turtle.color('white')
# starts at right:

def starting_frame():
    turtle.clear()
    turtle .Screen().bgcolor("green")
    turtle.write("The Snoring Detector\n" 
                 "is ready in a moment...", font=("Arial",
                                    50, "bold"), align="center")


def snoring_detection():
    turtle.clear()
    turtle.Screen().bgcolor("red")
    turtle.write("Snoring", font=("Ariel",
                                    120, "bold"), align="center")



    
def not_snoring_detection():
    turtle.clear()
    turtle .Screen().bgcolor("blue")
    turtle.write("Not Snoring", font=("Arial",
                                    120, "bold"), align="center")


def move_turtle(command,last_command):
    if command == 0 and last_command == 1:
       not_snoring_detection()
    elif command == 1 and last_command == 0:        
        snoring_detection()       
    elif command == 'stop':
        print('Stopping the turtle')
