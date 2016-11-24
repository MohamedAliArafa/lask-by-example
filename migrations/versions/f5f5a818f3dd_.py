"""empty message

Revision ID: f5f5a818f3dd
Revises: 83ee39f6c684
Create Date: 2016-11-16 23:45:42.062696

"""

# revision identifiers, used by Alembic.
revision = 'f5f5a818f3dd'
down_revision = '83ee39f6c684'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('price', postgresql.DOUBLE_PRECISION(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'price')
    ### end Alembic commands ###