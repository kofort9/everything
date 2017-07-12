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
import jinja2
import os
import webapp2
 
from google.appengine.ext import ndb


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.dirname(__file__)))

class Student(ndb.Model):
	name = ndb.StringProperty()
	grade = ndb.IntegerProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('student_input.html')
        self.response.write(template.render())
 
    def post(self):
		name_from_from = self.request.get('studentName')
		grade_from_from = self.request.get('studentGrade')
		grade_from_from = int(grade_from_from)


 		student_model = Student(name=name_from_from, grade=grade_from_from)
 		#saves to data base [.put()]
		student_key = student_model.put()

		template = jinja_environment.get_template('student_added.html')
		self.response.write(template.render(
            {
              'name': name_from_from,
              'student_id': student_key.id(),
            }
            ))
 
class ListHandler(webapp2.RequestHandler):
    def get(self):

    						#order of their grade desending 
		#students_query = Student.query().order(-Student.name)
		students_query = Student.query(Student.grade >70) #only students for grade higher then 70
		#many combos
		students_query = Student.query().order(-Student.name)
		#adding limit.. will only show two  .fetch(limit=2)
		list_of_students = students_query.fetch()
			

		template = jinja_environment.get_template('list.html')
		self.response.write(template.render(
        	{
        	'students': list_of_students,
        	}))

class OneStudentHandler(webapp2.RequestHandler):
	"""docstring for OneStudentHandler"""
	def get(self):
		student_id = self.request.get('id')
		student_id = int(student_id)
		student_model = Student.get_by_id(student_id)

		template =jinja_environment.get_template('onestudent.html')
		self.response.write(template.render(
			{
			'student': student_model,
			}))
		
 
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/list', ListHandler),
    ('/onestudent', OneStudentHandler)
], debug=True)