"""create transaction table

Revision ID: a4257c2529ab
Revises: 3e7f1f4d3919
Create Date: 2025-05-30 14:55:48.437613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4257c2529ab'
down_revision: Union[str, None] = '3e7f1f4d3919'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("transactions",
        sa.Column("transaction_id", sa.String, primary_key=True, nullable=False),
        sa.Column("timestamp", sa.DateTime, nullable=False),
        sa.Column("amount", sa.Float, nullable=False),
        sa.Column("currency", sa.String(3), nullable=False),
        sa.Column("sender_account", sa.String(34), nullable=False),
        sa.Column("receiver_account", sa.String(34), nullable=False),
        sa.Column("sender_country", sa.String(25), nullable=False),
        sa.Column("sender_municipality", sa.String(25), nullable=False),
        sa.Column("receiver_country", sa.String(25), nullable=False),
        sa.Column("receiver_country", sa.String(25), nullable=False),
        sa.Column("transaction_type", sa.String(15), nullable=False),
        sa.Column("notes", sa.String(255), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("transactions")
