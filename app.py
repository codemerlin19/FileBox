#winter training project
from flask import Flask, render_template
from flask_admin import Admin, BaseView, expose
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
path = op.join(op.dirname(__file__),'static')

app = Flask(__name__)
admin = Admin(app, template_mode='bootstrap3')
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "asdasuhdasdasd"
class PageView(BaseView):
	def is_accessible (self):
		return True
	@expose('/')
	def index(self):
		return self.render('admin/index.html')





@app.route("/")
def main():
	return render_template('index.html')

admin.add_view(FileAdmin(path+'/images/')) 

if __name__ == '__main__':
	app.run()
