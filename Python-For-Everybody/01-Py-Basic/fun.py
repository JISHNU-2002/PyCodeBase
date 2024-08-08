def function(string):
    words = []
    words = string.split()

    print(words)

    dict = {}

    for key in words:
        dict[key] = words.count(key)

    print(dict)
function("jishnu is a very good boy jishnu is awesome and super cool and super funny")