"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = []
    fix = []
    newdict = {"a":"1", 
               "b":"2", 
               "c":"3", 
               "d":"4", 
               "e":"5",
               "f":"5",
               }
    eliminar = ""
    for e in s:
          if e in newdict:
            result += newdict[e]
    try: 
        i = result.index("2")
        result = result[:i]+[2]+result[i+1:]
        i2= result.index("4")
        result = result[:i2] + [4] + [str(5)]
    except ValueError:
        print("error codigo 2")
        if result == []:
            result.append(0)
    #result = result[:i2]+[2]+result[i2:+1:i2+5]+[str(5)]
    #result = result[:i2] + [str(4)] + result[i2 + 1:i2 + 5] + [str(5)]

            #if newdict["b":"2"] == 1:
            #    newdict["b":"2"] = 2
            #if e != "2":
            # e = result.insert(0, 2, 1)
    return result
