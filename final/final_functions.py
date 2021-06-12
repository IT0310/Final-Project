"""A collection of function for doing my project."""
import math

pre_dic = {"RADIUS": "a straight line extending from the center of a circle or sphere to the circumference or surface",
                   "CHORD": "the line segment between two points on a given curve", 
                   "DIAMETER": "a straight line passing through the center of a circle or sphere and meeting the circumference or surface at each end"}
vocab_list = { }


#credit: function from assignment 3
def get_response():
    
    msg = input("INPUT :\t")
    #capitalize all letters in input to make it easier to understand
    msg = msg.upper()  
    
    return msg


def greeting(msg):
    """To start the program
    
    Parameters
    ----------
    msg : string
        String to start the program
        
    Returns
    -------
    output_string : string
        String that directs the user to choose function's option
    """ 
    msg = msg.upper()
    if msg == "HI" or msg == "HELLO":
        print("Hi, I am Mathy! Please select the below options: 'get defintion', 'create list', 'distance'! You have to type in each option again after finished using the previous one. To stop the conversation, please type in 'quit'. ")
        
        return "Hi, I am Mathy! Please select the below options: 'get defintion', 'create list', 'distance'! You have to type in each option again after finished using the previous one. To stop the conversation, please type in 'quit'. "
    
    else: 
        print("Please enter 'hi' or 'hello' to start the program")
        
        return "Please enter 'hi' or 'hello' to start the program"
    

def get_definition(msg):
    """to get the defintion of specific keyterm from the pre-existed dictionary
    
    Parameters
    ----------
    msg : string
        String that contain the specific keyterm
        
    Returns
    -------
    output_string : string
        String that present the definition of the specific keyerm
    """        
    if msg in pre_dic:
        print(pre_dic[msg])
        
        return pre_dic[msg]
    
    else:
        print("The keyterm is not defined, please re-start the program and choose a keyterm that's defined!")
        
        return "The keyterm is not defined, please re-start the program and choose a keyterm that's defined!"
    
def creat_list(msg):
    """to allow user to create their own string with pre-stored keyterms
    
    Parameters
    ----------
    msg : string
        String contain the specific keyterm that the user wants to store
        
    Returns
    -------
    output_string : dictionary
        user's customized dictionary of keyterms they want to store
    """            
    if msg in pre_dic:
        #the key and value of the user's vocab list will be from the pre-existed dictionary
        vocab_list[msg] = pre_dic[msg]
        
        print(vocab_list)
        print("Successfully added to list.")
        return vocab_list 
    
    else:
        
        print("The term is not find in the keyterm dictionary, please restart the program and try it again!")
        return "The term is not find in the keyterm dictionary, please restart the program and try it again!"
    
    
def pythagoran_theorem(msg):
    """to the distance between origin and the point user input
    
    Parameters
    ----------
    msg : string
        string that contain the location of the point user input
        
    Returns
    -------
    output_string : list
        list that include the result of distance after calculation
    """      
    
    
    num1 = int(msg.split(',', 1)[0])
    num2 = int(msg.split(',', 1)[1])
    distance = math.sqrt(num1 ** 2 + num2 ** 2)
    
    print(distance)
    return distance  
        
        
            
    
