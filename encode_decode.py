import random
import string
from termcolor import colored
while True:
    try:
        def add_random_letters(word):
            if len(word) < 3:
                return word[::-1]
            
            word_modified = word[-1] + word[1:-1] + word[0]
            start_letters = random.choices(string.ascii_lowercase, k=3)
            end_letters = random.choices(string.ascii_lowercase, k=3)
            
            new_word = ''.join(start_letters) + word_modified + ''.join(end_letters)
            return new_word  

        def remove_random_letters(word):
            if len(word) < 3:
                return word[::-1]
            word_modified = word[3:-3:1]
            word_last_modified =word_modified[-1] + word_modified[1:-1] + word_modified[0]
            return word_last_modified
            
            
        def decode_ms():
            user_info = input("\n" + "Write your message: ")
            words = user_info.split()
            
            p_words = [remove_random_letters(word) for word in words]
            p_sentc = " ".join(p_words)
            
            return p_sentc

        def encoded_ms():
            user_info = input("\n" + "Write your message: ")
            words = user_info.split()
            
            p_words = [add_random_letters(word) for word in words]
            p_sentc = " ".join(p_words)
            
            return p_sentc


        print("Welcome to my program!😄")
        print("This program can encode and decode your message.")
        ask_user = int(input("\n" + "1. encode or 2. decode: "))
        if ask_user == 1:
            print("-" * 50)
            endoded_message = encoded_ms()
            print("your encoded message is: " + (colored(endoded_message , "red")))
            print("-" * 50)
        else:
            print("-" * 50)
            decoded_message = decode_ms()
            print("your decoded message is: " + (colored(decoded_message , "light_yellow")))
            print("-" * 50)

        ask_user2 = input("\n" + "Do you want to continue? (yes/no): ")
        if ask_user2.lower().strip() != "yes":
            print("Thanks for using my program!😄")
            break
    
    except:
        print("Oops some error occured!")

    

    
    

