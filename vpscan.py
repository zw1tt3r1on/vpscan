import requests
import re
import argparse

parser = argparse.ArgumentParser(description='Automated Script for Identifying Unauthenticated Varnish Cache Purge')
parser.add_argument('-d', '--domain', help='Specify a single domain.')
parser.add_argument('-l', '--list', help='Specify a list of domains.')
args = parser.parse_args()
single_domain = args.domain
list_domains = args.list

pattern = r'"status":\s*"ok"'

def varnish_cache_purge(url):
    try:
        response = requests.request('PURGE', f'https://{url}')
        response_status = response.status_code
        if response_status == 200:
            response_text = response.text
            result = re.search(pattern, response_text)
            if result:
                return (f"[VULNERABLE] {url}")
            else:
                return (f"[NOT VULNERABLE] {url}")
        else:
            return (f"[NOT VULNERABLE] {url}")
    except:
        return (f"[NOT VULNERABLE] {url}")

if single_domain:
    print(varnish_cache_purge(single_domain))

elif list_domains:
    with open(list_domains, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    for url in urls:
        print(varnish_cache_purge(url))
else:
    print("[ERROR] Terminating Script...")