# FILE NAME - coin_toss.py

# NAME: Josh Fielding
# DATE: 10/2/25
# BRIEF DESCRIPTION: Generate Heads or Tails using a random number

import random

# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

########## ENTER YER CODE BELOW THIS LINE ##########

print('===== Coin Flipper =====')

# pick a random number between 1 and 100 
num = random.randint(1, 100)

# if random int is greater than 51 pick tails, and if anything else pick heads
if num >= 51:
    print('Tails')
else:
    print('Heads')


########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

The if else statement was the hardest.




'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[X] I'm solid. Totally got it.
'''
