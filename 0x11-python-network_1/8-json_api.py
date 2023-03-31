#!/usr/bin/python3
"""A Python Script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    # Get the command line argument for the letter
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Send the POST request to the API endpoint
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        # Parse the response JSON
        data = response.json()
        if data:
            # Print the ID and name of the user(s) found
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
