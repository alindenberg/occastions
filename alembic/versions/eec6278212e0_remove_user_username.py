"""remove user.username

Revision ID: eec6278212e0
Revises: f60d7913750f
Create Date: 2024-06-19 07:31:13.789776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eec6278212e0'
down_revision: Union[str, None] = 'f60d7913750f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_username', table_name='users')
    op.create_index(op.f('ix_users_created'), 'users', ['created'], unique=False)
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_users_created'), table_name='users')
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    # ### end Alembic commands ###
