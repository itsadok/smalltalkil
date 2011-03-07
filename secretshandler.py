from google.appengine.ext import db

class Secret(db.Model):
    secret = db.StringProperty()
    name = db.StringProperty()

def getSecret(name):
    a = db.GqlQuery("SELECT * FROM Secret WHERE name='%s'"%name).get()
    if a:
        return a.secret.encode("ascii")


def setSecret(name,secret):
    a = Secret()
    a.name = name
    a.secret = secret
    a.put()


def changeSecret(name, secret):
    a = getSecret(name)
    if a:
        a.secret = secret
        a.put()
