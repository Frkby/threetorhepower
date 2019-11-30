# A program made by DannyP
# if you don't know who, just imagine Adnpst but a far better programmer
# and a total chad
import tweepy
import time

credentials = []
recoveryData = []
# Eskeetit
# Function: Reads the contents of a text file that contains the twitter API
#           OAuth credentials to the credentials list. If i was less lazy
#           I would make this used for all file reading and writing
#           but im  Australian and not German
def ReadFile():
    credentialsDoc = open("credentialsTextDocument.txt", "r")
    for line in credentialsDoc:
        credentials.append(line)
    credentialsDoc.close()
    
# Function: Takes the credentials from the ReadFile Function and uses them for OAuth
def AssignAuthValues():
    consumer_key = credentials[0].rstrip()
    consumer_secret = credentials[1].rstrip()
    access_token = credentials[2].rstrip()
    access_token_secret = credentials[3].rstrip()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    global api
    global numOfTweets
    api = tweepy.API(auth)
# Function: Does what it says on the tin
def CrashRecovery():
    recoveryFile = open("recoveryFile.txt","r")
    for line in recoveryFile:
        recoveryData.append(line)
    credentialsDoc.close()
    recoveryExponent = recoveryData[-2]
    recoveryTime = recoveryData[-1]
# Function: Backs up the time and exponent each day cycle
def Backup(exponent):
    recoveryFile = open("recoveryFile.txt","w")
    recoveryFile.write("----------------------------")
    recoveryFile.write(str(exponent))
    recoveryFile.write(str(time.time()))
# Function: Gets the value of variable x to the power of three
# Variable: integer
def ThreePower(x):
    return 3**x
# Function: Tweets to the account
# Variable: String
def PostTweet(x):
    api.update_status(x)

