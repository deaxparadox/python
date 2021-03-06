"""add phone number nullable False

Revision ID: 6574d2913fc8
Revises: ab1bd9451056
Create Date: 2022-01-30 22:14:08.663060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6574d2913fc8'
down_revision = 'ab1bd9451056'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
