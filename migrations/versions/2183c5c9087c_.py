"""empty message

Revision ID: 2183c5c9087c
Revises: 
Create Date: 2019-04-29 18:15:20.438334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2183c5c9087c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###