"""added fields cod_account and balance

Revision ID: f5dc92d66b01
Revises: ea95597ee3a9
Create Date: 2023-06-26 17:38:10.260319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5dc92d66b01'
down_revision = 'ea95597ee3a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('cod_account', sa.Integer(), nullable=False))
    op.add_column('accounts', sa.Column('balance', sa.Float(), nullable=False))
    op.create_unique_constraint(None, 'accounts', ['cod_account'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'accounts', type_='unique')
    op.drop_column('accounts', 'balance')
    op.drop_column('accounts', 'cod_account')
    # ### end Alembic commands ###
