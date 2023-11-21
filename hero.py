# Source https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
# Is he gonna survive?

# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded 
# with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets 
# he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another 
# specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)

def hero(bullets, dragons):
    if bullets == 0: # he ise defeated if he carries no bullets
        return False
    else: # Check how many bullets he has
        if bullets < (dragons * 2): # Gets defeated if he carries less bullets than the number of dragons
            return False
        else: # Check if the bullets are enough ot kill all the dragons
            if bullets % (dragons * 2) == 0: # Wins
                return True
            elif bullets >= dragons * 2:
                return True