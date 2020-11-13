from flask import render_template, redirect, url_for, request, flash, current_app

from app.forms import RestorePassForm, RestorePassMailForm
from app.common.mail import send_email
from app.common.token import generate_confirmation_token, confirm_token
from app.auth.models import UserMail
from . import user_bp

@user_bp.route("/restore/", methods=["POST", "GET"])
def restore():
    form = RestorePassMailForm()
    if form.validate_on_submit():
        user = UserMail.get_by_email(form.email.data)
        if user:
            # Armamos el correo de recuperación de contraseña de usuario
            token = generate_confirmation_token(user.email)
            confirm_url = url_for('auth.confirm_restore_password', token=token, _external=True)
            html = render_template('user/restore_password_mail.html', confirm_url=confirm_url)
            subject = "Petition to restore your password."

            # Email configuration
            send_email(subject=subject,
                        sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
                        recipients=[user.email, ],
                        text_body=f'Hola {user.name}, you\'re ready to restore your password?.',
                        html_body=html)
            message = "An mail has been send to your email, to restore your password. Check it."
        else:
            message = "The mail you gived, isn't registered..."
        flash(message)
        return redirect(url_for('auth.login'))
    return render_template("user/restore_pass_form_mail.html", form=form)


@user_bp.route("/restore_password/", methods=["POST", "GET"])
def restore_password(): # 
    form = RestorePassForm()
    context = {
        "form": form
    }
    if form.validate_on_submit():
        user = UserMail.get_by_email(current_app.config['USERMAIL'])
        user.set_password(form.confirm.data)
        user.save()
        flash("Your account password is restored.")
        return redirect(url_for('auth.login'))
    return render_template("user/restore_password_form.html", **context)