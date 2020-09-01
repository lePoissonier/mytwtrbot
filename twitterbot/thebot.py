import tweepy
import time

print('ok')

CONSUMER_KEY = 'DPgPHp5dKUqLWmDtnQMZkKE1G'
CONSUMER_SECRET = 'tRXHC6U8ti9GYOhSnU9CpfPI7h2pdqEX55eE8WbsZJuz0HSya9'
ACCESS_KEY = '1036556466969366528-FuWYrSZHqbMlDSkucJ9EOmWV1KaFA5'
ACCESS_SECRET = 'tPodxVpd0Wj8pSdkULFFXvwADTmd1iWoi5VR0lRVNJ7mD'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use the id of your last twt for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in mentions:
        print(str(mention.id) + ' - ' + mention.text)
        if '#linosbot' in mention.text.lower():
            print('#linosbot détecté', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#linosbot détecté', mention.id)
            
while True:
    reply_to_tweets()
    time.sleep(15)