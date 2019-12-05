from firebase_admin import credentials, firestore, initialize_app


class FireStoreService:
    """
    This class should handle reading & writing from and to firebase.
    """

    def __init__(self):
        cred = credentials.Certificate('attendance-list.json')
        default_app = initialize_app(cred)
        self.db = firestore.client()
        self.worker_ref = self.db.collection('worker')

    def create_worker(self,json):
        self.worker_ref.document(json['id']).set(json)