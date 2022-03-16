"""add content column to posts table

Revision ID: 3097bcc105a1
Revises: 98f36f0f95a0
Create Date: 2022-01-30 21:19:38.730991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3097bcc105a1'
down_revision = '98f36f0f95a0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts", sa.Column(
            'content', sa.String(), nullable=False
        )
    )
    pass


def downgrade():
    op.drop_table(
        'posts', 'content'
    )
    pass
