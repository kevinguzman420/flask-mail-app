from flask import (render_template, redirect, url_for, current_app, flash, 
                    jsonify, request)
from flask_login import current_user
from flask_cors import cross_origin #
from werkzeug.utils import secure_filename
from pathlib import Path
from datetime import datetime
import os, json

from app.common.mail import send_email
from app.auth.models import UserMail
from . import admin_bp
from .forms import MarketingMailForm

@admin_bp.route("/admin/userss/", methods=["POST", "GET"])
def user_lists():
    return jsonify(
        username="current_user.name",
        email="current_user.email",
        id="current_user.id"
    )

@admin_bp.route("/admin/users/", methods=["POST", "GET"])
# @cross_origin()
def user_list(data=None):
    # if request.method == "POST":
    #     return request.get_json()

    # return current_app.config['MAIL_TEMPLATES_DIR']
    users = UserMail.get_all()
    form = MarketingMailForm()
    if form.validate_on_submit():
        message = form.message.data
        template_name = secure_filename(form.template_name.data+str(datetime.now().strftime("%x")))
        template_mail_dir = current_app.config['MAIL_TEMPLATES_DIR']
        os.makedirs(template_mail_dir, exist_ok=True)

        file_exist = os.path.isfile(current_app.config['MAIL_TEMPLATES_DIR']+'/'+template_name+'.html')
        if not file_exist:
            # Armamos el correo de recuperación de contraseña de usuario
            page_url = url_for('public.index', _external=True)

            file = open(current_app.config['MAIL_TEMPLATES_DIR'] + "/"+template_name+".html", "w")
            template_message = "<p>{0}</p> <br>".format(message) + "<a href='http://127.0.0.1:5000'>Visitamos</a>"
            file.write(template_message)
            file.close()

            html = render_template('mail_templates/'+template_name+'.html', confirm_url=page_url)
            subject = "You are welcome to this page."

            # Email configuration
            send_email(subject=subject,
                        sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
                        recipients=[user.email for user in users ],
                        text_body=f'Hola {current_user.name}, Bendiciones!.',
                        html_body=html)
            flash("The emails are have been successfully")
        else:
            flash("Already exist a file with a same name... please try another name.")
        return redirect(url_for("admin.user_list"))
    return render_template("admin/user_list.html", users=users, form=form)

@admin_bp.route("/admin/createmarketingemail/")
def create_marketing_email():
    pass
