global_container = {}
errors = []

symbolsFirstInVar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '$']

symbolsForNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']


def error(typeOfError, line, string):
    if type(line) == type(5):
        errors.append([typeOfError, 'line: ' + str(line), string])
        return True
    else:
        return False
    
def analyse(strs):
    i = 0
    for string in strs:
        tokens = string.split(' ')

        # variables
        if tokens[0] == 'str':
            if len(tokens) == 4:
                if tokens[2] == '=':
                    if tokens[1][0] in symbolsFirstInVar:
                        literal = tokens[3]
                        if literal[0] == literal[-1] == "'":
                            global_container[tokens[1]] = str(tokens[3])
                        
                        else:
                            error('typeError', i, string)
                    else:
                        error('nameError', i, string)
                else:
                    error('syntaxError', i, string)
            else:
                error('syntaxError', i, string)


        if tokens[0] == 'num':
            if len(tokens) == 4:
                if tokens[2] == '=':
                    if tokens[1][0] in symbolsFirstInVar:
                        literal = tokens[3]

                        def checkLiteral(number):
                            for letter in number:
                                if not(letter in symbolsForNumbers):
                                    return False
                            return True

                        if checkLiteral(tokens[3]):
                            global_container[tokens[1]] = float(tokens[3])
                        
                        else:
                            error('typeError', i, string)
                    else:
                        error('nameError', i, string)
                else:
                    error('syntaxError', i, string)
            else:
                error('syntaxError', i, string)


        if tokens[0] == 'bool':
            pass

        # if
        if tokens[0] == 'if':
            pass            


        i += 1

