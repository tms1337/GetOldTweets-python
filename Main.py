import sys

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got


def main():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('bitcoin').setSince("2017-10-17").setUntil(
        "2017-10-18")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    print(len(tweets))

    # for t in tweets:
    #     if t.favorites > 0:
    #         print(t)


if __name__ == '__main__':
    main()
