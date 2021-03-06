"""add last few columns to posts table

Revision ID: 5eadac3da23c
Revises: 98493805f1e0
Create Date: 2022-01-30 21:47:24.283467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5eadac3da23c'
down_revision = '98493805f1e0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column(
            "published",
            sa.Boolean(),
            nullable=False, 
            server_default="TRUE"
        )
    )
    op.add_column(
        "posts", 
        sa.Column(
            'created_at', 
            sa.TIMESTAMP(timezone=True),
            nullable=False, 
            server_default=sa.text('NOW()')
        )
    )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
