import webapp2

def buildCoder(shift):
	#stri = "abcdefghijklmnopqrstuwxyz"
    dict = {}
    for i in range(len("abcdefghijklmnopqrstuvwxyz")):
        dict["abcdefghijklmnopqrstuvwxyz".lower()[i]] = (2*"abcdefghijklmnopqrstuvwxyz".lower())[i+shift]
    for b in range(len("abcdefghijklmnopqrstuvwxyz")):
        dict["abcdefghijklmnopqrstuvwxyz".upper()[b]] = (2*"abcdefghijklmnopqrstuvwxyz".upper())[b+shift]
    return dict
    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    u = []
    for i in text: 
        try: u.append(coder[i]) 
        except: u.append(i)
        odp = ''.join(u)
    return odp
    

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    for a in text:
        z = applyCoder(text, buildCoder(shift))
    return z

def escape_html(s):
    for (i,o) in (('>', '&gt;'), ('<', '&lt;'), ('"', '&quot;'), ('&', '&amp;')):
		s = s.replace(i,o)
    return s



form="""
<form method="post">
	<h1>Enter some text to ROT13:</h1>
	<br>
	<input type="text" name="tekst" value="%(tekst)s">
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, tekst=""):
		self.response.out.write(form % {"tekst": escape_html(tekst)})
	def get(self):
		#self.response.out.write(form)
		self.write_form()
	def post(self):
		user_tekst = self.request.get('tekst')
		tekst = user_tekst
		
		if not (tekst):
			#self.response.out.write(form)
			self.write_form(user_tekst)
		else:
			self.write_form(applyShift(tekst, 13))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)