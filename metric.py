#!/usr/bin/env python3
#
# Name: metric.py
# Description: This program just uploads text from one file to another file
# 10 times a day, for the purpose of appearing as if I program all the time.
# I do, but like, probably not as much as a github metric might have you believe.
#
# Algorithm will be:
# Take the current start date (in epoch),
# Get the current date.
# Determine how many days apart they are.
# multiply that number by 10 (10 because that's how many commits I'll do per day)
# That number will be what line to start on. and stop on will be 10 lines after that.

import os, sys, time
