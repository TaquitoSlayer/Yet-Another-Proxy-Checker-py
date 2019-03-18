# YAPC-py
Yet Another Proxy Checker made in 10 minutes with Python.
![TaquitoSlayer](https://i.imgur.com/T5cWG3A.png)
### Features
  - Ability to filter proxies based on ping (ms) preference.
  - Corny comments inside the script.
  - Currently supporting Shopify-based sites that support the products.json endpoint, will add Supreme soon.
  - I didn't add the cache bypass in here, go away.
### Requirements
- Python 3.6 or higher.
- Like, maybe a sliver of brain, not even a fully developed one, just a sliver.

### How to use
 - Open Terminal/cmd and cd to directory with script
 - Fill in the variables to your preferences in proxycheck.py
```sh
file_unchecked = 'proxies_unchecked.txt' # name of text file in same directory to check
file_checked = 'proxies_good.txt'# name of text file in same directory to output
ping_wanted = 500 # max ping (ms) wanted from each proxy to be considered good
site = 'offthehook.ca' # what shopify site you want to test it under
```
- For the first time, run both lines in your command line
```sh
$ pip install -r requirements.txt
$ python proxycheck.py
```
- After first run, only second line needed to run

### Follow me on Twitter
- https://twitter.com/taquitoslayer
