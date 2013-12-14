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

def blog_key(name = 'default'):
	return db.Key.from_path('blogs', name)
		
class Comment(db.Model):
	subject = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	last_modified = db.DateTimeProperty(auto_now = True)

class MainPage(Handler):
	def render_front(self):
		comments = db.GqlQuery("SELECT * FROM Comment ORDER BY created DESC limit 10")
		self.render("blog.html", comments=comments)
	def get(self):
		self.render_front()
		
class PostPage(Handler):
	def get(self, post_id):
		key = db.Key.from_path('Post', int(post_id), parent=blog_key())
		post = db.get(key)
		
		if not post:
			self.error(404)
			return
		
		self.render("permalink.html", post=post)
			
class PostHandler(Handler):
	def render_front(self, subject="", blog="", error=""):
		self.render("post.html", subject=subject, blog=blog, error=error)
	def get(self):
		self.render_front()
	def post(self):
		subject = self.request.get('subject')
		blog = self.request.get('blog')
		
		if (subject and blog):
			a = Comment(parent = blog_key(), subject=subject, blog=blog)
			a.put()
			
			self.redirect("/%s" % str(a.key().id()))
		
		else:
			error = "subject and content, please!"
			self.render_front(subject, blog, error)
			
app = webapp2.WSGIApplication([('/', MainPage), ('/newpost', PostHandler), ('/([0-9]+)', PostPage)], debug=True)