"""empty message

Revision ID: b04a38ee0906
Revises: 
Create Date: 2021-07-23 11:53:24.923370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b04a38ee0906'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('landowners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('image_link', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('campsites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('tents', sa.Boolean(), nullable=True),
    sa.Column('campervans', sa.Boolean(), nullable=True),
    sa.Column('electricity', sa.Boolean(), nullable=True),
    sa.Column('toilet', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('region', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('campsite_image', sa.String(), nullable=True),
    sa.Column('campsite_owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['campsite_owner'], ['landowners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campsites')
    op.drop_table('landowners')
    # ### end Alembic commands ###
