import tweepy
import time
import random

import config

auth = tweepy.auth.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
api = tweepy.API(auth)

quotes = ['Just keep swimming. Just keep swimming. Just keep swimming, swimming, swimming.',
        'I shall call him Squishy and he shall be mine and he shall be my Squishy. Come on, Squishy Come on, little Squishy.', 
        'This is the Ocean, silly, we\'re not the only two in here.', 
        'Hey, look. "Esc-a-pay". I wonder what that means? That\'s funny, it\'s spelled just like the word "escape."', 
        'I shall call him Squishy and he shall be mine and he shall be my Squishy. Come on, Squishy Come on, little Squishy.',
        'Hey there, Mr. Grumpy Gills.', 'I want to touch it...', 
        'I\'m gonna get you. I\'m gonna get you.',
        'Nemo? That\'s a nice name...',
        'Have you seen a clown fish swim by?',
        'Uhhh... the sea monkeys have my money... yes, I\'m a natural blue...',
        'I wish I could speak whale...',
        'DUCK.',
        'Okay, he either said, "move to the back of the throat," or he "wants a root beer float".',
        'Oh don\'t worry. Whales don\'t eat clownfish. They eat krill.',
        'I suffer from short-term memory loss. It runs in my family... At least I think it does...']

p = 1 
while True:
    tweet = api.search('#NEMO', page=p, result_type='recent', count='100')[0]
    s = random.choice(quotes)
    api.update_status('@%s %s' % (tweet.from_user, s), tweet.id)
    r = random.randrange(5, 10) 
    print time.strftime('%H:%M:%S')
    print 'Just keep swimming for %s minutes.' % r
    time.sleep(60 * r)