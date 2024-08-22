from stack import Stack

balanced_paranthesis_dict = {
    '{' : '}',
    '[' : ']',
    '(' : ')'
}

def balanced_paranthesis(s):
    st = Stack()
    if (len(s)%2 == 1):
        return False
    
    opening = set('{([')
    matches = set([('{','}') , ('(',')') , ('[',']')])
    
    for item in s:
        if item in opening:
            st.push(item)
        else:
            last_item = st.pop()

            if (last_item, item) not in matches:
                return False
    return st.items == []


print(balanced_paranthesis('{}[()(])'))
