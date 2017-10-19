import sys

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

since = sys.argv[1]
until = sys.argv[2]

def main():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('bitcoin').setSince(since).setUntil(until)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    print(len(tweets))

    # for t in tweets:
    #     if t.favorites > 0:
    #         print(t)


if __name__ == '__main__':
    main()
