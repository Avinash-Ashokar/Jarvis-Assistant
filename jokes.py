import pyjokes


#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    return j
