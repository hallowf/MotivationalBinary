# MotivationalBinary (A.K.A. HEXadecimalChuck)

![Build](https://scrutinizer-ci.com/g/hallowf/MotivationalBinary/badges/quality-score.png?b=master) ![Build](https://scrutinizer-ci.com/g/hallowf/MotivationalBinary/badges/build.png?b=master)


## HEXadecimalChuck

This was supposed to be Motivational quotes in binary but due to the lack of free APIs that had the required needs of this project, and twitter's mas tweet length of 280 I just decided to use random quotes of Chuck Norris to hexadecimal

## How to use:

You will need twitter's api keys you can insert them in the file api_key.py
between the quotation marks "".

When you run tweeterBot.py it fetches a random chuck quote converts it into hexadecimal and posts it on twitter (You can setup a cron job to automate it or use the schedule module for python)

## Notes:

When a master_ID is provided in search_to_follow.py it fetches "a page" of the user's followers (it contains 20 ids) to traverse along the page an integer value is stored in a pickle file

To avoid timeouts due to rate limiting the program sleeps for 70 seconds in between friend_request (70 * 20 = 1400 Seconds - 38 minutes)

## Requirements:

You can use:

    pip install -r requirements.txt

It will install:

  * requests
  * TwitterAPI


## Resources:

### All trademarks and registered trademarks are the property of their respective owners.

### disclaimer: This product is not affiliated with Chuck Norris, any motion picture corporation, any television corporation, parent, or affiliate corporation. All motion pictures, products, and brands mentioned are the respective trademarks and copyrights of their owners. All material is intended for entertainment purposes only. The content found here is not necessarily true and should not be regarded as truth.

### Chuck quotes API

https://api.chucknorris.io/

### TwitterAPI - Python

https://github.com/geduldig/TwitterAPI

### Requests - Python

https://github.com/requests/requests/
