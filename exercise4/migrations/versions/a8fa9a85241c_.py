"""empty message

Revision ID: a8fa9a85241c
Revises: e1fef893b9bf
Create Date: 2021-03-28 18:16:24.820648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8fa9a85241c'
down_revision = 'e1fef893b9bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'owner', 'puppy', ['puppy_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'owner', type_='foreignkey')
    # ### end Alembic commands ###
