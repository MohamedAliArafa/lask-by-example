"""empty message

Revision ID: 9d53ee853b44
Revises: d7f9bf213f7b
Create Date: 2016-05-04 16:05:37.946409

"""

# revision identifiers, used by Alembic.
revision = '9d53ee853b44'
down_revision = 'd7f9bf213f7b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'DOB')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('DOB', sa.DATE(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
