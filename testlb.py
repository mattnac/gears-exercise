#!/usr/bin/python

import argparse
import requests
from collections import Counter
import sys

def parse_args():
    '''
    Parse and handle the required arguments to the script.
    '''
    parser = argparse.ArgumentParser(description="Args for the script")
    parser.add_argument("--host", help="Host to run the tests against", required=True)
    parser.add_argument("--num", help="Number of requests to send", required=True, type=int)

    args = parser.parse_args()

    return args

def do_requests(req_url, num_reqs):
    '''
    Perform requested numbers of requests
    '''
    x = 0
    responses = []
    while (x < num_reqs):
        r = requests.get(req_url)
        if r.status_code == 200:
            responses.append(r.text.strip())
        else:
            print "Got non 200 status code {}".format(r.status_code)
            sys.exit(1)
        x = x + 1

    return responses

def main():
    '''
    The main function.
    '''
    args = parse_args()

    num_reqs = args.num
    host = args.host
    req_url = "http://{}:8080".format(host)
    
    responses = do_requests(req_url, num_reqs)

    tally = Counter(responses)
    for node in sorted(tally):
        print "{}: {}".format(node, tally[node])

if __name__ == '__main__':
    main()
