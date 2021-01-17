#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------
#                  ΕΞΟΔΑ
#                  Ντίνι Ιορδάνης
#                  2021
# V 0.1
# ----------------------------------------------------------

import logging
import os
import sys
import datetime


version = "V 0.7 Alfa"

database = "outgoings.db"

# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE και Ημερομηνία ------------------
today = datetime.datetime.today().strftime("%d %m %Y")
log_dir = "logs" + "/" + today + "/"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
else:
    pass

log_file_name = "Εξοδα " + today + ".log"
log_file = os.path.join(log_dir, log_file_name)

# log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler(log_file, 'a', 'utf-8')  # or whatever
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # or whatever
handler.setFormatter(formatter)  # Pass handler as a parameter, not assign
root_logger.addHandler(handler)
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
