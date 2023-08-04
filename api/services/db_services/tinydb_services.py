from tinydb import TinyDB, Query

class TinyDBServices:

    db: TinyDB = TinyDB("db.json")

    def read(self):
        return self.db.all()
    
    def create(self, data):
        id = self.db.insert(data)
        return str(id)
    
    def delete(self):
        ...
    
    def search_by_phone(self, phone:str) -> dict|None:
        print("algo")
        user_query = Query()
        return self.db.search(user_query.phone == phone)


