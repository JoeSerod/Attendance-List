from firebase_admin import credentials, firestore, initialize_app

class FireStoreService:
    """
    This class should handle reading & writing from and to firebase.
    """

    def __init__(self):
        cred = credentials.Certificate('attendance-list.json')
        default_app = initialize_app(cred)
        self.db = firestore.client()
        self.student_ref = self.db.collection('students')