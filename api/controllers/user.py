from api.services.db_services.db_protocol import DBServicesProtocol
from api.services.db_services.tinydb_services import TinyDBServices

from api.entities.models.user import UserModel
from api.entities.dtos.signin import SigninDTO
from api.entities.factories.user_factory import UserFactory
from api.tools.responses.user_response import UserResponse
from api.tools.crypt.password_tool import PasswordCrypter
from api.tools.jwt.jwt_tools import JWT

class UserController:

    db_serivices: DBServicesProtocol = TinyDBServices()  

    def sign_up(self, user: UserModel) -> tuple[UserResponse, int]:
        result = self.db_serivices.search_by_phone(user.phone)
        if len(result) != 0:
            return (UserResponse(msg= "User already exist"), 400)
        user.password = PasswordCrypter.encrypt(user.password)
        user_dict = UserFactory.toDict(user)
        user_id = self.db_serivices.create(user_dict)
        token = JWT.encode({"name" : user.name})
        return (
            UserResponse(
                msg= "User Created", 
                token= token,
                userId= user_id
            ),
            200
        )
    
    def sign_in(self, userDTO: SigninDTO) -> tuple[UserResponse, int]:
        result = self.db_serivices.search_by_phone(userDTO.phone)
        if len(result) == 0 :
            return (UserResponse(msg= "Invalid Credentials"), 400)
        user_db: UserModel = UserFactory.fromDict(result[0])
        if not PasswordCrypter.verify(userDTO.password, user_db.password ):
            return (UserResponse(msg= "Invalid Credentials"), 400)
        token = JWT.encode({"name" : user_db.name})
        return (UserResponse(
            msg = "Logged",
            token= token,  
        ), 200)

    
    def get_all_user(self):
        return self.db_serivices.read()

