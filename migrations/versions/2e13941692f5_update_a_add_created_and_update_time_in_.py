"""update a add created and update time in table

Revision ID: 2e13941692f5
Revises: 75ae3ab1ecf8
Create Date: 2024-08-12 09:36:38.713000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e13941692f5'
down_revision: Union[str, None] = '75ae3ab1ecf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###