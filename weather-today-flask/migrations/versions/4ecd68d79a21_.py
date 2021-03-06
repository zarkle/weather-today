"""empty message

Revision ID: 4ecd68d79a21
Revises: 3f17791e2f9e
Create Date: 2019-04-03 15:37:10.704697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ecd68d79a21'
down_revision = '3f17791e2f9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_cities_city_name', table_name='cities')
    op.create_index(op.f('ix_cities_city_name'), 'cities', ['city_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cities_city_name'), table_name='cities')
    op.create_index('ix_cities_city_name', 'cities', ['city_name'], unique=True)
    # ### end Alembic commands ###
