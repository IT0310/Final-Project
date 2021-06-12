"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from final_functions import greeting, get_definition, creat_list, pythagoran_theorem, vocab_list

def test_greeting():
    assert(callable(greeting))
    assert(isinstance(greeting(""), str))
    assert(greeting('hi') == "Hi, I am Mathy! Please select the below options: 'get defintion', 'create list', 'distance'! You have to type in each option again after finished using the previous one. To stop the conversation, please type in 'quit'. ")
    assert(greeting('Hello') == "Hi, I am Mathy! Please select the below options: 'get defintion', 'create list', 'distance'! You have to type in each option again after finished using the previous one. To stop the conversation, please type in 'quit'. ")



def test_get_definition():
    assert(callable(get_definition))
    assert(isinstance(get_definition(""), str))
    assert(get_definition('CHORD') == 'the line segment between two points on a given curve')
    assert(get_definition('Minute') == "The keyterm is not defined, please re-start the program and choose a keyterm that's defined!")
           

def test_creat_list():
    assert(callable(creat_list))
    assert(isinstance(creat_list(""), str))
    assert(creat_list('CHORD') == {'CHORD': 'the line segment between two points on a given curve'})
    assert(creat_list('Sure') == "The term is not find in the keyterm dictionary, please restart the program and try it again!")
           
           
def test_pythagoran_theorem():
    assert(callable(pythagoran_theorem))
    assert(isinstance(pythagoran_theorem("2, 3"), float))
    assert(pythagoran_theorem("3, 4") == 5)



                 
    