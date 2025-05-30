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
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
