"""v1.0_initial_schema

Revision ID: 01407f473690
Revises: 
Create Date: 2025-03-21 17:42:05.174823
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '01407f473690'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Define a MetaData instance to hold our table definitions.
metadata = sa.MetaData()

# Define tables with a specified schema (in this case "meta")
User = sa.Table(
    'User',
    metadata,
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('features', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('HouseholdItems', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('SensorCount', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('created_at', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('username'),
    schema='meta'
)

License = sa.Table(
    'License',
    metadata,
    sa.Column('license_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('features', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('householdItems', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('SensorCount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('license_id'),
    sa.UniqueConstraint('license_id'),
    sa.UniqueConstraint('username'),
    schema='meta'
)

Permission = sa.Table(
    'Permission',
    metadata,
    sa.Column('permission_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('config', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('permission_id'),
    schema='meta'
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
    schema='meta'
)

def upgrade():
    # Create the "meta" schema if it does not exist
    op.execute("CREATE SCHEMA IF NOT EXISTS meta")
    
    # Create tables using the defined metadata (all tables will be created in the "meta" schema)
    op.create_table(
        User.name,
        *User.columns,
        *User.constraints,
        schema='meta'
    )

    op.create_table(
        License.name,
        *License.columns,
        *License.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_license_username', License.name, User.name,
        ['username'], ['username'],
        source_schema='meta', referent_schema='meta'
    )

    op.create_table(
        Permission.name,
        *Permission.columns,
        *Permission.constraints,
        schema='meta'
    )
    op.create_foreign_key(
        'fk_permission_user', Permission.name, User.name,
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
        'fk_house_user', House.name, User.name,
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
        'fk_room_house', Room.name, House.name,
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
        'fk_sensor_user', Sensor.name, User.name,
        ['user_id'], ['user_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_sensor_category', Sensor.name, Category.name,
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
        'fk_hrim_house', HouseRoomItemMapping.name, House.name,
        ['house_id'], ['house_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_hrim_room', HouseRoomItemMapping.name, Room.name,
        ['room_id'], ['room_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_hrim_sensor', HouseRoomItemMapping.name, Sensor.name,
        ['sensor_id'], ['sensor_id'],
        source_schema='meta', referent_schema='meta'
    )
    op.create_foreign_key(
        'fk_hrim_item', HouseRoomItemMapping.name, HouseItem.name,
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
        'fk_hr_user', HouseReading.name, User.name,
        ['user_id'], ['user_id'],
        source_schema='meta', referent_schema='meta'
    )

def downgrade():
    # Drop tables in reverse order, respecting dependencies
    op.drop_constraint('fk_hr_user', HouseReading.name, schema='meta', type_='foreignkey')
    op.drop_table(HouseReading.name, schema='meta')

    op.drop_constraint('fk_hrim_item', HouseRoomItemMapping.name, schema='meta', type_='foreignkey')
    op.drop_constraint('fk_hrim_sensor', HouseRoomItemMapping.name, schema='meta', type_='foreignkey')
    op.drop_constraint('fk_hrim_room', HouseRoomItemMapping.name, schema='meta', type_='foreignkey')
    op.drop_constraint('fk_hrim_house', HouseRoomItemMapping.name, schema='meta', type_='foreignkey')
    op.drop_table(HouseRoomItemMapping.name, schema='meta')

    op.drop_constraint('fk_sensor_category', Sensor.name, schema='meta', type_='foreignkey')
    op.drop_constraint('fk_sensor_user', Sensor.name, schema='meta', type_='foreignkey')
    op.drop_table(Sensor.name, schema='meta')

    op.drop_table(Category.name, schema='meta')

    op.drop_constraint('fk_room_house', Room.name, schema='meta', type_='foreignkey')
    op.drop_table(Room.name, schema='meta')

    op.drop_constraint('fk_house_user', House.name, schema='meta', type_='foreignkey')
    op.drop_table(House.name, schema='meta')

    op.drop_table(HouseItem.name, schema='meta')

    op.drop_constraint('fk_permission_user', Permission.name, schema='meta', type_='foreignkey')
    op.drop_table(Permission.name, schema='meta')

    op.drop_constraint('fk_license_username', License.name, schema='meta', type_='foreignkey')
    op.drop_table(License.name, schema='meta')

    op.drop_table(User.name, schema='meta')

    # Optionally, drop the schema itself
    op.execute("DROP SCHEMA IF EXISTS meta CASCADE")