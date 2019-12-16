from firebase_admin import credentials, firestore, initialize_app


class FireStoreService:
    """
    This class should handle reading & writing from and to firebase.
    """

    def __init__(self):
        cred = credentials.Certificate('attendance-list.json')
        default_app = initialize_app(cred)
        self.db = firestore.client()
        self.product_ref = self.db.collection('product')
        self.user_ref = self.db.collection('user')

    def create_product(self, json):
        self.product_ref.document(json['id']).set(json)

    def create_user(self, json):
        self.product_ref.document(json['phone_number']).set(json)