# Type Trainer
# This code was generated using ChatGPT (for help with tkinter and nltk modules)

import tkinter # for the window
from tkinter import messagebox # for the popups
import random # selecting random words
import time # for time stats at the end of the game
import nltk # word library

values = [] # keep track of the random words we generate from nltk
attempts = [] # keep track of user attempts to compare with values later
missed_words = "" # keep track of missed words to display as a string later
score = 0 # correct words
index = 0 # keep track of what word we are on


def get_amount():
     try:
          amount = int(entry_box.get()) # turn string input into integer
     except Exception: # if input couldn't be an integer
          window.destroy()
          messagebox.showerror("Type Trainer", "An error occurred while submitting amount.")

          return # exit the function

     start_game(amount)


def start_game(amount):
     global start, values
     
     if amount > 100 or amount < 1: # if the number is too high or low
          window.destroy()
          messagebox.showerror("Type Trainer", "Keep amount between 1 and 100")

          return # exit the function

     start_button.destroy() # remove the start button
     word_label.pack() # add the word label in instead of the start button

     entry_box.delete(0, tkinter.END) # clear the amount number in the input box

     for i in range(amount):
          values.append(random.choice(nltk.corpus.words.words())) # append a random word to are values list from nltk library

     window.bind("<Return>", new_word) # every time enter/return is pressed, we check and get a new word
     new_word() # call the function

     start = time.time() # start a timer


def new_word(*args): # *args allows function calling from an event or normally
     global index, score, missed_words, values

     if index != 0: # do not add an attempt for the first input (it was our amount)
          attempts.append(entry_box.get()) # otherwise add it to check later

     if len(attempts) == len(values): # if we have gotten through the set amount of words
          window.destroy() # close the window

          for i in range(len(attempts)): # for each attempt
               if attempts[i] == values[i]: # check it with the real array
                    score += 1 # add one if the strings match
               else:
                    missed_words += f"\n\n{attempts[i]}\n{values[i]}" # but if not, add a string to the missed words
          
          end = time.time() # stop the timer
          response = messagebox.askyesno("Type Trainer", f"Score: {score} / {len(attempts)}\n\nTime: {round(end - start, 2)} seconds\n\nAverage Seconds: {round((end - start) / len(attempts), 2)}\n\nSee which ones you missed?") # show a popup with the score, time, and seconds per word

          if response: # if the user presses yes
               messagebox.showinfo("Type Trainer", f"Words you missed:\n(incorrect, correct)\n{missed_words}") # show our missed words string
          
          return # close out of function so we don't get another word
     
     entry_box.delete(0, tkinter.END) # if we haven't finished, clear the word in the input box

     word_label.config(text=f"{index + 1}: {values[index]}") # make the text show next word in the random word array

     index += 1 # increase our index manually for the next word


window = tkinter.Tk() # create a window
title_label = tkinter.Label(window, text="Welcome to Type Trainer!", font=("Comic Sans MS", 18, "bold")) # create title label
entry_box = tkinter.Entry(window) # create our input box
word_label = tkinter.Label(window, font=("Comic Sans MS", 12)) # create our word label
start_button = tkinter.Button(window, text="Enter amount of words in the box, then click to start", font=("Comic Sans MS", 8), width=40, height=1, command=get_amount) # create the button for the start

window.title("Type Trainer") # window name

title_label.pack(pady=10, padx=40) # add our title
entry_box.pack(pady=8) # add our input box
start_button.pack(pady=15) # add our start button

window.mainloop() # show our window