# dailyfeed.py
This is a simple Reddit bot that will send a formatted PM with a link to the top post for selected subreddits.

This was intended to use for subreddits that tend to have only a few top posts, that the user can't justify subscribing to. Or to act like an easily automated daily feed script.

## Requirements/Installation
Praw: pip install praw

## How To Use
python dailyfeed.py -u recipient -f input_filepath

* specify who you want to send the PM to
* specify the input file of subreddits (one on each line)

### Example
python dailyfeed.py -u ElonMusk -f inputs.txt

## Other
OAuth authentication can also be handled in a praw.ini file within the working directory of this script, instead of in the script itself like this bot.

