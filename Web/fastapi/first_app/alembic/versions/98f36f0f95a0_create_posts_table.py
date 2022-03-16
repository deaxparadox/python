"""create posts table

Revision ID: 98f36f0f95a0
Revises: 8299d497ade8
Create Date: 2022-01-30 20:48:03.474661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98f36f0f95a0'
down_revision = '8299d497ade8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )
    pass 


def downgrade():
    op.drop_table('posts')
    pass
