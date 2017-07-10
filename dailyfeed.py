#!/usr/bin/env python
import praw, sys, datetime

#initialize reddit instance
reddit = praw.Reddit(client_id='',
                    client_secret='',
                    user_agent='',
                    password='',
                    username='')

#get subreddits from CL arguments
def getSubreddits():
    subList = []    
    for i in range (2,len(sys.argv)): 
            subList.append(sys.argv[i])
    return subList

#map submissions into a dictionary with subreddit, title, and link
def mapSubmissions(subList):
    global reddit
    dictionary = {} 
    for sub in subList:
        subreddit = reddit.subreddit(sub)
        count = 0
        for submission in subreddit.top('day'):       
            titleAndLink = [str(submission.title),str(submission.shortlink)]
            dictionary.update({str(submission.subreddit): titleAndLink})   
            count +=1
            if count==1:
                break          
    return dictionary

#build and send the message to redditor
def message(dictionary):
    global reddit
    body = ""
    for key, value in dictionary.iteritems():
        title = value[0]
        link = value[1]
        subredditName = "**r/" + str(key) + "**"
        body+=(subredditName +"\n\n" + title +": " + link + "\n\n")
    pmSubject = "Feed - " + str(datetime.date.today())
    recipient = sys.argv[1]
    reddit.redditor(recipient).message(pmSubject, body)
    
def main():
    dictionary = mapSubmissions(getSubreddits())
    message(dictionary)

if __name__ == "__main__":
    main()
    
        
