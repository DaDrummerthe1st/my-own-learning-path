"""test create table

Revision ID: 3e7f1f4d3919
Revises: 
Create Date: 2025-05-28 20:11:53.359678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e7f1f4d3919'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "employees",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("currently_employed", sa.Boolean, default=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("employees")
