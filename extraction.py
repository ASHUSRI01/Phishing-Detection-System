import re

def detect_input_type(text):
    url_pattern = re.compile(r'^https?://')
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    if url_pattern.match(text.strip()):
        return 'url'
    elif email_pattern.match(text.strip()):
        return 'email'
    else:
        return 'unknown'
