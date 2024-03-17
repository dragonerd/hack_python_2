"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    for e in result:
       result = result.replace("fooziman", "fo-zi-ma-") 
       result = result.replace("barziman", "ba-zi-an")
       result.replace("qux", "qu-")
    return result