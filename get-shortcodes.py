import instaloader
import time
import os

I = instaloader.Instaloader()
I.login()
query = instaloader.Hashtag.from_name(I.context,
                                      "100daysofpractice")
for post in query.get_all_posts():
    with open("shortcodes.txt", "a") as file_object:
        file_object.write(post.shortcode + "\n")
        time.sleep(1)
