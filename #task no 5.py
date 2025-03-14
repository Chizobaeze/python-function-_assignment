#task no 5

marketing_entries=["chi3oba","ebuka","que2n","co1lins","mayowa","eb1ere","segun"]

def bad_entries(clientel_name):
    """
    A function question to filter out bad entries and reportto the marketing team

    isalpha only returns values with alphabetical characters; thats why we used not

returning

    yield statement which is used to continue the iteration to the end of the list
    """
    for names in clientel_name:
        if not names.isalpha():
           yield f'This name is filtered for bad entries:{names}'

x=bad_entries(marketing_entries)

"""
assign the function bad entries to x

create a forloop to  iterate through it

"""
for i in x:
    print(i)