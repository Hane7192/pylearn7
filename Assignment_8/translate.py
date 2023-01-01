from gtts import gTTS
import os

def read_from_file():
    
    global words_bank
    f = open("translate.txt", "r")
    temp = f.read().split("\n")
    words_bank = []
    for i in range (0 , len(temp),2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)
    f.close()

def translate_from_english_to_persian():
    
    output =""
    user_text = input("Enter your english text: ").lower()
    user_sentences = user_text.split(".")
    for user_sentence in user_sentences: 
        user_words = user_sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word == word["en"]:
                    output = output + word["fa"]+ " "
                    break
            else:
                output = output + user_word + " "
                
        output = output + "."        
    print(output)

def translate_from_persian_to_english():

    output =""
    user_text = input("Enter your english text: ").lower()
    user_sentences = user_text.split(".")
    for user_sentence in user_sentences:
        user_words = user_sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word == word["fa"]:
                    output = output + word["en"]+ " "
                    break
            else:
                output = output + user_word + " "

        output = output + "."         
    
    print(output)
    audio = gTTS(text=output, lang="en", slow=False)
    audio.save("audio.mp3")
    os.system("start audio.mp3")

def add_a_new_word():
    new_en_word = input("Enter your english word to be added to the dictionary: ").lower()
    
    for word in words_bank:
        if new_en_word == word["en"]:
            print("your word is already exists")
            print(word["en"], ":", word["fa"] )
            break
    else:
        new_fa_word = input("Enter the persian meaning of your entered word: ").lower()
        new_word = {"en":new_en_word, "fa":new_fa_word}
        words_bank.append(new_word)
        f = open("translate.txt", "a")
        f.write("\n")
        f.write(new_en_word)
        f.write("\n")
        f.write(new_fa_word)
        f.close()
        print("you successfully add", new_en_word, ":", new_fa_word, "to the dictionary")
        

def show_menu():
    print("welcome to my translate")
    print("1- translate from english to persian")
    print("2- translate from persian to english")
    print("3- add a new word to database")
    print("4- exit")
    

read_from_file()

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        translate_from_english_to_persian()
    elif choice == 2:
        translate_from_persian_to_english()
    elif choice == 3:
        add_a_new_word()
    elif choice == 4:
        exit(0)
        

