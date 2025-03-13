#Task 1

#Question No 1
def get_firstname(full_name):
   """
   A function to extract just the first_name 

   the split takes the fullname and gives the [0] first value which is the firstname
   """
   return full_name.split()[0]
        
print(get_firstname('Chizoba Eze'))

#Question No 2
def get_firstname(full_name):
   """
   A function to return just the last_name 

   the split takes the fullname and gives the [0] second values which is the surname
   """
   return full_name.split()[1]
        
 #Question No 3         
print(get_firstname('Chizoba Eze'))

def first_last_name(full_name):

   """
   A function to concatenate and return the first and second value 

   return statement using f interpolation to return the fullname. 
   """
   return f'My fullname is {full_name.split()[0]} {full_name.split()[1]}'

print(first_last_name('Chizoba Eze'))


#Task 2
detail_attribute=['first_name','last_name','date of birth']

new_detail_attribute=[]
for detail in detail_attribute:
   """
   the task is to iterate over the list and replace element that doesnt have underscores

   using the append and replace the spaces in the list with underscore

   results: the list is modified and date of birth becomes date_of_birth
   """
   if detail == 'date of birth':
       new_detail_attribute.append(detail.replace(' ','_'))

   else:
      new_detail_attribute.append(detail)


print(new_detail_attribute)

#task 3
name_list=["Mayowa","chizoba","Chigozie"]

for list in name_list:
      """
      i filtered the list values that only has an upper value and ends with "a"

      list: printing out values that abide by the conditions in the if statements
      """
      if list[0].isupper() and list.endswith("a"):
         print(list)


name_list=["Mayowa","chizoba","Chigozie"]


def convert_name(name_list):
    
    """
    Function to return the modified name in the list that starts with an uppercase letter and does not end with 'a'.

     Returns: The modified name if a match is found

     The function returned `"Chigozia"
    """
    for list in name_list:
        if list[0].isupper() and not list.endswith("a"):
          return list[:-1] + "a"
        
print(convert_name(name_list))


#Task 4

marketing_data = ['Wofai', 'Zainab', 'A4atullah']

"""
A function to determine which of the names inthe list doesnt have a valid name

isalpha only returns values with alphabetical characters; thats why we used not

returning
 the value using f interpolation to return the name that has wrong characters

"""

def data_team(marketing_data):
    for data in marketing_data:
        if  not data.isalpha():  
            return (f'This name called {data} contains errors with the name and need to be checked')
            
        
print(data_team(marketing_data))








   
          

    