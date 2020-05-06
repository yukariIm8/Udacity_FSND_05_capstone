"""empty message

Revision ID: 0ed757ac4825
Revises:
Create Date: 2020-05-05 20:56:53.052702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ed757ac4825'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Actor',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=60), nullable=False),
                    sa.Column('age', sa.Integer(), nullable=False),
                    sa.Column('gender', sa.String(length=20), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('Movie',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=120), nullable=False),
                    sa.Column('release_date', sa.Date(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('Casting',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('actor_id', sa.Integer(), nullable=True),
                    sa.Column('movie_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['actor_id'], ['Actor.id'],
                                            ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['movie_id'], ['Movie.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Casting')
    op.drop_table('Movie')
    op.drop_table('Actor')
    # ### end Alembic commands ###
