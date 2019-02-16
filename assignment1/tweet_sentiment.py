import sys
import json

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    print('We out here')
    # sent_file = open(sys.argv[1])
    # tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# print(scores.items()) # Print every (term, score) pair in the dictionary

tweetcleanup = {}
tweets = {}
# for line in open('output.json', 'r'):
for line in open('output.json', 'r'):
    tweets.update(json.loads(line))
    if 'id' in tweets:
        tweetcleanup.update({tweets['id']:tweets['text']})

if __name__ == '__main__':
    main()
