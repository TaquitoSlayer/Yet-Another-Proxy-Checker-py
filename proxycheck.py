# imagine importing 8 modules to check some proxies
# your mcm bot's proxycheck probably uses over 15 though just so it gives you red/green colors
# import colorama WHEN
from multiprocessing import Process
from threading import Thread
import time
from itertools import cycle
import random
import requests
import logging
from sys import platform
# from tqdm import tqdm

r = requests.session()
logging.basicConfig(level=logging.INFO, format = '%(asctime)s: %(message)s')

# ok let's be honest, random user-agent hella placebo and inconsistent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}

################ vchange this shitv ################
file_unchecked = 'proxies_unchecked.txt'
file_checked = 'proxies_good.txt'
ping_wanted = 500
site = 'offthehook.ca'
################ ^change this shit^ ################

# thanks again to @idontcop for this method, been using it for 2 years
def proxy_parse(proxy):
    proxy_parts = proxy.split(':')
    if len(proxy_parts) == 2:
        ip, port = proxy_parts
        formatted_proxy = {'http': f'https://{ip}:{port}/',}
    elif len(proxy_parts) == 4:
        ip, port, user, password = proxy_parts
        formatted_proxy = {'http': f'https://{user}:{password}@{ip}:{port}/',}
    formatted_proxy = formatted_proxy['http']
    return formatted_proxy

def read_proxies(file):
    with open(file) as txt_file:
        proxies = txt_file.read().splitlines()
    return proxies

# imagine using a function before all other functions are declared
# can i get a REEEEEE?
proxies = read_proxies(file_unchecked)

# we check for a successful return on the products.json['products']['handle'] method for shopify
# made to be modified without the need for try/excepts as that's taken care of in main()
def List(url, proxy):
    json_url = f'https://{url}/products.json'
    dump = r.get(json_url, headers = headers, proxies={"http": proxy, "https": proxy}, timeout=10) # make timeout=None if you wanna live life on the edge - fuck pep8 standards on these comments too
    products = dump.json()['products']
    for product in products:
        _placeholder = product['handle']

def main(proxy):
    proxy_formatted = proxy_parse(proxy)
    try:
        start = time.time()
        List(site, proxy_formatted)
        end = time.time()
        # before some of yall start coming at me, i know this is on how long it took the script to respond, not the actual connection time
        # to those that gunna call me out, i made this in entire script in 10 minutes, 3 minutes of which were watching the Oilers lose another game
        time_elapsed = end - start
        time_elapsed = time_elapsed * 1000 # quick maths
        if time_elapsed < ping_wanted:
            with open(file_checked, 'a') as f:
                f.write(f'{proxy}\n')
            logging.info(f'{proxy} - GOOD PROXY {round(time_elapsed)}ms')
        else:
            logging.info(f'{proxy} - SLOW PROXY {round(time_elapsed)}ms')
    except:
        # if no response received, or too many retries or exceeds 10 seconds, call it a bad little proxy.
        # BAD PROXY! GO TO YOUR CORNER.
        logging.info(f'{proxy} - BAD PROXY')


if __name__ == '__main__':
    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        # for proxy in tqdm(proxies): - added this cancer and it ended up fucking with the threads
        for proxy in proxies:
            # cpu bound weeeeeeeeeeee
            p = Process(target=main, args=(proxy,))
            p.start()
        p.join() # i only added this cause it's correct not cause i wanted to
        time.sleep(3)
    elif platform == "win32":
        for proxy in proxies:
            # i've had issues with multiprocessing on windows, which i've eventually fixed for myself but i don't plan on fixing it for everyone else
            p = Thread(target=main, args=(proxy,))
            p.start()
        p.join()
        time.sleep(3)

# i added comments to this cause im really bored
