"""empty message

Revision ID: 596e7848124b
Revises: b66f4b424b7a
Create Date: 2016-05-04 15:52:57.714023

"""

# revision identifiers, used by Alembic.
revision = '596e7848124b'
down_revision = 'b66f4b424b7a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('mobile', sa.String(), nullable=False),
    sa.Column('gender', sa.CHAR(), nullable=True),
    sa.Column('DOB', sa.Date(), nullable=True),
    sa.Column('profile_pic', sa.String(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopping_cart',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'item_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping_cart')
    op.drop_table('user')
    ### end Alembic commands ###
