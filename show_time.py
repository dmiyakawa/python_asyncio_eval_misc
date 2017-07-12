#!/usr/bin/env python

import datetime
import time

while True:
    print('now:       {}'.format(datetime.datetime.now()))
    print('time:      {}'.format(time.time()))
    print('monotonic: {}'.format(time.monotonic()))
    print('-----')
    time.sleep(1)
