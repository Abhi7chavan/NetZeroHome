"""v1.0_initial_schema

Revision ID: 01407f473690
Revises: 
Create Date: 2025-03-21 17:42:05.174823
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision = '01407f473690'
down_revision = None
branch_labels = None
depends_on = None

# Define MetaData instance
metadata = sa.MetaData()

# Define tables
User = sa.Table(
    "User",
    metadata,
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('license_id', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),  # Removed duplicate password column
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('features', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('HouseholdItems', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('SensorCount', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.String(), nullable=False),  # References role.role_id
    sa.Column('created_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.Column('updated_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())"), onupdate=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('license_id'),  # Removed unique constraint on role_id
    schema="meta"
)

License = sa.Table(
    "License",
    metadata,
    sa.Column('license_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False, unique=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('features', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('HouseholdItems', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('SensorCount', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.Column('updated_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())"), onupdate=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.PrimaryKeyConstraint('license_id'),
    schema="meta"
)

Permission = sa.Table(
    "Permission",
    metadata,
    sa.Column('permission_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('config', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.Column('updated_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())"), onupdate=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.PrimaryKeyConstraint('permission_id'),
    schema="meta"
)

HouseItem = sa.Table(
    'HouseItem',
    metadata,
    sa.Column('item_id', sa.String(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('voltage_volts', sa.Float(), nullable=False),
    sa.Column('current_amps', sa.Float(), nullable=True),
    sa.Column('power_watts', sa.Float(), nullable=True),
    sa.Column('operating_time_hours', sa.Float(), nullable=True),
    sa.Column('power_factor', sa.Float(), nullable=True),
    sa.Column('min_power_watts', sa.Float(), nullable=True),
    sa.Column('max_power_watts', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('item_id'),
    schema='meta'
)

House = sa.Table(
    'House',
    metadata,
    sa.Column('house_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('rooms', sa.JSON(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('issolar', sa.Boolean(), nullable=False),
    sa.Column('electric_vehicles', sa.Integer(), nullable=True),
    sa.Column('number_of_devices', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('house_id'),
    schema='meta'
)

Role = sa.Table(
    'role',
    metadata,
    sa.Column('role_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('permission', sa.JSON(), nullable=True),  # Renamed to 'permissions' for clarity
    sa.PrimaryKeyConstraint('role_id'),
    schema='meta'
)

Room = sa.Table(
    'Room',
    metadata,
    sa.Column('room_id', sa.String(), nullable=False),
    sa.Column('house_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('room_id'),
    schema='meta'
)

Sensor = sa.Table(
    'Sensor',
    metadata,
    sa.Column('sensor_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('category_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.Column('updated_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())"), onupdate=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.PrimaryKeyConstraint('sensor_id'),
    schema='meta'
)

Category = sa.Table(
    'Category',
    metadata,
    sa.Column('category_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('category_id'),
    schema='meta'
)

HouseRoomItemMapping = sa.Table(
    'HouseRoomItemMapping',
    metadata,
    sa.Column('mapping_id', sa.String(), nullable=False),
    sa.Column('house_id', sa.String(), nullable=False),
    sa.Column('room_id', sa.String(), nullable=False),
    sa.Column('sensor_id', sa.String(), nullable=False),
    sa.Column('item_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.Column('updated_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())"), onupdate=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.PrimaryKeyConstraint('mapping_id'),
    schema='meta'
)

HouseReading = sa.Table(
    'HouseReading',
    metadata,
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('Total_Energy', sa.Float(), nullable=False),
    sa.Column('cost', sa.Numeric(10, 2), nullable=False),
    sa.Column('time', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())")),
    sa.Column('updated_at', sa.BigInteger, server_default=sa.text("EXTRACT(EPOCH FROM now())"), onupdate=sa.text("EXTRACT(EPOCH FROM now())")),
    schema='meta'
)

def upgrade():
    op.execute("CREATE SCHEMA IF NOT EXISTS meta")
    
    # Create Role table first (master table)
    op.create_table(
        Role.name,
        *Role.columns,
        *Role.constraints,
        schema='meta'
    )
    
    # Create User table with correct foreign key
    op.create_table(
        User.name,
        *User.columns,
        *User.constraints,
        schema="meta"
    )
    op.create_foreign_key(
        'fk_user_role', 'User', 'role',  # From User.role_id to role.role_id
        ['role_id'], ['role_id'],
        source_schema='meta', referent_schema='meta'
    )

    op.create_table(
        License.name,
        *License.columns,
        *License.constraints,
        schema="meta"
    )

    op.create_table(
        Permission.name,
        *Permission.columns,
        *Permission.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_permission_user', 'Permission', 'User',
        ['user_id'], ['user_id'],
        source_schema='meta', referent_schema='meta'
    )

    op.create_table(
        HouseItem.name,
        *HouseItem.columns,
        *HouseItem.constraints,
        schema='meta'
    )

    op.create_table(
        House.name,
        *House.columns,
        *House.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_house_user', 'House', 'User',
        ['user_id'], ['user_id'],
        source_schema='meta', referent_schema='meta'
    )

    op.create_table(
        Room.name,
        *Room.columns,
        *Room.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_room_house', 'Room', 'House',
        ['house_id'], ['house_id'],
        source_schema='meta', referent_schema='meta'
    )
    
    op.create_table(
        Category.name,
        *Category.columns,
        *Category.constraints,
        schema='meta'
    )

    op.create_table(
        Sensor.name,
        *Sensor.columns,
        *Sensor.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_sensor_user', 'Sensor', 'User',
        ['user_id'], ['user_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_sensor_category', 'Sensor', 'Category',
        ['category_id'], ['category_id'],
        source_schema='meta', referent_schema='meta'
    )

    op.create_table(
        HouseRoomItemMapping.name,
        *HouseRoomItemMapping.columns,
        *HouseRoomItemMapping.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_hrim_house', 'HouseRoomItemMapping', 'House',
        ['house_id'], ['house_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_hrim_room', 'HouseRoomItemMapping', 'Room',
        ['room_id'], ['room_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_hrim_sensor', 'HouseRoomItemMapping', 'Sensor',
        ['sensor_id'], ['sensor_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_hrim_item', 'HouseRoomItemMapping', 'HouseItem',
        ['item_id'], ['item_id'],
        source_schema='meta', referent_schema='meta'
    )

    op.create_table(
        HouseReading.name,
        *HouseReading.columns,
        *HouseReading.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_hr_user', 'HouseReading', 'User',
        ['user_id'], ['user_id'],
        source_schema='meta', referent_schema='meta'
    )

def downgrade():
    # Drop in reverse order
    op.drop_constraint('fk_hr_user', 'HouseReading', schema='meta', type_='foreignkey')
    op.drop_table('HouseReading', schema='meta')

    op.drop_constraint('fk_hrim_item', 'HouseRoomItemMapping', schema='meta', type_='foreignkey')
    op.drop_constraint('fk_hrim_sensor', 'HouseRoomItemMapping', schema='meta', type_='foreignkey')
    op.drop_constraint('fk_hrim_room', 'HouseRoomItemMapping', schema='meta', type_='foreignkey')
    op.drop_constraint('fk_hrim_house', 'HouseRoomItemMapping', schema='meta', type_='foreignkey')
    op.drop_table('HouseRoomItemMapping', schema='meta')

    op.drop_constraint('fk_sensor_category', 'Sensor', schema='meta', type_='foreignkey')
    op.drop_constraint('fk_sensor_user', 'Sensor', schema='meta', type_='foreignkey')
    op.drop_table('Sensor', schema='meta')

    op.drop_table('Category', schema='meta')

    op.drop_constraint('fk_room_house', 'Room', schema='meta', type_='foreignkey')
    op.drop_table('Room', schema='meta')

    op.drop_constraint('fk_house_user', 'House', schema='meta', type_='foreignkey')
    op.drop_table('House', schema='meta')

    op.drop_table('HouseItem', schema='meta')

    op.drop_constraint('fk_permission_user', 'Permission', schema='meta', type_='foreignkey')
    op.drop_table('Permission', schema='meta')

    op.drop_table('License', schema='meta')

    op.drop_constraint('fk_user_role', 'User', schema='meta', type_='foreignkey')
    op.drop_table('User', schema='meta')

    op.drop_table('role', schema='meta')

    op.execute("DROP SCHEMA IF EXISTS meta CASCADE")