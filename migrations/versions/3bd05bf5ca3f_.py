"""empty message

Revision ID: 3bd05bf5ca3f
Revises: a277cf1eb364
Create Date: 2023-02-15 15:42:32.367178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bd05bf5ca3f'
down_revision = 'a277cf1eb364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stat', sa.Column('player_id', sa.Integer(), nullable=False))
    op.add_column('stat', sa.Column('set_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'stat', 'player', ['player_id'], ['id'])
    op.create_foreign_key(None, 'stat', 'set', ['set_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stat', type_='foreignkey')
    op.drop_constraint(None, 'stat', type_='foreignkey')
    op.drop_column('stat', 'set_id')
    op.drop_column('stat', 'player_id')
    # ### end Alembic commands ###