import sys

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

month = sys.argv[1]
year = sys.argv[2]

since = int(sys.argv[3])
until = int(sys.argv[4])


def to_digit(i):
    if i < 10:
        return '0%d' % i
    else:
        return str(i)


def main():

    for i in range(since, until):

        since_str = '%s-%s-%d' % (year, month, to_digit(i))
        until_str = '%s-%s-%d' % (year, month, to_digit(i+1))
        print('Since %s, until %s' % (since_str, until_str))
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch('bitcoin').setSince(since_str).setUntil(until_str)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
        print(len(tweets))

    # for t in tweets:
    #     if t.favorites > 0:
    #         print(t)


if __name__ == '__main__':
    main()
