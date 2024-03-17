"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result2 = s
    newresult = []
    newlist = {"1":"2"},{"3":"4"},{"5":"6"}
    for e in result2:
      if result2 == s:
        result2 = newlist
    
    result = list(result2)
    
    return result
        
    #result.append(newlist) #Elimina {"a":"b"}  
    #del result["c","d"]
    #del result[1] #elimina {"e":"f"}
    #result[0]["1"] = "2"
    #newdict1 = {"1": "2"},{"3", "4"},{"5":"6"}
    #result.append(newdict1)
    
    #newdict2 = ("3", "4")
    #result.append(newdict2)
    
    #newdict3 = {"5": "6"}
    #result.append(newdict3)
    #return result