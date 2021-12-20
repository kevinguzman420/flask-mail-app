from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse

from app.common.mail import send_email

from app.common.token import generate_confirmation_token, confirm_token
from .models import UserMail
from .forms import SignupForm, LoginForm
from app.forms import RestorePassForm, RestorePassMailForm
from app import login_manager
from . import auth_bp
from .decorators import check_confirmed

import datetime

@auth_bp.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = UserMail.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.index')
            message = f'Welcome again {user.name}'
            flash(message)
            return redirect(next_page)
        else:
            message = "Your datas are incorrect."
        flash(message)
    return render_template("auth/login.html", form=form)

@auth_bp.route("/signup/", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = SignupForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = UserMail.get_by_email(email)
        if user is not None:
            message = f'The email {email} its in use for another user'
        else:
            user = UserMail(name=name, email=email)
            user.set_password(password)
            user.save()
        
            ##
            token = generate_confirmation_token(user.email)
            confirm_url = url_for('auth.confirm_email', token=token, _external=True)
            html = render_template('auth/activate.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            ##
            
            # Email configuration
            send_email(subject=subject,
                        sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
                        recipients=[email, ],
                        text_body=f'Hola {name}, you\'re welcome.',
                        html_body=html)

            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('auth.unconfirmed')
                message = f'User created! You\'re welcome to this page... check your email {email}'
                flash(message)
            return redirect(next_page)
        # try:
        #     pass
        # except:
            # message = "Has been an error in the database."
        flash(message)
    return render_template("auth/signup.html", form=form)

@auth_bp.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("public.index"))

@login_manager.user_loader
def load_user(user_id):
    return UserMail.get_by_id(int(user_id))

# INSERT INTO user_mail VALUES(1,'name','name@xyz.com','test','2020-02-02',0,null);
# UPDATE user_mail SET confirmed=0, confirmed_on=NULL WHERE id=;
# INSERT INTO user_mail VALUES(2,'name2','name2@xyz.com','test','2020-02-02',0,null);

# View to confirmation the email
@auth_bp.route("/confirm/<token>")
@login_required
def confirm_email(token):
    email = confirm_token(token)
    if email:
        user = UserMail.query.filter_by(email=email).first_or_404()
        if user.confirmed:
            if current_user.is_authenticated:
                flash('Account already confirmed and you logged.')
                return redirect(url_for('public.index'))
            flash('Account already confirmed. Please login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            user.confirmed = True
            user.confirmed_on = datetime.datetime.now()
            user.save()
            flash('You have confirmed your account. Thanks!', 'success')
            return redirect(url_for('public.index'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('auth.unconfirmed'))
        flash('The confirmation link is invalid or has expired. Please login.', 'danger')
        return redirect(url_for('auth.login'))

@auth_bp.route("/unconfirmed/")
@login_required
def unconfirmed():
    if current_user.confirmed:
        flash("Your email account has been confirmed.")
        return redirect(url_for('public.index'))
    flash("Please confirm your account")
    return render_template('auth/unconfirmed.html')


@auth_bp.route("/resend/")
@login_required
def resend_confirmation(urlfor, render_to, subject, txt_body, flash_message, redirect_page):
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for(urlfor, token=token, _external=True)
    html = render_template(render_to, confirm_url=confirm_url)
    subject = subject
    send_email(subject=subject,
            sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
            recipients=[current_user.email, ],
            text_body=txt_body,
            html_body=html)
    flash(flash_message)
    return redirect(url_for(redirect_page))


# Forget the password
# @auth_bp.route("/restore/<token>/")
@auth_bp.route("/account/", methods=["POST", "GET"])
def account():
    form = RestorePassForm()
    if form.validate_on_submit():
        user = UserMail.get_by_email(current_user.email)
        if user:
            user.set_password(form.confirm.data)
            user.save()
            flash("Your account password is restored.")
            return redirect(url_for('public.index'))
        else:
            flash("Has ocurred an error, please trying again.")
    return render_template("auth/restore_password_form.html", form=form)
            


@auth_bp.route("/confirm_restore_password/<token>/")
def confirm_restore_password(token):
    email = confirm_token(token)
    if email:
        try:
            user = UserMail.query.filter_by(email=email).first_or_404()
            flash("Restore your password:")
        except:
            flash("HAS OCURRED AN ERROR, PLEASE TRYING AGAIN.")
            return redirect(url_for("auth.login"))
        current_app.config['USERMAIL'] = user.email
        return redirect(url_for('user.restore_password'))
    else:
        flash('The confirmation link is invalid or has expired. Please login.', 'danger')
        return redirect(url_for("auth.login"))



@auth_bp.route("/unconfirmed/")
@login_required
def unconfirmed_restart_password():
    if current_user.confirmed:
        flash("Your email account has been confirmed.")
        return redirect(url_for('public.index'))
    flash("Please confirm your account")
    return render_template('auth/unconfirmed.html')