#!/usr/bin/env python
# coding=utf8

import typer
import time
from rich import print
from rich.progress import track
import feed

app = typer.Typer()

@app.command()
def url(url: str):
    print(f"Please enter a url {url}")

def main():
    total = 0
    for value in track(range(100), description="Please wait..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Feed created in {total}.")

if __name__ == "__main__":
    typer.run(feed)
