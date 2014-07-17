import flask, flask.views
import os
import utils

class Books(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('books.html')
        
    @utils.login_required
    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return flask.redirect(flask.url_for('login'))