"""sdffggf

Revision ID: 2e6100c7c10a
Revises: 0b341e472fdd
Create Date: 2021-10-23 17:51:34.033878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e6100c7c10a'
down_revision = '0b341e472fdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('BookwithUser', sa.Column('user_email', sa.String(length=250), nullable=True))
    op.create_index(op.f('ix_BookwithUser_user_email'), 'BookwithUser', ['user_email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_BookwithUser_user_email'), table_name='BookwithUser')
    op.drop_column('BookwithUser', 'user_email')
    # ### end Alembic commands ###
