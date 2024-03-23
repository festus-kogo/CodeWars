# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

def check_exam(arr1,arr2):
    correct_answer = 4
    incorrect_answer = 1
    black_answer = 0
    score = 0
    
    for i, v in enumerate(arr2):
        if not v: # If empty
            score +=black_answer

        else: # Continue to loop
            if v == arr1[i]:
                score += correct_answer
            elif v != arr1[i]:
                score -= incorrect_answer            
    
    if score < 0:
        return 0
        
    return score
        
    
  
