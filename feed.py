"""
    =======
    feedgen
    =======

    This module can be used to generate web feeds in both ATOM and RSS format.
    It has support for extensions. Included is for example an extension to
    produce Podcasts.

    :copyright: 2013 by Lars Kiesow
    :license: FreeBSD and LGPL, see license.* for more details.


    -------------
    Create a Feed
    -------------

    I need to capture the url passed into the cli from the main.py in the fg.id() method. Same with all the other methods. Is there a way to do this or do I need to structure the file some other way?

        >>> from feedgen.feed import FeedGenerator
        >>> fg = FeedGenerator()
        >>> fg.id('http://lernfunk.de/media/654321')
        >>> fg.title('Some Testfeed')
        >>> fg.author( {'name':'John Doe','email':'john@example.de'} )
        >>> fg.link( href='http://example.com', rel='alternate' )
        >>> fg.logo('http://ex.com/logo.jpg')
        >>> fg.subtitle('This is a cool feed!')
        >>> fg.link( href='http://larskiesow.de/test.atom', rel='self' )
        >>> fg.language('en')
"""

from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.id('http://lernfunk.de/media/654321')
fg.title('Some Testfeed')
fg.author( {'name':'John Doe','email':'john@example.de'} )
fg.link( href='http://example.com', rel='alternate' )
fg.logo('http://ex.com/logo.jpg')
fg.subtitle('This is a cool feed!')
fg.link( href='http://larskiesow.de/test.atom', rel='self' )
fg.language('en')

atomfeed = fg.atom_str(pretty=True) # Get the ATOM feed as string
rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string
fg.atom_file('atom.xml') # Write the ATOM feed to a file
fg.rss_file('rss.xml') # Write the RSS feed to a file