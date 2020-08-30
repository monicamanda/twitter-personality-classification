# twitter-personality-classification
Classification of twitter user's personality to Big Five Model. Feature extraction used in this system are detecting emotion, detecting sentiment, and social factors. Dataset contain 400 users who use bahasa Indonesia as their first language and total 80.000 tweets.

# Big Five Personality
Personality based on a theory that human personality associated with five board dimensions with only one dimension dominated. And the five factors are:
- Openness to Experience (O)
- Conscientiousness (C)
- Extraversion (E)
- Agreeableness (A)
- Neuroticism (N)

# Detecting Emotion and Sentiment
To find out the emotion and sentiment that match a particular word from user's tweet, dictionary that used is NRC Word-Emotion Association Lexicon by Saif Mohammad 
NRC Emotion Lexicon is a list of words and their associations with 8 basic emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) and 2 sentiments (negative and positive). The annotations were manually done by crowdsourcing.
http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm (available in bahasa Indonesia too)

# Social Factors
get user's social data from twitter like number of following, followers, retweet, and favorite.

# Naive Bayes
A classifier to classify and predict personality. Use scikit-learn library.
