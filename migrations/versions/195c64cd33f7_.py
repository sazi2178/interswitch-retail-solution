"""empty message

Revision ID: 195c64cd33f7
Revises: 
Create Date: 2019-07-31 08:55:31.865454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '195c64cd33f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'description')
    # ### end Alembic commands ###
