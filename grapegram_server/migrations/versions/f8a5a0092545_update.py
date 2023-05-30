"""update

Revision ID: f8a5a0092545
Revises: 703670ce36ed
Create Date: 2023-05-26 04:54:44.235493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f8a5a0092545"
down_revision = "703670ce36ed"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("chat", sa.Column("name", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("chat", "name")
    # ### end Alembic commands ###
