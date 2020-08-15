"""empty message

Revision ID: 98c6055fe14d
Revises: 9712d29e24c8
Create Date: 2020-08-13 11:45:16.922010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "98c6055fe14d"
down_revision = "9712d29e24c8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "organisations",
        sa.Column(
            "enabled_oeg_report",
            sa.Boolean(),
            server_default=sa.false(),
            nullable=False,
        ),
    )
    op.add_column(
        "project_info",
        sa.Column("reported", sa.Boolean(), server_default=sa.false(), nullable=False,),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project_info", "reported")
    op.drop_column("organisations", "enabled_oeg_report")
    # ### end Alembic commands ###
