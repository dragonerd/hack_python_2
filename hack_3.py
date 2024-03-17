"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""
def fn_hack_3(s):

    listados = {'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v', 'm' : 'm', 'z' : 'z', 'r' : 'r'}
    result = ""
    for e in s:
        if e in listados:
            result += listados[e]
        else:
            result += e.upper()
    
    return result