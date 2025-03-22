"""1.1_add_masters_tables

Revision ID: 12a7818caac6
Revises: 01407f473690
Create Date: 2025-03-22 14:41:40.324124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from typing import Sequence, Union
import uuid

# revision identifiers, used by Alembic.
revision: str = '12a7818caac6'
down_revision: Union[str, None] = '01407f473690'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Debugging: Check if table exists
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    has_table = inspector.has_table("HouseItem", schema="meta")
    if not has_table:
        raise Exception("Table meta.HouseItem does not exist. Verify migration 01407f473690 and database connection.")

    # List to store generated UUIDs for downgrade
    item_ids = [str(uuid.uuid4()) for _ in range(20)]
    
    # Explicitly qualify table with schema
    house_item_table = sa.table(
        'HouseItem',
        sa.column('item_id', sa.String),
        sa.column('item_name', sa.String),
        sa.column('voltage_volts', sa.Float),
        sa.column('current_amps', sa.Float),
        sa.column('power_watts', sa.Float),
        sa.column('operating_time_hours', sa.Float),
        sa.column('power_factor', sa.Float),
        sa.column('min_power_watts', sa.Float),
        sa.column('max_power_watts', sa.Float),
        schema='meta'  # Explicit schema
    )

    op.bulk_insert(
        house_item_table,
        [
            {'item_id': item_ids[0], 'item_name': 'LED Bulb', 'voltage_volts': 120.0, 'current_amps': 0.083, 'power_watts': 10.0, 'operating_time_hours': 5.0, 'power_factor': 0.9, 'min_power_watts': 8.0, 'max_power_watts': 12.0},
            {'item_id': item_ids[1], 'item_name': 'Ceiling Fan', 'voltage_volts': 120.0, 'current_amps': 0.625, 'power_watts': 75.0, 'operating_time_hours': 8.0, 'power_factor': 0.85, 'min_power_watts': 60.0, 'max_power_watts': 90.0},
            {'item_id': item_ids[2], 'item_name': 'Refrigerator', 'voltage_volts': 120.0, 'current_amps': 1.5, 'power_watts': 180.0, 'operating_time_hours': 24.0, 'power_factor': 0.95, 'min_power_watts': 150.0, 'max_power_watts': 200.0},
            {'item_id': item_ids[3], 'item_name': 'Microwave Oven', 'voltage_volts': 120.0, 'current_amps': 10.0, 'power_watts': 1200.0, 'operating_time_hours': 0.5, 'power_factor': 0.9, 'min_power_watts': 1000.0, 'max_power_watts': 1400.0},
            {'item_id': item_ids[4], 'item_name': 'Television', 'voltage_volts': 120.0, 'current_amps': 0.5, 'power_watts': 60.0, 'operating_time_hours': 4.0, 'power_factor': 0.9, 'min_power_watts': 50.0, 'max_power_watts': 70.0},
            {'item_id': item_ids[5], 'item_name': 'Laptop Charger', 'voltage_volts': 120.0, 'current_amps': 0.75, 'power_watts': 90.0, 'operating_time_hours': 3.0, 'power_factor': 0.95, 'min_power_watts': 80.0, 'max_power_watts': 100.0},
            {'item_id': item_ids[6], 'item_name': 'Air Conditioner', 'voltage_volts': 240.0, 'current_amps': 6.0, 'power_watts': 1440.0, 'operating_time_hours': 10.0, 'power_factor': 0.9, 'min_power_watts': 1200.0, 'max_power_watts': 1600.0},
            {'item_id': item_ids[7], 'item_name': 'Electric Kettle', 'voltage_volts': 120.0, 'current_amps': 12.5, 'power_watts': 1500.0, 'operating_time_hours': 0.2, 'power_factor': 1.0, 'min_power_watts': 1400.0, 'max_power_watts': 1600.0},
            {'item_id': item_ids[8], 'item_name': 'Washing Machine', 'voltage_volts': 120.0, 'current_amps': 4.0, 'power_watts': 480.0, 'operating_time_hours': 1.5, 'power_factor': 0.85, 'min_power_watts': 400.0, 'max_power_watts': 550.0},
            {'item_id': item_ids[9], 'item_name': 'Dishwasher', 'voltage_volts': 120.0, 'current_amps': 10.0, 'power_watts': 1200.0, 'operating_time_hours': 2.0, 'power_factor': 0.9, 'min_power_watts': 1000.0, 'max_power_watts': 1300.0},
            {'item_id': item_ids[10], 'item_name': 'Toaster', 'voltage_volts': 120.0, 'current_amps': 7.5, 'power_watts': 900.0, 'operating_time_hours': 0.1, 'power_factor': 1.0, 'min_power_watts': 800.0, 'max_power_watts': 1000.0},
            {'item_id': item_ids[11], 'item_name': 'Hair Dryer', 'voltage_volts': 120.0, 'current_amps': 12.5, 'power_watts': 1500.0, 'operating_time_hours': 0.25, 'power_factor': 0.95, 'min_power_watts': 1400.0, 'max_power_watts': 1600.0},
            {'item_id': item_ids[12], 'item_name': 'Desktop PC', 'voltage_volts': 120.0, 'current_amps': 3.0, 'power_watts': 360.0, 'operating_time_hours': 6.0, 'power_factor': 0.9, 'min_power_watts': 300.0, 'max_power_watts': 400.0},
            {'item_id': item_ids[13], 'item_name': 'Electric Heater', 'voltage_volts': 240.0, 'current_amps': 6.25, 'power_watts': 1500.0, 'operating_time_hours': 4.0, 'power_factor': 1.0, 'min_power_watts': 1400.0, 'max_power_watts': 1600.0},
            {'item_id': item_ids[14], 'item_name': 'Coffee Maker', 'voltage_volts': 120.0, 'current_amps': 8.0, 'power_watts': 960.0, 'operating_time_hours': 0.3, 'power_factor': 0.95, 'min_power_watts': 900.0, 'max_power_watts': 1000.0},
            {'item_id': item_ids[15], 'item_name': 'Vacuum Cleaner', 'voltage_volts': 120.0, 'current_amps': 10.0, 'power_watts': 1200.0, 'operating_time_hours': 0.5, 'power_factor': 0.9, 'min_power_watts': 1000.0, 'max_power_watts': 1300.0},
            {'item_id': item_ids[16], 'item_name': 'Blender', 'voltage_volts': 120.0, 'current_amps': 3.0, 'power_watts': 360.0, 'operating_time_hours': 0.1, 'power_factor': 0.9, 'min_power_watts': 300.0, 'max_power_watts': 400.0},
            {'item_id': item_ids[17], 'item_name': 'Electric Stove', 'voltage_volts': 240.0, 'current_amps': 20.0, 'power_watts': 4800.0, 'operating_time_hours': 1.0, 'power_factor': 1.0, 'min_power_watts': 4000.0, 'max_power_watts': 5000.0},
            {'item_id': item_ids[18], 'item_name': 'Water Heater', 'voltage_volts': 240.0, 'current_amps': 18.75, 'power_watts': 4500.0, 'operating_time_hours': 2.0, 'power_factor': 1.0, 'min_power_watts': 4000.0, 'max_power_watts': 4800.0},
            {'item_id': item_ids[19], 'item_name': 'Game Console', 'voltage_volts': 120.0, 'current_amps': 1.0, 'power_watts': 120.0, 'operating_time_hours': 3.0, 'power_factor': 0.9, 'min_power_watts': 100.0, 'max_power_watts': 150.0},
        ]
    )

    # Store item_ids in a temporary table for downgrade
    op.execute("CREATE TEMPORARY TABLE temp_item_ids (item_id VARCHAR);")
    for item_id in item_ids:
        op.execute(f"INSERT INTO temp_item_ids (item_id) VALUES ('{item_id}');")
        
        
    category_table = sa.table('Category',sa.column('category_id',sa.String),sa.Column('name',sa.String),schema='meta')
    
    
    item_ids = [str(uuid.uuid4()) for _ in range(3)]
    
    op.bulk_insert(category_table,[{'category_id':item_ids[0],'name':'Electric'},{'category_id':item_ids[1],'name':'Water'},{'category_id':item_ids[2],'name':'Flow',}])



def downgrade() -> None:
    """Downgrade schema."""
    # Delete rows using the stored item_ids from the temporary table
    op.execute("DELETE FROM meta.\"HouseItem\" WHERE item_id IN (SELECT item_id FROM temp_item_ids);")
    op.execute("DROP TABLE temp_item_ids;")