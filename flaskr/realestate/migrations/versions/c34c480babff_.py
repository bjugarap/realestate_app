"""empty message

Revision ID: c34c480babff
Revises: b62f4d8c3828
Create Date: 2024-05-09 02:54:49.851139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c34c480babff'
down_revision = 'b62f4d8c3828'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logins',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('agents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=128), nullable=False),
    sa.Column('login_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['login_id'], ['logins.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=128), nullable=False),
    sa.Column('login_id', sa.Integer(), nullable=True),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agents.id'], ),
    sa.ForeignKeyConstraint(['login_id'], ['logins.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('review_date', sa.DateTime(), nullable=True),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.Column('listing_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agents.id'], ),
    sa.ForeignKeyConstraint(['listing_id'], ['listings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('listings', schema=None) as batch_op:
        batch_op.alter_column('agent_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key(None, 'agents', ['agent_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('listings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('agent_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.drop_table('reviews')
    op.drop_table('photos')
    op.drop_table('clients')
    op.drop_table('agents')
    op.drop_table('logins')
    # ### end Alembic commands ###
