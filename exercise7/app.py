from myproject import app
from flask import render_template
import os
@app.route('/')
def index():
  return render_template('index.htm')

if __name__=='__main__':
  os.system('flask db migrate')
  os.system('flask db upgrade')
  app.run(debug=True)