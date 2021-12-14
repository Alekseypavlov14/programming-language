FILETYPE = 'cmnd'

def testfilename(filename):
    mistakes = []

    if type(filename) != type('string'):
        mistakes.append('typeError')
    
    if str(filename)[-1] == '.':
        mistakes.append('nameError')

    typeoffile = filename.split('.')[-1]
    if typeoffile != FILETYPE:
        mistakes.append('Wrong filename')

    if len(mistakes) == 0:
        return True
    else:
        return False