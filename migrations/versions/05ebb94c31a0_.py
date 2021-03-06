"""empty message

Revision ID: 05ebb94c31a0
Revises: c42102e41cae
Create Date: 2021-01-10 12:51:40.436671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05ebb94c31a0'
down_revision = 'c42102e41cae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(length=16), nullable=True),
    sa.Column('time', sa.String(length=8), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request_model')
    # ### end Alembic commands ###
