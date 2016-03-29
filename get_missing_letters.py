import string
from sys import version_info
def get_missing_letters(sentence):
    alphabet = "abcdefghijklmnopqrstuvqxyz"
    missing_letters = ""
    lower_case_sentence = sentence.lower()
    for letter in alphabet:
        if letter not in lower_case_sentence and letter not in missing_letters:
                missing_letters += letter
    return missing_letters

#further exploration of implentations

#returns true if the passed in sentence is an anagram
#returns false otherwise
def is_anagram(sentencea):
    return set(string.lowercase).issubset(set(sentence.lower()))

#returns a set of the letters in the alphabet that are not in
#the lower case version of the sentence
def get_set_of_missing_letters(sentence):
    alphabet = "abcdefghijklmnopqrstuvqxyz"
    return (set(alphabet)-set(sentence.lower()))
    
def getResponse(py3):
    if py3:
        response = input("which input would you like to run?")
    else:
        response = raw_input("Which program would you like to run?")
    return response

def getAnagram(py3):
    if py3:
        anagram = input("An anagram is a string of characters that, ignoring upper or lower case, contains all twenty six letters of the alphabet")       
    else:
        anagram = raw_input("An anagram is a string of characters that, ignoring upper or lower case, contains all twenty six letters of the alphabet")
    return anagram

def displayTasks():
    print ("1.) get_missing_letters")
    #print ("2.) is_anagram")
    #print ("3.) get_set_of_missing_letters")


def executeTask(response):                       
    anagram = getAnagram(py3)
    missing_letters = get_set_of_missing_letters(anagram)
    if int(missing_letters) < 26:
        print (anagram + " is missing " + missing_letters)
    else:
        print ("Congratulations, you entered an anagram")

def main():
    py3 = version_info[0] > 2 #version control!
    displayTasks()
    task = getResponse(py3)
    if task == "1" or "get_missing_letters":
        executeTask(task)                       
    
if __name__== "__main__":
    main()
