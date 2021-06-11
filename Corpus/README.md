# Corpus

## Data

We used the tweets from the list provided by [1], you can find the set of ids [here](https://figshare.com/articles/Twitter_event_datasets_2012-2016_/5100460 "Set of ids for the corpus").
The corpus contains around 150 million of ids, at the time we wrote this lines we were able to retrieve around 82 million of tweets.

[1] Zubiaga, A. (2018). A longitudinal assessment of the persistence of twitter datasets. J. Assoc. Inf. Sci. Technol., 69(8):974–984.

## Parts of this repository

* [Extractive Oracle](./Extractive%20Oracle): Contains the extractive Oracles we made for each event with ROUGE-2 and Cosine similarities.
* [Gold Standard](./Gold%20Standard): Contains the Gold Standard for each event using the [Wikipedia Current Events Portal](https://en.wikipedia.org/wiki/Portal:Current_events). Warning: given dates in Gold Standard are expressed in local time, you may have to convert tweets timestamps from UTC time to local time for proper comparison.

For more annotations including tweets ids, please contact us. We can't release this amount of tweets ids on this Git due to the distibution restrictions imposed by Twitter.