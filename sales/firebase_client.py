import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from settings import base


class FirebaseClient:

    def __init__(self):
        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(
                credentials.Certificate(base.FIRESTORE_PATH)
            )

        self._db = firestore.client()
        self._collection = self._db.collection(u'salesSummary')

    def create(self, data):
        """Create salesSummary in firestore database"""
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        doc_ref = self._collection.document()
        doc_ref.set(data)

    def update(self, id, data):
        """Update salesSummary on firestore database using document id"""
        data['updated_at'] = datetime.now()
        doc_ref = self._collection.document(id)
        doc_ref.update(data)

    def get_latest(self):
        """Get the latest salesSummary based on created or updated time"""
        docs = self._collection.order_by('created_at', direction='DESC').limit(1).stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    def delete_by_id(self, id):
        """Delete salesSummary on firestore database using document id"""
        self._collection.document(id).delete()

    def get_by_id(self, id):
        """Get salesSummary on firestore database using document id"""
        doc_ref = self._collection.document(id)
        doc = doc_ref.get()

        if doc.exists:
            return {**doc.to_dict(), "id": doc.id}
        return

    def all(self):
        """Get all salesSummary from firestore database"""
        docs = self._collection.stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]

    def filter(self, field, condition, value):
        """Filter salesSummary using conditions on firestore database"""
        docs = self._collection.where(field=field, op_string=condition, value=value).stream()
        return [{**doc.to_dict(), "id": doc.id} for doc in docs]
