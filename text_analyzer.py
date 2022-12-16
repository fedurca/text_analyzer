# echo.py
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


import sys
# import task_template as txt

valid_users = {"bob": "123",
               "ann": "pass123",
               "mike": "password123",
               "liz": "pass123"}
login_req = 0
user = ""
DEBUG = 0


if(login_req):
    user = input("username:")
    pwd = input("password:")
    if user in valid_users:
        if (pwd == valid_users.get(user)):
            pass
        else:
            print("invalid password, terminating the program..")
            sys.exit()
        print(valid_users.get(user))
    else:
        print("unregistered user, terminating the program..")
        sys.exit()
print("-"*40)
print("Welcome to the app,", user)
print("We have 3 texts to be analyzed.")
print("-"*40)

chosen_text = 0 
texts_size = len(TEXTS)
while(not(1 <= chosen_text <= texts_size)):
    try:
        chosen_text = int(input("Enter a number btw. 1 and  {0} to select: ".format(texts_size)))
    except ValueError:
        print("incorrect value - insert single number in required range")

chosen_text = chosen_text-1
print(chosen_text)

"""
text_chosen = 0
while (text_chosen not in range(1,3)):
    chosen_text = input("Enter a number btw. 1 and 3 to select: ")
    text_chosen = int(int(chosen_text)-1)
    print(chosen_text)
    print(text_chosen)
       
    
    
    int(input("Enter a number btw. 1 and 3 to select: ")) in range(1,3)):
    

choosen_text = 0
while (0 < choosen_text < 3):
    chosen_text = input("Enter a number btw. 1 and 3 to select: ")
    chosen_text = int(int(chosen_text)-1)
"""

words_list = TEXTS[chosen_text].split()

stats = {"words_count": len(words_list),
         "words_titlecase": 0,
         "words_uppercase": 0,
         "words_lowercase": 0,
         "words_numeric": 0,
         "words_sum_of_numbers": 0,
         "words_max_len": 0}

word = 0
for _ in words_list:
    words_list[word] = words_list[word].replace(",", "")
    words_list[word] = words_list[word].replace(".", "")
    word += 1

for word in words_list:
    if (word.istitle()):
        stats["words_titlecase"] += 1
    if (word.isalpha() and word.isupper()):
        stats["words_uppercase"] += 1
    if (word.islower()):
        stats["words_lowercase"] += 1
    if (word.isnumeric()):
        stats["words_numeric"] += 1
        stats["words_sum_of_numbers"] += int(word)
    if (len(word) >= int(stats["words_max_len"])):
        stats["words_max_len"] = len(word)

print("There are", stats["words_count"], "words in the selected text.")
print("There are", stats["words_titlecase"], "titlecase words.")
print("There are", stats["words_uppercase"], "uppercase words.")
print("There are", stats["words_lowercase"], "lowercase words.")
print("There are", stats["words_numeric"], "numeric strings.")
print("The sum of all the numbers", stats["words_sum_of_numbers"])

lenghts = {}

for word in words_list:
    if len(word) in lenghts.keys():
        # print("klic", len(word) ,"je v seznamu, zvysuji o vyskyt jedna")
        lenghts[len(word)] += 1
    else:
        lenghts[len(word)] = 1
    
# max_len = stats["words_max_len"]

print("-"*40)
# print("LEN|  OCCURENCES  |NR.")
print(f'{"LEN":>3}{"|"}')
      # {"  OCCURENCES"<{stats["words_max_len"]+3}}{"|"}')

print("-"*40)


dict_member = 1
while (dict_member < stats["words_max_len"]):
    print(f'{dict_member:>3}{"|"}{lenghts[dict_member]*"*":<{stats["words_max_len"]+3}}{"|"}{lenghts[dict_member]:<{stats["words_max_len"]}}')
    dict_member += 1

# WALK = 0


"""
for i in range(1, int(stats["words_max_len"])+1):
    print(f'{i:>3}|{"*"*lenghts[i]:< stats["words_max_len"]}|{lenghts[i]:<0}')
    WALK += 1
    if (DEBUG != 0):
        for j in words_list:
            if (len(j) == WALK):
                print("SOUCASTI JE:", j)
"""