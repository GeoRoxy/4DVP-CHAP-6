"""empty message

Revision ID: b17afc77ba83
Revises: 32b00d06d892
Create Date: 2020-10-12 13:24:36.666256

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b17afc77ba83'
down_revision = '32b00d06d892'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mailbox', sa.Column('disabled', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mailbox', 'disabled')
    # ### end Alembic commands ###
