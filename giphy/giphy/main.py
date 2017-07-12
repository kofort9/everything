#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import urllib2
import urllib
import jinja2
import os

jinja_environment = jinja2.Environment(
	loader = jinja2.FileSystemLoader(
		os.path.dirname(__file__))) 

class MainHandler(webapp2.RequestHandler):
	def get(self):






		giphy_data_source = urllib2.urlopen(
            "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=10")
		giphy_json_content = giphy_data_source.read()
		parsed_giphy_dictionary = json.loads(giphy_json_content)
		gif_url = parsed_giphy_dictionary['data'][2]['images']['original']['url']
		#self.response.write(gif_url)

		template  = jinja_environment.get_template("giphy.html")
		self.response.write(template.render(
			{ "gif": gif_url
			}))


class SearchHandler(webapp2.RequestHandler):
	"""docstringSfor searchHandler"""
	def get(self):
		template = jinja_environment.get_template("search.html")
		self.response.write(template.render())
		

class GiphyHandler(webapp2.RequestHandler):
	"""docstring for GiphyHandler"""
	def get(self):
		sQuery = self.request.get('sQuery')
		base_url = 'http://api.giphy.com/v1/gifs/search?'
		url_params = {'q': sQuery, 'api_key': 'dc6zaTOxFJmzC', 'limit':5}
		content = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
		content_dictionary = json.loads(content)
		template = jinja_environment.get_template("giphy.html")
		self.response.out.write(template.render({
			'content' : content_dictionary,
			}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/search', SearchHandler),
    ('/gif', GiphyHandler)

], debug=True)
