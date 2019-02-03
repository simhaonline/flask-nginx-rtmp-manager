from .shared import db

class Stream(db.Model):
    __tablename__ = "Stream"
    id = db.Column(db.Integer, primary_key=True)
    linkedChannel = db.Column(db.Integer,db.ForeignKey('Channel.id'))
    streamKey = db.Column(db.String(255))
    streamName = db.Column(db.String(255))
    topic = db.Column(db.Integer)
    currentViewers = db.Column(db.Integer)
    totalViewers = db.Column(db.Integer)
    channelMuted = db.Column(db.Boolean)
    upvotes = db.relationship('streamUpvotes', backref='stream', lazy="joined")

    def __init__(self, streamKey, streamName, linkedChannel, topic):
        self.streamKey = streamKey
        self.streamName = streamName
        self.linkedChannel = linkedChannel
        self.currentViewers = 0
        self.totalViewers = 0
        self.topic = topic
        self.channelMuted = False

    def __repr__(self):
        return '<id %r>' % self.id

    def get_upvotes(self):
        return len(self.upvotes)

    def add_viewer(self):
        self.currentViewers = self.currentViewers + 1
        db.session.commit()

    def remove_viewer(self):
        self.currentViewers = self.currentViewers - 1
        db.session.commit()

    def serialize(self):
        if self.channel.record == True:
            return {
                'id': self.id,
                'channelID': self.linkedChannel,
                'channelEndpointID': self.channel.channelLoc,
                'owningUser': self.channel.owningUser,
                'streamPage': '/view/' + self.channel.channelLoc + '/',
                'streamURL': '/live-rec/' + self.channel.channelLoc + '/index.m3u8',
                'streamName': self.streamName,
                'topic': self.topic,
                'currentViewers': self.currentViewers,
                'totalViewers': self.currentViewers,
                'upvotes': self.get_upvotes()
            }
        else:
            return {
                'id': self.id,
                'channelID': self.linkedChannel,
                'channelEndpointID': self.channel.channelLoc,
                'owningUser': self.channel.owningUser,
                'streamPage': '/view/' + self.channel.channelLoc +'/',
                'streamURL': '/live/' + self.channel.channelLoc + '/index.m3u8',
                'streamName': self.streamName,
                'topic': self.topic,
                'currentViewers': self.currentViewers,
                'totalViewers': self.currentViewers,
                'upvotes': self.get_upvotes()
            }