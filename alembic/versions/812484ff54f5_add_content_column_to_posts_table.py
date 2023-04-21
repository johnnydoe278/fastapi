"""add content column to posts table

Revision ID: 812484ff54f5
Revises: f44f88480024
Create Date: 2023-04-16 20:14:41.719478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '812484ff54f5'
down_revision = 'f44f88480024'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
