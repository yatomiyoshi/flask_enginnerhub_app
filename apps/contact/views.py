from email_validator import EmailNotValidError, validate_email
from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import login_required

contact = Blueprint(
    'contact', __name__, template_folder='templates', static_folder='static'
)



@contact.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        user_name = request.form['user_name']
        email = request.form['email']
        message = request.form['message']
        
        is_valid = True
        if not user_name:
            flash('ユーザー名を入力してください。')
            is_valid = False

        if not email:
            flash('メールアドレスを入力してください。')
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash('メールアドレスが不正です。')
            is_valid = False
        
        if not message:
            flash('メッセージを入力してください。')
            is_valid = False
        
        if not is_valid:
            return redirect(url_for('contact.index'))
        
        print(user_name, email, message)
        
        return redirect(url_for('contact.complete'))
    return render_template('contact/index.html')

@contact.route('/complete')
@login_required
def complete():
    return render_template('contact/complete.html')