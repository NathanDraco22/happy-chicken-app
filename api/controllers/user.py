from fastapi.responses import JSONResponse

from api.services.db_services.db_protocol import DBServicesProtocol
from api.services.db_services.tinydb_services import TinyDBServices

from api.entities.models.user import UserModel
from api.entities.factories.user_factory import UserFactory

class UserController:

    db_serivices: DBServicesProtocol = TinyDBServices()  

    def sign_up(self, user: UserModel):
        result = self.db_serivices.search_by_phone(user.phone)
        if len(result) != 0:
            return JSONResponse(
                content = {"msg" : "User already exists", "result" : result},
                status_code = 400
            )
        user_dict = UserFactory.toDict(user)
        self.db_serivices.create(user_dict)
        return JSONResponse(
                content = {"msg" : "User Created"},
                status_code = 200
        )
    
    
    def get_all_user(self):
        return self.db_serivices.read()

