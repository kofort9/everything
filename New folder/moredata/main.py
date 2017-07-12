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
import jinja2
import os

from google.appengine.ext import ndb

jinja_enviroment = jinja2.Environment(
	loader =jinja2.FileSystemLoader(
		os.path.dirname(__file__)))

class Tweets(ndb.Model):
	post = ndb.StringProperty()
	timestamp = ndb.TimeProperty()

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_enviroment.get_template('drafttweets.html')
		self.response.write(template.render())

	def post(self):
		draft_from_from = self.request.get('draft')

		tweet_model = Tweets(post=draft_from_from)
 		#saves to data base [.put()]
		tweet_key = tweet_model.put()
		
		template = jinja_enviroment.get_template('tweets.html')
		self.response.write(template.render(
			{
			'tweet': draft_from_from,
			}))
class SavedTweetHandler(webapp2.RequestHandler):
	"""docstring for tweet"""
	def get(self):
		tweet_query = Tweets.query().order(-Tweets.timestamp)
		list_of_tweets = tweet_query.fetch(limit=10)

		template = jinja_enviroment.get_template('tweetlist.html')
		self.response.write(template.render(
			{
			'listoftweet': list_of_tweets,
			}))




		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/savedtweets', SavedTweetHandler),
], debug=True)
