from __future__ import absolute_import
from __future__ import print_function
import sys , urllib.request , os, time
import requests
from six.moves import input
import webbrowser

def timebanner(s):

    for c in s + '\n' :

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep( 0 / 100)




A = """
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>
<          user-link                    >
< snapchat.com/add/flaah999             >
< instagram.com/0xfff0800               >
< T.me/Xfff0800                         >
<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

"""
print ("")
print(A)



url = input("\n username : ")

link = {
        'https://www.facebook.com',
        'https://twitter.com',
        'https://www.instagram.com',
        'https://www.youtube.com/user',
        'https://www.producthunt.com/@',
        'https://www.pinterest.com',
        'https://www.flickr.com/people',
        'https://vimeo.com',
        'https://soundcloud.com',
        'https://disqus.com',
        'https://medium.com/@',
        'https://about.me',
        'https://flipboard.com',
        'https://slideshare.net',
        'https://open.spotify.com/user',
        'https://www.scribd.com',
        'https://www.patreon.com',
        'https://bitbucket.org',
        'https://gitlab.com',
        'https://www.github.com',
        'https://www.goodreads.com',
        'https://www.instructables.com/member',
        'https://www.codecademy.com',
        'https://en.gravatar.com',
        'https://pastebin.com/u',
        'https://foursquare.com',
        'https://tripadvisor.com/members',
        'https://www.wikipedia.org/wiki/User:',
        'https://news.ycombinator.com/user?id=',
        'https://www.codementor.io',
        'https://www.trip.skyscanner.com/user',
        'https://blogspot.com',
        'https://wordpress.com',
        'https://tumblr.com',
        'https://livejournal.com',
        'https://slack.com',
        'https://ask.fm',
        'https://www.snapchat.com/add',
        'https://www.tiktok.com/@',
        'https://haraj.com.sa/users',
        'https://t.me/',


    }


for link2 in link :

    link3 = link2+"/"+url

    try :

        openurl = urllib.request.urlopen(link3)

        print ( link3 + " ==> \n good ")


    except urllib.error.URLError as msg :
        
                print ( link3 + " ==> \n sorry ")


print('Searching for user tweets is in progress')

o = webbrowser.open_new('https://mobile.twitter.com/search?q='+url+'')


print('Searching for the user in Google')

p = webbrowser.open_new('http://www.google.com/search?q='+url+'&pov=107128685182183119625&usg=__uAMtO0js_mAj03ni57W7YeWKuB8=&hl=ar')
