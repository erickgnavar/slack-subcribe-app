# coding: utf-8
import os
import requests
from flask import Flask
from flask import request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/thanks/')
def thanks():
    message = u'Ya estas registrado, te llegará un correo con la invitación'
    return render_template('home.html', message=message)


@app.route('/request-invitation/', methods=['post'])
def request_invitation():
    url = 'https://{teamdomain}.slack.com/api/users.admin.invite'.format(
        teamdomain=os.environ.get('TEAM_DOMAIN', ''))
    params = {
        'email': request.form.get('email'),
        'token': os.environ.get('TOKEN', '')
    }
    requests.post(url, params=params)
    return redirect('/thanks/')

if __name__ == '__main__':
    app.run()
