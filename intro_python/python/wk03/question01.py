Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def get_answer (question):
    gotanswer = False
    while gotanswer == False:
        x = str(input(question + '? [Y/N]: '))
        if x.lower() == "y" or x.upper() == "YES":
            gotanswer = True
            return True
        elif x.lower() == "n" or x.upper() == "NO":
            gotanswer = True
            return False      

# Ask question and define result
if get_answer('Are we learning any python yet'):
    print('Yes')
else:
    print('No')
