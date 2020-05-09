#!/usr/bin/env python
import sys, datetime, time, traceback, argparse
import praw
from concurrent.futures import ThreadPoolExecutor
from functools import partial

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="Username of recipient Redditor", required=True)
parser.add_argument("-f", "--filepath", help="Filepath of input subreddits", required=True)
args = parser.parse_args()

def build_subject() -> str:
    return "Feed - " + str(datetime.date.today())

# asynchronously get top posts and then join
def build_body(sub_names, reddit) -> str:

    # Keep reddit param constant
    func = partial(get_formatted_post, reddit=reddit)

    with ThreadPoolExecutor() as exe:
        results = exe.map(func, sub_names)
        return "".join(results)

# get top post from subreddit and format as string
def get_formatted_post(sub_name, reddit) -> str:
    subreddit = reddit.subreddit(sub_name)
    try:

        # top returns an Iterator, get the first value
        submission = next(subreddit.top('day', limit=1))

        # format post
        formatted_sub_name = subreddit_name = "**r/" + str(submission.subreddit) + "**"
        title = str(submission.title)
        link = str(submission.shortlink)
        formatted_post = (formatted_sub_name +"\n\n" + title +": " + link + "\n\n")

        return formatted_post

    except Exception as e:
        traceback.print_exc()
        formatted_sub_name = "**r/" + str(subreddit) + "**" + "\n\n"
        return formatted_sub_name  +  "Error encountered for r/" + str(subreddit) + "\n\n"

def pm(subject, body, recipient, reddit) -> None:
    reddit.redditor(recipient).message(subject, body)

if __name__ == "__main__":
    # Read inputs from file line by line and ignore empty
    all_lines = open(args.filepath, "r").read().splitlines()
    input_subs = [sub for sub in all_lines if sub]

    # initialize reddit instance
    reddit = praw.Reddit('bot1')

    start = time.time()

    # build and send message
    subject = build_subject()
    body = build_body(input_subs, reddit)
    pm(subject, body, args.username, reddit)

    end = time.time()
    print("Time: " + str(end - start))
