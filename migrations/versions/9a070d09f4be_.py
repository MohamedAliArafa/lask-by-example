"""empty message

Revision ID: 9a070d09f4be
Revises: 6aa9929c4055
Create Date: 2016-05-12 20:50:08.902983

"""

# revision identifiers, used by Alembic.
revision = '9a070d09f4be'
down_revision = '6aa9929c4055'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gender', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'gender')
    ### end Alembic commands ###
