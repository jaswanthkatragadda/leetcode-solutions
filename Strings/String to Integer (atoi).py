class Solution:
    def myAtoi(self, s: str) -> int:
      stri = ""
      started = False
      sign = 1
      for i in range(len(s)) :
        ch = s[i]

        if ch == " " :
            if started :
                break
            continue 

        elif ch == "-":
            if started :
                break
            started = True
            sign = -1

        elif ch == "+" :
            if started :
                break
            started = True
            
        elif ch.isdigit() :
            stri += ch
            started = True

        else :
            break


      if len(stri) == 0 :
        return 0

      stri = int(stri)

      ans = sign * stri

      ans = max(-2**31, min(ans, 2**31 - 1))

      return ans
