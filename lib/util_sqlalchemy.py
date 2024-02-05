import datetime

from sqlalchemy import DateTime
from sqlalchemy.types import TypeDecorator

from lib.util_datetime import tzware_datetime
from snakeeyes.extensions import db


class AwareDateTime(TypeDecorator):
    
    impl = DateTime(timezone=True)

    def process_bind_param(self, value, dialect):
        if isinstance(value, datetime.datetime) and value.tzinfo is None:
            raise ValueError('{!r} must be TZ-aware'.format(value))
        return value

    def __repr__(self):
        return 'AwareDateTime()'


class ResourceMixin(object):
    
    created_on = db.Column(AwareDateTime(),
                           default=tzware_datetime)
    updated_on = db.Column(AwareDateTime(),
                           default=tzware_datetime,
                           onupdate=tzware_datetime)

    @classmethod
    def sort_by(cls, field, direction):
        
        if field not in cls.__table__.columns:
            field = 'created_on'

        if direction not in ('asc', 'desc'):
            direction = 'asc'

        return field, direction

    @classmethod
    def get_bulk_action_ids(cls, scope, ids, omit_ids=[], query=''):
        
        omit_ids = list(map(str, omit_ids))

        if query and scope == 'all_search_results':
            
            ids = cls.query.with_entities(cls.id).filter(cls.search(query))

            ids = [str(item[0]) for item in ids]

        if omit_ids:
            ids = [id for id in ids if id not in omit_ids]

        return ids

    @classmethod
    def bulk_delete(cls, ids):
        
        delete_count = cls.query.filter(cls.id.in_(ids)).delete(
            synchronize_session=False)
        db.session.commit()

        return delete_count

    def save(self):
        
        db.session.add(self)
        db.session.commit()

        return self

    def delete(self):
        
        db.session.delete(self)
        return db.session.commit()

    def __str__(self):
        
        obj_id = hex(id(self))
        columns = self.__table__.c.keys()

        values = ', '.join("%s=%r" % (n, getattr(self, n)) for n in columns)
        return '<%s %s(%s)>' % (obj_id, self.__class__.__name__, values)
