# dailyfeed.py
This is a simple Reddit bot that will provide send a formatted PM with a link to the top post for selected subreddits. 

This was intended to use for subreddits that tend to have only a few top posts, that the user can't justify subscribing to.

## Requirements/Installation
Praw: pip install praw

## How To Use
python dailyfeed.py recipient subreddit 

* specify the subreddits (space out multiple) to go through as additional arguments to the call
* specify who you want to send the PM to 

###Example
python dailyfeed.py RecipientRedditor fantheories lifeofnorman youshouldknow 

##Other
OAuth authentication can also be handled in a praw.ini file within the working directory of this script, instead of in the script itself like this bot.

