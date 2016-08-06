(ns tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          :p 1
          )
    }
    ;; bolt configuration 1
    {"parse-tweet-bolt" (python-bolt-spec
          options
          {"tweet-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["word"]
          :p 1
          )
    ;; bolt configuration 2 
    "count-bolt" (python-bolt-spec
          options
          {"parse-tweet-bolt" :shuffle}
          "bolts.wordcount.WordCounter"
          ["word" "count"]
          :p 1
          )
    }
  ]
)
