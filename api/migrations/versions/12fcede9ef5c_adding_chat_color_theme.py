"""adding chat_color_theme

Revision ID: 12fcede9ef5c
Revises: 5fda94355fce
Create Date: 2024-05-26 05:51:41.171154

"""
import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = '12fcede9ef5c'
down_revision = '5fda94355fce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chat_color_theme', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('chat_color_theme_inverted', sa.Boolean(), server_default=sa.text('false'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sites', schema=None) as batch_op:
        batch_op.drop_column('chat_color_theme_inverted')
        batch_op.drop_column('chat_color_theme')

    # ### end Alembic commands ###
