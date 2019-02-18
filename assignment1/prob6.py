import sys
import json
import re
from operator import itemgetter

def main():
    happy_score = 0
    # afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    occur = {}

    for line in tweet_file:
        tweetlines = json.loads(line)
        if 'entities' in tweetlines.keys():
            entities = tweetlines['entities']
            if 'hashtags' in entities.keys():
                tags = entities['hashtags']
                if len(tags) > 0:
                    for tag in tags:
                        hashtag = tag['text'].encode('ascii', 'ignore').lower()
                        hashtag = re.sub(r'[^a-zA-Z0-9]','', hashtag)
                        if hashtag in occur:
                            occur[hashtag] += 1
                        else:
                            occur[hashtag] = 1
    occurrences = sorted(occur.items(), key=itemgetter(1), reverse = True)
    for i in range(1, 11):
        print('{} {}'.format(occurrences[i][0],occurrences[i][1]))

if __name__ == '__main__':
    main()