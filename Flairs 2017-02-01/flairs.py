from config import const, creds
import praw

# Requires bot be given 'flair' permission

subname = "competitiveoverwatch"
reddit = praw.Reddit(client_id = creds.client_id,
                         client_secret = creds.client_secret,
                         password = creds.password,
                         user_agent = const.user_agent,
                         username = creds.username)

flairs = {}
for f in subreddit.flair():
    name = f['flair_css_class']
    if not name in flairs:
        flairs[name] = 0

    flairs[name] += 1

sorted_flairs = sorted(flairs.items(), key=lambda x: x[1], reverse=True)
for name, count in sorted_flairs:
    print("{0}: {1}".format(name, count))