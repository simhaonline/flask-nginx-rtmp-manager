from flask_security.forms import RegisterForm, StringField, Required,ConfirmRegisterForm,ForgotPasswordForm, LoginForm
from flask_security import UserMixin, RoleMixin
from .shared import db

class ExtendedRegisterForm(RegisterForm):
    username = StringField('username', [Required()])
    email = StringField('email', [Required()])

    def validate(self):
        success = True
        if not super(ExtendedRegisterForm, self).validate():
            success = False
        if db.session.query(User).filter(User.username == self.username.data.strip()).first():
            self.username.errors.append("Nom d'utilisateur déà utilisé")
            success = False
        if db.session.query(User).filter(User.email == self.email.data.strip()).first():
            self.email.errors.append("Adresse E-mail déjà utilisée")
            success = False
        return success

class ExtendedConfirmRegisterForm(ConfirmRegisterForm):
    username = StringField('username', [Required()])

class OSPLoginForm(LoginForm):
    def validate(self):
        response = super(OSPLoginForm, self).validate()

        return response

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    fs_uniquifier = db.Column(db.String(255))
    password = db.Column(db.String(255))
    biography = db.Column(db.String(2048))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    pictureLocation = db.Column(db.String(255))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    invites = db.relationship('invitedViewer', backref='user', lazy="joined")
    channels = db.relationship('Channel', backref='owner', lazy="joined")
    notifications = db.relationship('userNotification', backref='user', lazy="joined")
    subscriptions = db.relationship('channelSubs', backref='user', cascade="all, delete-orphan", lazy="joined")