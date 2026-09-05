class google():
    __ceo = "Sundar Pichai"
    __cofounder = "satyam gaur"

class google_sub_india(google):
    __name = "google india"
    def __init__(self, mannager, location):
        self.mannager = mannager
        self.location = location

obj1 = google_sub_india("satyam gaur", "azamgarh")

print(obj1.__dict__) 




