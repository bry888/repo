import os
import webapp2
import jinja2
from google.appengine.ext import db

'''
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)
'''

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
		
form="""
<form method="post">
	<h1>Signup</h1>
	<label> Username
	<input type="text" name="username" value="%(username)s"><span style='color: red'> %(error1)s</span></label><br>
	<label> Password
	<input type="password" name="password" value="%(password)s"><span style='color: red'> %(error2)s</span></label><br>
	<label> Verify Password
	<input type="password" name="verify" value="%(verify)s"><span style='color: red'> %(error3)s</span></label><br>
	<label> Email (optional)
	<input type="text" name="email" value="%(email)s"><span style='color: red'> %(error4)s</span></label><br>
	<input type="submit">
</form>
"""

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	def render_str(self, template, **params):
		t = jinja_environment.get_template(template)
		return t.render(params)
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))
		
class Art(db.Model):
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

class MainPage(Handler):
	def render_front(self, title="", art="", error=""):
		arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
	
		self.render("abc.html", title=title, art=art, error=error, arts=arts)
	def get(self):
		self.render_front()
		#self.render("front.html")
	def post(self):
		title = self.request.get('title')
		art = self.request.get('art')
		
		if title and art:
			a = Art(title=title, art=art)
			a.put()
			
			self.redirect("/")
		else:
			error = "we need art and title"
			self.render_front(title, art, error)
			
class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get('username')
		self.response.out.write("Welcome, " + username + "!")
	
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)