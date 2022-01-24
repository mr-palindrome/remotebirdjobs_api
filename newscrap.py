import snscrape.modules.twitter as twitterScraper
import json

job_board_list = [
    "RemoteTechJobs0", 
    "zobjobsUS", 
    "RemoteSonar", 
    "RecruitngEdge",
    "CodingJobsIt",
    "jobscanCo",
    "JobHuntOrg",
    "justremoteco",
    "nodeskco",
    "weworkremotely",
    "jobmote",
    "WantRemoteJob",
    "daily_remote",
    "remoteworkhub",
    "workingnomads",
    "DevStartupJobs",
    "zobjobsGB",
    "growremotelyio",
    "jobsincrypto",
    "Rezoomex",
    "_remotify",
    "Up2staff",
    "zobjobsCA",
]

block_list = ["https://twitter.com/" + e for e in job_board_list]


def scrape(query):
    scraper = twitterScraper.TwitterSearchScraper(query)
    tweets = []
    max_count = 30
    for i, tweet in enumerate(scraper.get_items()):
        if i > (max_count - 1):
            break

        if str(tweet.user) not in block_list:
            tweets.append({
                # "sno":str(i+1),
                "id": str(tweet.id),
                "url": str(tweet.url)
                # "url": tweet.url,
                # "user": str(tweet.user),
                # "content": tweet.content,
                # "date": str(tweet.date)
            })
        else:
            max_count += 1

    f = open("tweets.json", "w")
    j = json.dumps(tweets)

    f.write(j)
    f.close()


if __name__ == "__main__":
    # scrape("develoepr job remote")
    pass
