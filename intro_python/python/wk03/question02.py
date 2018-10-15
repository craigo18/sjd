# Ask Question from data Dictionary (hash)
data = {"Q": "Is it an aquatic animal"}

# A simple Y/N validation function
# q_text = Question text
# Get question from data

def get_answer (question):
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
if get_answer(data['Q']):
    print('Yes')
else:
    print('No')
