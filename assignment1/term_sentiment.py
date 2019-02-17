import sys
import json

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # print(scores.items()) # Print every (term, score) pair in the dictionary

    tweetcleanup = {}
    tweets = {}
    newsentimentlist = {}

    # with open('output.txt', 'r') as f:
        # for line in f:
    for line in tweet_file:
        tweets.update(json.loads(line))
        if 'created_at' in json.loads(line):
            tweet_word_list = tweets['text'].split()
            sentiment_score = 0
            word_score = 0
            for i in range(len(tweet_word_list)):
                word_score = scores.get(tweet_word_list[i],0)
                sentiment_score += word_score

            for i in range(len(tweet_word_list)):
                if tweet_word_list[i].encode('utf-8') not in scores.keys():
                    tempwordholder = tweet_word_list[i]
                    # if tweet_word_list[i] not in newsentimentlist.keys()
                    if sentiment_score > 0:
                        termwordscore = 0.5
                        # newsentimentlist.update({tweet_word_list[i]:termwordscore})
                    elif sentiment_score < 0:
                        termwordscore = -0.5
                    elif sentiment_score == 0:
                        termwordscore = 0
                        # newsentimentlist.update({tweet_word_list[i]:termwordscore})
                if tweet_word_list[i] in newsentimentlist.keys():
                    old_score = newsentimentlist[tweet_word_list[i]]
                    new_score = old_score + termwordscore
                    newsentimentlist.update({tweet_word_list[i]:new_score})
                    tempscoreholder = new_score
                else:
                    newsentimentlist.update({tweet_word_list[i]:termwordscore})
                    tempscoreholder = termwordscore
                # print('{} {}\n'.format(tempwordholder, tempscoreholder))
    for k, v in newsentimentlist.items():
        print('{} {}'.format(k,v))

if __name__ == '__main__':
    main()
