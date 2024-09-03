class Person():
    def give_name(self, name , lastname):
        self.name = name
        self.lastname = lastname

    




geraldine = Person()
yaritza = Person()

geraldine.give_name("geraldine", "garces")
yaritza.give_name ("yaritza", "díaz")

print(geraldine.name,geraldine.lastname)
print(yaritza.name, yaritza.lastname)

