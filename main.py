#!/usr/bin/env python
# coding=utf8

import feedparser
import typer
# from typing import Optional
# import sys
# import datetime
# import urllib
# import pprint
# import datetime
# import json

# We'll need to instantiate the Typer class so we can
# work with it later when we need to get input
# from the command line
app = typer.Typer()


# Here I created a function where I pass a default parameter
# and assign that parameter to the app variable I created above the function
# I have not run this yet so not sure of any scope issues

# noinspection PyStatementEffect
def main(url: str = typer.Option(..., prompt="Please enter the url you'd like to parse")):
    """
    This is where I'll place most of
    the business logic for this script
    """
    app.echo(f"{url}")
    fp = feedparser.parse(url)
    fp['feed']['title']
    print(fp)


if __name__ == "__main__":
    main()
