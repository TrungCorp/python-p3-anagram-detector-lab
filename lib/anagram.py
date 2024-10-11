# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
    
    def match(self,array):
        list_obj = []
        for word_obj in array:
            if(sorted(word_obj) == sorted(self.word)):
                list_obj.append(word_obj)
        return list_obj
            