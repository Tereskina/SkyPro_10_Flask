import json


class Candidate:

    def __init__(self, id, name, picture, position, gender, age, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills


def load_candidates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        raw_str = json.load(f)

    candidates_ = []

    for candidate in raw_str:
        temp = Candidate(
            candidate['id'],
            candidate['name'],
            candidate['picture'],
            candidate['position'],
            candidate['gender'],
            candidate['age'],
            candidate['skills'])

        candidates_.append(temp)

    return candidates_


def format_candidates(candidates):
    """Форматирование списка кандидатов"""
    # candidates = load_candidates('candidates.json')
    page = ""
    for candidate in candidates:
        page += "Имя кандидата: " + candidate.name + '\n'
        page += "Позиция кандидата: " + candidate.position + '\n'
        page += "Навыки: " + candidate.skills + '\n''\n'
    return "<pre>" + page + "</pre>"


def get_candidate_by_id(uid: int):
    candidates = load_candidates('candidates.json')
    for candidate in candidates:
        if candidate.id == uid:
            return candidate
    return None


def get_candidate_by_skill(skill):
    candidates = load_candidates('candidates.json')
    page = []
    for candidate in candidates:
        if skill in candidate.skills.lower().split(', '):
            page.append(candidate)
    return page
