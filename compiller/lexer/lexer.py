def create_tokens(file_text):
    if type(file_text) != type('str'):
        return False

    strings = file_text.split(';\n')     

    return strings