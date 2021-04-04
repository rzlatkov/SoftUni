class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        found = [c for c in self.categories if c.id == category_id]
        if found:
            cat = found[0]
            cat.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        found = [t for t in self.topics if t.id == topic_id]
        if found:
            top = found[0]
            top.topic = new_topic
            top.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        found = [d for d in self.documents if d.id == document_id]
        if found:
            doc = found[0]
            doc.file_name = new_file_name

    def delete_category(self, category_id):
        found = [c for c in self.categories if c.id == category_id]
        if found:
            cat = found[0]
            self.categories.remove(cat)

    def delete_topic(self, topic_id):
        found = [t for t in self.topics if t.id == topic_id]
        if found:
            top = found[0]
            self.topics.remove(top)

    def delete_document(self, document_id):
        found = [d for d in self.documents if d.id == document_id]
        if found:
            doc = found[0]
            self.documents.remove(doc)

    def get_document(self, document_id):
        found = [d for d in self.documents if d.id == document_id]
        if found:
            doc = found[0]
            return doc

    def __repr__(self):
        output = ''
        for d in self.documents:
            output += d.__repr__() + '\n'
        return output
