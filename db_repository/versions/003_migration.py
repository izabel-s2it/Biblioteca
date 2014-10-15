from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
followers = Table('followers', pre_meta,
    Column('follower_id', INTEGER),
    Column('followed_id', INTEGER),
)

post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('about_me', VARCHAR(length=140)),
    Column('last_seen', DATETIME),
)

book = Table('book', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('titulo', String(length=120)),
    Column('autor', String(length=120)),
    Column('editora', String(length=100)),
    Column('categoria', String(length=120)),
    Column('status', String(length=20)),
    Column('quantidade', Integer),
    Column('descricao', String(length=120)),
    Column('tipo', String(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['followers'].drop()
    pre_meta.tables['post'].drop()
    pre_meta.tables['user'].drop()
    post_meta.tables['book'].columns['tipo'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['followers'].create()
    pre_meta.tables['post'].create()
    pre_meta.tables['user'].create()
    post_meta.tables['book'].columns['tipo'].drop()
