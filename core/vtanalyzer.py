#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Alvaro Nunez
#
#This file is part of SniffVPN.
#
#SniffVPN is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#SniffVPN is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with SniffVPN.  If not, see <http://www.gnu.org/licenses/>.

import json, urllib, urllib2

def vtanalyzer(url):
  data = urllib.urlencode({'url': url})
  req = urllib2.Request('https://www.virustotal.com/en/url/submission/', data)
  req.add_header('Referer', 'https://www.virustotal.com/en/')
  req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
  response = urllib2.urlopen(req)
  json = '{"url": "'+url+'", '+response.read()[1:]

  vtjson = open("panel/data/vtanalyzer.json", "a")
  vtjson.write(json+",")
  vtjson.close()