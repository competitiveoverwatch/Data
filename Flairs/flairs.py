from config import const, creds
import praw

# Requires bot be given 'flair' permission

reddit = praw.Reddit(client_id = creds.reddit_client_id,
                         client_secret = creds.reddit_client_secret,
                         password = creds.reddit_password,
                         user_agent = const.user_agent,
                         username = creds.reddit_username)

subreddit = reddit.subreddit(const.subreddit)

flairs = {}
for f in subreddit.flair():
    name = f['flair_css_class']
    if not name in flairs:
        flairs[name] = 0

    flairs[name] += 1

sorted_flairs = sorted(flairs.items(), key=lambda x: x[1], reverse=True)
for name, count in sorted_flairs:
    print("{0}: {1}".format(name, count))