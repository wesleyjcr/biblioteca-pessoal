"""empty message

Revision ID: 726af3010192
Revises: 6764e95ca47c
Create Date: 2020-08-02 14:16:02.374006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '726af3010192'
down_revision = '6764e95ca47c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'title')
    # ### end Alembic commands ###