class Agent:
    def __init__(self, name, lastname, user, phone, email, password, address, document_type, document_number, rol):
        self.name = name
        self.lastname = lastname
        self.user = user
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
        self.document_type = document_type
        self.document_number = document_number
        self.rol = rol
    def toDBCollection(self):
        return{
            'name': self.name,
            'lastname': self.lastname,
            'user': self.user,
            'phone': self.phone,
            'email': self.email,
            'password': self.password,
            'address': self.address,
            'document_type': self.document_type,
            'document_number': self.document_number, 
            'rol': self.rol
        }
