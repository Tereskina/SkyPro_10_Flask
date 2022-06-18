from flask import Flask
from utils import load_candidates, format_candidates, get_candidate_by_id, get_candidate_by_skill

app = Flask(__name__)


@app.route('/',)
def page_main():
    """Главная страница"""
    candidates = load_candidates('candidates.json')
    return format_candidates(candidates)


@app.route('/candidates/<int:uid>',)
def page_candidate(uid):
    """Поиск кандидата по id"""
    candidate = get_candidate_by_id(uid)
    page = f'<img src="{candidate.picture}">'
    page += format_candidates([candidate])
    return page


@app.route('/skills/<skill>',)
def page_skill(skill):
    """Поиск по навыку"""
    skill_lower = skill.lower()
    candidates = get_candidate_by_skill(skill_lower)
    page = format_candidates(candidates)
    return page


app.run()
