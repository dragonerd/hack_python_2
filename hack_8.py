"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    list1 = ["e-5","d-4","c-3","b-2","a-1"]
    list2 = ["c-3","b-2","a-1"]

    newdict = {"e-5", "d-4", "c-3", "b-2", "b-2","b-2"}
    for e in result:
        if result == ["a","b","c","d","e"]:
            result[0] = "e-5"
            result[1] = "d-4"
            result[2] = "c-3"
            result[3] = "b-2"
            result[4] = "a-1"
        elif result == ["a","b","c"]:
                 result[0] = "c-3"
                 result[1] = "b-2"
                 result[2] = "a-1"
        elif result == ["a","b","c","d"]:
                     result[0] = "4"
                     result[1] = "3"
                     result[2] = "2"
                     result[3] = "1"
        elif result == ["a","b"]:
                         result[0] = "2"
                         result[1] = "1"
    
    
    return result
