"""add_article

Revision ID: f5906a304a42
Revises: 
Create Date: 2023-09-02 13:55:11.868897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5906a304a42'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('create schema stone')
    op.create_table('t_article',
    sa.Column('id_article', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_article'),
    schema='stone',
    comment='Article'
    )
    op.create_index(op.f('ix_stone_t_article_id_article'), 't_article', ['id_article'], unique=False, schema='stone')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stone_t_article_id_article'), table_name='t_article', schema='stone')
    op.drop_table('t_article', schema='stone')
    op.execute('drop schema stone')
    # ### end Alembic commands ###