from i3pystatus import IntervalModule
from os.path import join

import json
import logging
import random
import os
import datetime

class File(IntervalModule):

    settings = (
        "file",
        "original_date",
        "color",
        "interval"
    )
    color = "#FFFFFF"
    format="{key}"

    # def go_next(self):
    #     logging.info('hi from go_next')
        # logging.info(f'{total} is total from before run')



    def run(self):
        # initialize logging
        logging.basicConfig(filename='learnvim.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG)

        # file="/home/anya/dotfiles/commands.txt"
        file = self.file

        # Total is a dict of the form {line number: line/tip/command/thing to learn}
        total = {}

        if datetime.datetime.now().time().hour == 23:
            self.interval=10


        # read in file and populate total
        with open(file, "r") as f:
            line = f.readline()
            key = 1
            while line:
                total[key] = line.strip()
                line = f.readline()
                key+=1

        # original_date = datetime.datetime.strptime("2021-05-30", '%Y-%m-%d')
        # calculate how many lines in the file
        num_things_to_learn = len(total)


        # take the date from the config file, convert to datetime object, and find which day we're on
        original_date = datetime.datetime.strptime(self.original_date, '%Y-%m-%d')
        current_date = datetime.datetime.today()
        todays_line_number = (current_date-original_date).days + 1

        # if there are no more things to learn, display "Done learning!"
        if num_things_to_learn < todays_line_number:
            cdict = {"key": "Done learning!"}
        else:
            cdict = {"key": total[todays_line_number]}


        logging.info(f'{cdict} is cdict')

        self.data = cdict
        self.output = {
            "full_text": self.format.format(**cdict),
            "color": self.color
        }
