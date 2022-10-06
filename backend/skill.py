from flask import jsonify


def create(app, db):
    class Skill(db.Model):
        __tablename__ = 'Skill'

        Skill_ID = db.Column(db.Integer, primary_key=True)
        Skill_Name = db.Column(db.String(50))

        def __init__(self, Skill_ID, Skill_Name):
            self.Skill_ID = Skill_ID
            self.Skill_Name = Skill_Name

        def json(self):
            return {"Skill_Name": self.Skill_Name, "Skill_ID": self.Skill_ID}




        @app.route("/skills")
        def skill_get_all():
            skill_list = Skill.query.all()
            if skill_list:
                return jsonify(
                    {
                        "code": 200,
                        "data": {
                            "skills": [skill.json()['Skill_Name'] for skill in skill_list]
                        }
                    }
                )
            return jsonify(
                {
                    "code": 404,
                    "message": "There are no Courses."
                }
            ), 404