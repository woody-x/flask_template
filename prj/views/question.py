from flask import Blueprint, render_template, request, url_for
from prj.models import Question
from prj.forms import QuestionForm
from werkzeug.utils import redirect
from prj import db
from datetime import datetime

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/')
def question_list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question_detail.html', question=question)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('question_form.html', form=form)
