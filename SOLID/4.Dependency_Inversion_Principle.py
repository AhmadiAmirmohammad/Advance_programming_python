#High-level modules (business logic)
# should not directly depend on low-level modules (implementation details).
# Both should depend on abstraction, not details.

#Dependency Inversion Principle (DIP)
# class MySQLDatabase:
#     def save(self, data):
#         print(f"ذخیره {data} در MySQL")
#
#
# class UserService:
#     def __init__(self):
#         self.db = MySQLDatabase()  # وابستگی مستقیم و سفت به یک پیاده‌سازی خاص!
#
#     def register_user(self, user):
#         self.db.save(user)

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f' {data} save in MySQL')

class MongoDatabase(Database):
    def save(self, data):
        print(f'save in {data} MongoDB')


class UserService:
    def __init__(self, db: Database):
        # Depends on abstraction, not specific implementation
        self.db = db

    def register_user(self, user):
        self.db.save(user)


# Now we can 'inject' any database without changing the UserService
service1 = UserService(MySQLDatabase())
service1.register_user('Ali')

service2 = UserService(MongoDatabase())
service2.register_user('Sara')