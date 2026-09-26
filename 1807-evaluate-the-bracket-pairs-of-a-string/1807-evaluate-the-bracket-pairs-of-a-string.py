class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        dictt = dict()

        for i in knowledge :
            dictt[i[0]] = i[1]

        i = 0
        res = []

        while i < len(s) :
            if  s[i] == '(' :
                j = s.find(')',i+1)
                res.append(dictt.get(s[i+1:j],"?")
                )
                i = j
            else :
                res.append(s[i])
            
            i+=1

        return "".join(res)

        