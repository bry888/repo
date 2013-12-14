import webapp2



def escape_html(s):
    for (i,o) in (('>', '&gt;'), ('<', '&lt;'), ('"', '&quot;'), ('&', '&amp;')):
		s = s.replace(i,o)
    return s

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


class MainPage(webapp2.RequestHandler):
	def write_form(self, error1="", error2="", error3="", error4="", username="", password="", verify="", email=""):
		self.response.out.write(form % {"error1": error1, "error2": error2, "error3": error3, "error4": error4, "username": escape_html(username), "password": escape_html(password), "verify": escape_html(verify), "email": escape_html(email)})
	def get(self):
		#self.response.out.write(form)
		#self.render("signup.html")!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
			self.redirect("/thanks?username=" + username)
		else:
			self.write_form(error1, error2, error3, error4, user_username, "", "", user_email)

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get('username')
		self.response.out.write("Welcome, " + username + "!")
	
app = webapp2.WSGIApplication([('/', MainPage), ('/thanks', ThanksHandler)], debug=True)