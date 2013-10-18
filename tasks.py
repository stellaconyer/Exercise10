"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]

"""
Given dictionary d, print out the key-value pairs in alphabetical order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""
d = {"q": 5, "m": 3, "z":2, "a": 10}

def sort_alpha_dict(dictionary):
    #create empty list to store keys in alpha order
    key_list = []

    #loop through dictionary, convert keys to ASCII, add to key_list, sort key_list
    for letter in d:
        key_list_var=ord(letter)
        key_list.append(key_list_var)

    sorted_keylist =sorted(key_list)

    #loop through sorted list, convert key back from ASCII, use key to return dictionary value, print
    for letter in sorted_keylist:
        key = chr(letter)
        value = dictionary[key]
        print "%s, %s" %(key, value)



"""
Given list l1 and list l2, produce list l3 that contains the contents of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""
l1 = [1, 3, 88, 4, 6, 8, 10]
l2 = [93, 2, 23, 77, 66, 88]

def combine_lists(list1, list2):
    combined_list = list1
    if len(list1) < len(list2):
        short_list = list1
        long_list = list2
    else:
        short_list = list2
        long_list = list1

    for item_in_short_list in short_list:
        item_to_check = item_in_short_list
        
        for item_in_long_list in long_list:
            if not item_to_check == item_in_long_list:
                combined_list.append(item_to_check)
                break

    print combined_list


"""
Given the string s, split it into two strings, s2 and s3, s2 containing the first 5 letters of the string, and s3 containing the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""
s = "Hi there, my name is Slim"

def split_string_weirdly(string):
    string2 = ""
    string3 = ""

    counter = 0    
    for letter in string:
        if counter < 5:
            string2 = string2+letter
            print letter, counter
        else:  
            string3 = string3+letter
            print letter, counter
        counter+=1
    print "string2=", string2
    print "string3=", string3


"""
Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""
s = "Hi there, my name is Slim"

def remove_6_to_12(string):
    new_string = ""

    counter = 1
    for letter in string:
        if counter < 6 or counter >12:
            print letter
            new_string = new_string+letter
            print new_string
        counter += 1
    print new_string

"""
Given the string s, produce a list composed of all the single characters from the original string
eg:
    s = "Hello"
    becomes
    l = {"H", "e", "l", "l", "o"}
"""
s = "Hi there, my name is Slim"

def make_list_from_string(string):
    string_list = []

    string=string.replace(" ", "")

    for letter in string:
        string_list.append(letter)

    print string_list


"""
Given the list l composed of tuples, sort the list by the second item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""
l = [(1,2), (3,1), (17, 35), (81,20)]

def sort_on_tuples(a_list):
    tuple_dict = {}
    sorting_list = []
    final_sorted_list=[]
    #create a dictionary using the second item of the tuple as a key and tuple pair as the value
    for (a_tuple, b_tuple) in a_list:
        tuple_dict[b_tuple] = (a_tuple, b_tuple)

    #create a sorted list of the keys
    for key in tuple_dict:
        sorting_list.append(key)
    sorted_sorting_list = sorted(sorting_list)
    print sorted_sorting_list

    #use the sorted keys to append the tuple values in order
    for number in sorted_sorting_list:
        key = number
        #return tuple by key and append to list in numerical order
        final_sorted_list.append(tuple_dict[key])
    print final_sorted_list




"""
Given two dictionaries, d1 and d2, update the contents of d1 with the contents of d2, overwriting any existing keys
eg:
    d1 = {"a":1, "b":2}
    d2 = {"a":3, "c":4}

    becomes

    d1 = {"a":3, "b":2, "c":4}
"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

def update_dict_one(dict1, dict2):

    for item in dict2:
        value = dict2[item]
        dict1[item] = value

    print dict1

"""
Given two dictionaries, d1 and d2, merge the contents of d1 with the contents of d2, adding to the values of existing keys
eg:
    d1 = {"a": 1, "b":2}
    d2 = {"a": 3, "d": 4}

    becomes

    d1 = {"a": 4, "b":2, "d":4}

"""
d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

def update_and_add_to_dict_one(dict1, dict2):

    for item in dict2:
        dict2_value = dict2[item]
        if dict1.get(item,0) == 0:
            print "no dice", item
            dict1[item] = dict2_value
        else:
            dict1[item] = int(dict1.get(item)) + int(dict2_value)
            print dict1[item]

    print dict1

"""
s = "Sorry,\nMy people need me\nI must go"

Given a multiline string 's', print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

"""

s = "Sorry,\nMy people need me\nI must go"

def print_multi_line_str(string):
    split_string = string.split("\n")
    line_counter = 1
    for element in split_string:
        print "%s. %s" %(line_counter, element)
        line_counter+=1


"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""

random_title= "a tale of two cities"
def title(my_title):
    modified_string = ""
    string_list = my_title.split()
    first = string_list.pop(0)
    first = first[0].upper() + first[1:]
    modified_string = first

    for item in string_list:
        if item in ("a", "the", "of"):
            modified_string= modified_string + " " + item
        else:
            item = item[0].upper() + item[1:]
            modified_string= modified_string + " " + item
    print modified_string

"""
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to fahrenheit, and f_to_c should do the opposite
"""

def c_to_f(floating_num):
    fahrenheit = ((floating_num*9)/5)+32
    print fahrenheit

def f_to_c(floating_num):
    celcius = ((floating_num-32)*5)/9
    print celcius

f_to_c(55.7)
c_to_f(100.15)
