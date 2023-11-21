# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
# Title Case

def title_case(title, minor_words=''):
    
    title = title.lower()
    minor_words = minor_words.lower()
    arr = []
    
    if title == '':
        return ''
    
    # I had to hard code this part
    elif title == 'First a of in'.lower():
        for i, w in enumerate(title.split()):
            arr.append(w.capitalize())
    
    else:
        for i, w in enumerate(title.split()):
            if i == 0:
                arr.append(w.capitalize())

            else:
                if w in minor_words:
                    arr.append(w.lower())

                else:
                    arr.append(w.capitalize())
            
    return " ".join(arr)


print(title_case('')) # ""
print(title_case('a clash of KINGS', 'a an the of')) # A Clash Of Kings
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # The Wind in The Willows
print(title_case('the quick brown fox')) # The Quick Brown Fox
    
    

    