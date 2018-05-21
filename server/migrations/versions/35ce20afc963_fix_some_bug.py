"""fix some bug

Revision ID: 35ce20afc963
Revises: 
Create Date: 2018-05-21 15:35:35.899407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ce20afc963'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exam_rooms', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('schedules', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schedules', 'id')
    op.drop_column('exam_rooms', 'id')
    # ### end Alembic commands ###
