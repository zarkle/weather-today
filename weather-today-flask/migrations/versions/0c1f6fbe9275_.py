"""empty message

Revision ID: 0c1f6fbe9275
Revises: 4ecd68d79a21
Create Date: 2019-04-03 16:26:56.477175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c1f6fbe9275'
down_revision = '4ecd68d79a21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cities', sa.Column('description', sa.String(length=256), nullable=True))
    op.add_column('cities', sa.Column('temp', sa.String(length=8), nullable=True))
    op.drop_index('ix_cities_city_name', table_name='cities')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_cities_city_name', 'cities', ['city_name'], unique=False)
    op.drop_column('cities', 'temp')
    op.drop_column('cities', 'description')
    # ### end Alembic commands ###