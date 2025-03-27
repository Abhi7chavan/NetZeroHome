from models.role import role

class Roleservice:
    def get_role(self,db):
        roles = db.query(role).all()
        return [role.as_dict() for role in roles]