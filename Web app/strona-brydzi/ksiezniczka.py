import webapp2

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
	<br><br><br><br><br><br>
</form>
"""

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
	
app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)], debug=True)