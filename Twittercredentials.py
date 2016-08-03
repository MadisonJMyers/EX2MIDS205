import tweepy

consumer_key = "gv8Qc8CZEvVIE7lMgTox9lNJj";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "qCjUn027fKP4mKhTAwkwf9xhsD8KBKu6c42aMGFkLtVxMoPX4V";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "3262865660-oTq0I5zlEZQTHkPiNSYxoyIDVtRukxEhU1jjuuE";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "FLjwQ34rTklsXq4C9vMWWznSZHYIFHkg8SUfX97U3ew67";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



