import random

words_bank = ["mahsa" , "nika" , "sarina" , "kian" , "hadis" , "hamidreza" , "merhrshad" , "khodanour" , "ghazaleh" , "navid" , "abolfazl" , "hanane" , "asra" , "danial"]
user_mistakes = 0
good_chars = []
bad_chars = []
string = ""

word = random.choice(words_bank)

while user_mistakes < 6:
    
    for i in range(len(word)):
        
        if word[i] in good_chars:
            string = string + word[i]
        
        else:
            string = string + "_ "
        
    print(string , end ="")
    
    

    if "_" in string:

        user_char = input("\nPlease enter your guess: ")

        if len(user_char) == 1:
                    
            if user_char.lower() in word:
                good_chars.append(user_char.lower())
                print("✅")
                    
            else:
                bad_chars.append(user_char)
                print("❌")
                user_mistakes = user_mistakes + 1

        else:
            print ("what the hell !! Enter properly!")

        string = ""
    
    else:
        print("\nCongradulation! You saved his/her life 👏")
        break

        

if user_mistakes == 6:
    print("I'm sorry! She/He was murdered 😔")
