import db
		
class User():
	def __init__(self, user_id):
		user = db.getConfigAcc(user_id)
		self.id = user['id']
		self.key = user['key']
		self.secret = user['secret']
		self.credits = user['credits']
