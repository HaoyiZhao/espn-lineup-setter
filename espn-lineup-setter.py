#!/usr/bin/env python3

import sys
from selenium import webdriver
import unittest

class LineupSetter(unittest.TestCase):
    def setUpDriver(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://www.espn.com/fantasy/basketball/")

if __name__ == '__main__':
	if len(sys.argv) > 1:
		LineupSetter.season_id = sys.argv.pop()
		LineupSetter.team_id = sys.argv.pop()
		LineupSetter.league_id = sys.argv.pop()