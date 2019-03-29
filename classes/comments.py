from .shared import db
from datetime import datetime

class videoComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer,db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime)
    comment = db.Column(db.String(2048))
    videoID = db.Column(db.Integer,db.ForeignKey('RecordedVideo.id'))

    def __init__(self, userID, comment, videoID):
        self.userID = userID
        self.timestamp = datetime.now()
        self.comment = comment
        self.videoID = videoID

    def __repr__(self):
        return '<id %r>' % self.id