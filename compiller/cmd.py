import sys
import filename.testfilename as testfilename
import lexer.lexer as lexer
import analyse.analyse as analyse

arguments = sys.argv[1:]

filename = str(arguments[0])

if testfilename.testfilename(filename):
    file = open('forFiles/' + filename, encoding='utf-8')
    file_text = file.read()

    print('Filename: ' + filename)
    print('Filetext: ' + file_text)

    strs = lexer.create_tokens(file_text)
    print('Strings: ' + str(strs))

    analyse.analyse(strs)

    print(analyse.errors)
