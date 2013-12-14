import webapp2
import jinja2
import os
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

		
class Komentarz(db.Model):
	nick = db.StringProperty(required=True)
	comment = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

class MainPage(Handler):
	def render_front(self, error="", kolor="", robic="", marzenie=""):
		self.render("1.html", error=error, kolor=kolor, robic=robic, marzenie=marzenie)
	def get(self):
		self.render_front()
	def post(self):
		kolor = self.request.get('kolor')
		robic = self.request.get('robic')
		marzenie = self.request.get('marzenie')
		
		if not (kolor and robic and marzenie):
			error = "Wypelnij porzadnie!"
			self.render_front(error, kolor, robic, marzenie)
	
		else:
			error = ""
			self.redirect("/thanks")
	
class ThanksHandler(Handler):
	def get(self):
		self.render("2.html")
		
class AddComHandler(Handler):
	def render_front(self, nick="", comment="", error=""):
		self.render("3.html", nick=nick, comment=comment, error=error)
	def get(self):
		self.render_front()
	def post(self):
		nick = self.request.get('nick')
		comment = self.request.get('comment')
	
		#a = db.GqlQuery("select * FROM Komentarz where nick='mniam'")
		#b = a[0]
		#b.delete()
		
		if (nick and comment):
			com = Komentarz(nick=nick, comment=comment)
			com.put()
			self.redirect("/comments")
			
		else:
			error = "Wpisz Nick i Komentarz"
			self.render_front(nick, comment, error)
	
class CommentsHandler(Handler):
	def get(self):
		comments = db.GqlQuery("SELECT * FROM Komentarz ORDER BY created DESC")
		self.render('4.html', comments=comments)
				
			
app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler), ('/addcom', AddComHandler), ('/comments', CommentsHandler)], debug=True)