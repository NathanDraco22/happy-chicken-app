from tinydb import TinyDB

class TinyDBServices:

    db: TinyDB = TinyDB("db.json")

    def read(self):
        return self.db.all()
    
    def create(self, data):
        id = self.db.insert({"name" : data})
        return str(id)
    
    def delete(self):
        ...


