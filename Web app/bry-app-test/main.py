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
	
	def set_secure_cookie(self, name, val):
		cookie_val = make_secure_val(val)
		self.response.headers.add_header(
			'Set-Cookie',
			'%s=%s; Path=/' % (name, cookie_val))
			
	def read_secure_cookie(self, name):
		cookie_val = self.request.cookies.get(name)
		return cookie_val and check_secure_val(cookie_val)
		
	def login(self, user):
		self.set_secure_cookie('user_id', str(user.key().id()))
		
	def logout(self):
		self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
		
	def initialize(self, *a, **kw):
		webapp2.RequestHandler.initialize(self, *a, **kw)
		uid = self.read_secure_cookie('user_id')
		self.user = uid and User.by_id(int(uid))
	
#############################################		
import hashlib

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

def make_pw_hash(name, pw, salt=None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (salt, h)
	
def valid_pw(name, pw, h):
	salt = h.split(',')[0]
	return h == make_pw_hash(name, pw, salt)

# # # # #
def valid_username(username):
	if " " in str(username):
		return None
	else:
		return username

def valid_email(email):
	l = []
	e = str(email)
	for i in e:
		l.append(i)
	if ('@' in l and '.' in l and l.index('@') < l.index('.') and l.index('@') != 0 and l.index('.') != len(email)-1 and len(l)>4) or email == "":
		return True
	else:
		return False
# # # # #

class User(db.Model):
	name = db.StringProperty(required=True)
	pw_hash = db.StringProperty(required=True)
	email = db.StringProperty()
	
	@classmethod
	def by_id(cls, uid):
		return User.get_by_id(uid, parent = users_key()
	def by_name(cls, name):
		u = User.all().filter('name=', name).get()
		return u
	def register(cls, name, pw, email=None):
		pw_hash = make_pw_hash(name, pw)
		return User(parent = users_key(),
					name = name,
					pw_hash = pw_hash,
					email = email)
	def login(cls, name, pw):
		u = cls.by_name(name)
		if u and valid_pw(name, pw, u.pw_hash):
			return u
		

	
class Signup(Handler):
	def write_form('hash.html', error1="", error2="", error3="", error4="", username="", password="", verify="", email=""):
		self.response.out.write(form % {"error1": error1, "error2": error2, "error3": error3, "error4": error4, "username": escape_html(username), "password": escape_html(password), "verify": escape_html(verify), "email": escape_html(email)})
	def get(self):
		self.write_form()
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')
		
		username = valid_username(user_username)
		ok_email = valid_email(user_email)
		
		error1 = ""
		error2 = ""
		error3 = ""
		error4 = ""
		if not (username):
			error1 = "That's not a valid username."
		if not (user_password):
			error2 = "That wasn't a valid password."
			#self.write_form("That's not a valid username.", "That wasn't a valid password.", "", "", user_username, user_password, user_verify, user_email)
		if user_password != user_verify:
			error3 = "Your passwords didn't match."
			#self.write_form("", "", "Your passwords didn't match.", "", user_username, "", "", user_email)
		if ok_email == False:
			error4 = "That's not a valid email."
			#self.write_form("", "", "", "That's not a valid email.", user_username, user_password, user_verify, user_email)
		
		if (username and user_password and user_verify and user_password==user_verify):
			self.redirect("/welcome?username=" + self.username)			
		else:
			self.write_form(error1, error2, error3, error4, user_username, "", "", user_email)

			
class Register(Signup):
	def done(self):
		u = User.by_name(self.username)
		if u:
			msg = 'That user already exists'
			self.render('hash.html', error_username = msg)
		else:
			u = User.register(self.username, self.password, self.email)
			u.put()
			
			self.login(u)
			self.redirect('/welcome')
			
class Login(Handler):
	def get(self):
		self.render('login.html')
	def post(self):
		username = self.request.get('username')
		password = self.request.get('password')
		
		u = User.login(username, password)
		if u:
			self.login(u)
			self.redirect('/welcome')
		else:
			msg = 'Invalid login'
			self.render('login.html', error = msg)
			
	self.response.headers['Content-Type'] = 'text/plain'
			user = str(username)
			password = str(user_password)
			user_cookie_str = self.request.cookies.get('user')
			password_cookie_str = self.request.cookies.get('password')
			if user_cookie_str and password_cookie_str:
				cookie_val = check_secure(password_cookie_str)
				if cookie_val:
					user = user_cookie_str
		
			new_cookie_val = make_secure(str(password))
		
			self.response.headers.add_header('Set-Cookie', 'password=%s' % password)
	
			if new_cookie_val:
				self.redirect("/welcome")
			else:
				self.redirect('/')		
			

class Welcome(Handler):
	def get(self):
		username = self.request.get('username')
		if valid_username(username):
			self.render('welcome.html', username = username)
		else:
			self.redirect('/signup')
		
	
app = webapp2.WSGIApplication([('/', Signup),
							   ('/welcome', Welcome),
							   ('/signup', Register),
							   ('/login', Login),
							   ('/logout', Logout)
							   ], debug=True)