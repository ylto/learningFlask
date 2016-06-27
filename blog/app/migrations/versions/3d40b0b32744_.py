"""empty message

Revision ID: 3d40b0b32744
Revises: None
Create Date: 2016-06-27 19:19:28.351103

"""

# revision identifiers, used by Alembic.
revision = '3d40b0b32744'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('status', sa.SmallInteger(), server_default='0'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'status')
    ### end Alembic commands ###
