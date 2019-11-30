# python pls
from TwitterBot import *
import time

#Setup
ReadFile()
AssignAuthValues()
exponent = 0
Backup(exponent)
while True:
    exponent += 1
    result = ThreePower(exponent)
    StringToTweet = "3 to the power of " + str(exponent) + " is "+ str(result)
    PostTweet(StringToTweet)
    time.sleep(86400)