#!/usr/bin/env python

import requests
import collectd
import re
import json
import sys

#def readconf(config):
#    for node in config.children:
#        for k in ['interval', 'url']:
#            if node.key == k:
#                cfg[k] = node.values[0]
#                collectd.info('{0} set to: {1}'.format(k, cfg[k]))

def readvals(cons = False):
    if not cons:
        conn.info('calling {0}'.format(cfg['url']))

    try:
        r = requests.get(cfg['url'])
        t = re.search('\{[^\}]+\}', r.text)
        j = json.loads(t.group(0))
    except ValueError as e:
        if not cons:
            conn.info(str(e))
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
        c = conn.Values(type = v['t'])
        c.plugin = v['k']
        c.dispatch(values = [v['v']])

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            new_key = argv[0].replace('-', '', 1)
            opts[new_key] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    print('Opts input:')
    print(opts)
    return opts

if __name__ == '__main__':
    cfg = getopts(sys.argv)
    readvals(True)
    collectd.start_threads()
    conn = collectd.Connection(cfg['host_name'], cfg['collectd_name'], cfg['collectd_port'])
else:
    conn.register_config(readconf)
    conn.register_read(readvals, int(cfg['interval']))
