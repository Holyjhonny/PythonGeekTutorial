import keyword

print(keyword.kwlist)
value = input("Enter Keyword or other (to be added)")
if value == 'Keyword':
    key = input("Enter of of the keywords for documentation")
    if key == 'False':
        print(False,':keyword to represent boolean {}'.format(False))
    elif key == 'None':
        print(None,':keyword to denote a nul value or a void{}'.format(None))
    elif key == 'True':
        print(True,':keyword to represent boolean {}'.format(True))
    elif key == 'for':
        print('for: used to control flow and for looping')
    elif key == 'while':
        print('while: used to control flow and for looping')
    elif key == 'break':
        print('break: the statement is used to break out of the loop')
    elif key == 'continue':
        print('continue: keyword skips the current iteration of the loop but dose not end the loop')
    elif key == 'if':
        print('if: Truth expression forces control to of in "if" statement blocks')
    elif key == 'else':
        print('else: it is a control statment for decision making')
    elif key == 'elif':
        print('elif: short for else if')
    elif key == 'def':
        print('def: keyword is used to declare user defined functions')
    elif key == 'return':
        print('return: this keyword is used to return from the function')
    elif key == 'yield':
        print('yield: keyword is used like a return but is used to return a generator')
    elif key == 'class':
        print('class:keyword is used to declare user defined classes')
    elif key == 'with':
        print('with:keyword is used to wrap the execution of block of code within methods defined by context manager: with open(filepath,w)')
    elif key == 'as':
        print('as: keyword is used to create the alias for the module imported')
    elif key == 'pass':
        print('pass: is the null statement in python. Nothing happens when this is encountered')
    elif key == 'lambda':
        print('lambda: keyword is used to make inline returning functions with no statements allowed internally')
    elif key == 'import':
        print('import: This staement is used to include a particular modeule into current program')
    elif key == 'from':
        print('from: Generally used with import, from is used to import partifular functionality from the moduled imported')
    elif key == 'try':
        print('try: This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed')
    elif key == 'assert':
        print('assert: This function is used for debugging purposes. Usually used to check the correctness of code. If a statement is evaluated to be true, nothing happens, but when it is false, “AssertionError” is raised. One can also print a message with the error, separated by a comma.')
    elif key == 'del':
        print('del: is used to delete a reference to an object. Any variable or list value can be deleted using del')
    elif key == 'global':
        print('global: This keyword is used to define a variable inside the function to be of a global scope.')
    elif key == 'non-local':
        print('non-local : This keyword works similar to the global, but rather than global, this keyword declares a variable to point to variable of outside enclosing function, in case of nested functions.')
    else:
        Exception(TypeError)


