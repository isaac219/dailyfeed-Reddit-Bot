#!/usr/bin/env python
import praw, sys, datetime

if len(sys.argv) < 3:
    sys.exit("Syntax Error - Usage: %s recipient (subreddit)" % sys.argv[0])

#initialize reddit instance
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     password='',
                     username='')

#get subreddits from CL arguments
def get_subreddits():
    sub_list = []
    for i in range (2,len(sys.argv)):
            sub_list.append(sys.argv[i])
    return sub_list

#map submissions into a dictionary with subreddit, title, and link
def map_submissions(sub_list):
    global reddit
    dictionary = {}
    for sub in sub_list:
        subreddit = reddit.subreddit(sub)
        count = 0
        for submission in subreddit.top("day"):       
            title_and_link = [str(submission.title),str(submission.shortlink)]
            dictionary.update({str(submission.subreddit): title_and_link})
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
        subreddit_name = "**r/" + str(key) + "**"
        body+=(subreddit_name +"\n\n" + title +": " + link + "\n\n")
    pm_subject = "Feed - " + str(datetime.date.today())
    recipient = sys.argv[1]
    reddit.redditor(recipient).message(pm_subject, body)

def main():
    dictionary = map_submissions(get_subreddits())
    message(dictionary)

if __name__ == "__main__":
    main()
