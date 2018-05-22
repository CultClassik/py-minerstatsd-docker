#!/usr/bin/env python

import requests
import collectd
import re
import json
import sys

def readconf(config):
    for node in config.children:
        for k in ['interval', 'url']:
            if node.key == k:
                cfg[k] = node.values[0]
                collectd.info('{0} set to: {1}'.format(k, cfg[k]))

def readvals(cons = False):
    if not cons:
        collectd.info('calling {0}'.format(cfg['url']))

    try:
        r = requests.get(cfg['url'])
        t = re.search('\{[^\}]+\}', r.text)
        j = json.loads(t.group(0))
    except ValueError, e:
        if not cons:
            collectd.info(str(e))
        else:
            print(str(e))
        return

    val = [
        {
            'k': 'reportedHashRate',
            'v': j['result'][2].split(';')[0],
            't': 'gauge' 
        },
    ]

    if cons:
        print(val)
        return

    for v in val:
        c = collectd.Values(type = v['t'])
        c.plugin = v['k']
        c.dispatch(values = [v['v']])

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def validate_cfg(cfg):
    # ensure we have a url and interval defined

if __name__ == '__main__':
    readvals(True)
    cfg = getopts(argv)
else:
    collectd.register_config(readconf)
    collectd.register_read(readvals, int(cfg['interval']))
