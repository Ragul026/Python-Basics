def shout(text):
    return text.upper()

funcs = [shout, str.lower, str.capitalize]

for f in funcs:
    print(f.__name__, ":", f("Hello GitHub! I am C Ragul. I am learning Python."))
