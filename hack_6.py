"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = []
    newdict = {"a":"1", "b":"-", "c":"3", "d":"-", "e":"5"}
    
    new_txt = []
    if not s:
        new_txt = ["0"]
        return new_txt
    
    for e in s:
          if e in newdict:
            result += newdict[e]
            #if e  == ["9"]:
             #     e.append(e)

              
    return result
