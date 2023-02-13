"""empty message

Revision ID: 919436382503
Revises: 66db0f8893ee
Create Date: 2023-02-13 00:34:39.347792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919436382503'
down_revision = '66db0f8893ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('game_number', sa.Integer(), nullable=True),
    sa.Column('player_a_score', sa.Integer(), nullable=True),
    sa.Column('player_b_score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###
