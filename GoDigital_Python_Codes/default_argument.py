#Default Argument
#if you passed another argument to function default parameter are silenced
def banner(message,border='-'):
    line=border * len(message)
    print(line)
    print(message)
    print(line)