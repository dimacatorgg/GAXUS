
from neomodel import StringProperty,StructuredNode,RelationshipTo

class User(StructuredNode):
    name = StringProperty(required=True)
    gmail = StringProperty(required=True)
    password = StringProperty(required=True)
    friend = RelationshipTo("User","FRIEDNS")
