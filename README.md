## History of this code

De-spammed this blog (with Naive Bayes)

This morning, I was trying to decrease the amount of email in my inbox. I had a few messages with
subjects like:

* comment on http://www.asheesh.org/note/debian/freed-software
* comment on http://www.asheesh.org/note/sysop/comments
* comment on http://www.asheesh.org/note/debian/freed-software

But all the comments in this case are spam. I'm using an Akismet API plugin
for pyblosxom, but that has a few shortcomings. Like anything else, it misses
some spam, but moreover, it doesn't help me find and remove old spam comments
in bulk.

So I wrote a small tool this morning. Here is how it works:

* It loops over the comments directory.
* It converts each comment into a mailbox file, and passes it spambayes for processing.
* It shows me the guess spambayes has, as well as spambayes' certainty, and asks me to confirm. If I confirm it is spam, it asks if I want to delete it. (If it notices spambayes got it wrong, it retrain$
* After I have dealt with the comment, it creates a stamp file next to the comment so that it won't ask me about that the next time I run the tool.

Voila! A spam moderation queue with artificial intelligence.

## Author

Asheesh Laroia <asheesh@asheesh.org>

## License

CC Zero.
