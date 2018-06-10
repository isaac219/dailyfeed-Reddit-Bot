#!/usr/bin/env python
import praw, sys, datetime, time
from threading import Thread

if len(sys.argv) < 3:
    sys.exit("Syntax Error - Usage: %s recipient (subreddit)" % sys.argv[0])

#initialize reddit instance
reddit = praw.Reddit('bot1') 

#get title and link from top daily post of each subreddit
def get_post(sub, result, index):
    try:
        subreddit = reddit.subreddit(sub)
        for submission in subreddit.top('day'):
            subreddit_name = "**r/" + str(submission.subreddit) + "**"
            title = str(submission.title)
            link = str(submission.shortlink)
            result[index] = (subreddit_name +"\n\n" + title +": " + link + "\n\n")
            return True
    except:
        print("Error encountered for " + sub)
        subreddit_name = "**r/" + str(subreddit) + "**" + "\n\n"
        result[index] = subreddit_name +  "Error encountered for r/" + str(subreddit) + "\n\n"

#create threads for retrieving each subreddit post and send the pm
def build_message(args):
    sub_list = []

    for i in range (2,len(args)):
            sub_list.append(args[i])

    subject= "Feed - " + str(datetime.date.today())
    body = ""

    threads = [None] * len(sub_list)
    results = [None] * len(sub_list)

    for i in range(len(sub_list)):
        threads[i] = Thread(target=get_post,args=(sub_list[i], results, i))
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()

    for r in results:
        if(r != None): 
            body += r
    
    return (subject, body)

#send the message (subject, body) to the recipient
def pm(message, recipient):
    subject = message[0]
    body = message[1]
    reddit.redditor(recipient).message(subject, body)

if __name__ == "__main__":
    start = time.time()
    pm(build_message(sys.argv), sys.argv[1])
    end = time.time()
    print(end - start)
