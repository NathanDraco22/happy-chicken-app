from ..models.user import UserModel


class UserFactory:

    @staticmethod
    def toDict(user: UserModel) -> dict[str,str]:
        return vars(user)
    
    @staticmethod
    def fromDict(json: dict[str, str]) -> UserModel:
        user = UserModel()
        for k,v in json.items():
            setattr(user, k, v)
        return user