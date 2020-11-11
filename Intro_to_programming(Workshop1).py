# The following are code scripts written during the Intro to Programming with Python 
# The goal is to examine how code strutures work.

#Some terms/functions to know:

#Strings/Integers(Int): Computers stores and treats different "types" of data in different ways. We will only 
#concern oursleves with integers and text for now.
#Text is referred to as Strings and _must_ have quotation marks ("") surrounding them.
#Integers are shortened to Int and are _whole_ numbers (no decimal point)
#We make this distinction as some data types can not interact with each other without some conversion, as an example here
#is a _string_ that has some numbers : "hello1234" and here's an _int_ that equals a number : 960. These two values are of 
#different data types and can not interact with each other without conversion ("hello1234" + 960 = ?)

#Functions: functions are single lines of code that return a value for us, or do a task.
#           Functions often take in parameters, which can be thought of as options the function provides
#For instance, the print() function will show text on the console for the user to see. The print() functions takes 
#in a paramter which is the message you want the user to see. i.e if I want the user to see "Hello world", I would type:
#print("Hello world")


# ----------------------------------------------------

#Script 1: Password generator
#This script will ask the use for the number and length of strings to generate, and return
#To achieve this we will:
#1. Take the user's input for the number and length of passwords they desire

#2. Create a list of characters we will randomly choose from

#3. For every password we will choose X characters randomly and put them in a string

#4. We will create Y passwords by repeating ("looping" over) step 3

import random #use a very useful package - packages are code written by others, and come with useful functions we can utilize
              #In our case, this package provides a function to randomly choose a character from a list

#Ask the user for input.
#To prompt the user to insert their input we call the input() function
print("Please insert the length of the desired password:")
length_of_password = int(input()) #Here we ask the user for input; notice the use of the int() function to convert the user input from a string to a number (int)

print("Please insert the number of passwords you want:")
number_of_passwords = int(input())

characters = "abcdefghijklmnopqrstuvwxyz1234567890!@$%&*" #here is the list of characters we will choose from; we can add upper case characters to make the passwords stronger

#To generate a password of length X we need to choose a random charcater from the list X times
#To do the same thing X times in code, we put the code we want to repeat in a loop, as follows

# for i in range(X):  # for loop that will run the code underneath it X times
    #Code we want to be repeated - notice the TAB at the start of the line!

# loop to generate multiple passwords
for j in range(number_of_passwords): # for loop that will run the code underneath it "number_of_passwords" times
    password = "" #start with an empty string to hold our password
    
    # loop to generate one password
    for i in range(length_of_password):  # for loop that will run the code underneath it "length_of_password" times
        #password starts empty ("") but we can add to it with the operator "+="
        #the list of characters can be access using square brackets : [P] where P is the position in the list we want
        #random.randint(0, 40) is a fucntion provided by the package we imported, and randint(x,y) will return a number between 0 and 40
        
        password += characters[random.randint(0, 40)]  # get a character from our list randomly and add it to the password
    
    print(password) #print the password after its generated


# -------------------------------------------------------
#Script 2 : Ceaser Cipher Code
#This script will take in a user message and return it encoding using a ceaser cipher (https://en.wikipedia.org/wiki/Caesar_cipher)
#To achieve this we will:
#1. Take the user's input for the message they want to encrypt and the encryption key

#2. Create a list of characters we will randomly choose from

#3. For every character we will:
#             a. Get its position in the alphabet
#             b. Get the new position of the character using the encryption key
#             c. Add the character from the _new position_ to our encrypted message

#4. Print the encrpyted message

print("Please insert the message u want to encrypt:")
message = input() #Same as above, we ask the user for input, though notice we don't use int() here because the message is indeed a string (text)

print("Please insert the encryption key:")
key = int(input()) #ask for the encryption key

alphabet = "abcdefghijklmnopqrstuvwxyz" #we need this string to find the position of each character in the alphabet

encrypted_msg = "" #starts empty
for i in range(len(message)): #we will repeat this loop as much as the length of the message
    #1. find position of letter
    letter_of_interest = message[i] #here we are getting the character at position i from the user's message
    position_of_letter = alphabet.index(letter_of_interest) #here we use the index() function to get the postion of a character in the alphabet

    #2. get new position
    position_of_letter += key
    position_of_letter = position_of_letter % 26 #we use the modulo operator (%) to make sure the new position is always inside our alphabeet 

    #3. get character at the new position
    new_letter = alphabet[position_of_letter]

    # 4. create encrpyted message
    encrypted_msg += new_letter

print(encrypted_msg) #print the encrpyted message


# -----------------------------------------------------
#Script 3 : API requests
#This script calls an online service to get current people in space
#To achieve this we will:
#1. Send the request to the website we are interested in

#2. Convert the response to a JSON object

#3.Print the response

from urllib import request #this package alloes us to send internet request
import json #this package allows us to interpret json data

s_request = request.urlopen("http://api.open-notify.org/astros.json") #This sends a request to the website/api and saves the response

data = json.load(s_request) #Here we convert our request to JSON format

print(data) #print the response from the web

#This is how we can access JSON objects!
# print(data["people"]) #print only the list people

# print(data["people"][1]["name"]) #print the name of the second person in the list

# for i in range(len(data["people"])):  #print the names of the people in the list
#     print(data["people"][i]["name"])