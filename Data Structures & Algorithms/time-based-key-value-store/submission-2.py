from collections import defaultdict 
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        
        
    #set just appends a new (key,value,timestamp) into hashmap 
    #might want to store it in a way that timestamp is ordered
    #from smallest -> largest 
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
        

    #double conditional:
    #returns most recent value of key (based on timestamp) 
    # given that set was ever called on this key and we want to 
    # get the key with a timestamp that's right before the one
    # we give in the parameter 
    def get(self, key: str, timestamp: int) -> str:
        res = "" 
        if key not in self.hashmap:
            return "" 

        for i in self.hashmap[key]:
            if i[-1] <= timestamp:
                res = i[0]
        return res 