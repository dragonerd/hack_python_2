"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    #dict = {"foo":"fookziman","bar":"barziman"} 
    del result["bar"]
    del result["foo"]
    result["Foo"] = "Fooziman"
    
 #   result = ""
  #  newlist = {"bar":"barziman"}
    #x = result["foo"]
   # for e in s:
    #    if e in newlist:
     #       result += newlist[e]
    #for e in result:
     #  if e == delclave:
      #      del result[delclave] 
    return result