import sys
import json
import re

running_dic = {}


def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    total_count = 0
    # afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    # afinnfile = open("AFINN-111.txt")
    # scores = {} # initialize an empty dictionary
    # for line in afinnfile:
      # term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      # scores[term] = int(score)  # Convert the score to an integer.

    # print(scores.items()) # Print every (term, score) pair in the dictionary

    tweetcleanup = {}

    for line in tweet_file:
        tweetlines = json.loads(line)
        if 'text' in tweetlines.keys():
            tweets = tweetlines['text']
            tweet_words = tweets.split(' ')
            for wd in tweet_words:
                corrected_words = wd.encode("ascii", "ignore")
                if corrected_words.startswith('@') or corrected_words.startswith('http://') or corrected_words.startswith('https://'):
                    corrected_words = ''
                else:
                    corrected_words = re.sub(r'[^a-zA-Z0-9]','', corrected_words)
                if corrected_words != '':
                    total_count += 1
                if corrected_words in running_dic:
                    running_dic[corrected_words] += 1
                else:
                    running_dic[corrected_words] = 1
    for wrd in running_dic:
        total_score = float(running_dic[wrd]) / total_count
        print ('{} {}'.format(wrd, total_score))

if __name__ == '__main__':
    main()
