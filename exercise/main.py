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
import logging
import os
import math
import random
import urllib2
import json

def crackedCookie():

	fortunes = ['A beautiful smart and loving person will be coming into your life.', 
				'A dubious friend may be an enemy in camouflage.',
				'A feather in the hand is better than a bird in the air.',
				'A fresh start will put you on your way.',
				'A friend asks only for your time not your money.',
				'A friend is a present you give yourself.',
				'A gambler not only will lose what he has, but also will lose what he doesn\'t have.',
				'A golden egg of opportunity falls into your lap this month.',
				'A good friendship is often more important than a passionate romance.',
				'A good time to finish up old tasks.']

	randomNumber = random.randint(0,len(fortunes)-1) 
	#*fortunes.length
	#randomNumber = Math.floor(randomNumber)
	selectedFortune = fortunes[randomNumber]
	return selectedFortune
	
def is_palindrome(word):
	first_half = None
	second_half = None
	#word.replace(' ','')
 
 	if len(word) % 2 == 0:
		first_half = len(word) / 2
		second_half = len(word) / 2
	else:
		first_half = (len(word) / 2) +1
		second_half = (len(word) / 2)

	first_half = word[:first_half]
	second_half = word[second_half:]
	second_half = second_half[::-1]
 
	if first_half == second_half: 
		return word + ' is a palindrome!'
	else:
		return word + ' is not a palindrome...'


jinja_environment =jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
	def get(self):	
		
		response = urllib2.urlopen('https://randomuser.me/api/?results=10')
		content = response.read()
		content_dictionary = json.loads(content)
		template = jinja_environment.get_template('random_user.html')
		self.response.write(template.render({
			'content': content_dictionary
			}))
		

class PalindromeHandler(webapp2.RequestHandler):
	"""docstring for PalindromeHandler"""
	def get(self):
		palindrome_output = is_palindrome('racecar')
		template = jinja_environment.get_template(
			'palindrome.html')
		self.response.write(template.render(
			{
			'palindrome': palindrome_output,
			'word': 'racecar'}))
		
class FortuneHandler(webapp2.RequestHandler):
	"""docstring for FortuneHandler"""
	def get(self):
		fortune_output = crackedCookie()
		template = jinja_environment.get_template(
			'fortune.html')
		self.response.write(template.render({
			'fortune': fortune_output,
			'date': '06.05.2017: '
			#'all_fortunes': fortunes,
			}))
		email ={
		'subject':'Hello!',
		'text': 'hi how are you??"',
		'sender': 'kofort9@gmail.com'
		}


class EmailsHandeler(webapp2.RequestHandler):
	"""docstring for EmailsHandeler"""
	def get(self):
		emails =[ 
		{'title': 'help', 'sender': 'fakeaccount@gmail.com'},
		{'title': 'money pls', 'sender': 'fakeaccount@gmail.com'},
		{'title': 'hey!', 'sender': 'a_friend@gmail.com'},
		{'title': 'spam', 'sender': 'fakeaccount@gmail.com'},
		{'title': 'day 11 hmwk', 'sender': 'drb@hampton.edu'},
		]

		template = jinja_environment.get_template('emails.html')
		self.response.write(template.render(
            {
                'emails': emails
            }))

class SumHandler(webapp2.RequestHandler):
	"""docstring for SumHandler"""
	def get(self):
		num1 = self.request.get('num1')
		num2 = self.request.get('num2')

		num1 = int(num1)
		num2 = int(num2)

		sum_of_nums = num1 +num2

		template = jinja_environment.get_template('sum.html')
		self.response.write(template.render({

			'num1': num1,
			'num2': num2,
			'sum' : sum_of_nums

			}))
		# in URL: sum?num1=9&num2=4

class MoviesHandeler(webapp2.RequestHandler):
	"""docstring for MoviesHandeler"""
	def get(self):

		name = self.request.get('name')
		length = self.request.get('length')
		num_reviews = self.request.get('num_reviews')
		stars = self.request.get('stars')

		template = jinja_environment.get_template('movies.html')
		self.response.write(template.render({

			'name': name,
			'length': length,
			'num_reviews': num_reviews,
			'stars': stars
			}))

class MadlibsHandler(webapp2.RequestHandler):
	"""docstring for MadlibsHandler"""
	def get(self):

		template = jinja_environment.get_template('madlibs_input.html')
		self.response.write(template.render())
		
	def post(self):
		character_name = self.request.get('characterName')
		adjective = self.request.get('adj')

		character_name.upper()
		adjective.upper()
		template = jinja_environment.get_template('madlibs_output.html')
		self.response.write(template.render({
			'name': character_name,
			'adjective': adjective,
			}))

class MoreMadlibsHandler(webapp2.RequestHandler):
	"""docstring for Moremadlibs"""
	def get(self):

		template = jinja_environment.get_template('more_input.html')
		self.response.write(template.render())
	
	def post(self):

		timeofday = self.request.get('time_of_day')
		time_1 = self.request.get('time1')
		food = self.request.get('food')
		liquid = self.request.get('liquid')
		verb_1 = self.request.get('verb1')
		noun_1 = self.request.get('noun1')
		thingthatmoves = self.request.get('thing_that_moves')
		verb_2 = self.request.get('verb2')
		singular_noun =self.request.get('singularnoun')
		verb_3 = self.request.get('verb3')
		noun_2 = self.request.get('noun2')
		specificnoun = self.request.get('noun3')
		verb_4 = self.request.get('verb4')
		plural_noun = self.request.get('pluralnoun')
		adj = self.request.get('adj')
		verb_5 = self.request.get('verb5')
		noun_3 = self.request.get('noun3')
		noun_4 = self.request.get('noun4')
		verb_6 = self.request.get('verb6')
		time_2 = self.request.get('time2')



		template = jinja_environment.get_template('more_output.html')
		self.response.write(template.render({
			'time_of_day': timeofday,
			'time1': time_1,
			'foof': food,
			'liquid': liquid,
			'verb1': verb_1,
			'verb2': verb_2,
			'verb3': verb_3,
			'verb4': verb_4,
			'verb5': verb_5,
			'verb6': verb_6,
			'noun1': noun_1,
			'noun2': noun_2,
			'specificnoun': noun_3,
			'noun4': noun_4,
			'thing_that_moves':thingthatmoves,
			'singularnoun': singular_noun,
			'pluralnoun': plural_noun,
			'adj': adj,
			'time2': time_2
			}))

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/palindrome',PalindromeHandler),
	('/fortune',FortuneHandler),
	('/emails',EmailsHandeler),
	('/sum', SumHandler),
	('/movies', MoviesHandeler),
	('/madlibs', MadlibsHandler),
	('/moremadlibs',MoreMadlibsHandler)

], debug=True)
