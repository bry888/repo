import os
import webapp2
import jinja2
from google.appengine.ext import db


jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
		

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	def render_str(self, template, **params):
		t = jinja_environment.get_template(template)
		return t.render(params)
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))
		
		
import hashlib
#############################################
def hash_it(s):
	return hashlib.md5(s).hexdigest()
	
def make_secure(s):
	return "%s| %s" % (s, hash_it(s))
	
def check_secure(h):
	val = h.split('|')[0]
	if h == make_secure(val):
		return val
##############################################

import string
import random

def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw):
	salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h, salt)
	
def valid_pw(name, pw, h):
	pass
	
class MainPage(Handler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		visits = 0
		visit_cookie_str = self.request.get('visits')
		if visit_cookie_val:
			cookie_val = check_secure(visit_cookie_str)
			if cookie_val:
				visits = int(cookie_val)
		
	visits += 1
	
	new_cookie_val = make_secure(str(visits))
		
	self.response.headers.add_header('Set-Cookie', 'visits=%s' % visits)
	
	if visits > 10000:
		self.write("you are the best!")
	else:
		self.write('you`ve been here %s times!' % visits)
		
webapp2.WSGIApplication([('/', MainPage)], debug=True)