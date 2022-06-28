#!/usr/bin/env python
# coding=utf8

import feedparser
import typer
import sys
import datetime
import urllib
import pprint
import datetime
import json

app = typer.Typer()

def main(url: str = app.Option(...,prompt="Please enter the url you'd like to parse")):
  app.echo(f"{url}")
  fp = feedparser.parse(url)
  fp['feed']['title']
  print(fp)




if __name__ == "__main__":
    app()