#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import os
import collections

regex = "From \d+@.+"

mbox_file = '/PATH/TO/MBOX_FILE.MBOX'
path_to_write = '/PATH/TO/WRITE/EML_FILES'

to_search = re.compile(regex)

counter = 0

if os.path.isfile(mbox_file):
    with open(mbox_file, 'r') as f:
        new_file = f.read()
        mails = re.split(regex, new_file)
        for mail in mails:
            mail = mail.strip('\n')
            with open(path_to_write + 'mail_' + str(counter) + '.eml', 'w+') as message:
                try:
                    message.write(mail)
                    counter += 1
                except Exception as e:
                    print e

print "Total msgs: " + str(counter)
