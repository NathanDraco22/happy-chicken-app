from api.services.db_services.db_protocol import DBServicesProtocol
from api.services.db_services.tinydb_services import TinyDBServices

class UserController:

    db_serivices: DBServicesProtocol = TinyDBServices()  

    def sign_up(self, name: str):
        #verificar si existe
        #guardar en base de datos
        self.db_serivices.create(name)
        return True
    
    def get_all_user(self):
        return self.db_serivices.read()

