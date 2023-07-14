s="()"



for i in range(len(s)):

            if i%2==0:
                if(s[i]=='(') or (s[i]=='[') or (s[i]=='{') and 
                (s[i+1]==')') or (s[i+1]==']') or (s[i+1]=='}'):
                return True
                else:
                    return False
            else:
                if(s[i]==')' or s[i]==']' or s[i]=='}') and 
                (s[i-1]=='(' or s[i-1]=='[' or s[i-1]=='{'):
                return True
                else:
                    return False