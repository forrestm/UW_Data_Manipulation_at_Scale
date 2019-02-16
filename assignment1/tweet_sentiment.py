import sys
import json

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    print('Starting the scoring')

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# print(scores.items()) # Print every (term, score) pair in the dictionary

tweetcleanup = {}
tweets = {}

with open('output.txt', 'r') as f:
    for line in f:
        tweets.update(json.loads(line))
        if 'created_at' in json.loads(line):
            # tweetcleanup.update({tweets['id']:tweets['text']})
            tweet_word_list = tweets['text'].split()
            sentiment_score = 0
            word_score = 0
            for i in range(len(tweet_word_list)):
                word_score = scores.get(tweet_word_list[i],0)
                sentiment_score += word_score
            with open('orderedscores.txt', 'a') as the_file:
                the_file.write('{}\n'.format(sentiment_score))
                # tweetcleanup.update({tweets['id']:sentiment_score})
        else:
            with open('orderedscores.txt', 'a') as the_file:
                the_file.write('{}\n'.format(0))
                # tweetcleanup.update({'noid':0})

if __name__ == '__main__':
    main()
