import webapp2
from google.appengine.ext import db

def escape_html(s):
    for (i,o) in (('>', '&gt;'), ('<', '&lt;'), ('"', '&quot;'), ('&', '&amp;')):
		s = s.replace(i,o)
    return s

form="""
<form method="post" style="background-color:pink"> 
	<br>
	<h1 style="text-align:center">Dowiedz sie kim jestes!</h1>
	<h2 style="text-align:center">Wypelnij ankiete</h2>
	<br>
	<div style="margin-left:360px">
	<h4>Jaki kolor lubisz najbardziej?</h4>
	<select name='kolor' value="%(kolor)s">
		<option></option>
		<option>rozowy</option>
		<option>zolty</option>
		<option>blekitny</option>
		<option>zloty</option>
	</select>
	<h4>Co najbardziej lubisz robic?</h4>
	<select name='robic' value="%(robic)s">
		<option></option>
		<option>stroic sie</option>
		<option>robic zakupy</option>
		<option>spiewac w lesie</option>
		<option>tulic zwierzatka</option>
	</select>
	<h4>Jakie jest twoje marzenie?</h4>
	<select name='marzenie' value="%(marzenie)s">
		<option></option>
		<option>byc piekna</option>
		<option>ksiaze</option>
		<option>wladac swiatem</option>
		<option>miec palac</option>
	</select>
	<br>
	<br>
	<input type="submit">
	<br>
	<div style='color: red'><b>%(error)s</b></div>
	</div>
	<br><br><br><br><br><br><br>
</form>
"""

form2="""
<form style="background-color:pink">
	<br>
	<h1 style="text-align:center">Jestes ksiezniczka!</h1>
	<img src="http://files.students.ch/uploads/b/2009/03/26/z1802811x.jpg"/ style="margin-left:35%">
	<br><br><br><br>
	<div style="text-align: center; font-size: 20px">
	<a href="http://strona-brydzi.appspot.com/addcom" style="margin-right:30px; background-color:white; padding: 10px; color: #CC0033"><b>Dodaj Komentarz</b></a>
	<a href="http://strona-brydzi.appspot.com/comments" style="margin-left:30px; background-color:white; padding: 10px; color: #CC0033">Komentarze</a>
	</div>
	<br><br>
</form>
"""

form3="""
<form method="post" style="background-color:pink">
	<br>
	<h1>Dodaj komentarz</h1>
	<br>
	<label> Nick
	<input type="text" name="nick" value="%(nick)s"><span style='color: red'> %(error1)s</span></label><br>
	<br>
	<textarea name="comment"></textarea>
	<br>
	<input type="submit">
	<br>
	<div style='color: red'><b>%(error2)s</b></div>
	<br><br><br><br><br><br>
</form>
"""

form4="""
<form style="background-color:pink">
	<br>
	<h1 style="margin-left: 30px">Komentarze</h1>
	<br>
	<div>%(comments)s</div>
	<br><br><br><br><br><br>
</form>
"""

class Komentarz(db.Model):
	nick = db.StringProperty(required=True)
	comment = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", kolor="", robic="", marzenie=""):
		self.response.out.write(form % {"error": error, "kolor": escape_html(kolor), "robic": escape_html(robic), "marzenie": escape_html(marzenie)})
	def get(self):
		self.write_form()
	def post(self):
		user_kolor = self.request.get('kolor')
		user_robic = self.request.get('robic')
		user_marzenie = self.request.get('marzenie')
		
		if not (user_kolor and user_robic and user_marzenie):
			self.write_form("wypelnij porzadnie!", user_kolor, user_robic, user_marzenie)
		else:
			self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(form2)

class AddComHandler(webapp2.RequestHandler):
	def write_form(self, error2="", nick="", comment=""):
		self.response.out.write(form3 % {"error2": error2, "nick": escape_html(nick), "comment": escape_html(comment)})
	def get(self):
		self.write_form()
	def post(self):
		nick = self.request.get('nick')
		comment = self.request.get('comment')
		
		if nick and comment:
			com = Komentarz(nick=nick, comment=comment)
			com.put()
			self.redirect("/comments")
		else:
			self.write_form("Wypelnij pola!", nick, comment)
		
class CommentsHandler(webapp2.RequestHandler):
	def get(self):
		comments = db.GqlQuery("SELECT * FROM Komentarz ORDER BY created DESC")
		self.response.out.write(form4 % {'comments': comments})
		
	
		
app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler), ('/addcom', AddComHandler), ('/comments', CommentsHandler)], debug=True)