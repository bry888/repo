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


months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

# valid_month("january") => "January"    
# valid_month("foo") => None

mon = []
for m in months:
   mon.append(m[:3].lower())
    
def valid_month(month):
    mm = month[:3].lower()
    if mm in mon:
        return str(month[0].upper())+str(month[1:].lower())
    else:
        return None

#print valid_month('JaNuary')


def valid_day(day):
    if day.isdigit()==True and 1<=int(day)<=31:
        return int(day)
    else:
        return None
    
#print valid_day('31')


def valid_year(year):
    if year.isdigit()==True and 1900<=int(year)<=2020:
        return int(year)
    else:
        return None

#print valid_year('2000')

def escape_html(s):
    for (i,o) in (('>', '&gt;'), ('<', '&lt;'), ('"', '&quot;'), ('&', '&amp;')):
		s = s.replace(i,o)
    return s


form="""
<form method="post">
	What is your birthday?
	<br>
	<label>Month
	<input type="text" name="month" value="%(month)s"></label>
	<label> Day
	<input type="text" name="day" value="%(day)s"></label>
	<label> Year
	<input type="text" name="year" value="%(year)s"></label>
	<div style='color: red'>%(error)s</div>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error, "month": escape_html(month), "year": escape_html(year), "day": escape_html(day)})
	def get(self):
		#self.response.out.write(form)
		self.write_form()
	def post(self):
		#user_month = valid_month(self.request.get('month'))
		#user_day = valid_day(self.request.get('day'))
		#user_year = valid_year(self.request.get('year'))
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')
		
		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)
		
		#if not (user_month and user_day and user_year):
		if not (month and day and year):
			#self.response.out.write(form)
			self.write_form("Not valid", user_month, user_day, user_year)
		else:
			self.redirect("/thanks")
	
class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Date is OK")
	
app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)], debug=True)