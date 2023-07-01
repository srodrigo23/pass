"""
sumary_line
"""

from flask import Flask
from flask import render_template
from flask import request
from sha import encript_string

app = Flask(__name__)

@app.route('/')
def hello():
    """sumary_line"""
    return render_template(
        'index.html', 
        
    )

@app.route('/sha', methods=['GET', 'POST'])
def calculate_sha():
    """sumary_line"""
    form_value = request.form.get("formValue","")
    ans = encript_string(hash_string=form_value)

    if form_value != "":
        return render_template(
            'index.html', 
            sha_value=ans,
            form_value=form_value
        )
    else:
        return render_template(
            'index.html'
        )
    
# class Item:
#     def __init__(self) -> None:
#         self.href = "href"
#         self.caption  = "This is the caption"
        
if __name__ == '__main__':
   app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )