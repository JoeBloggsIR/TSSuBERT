# TSSuBERT

This GitHub repository contains the Corpus and Model contributions of the paper introducing the TSSuBERT model (under submission).

## Parts of this repository

* [Corpus](./Corpus): Contains the Gold Standard and two extractive Oracle for the corpus.
* [Model](./Model): Contains the architecture of the model using TensorFlow as well as the transformers library and the trained weights we used in the paper.

## Data

We used the tweets from the list provided by [1], you can find the set of ids [here](https://figshare.com/articles/Twitter_event_datasets_2012-2016_/5100460 "Set of ids for the corpus").
The corpus contains around 150 million of ids, at the time we wrote this lines we were able to retrieve around 82 million of tweets.

[1] Zubiaga, A. (2018). A longitudinal assessment of the persistence of twitter datasets. J. Assoc. Inf. Sci. Technol., 69(8):974–984.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

