"""1.1_add_masters_tables

Revision ID: 12a7818caac6
Revises: 01407f473690
Create Date: 2025-03-22 14:41:40.324124
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
import uuid

# Revision identifiers, used by Alembic
revision: str = '12a7818caac6'
down_revision: Union[str, None] = '01407f473690'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    # Check if HouseItem exists (assumes meta schema from prior migration)
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if not inspector.has_table("HouseItem", schema="meta"):
        raise Exception("Table meta.HouseItem does not exist. Verify migration 01407f473690.")

    # Generate UUIDs for HouseItem
    item_ids = [str(uuid.uuid4()) for _ in range(20)]
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
        schema='meta'
    )

    op.bulk_insert(house_item_table, [
        {'item_id': item_ids[0], 'item_name': 'LED Bulb', 'voltage_volts': 120.0, 'current_amps': 0.083, 'power_watts': 10.0, 'operating_time_hours': 5.0, 'power_factor': 0.9, 'min_power_watts': 8.0, 'max_power_watts': 12.0},
        # ... (other items unchanged for brevity)
        {'item_id': item_ids[19], 'item_name': 'Game Console', 'voltage_volts': 120.0, 'current_amps': 1.0, 'power_watts': 120.0, 'operating_time_hours': 3.0, 'power_factor': 0.9, 'min_power_watts': 100.0, 'max_power_watts': 150.0},
    ])

    # Store item_ids for downgrade
    op.execute("CREATE TEMPORARY TABLE temp_item_ids (item_id VARCHAR);")
    for item_id in item_ids:
        op.execute(f"INSERT INTO temp_item_ids (item_id) VALUES ('{item_id}');")

    # Category table (meta schema)
    category_table = sa.table(
        'Category',
        sa.column('category_id', sa.String),
        sa.column('name', sa.String),
        schema='meta'
    )
    category_ids = [str(uuid.uuid4()) for _ in range(3)]
    op.bulk_insert(category_table, [
        {'category_id': category_ids[0], 'name': 'Electric'},
        {'category_id': category_ids[1], 'name': 'Water'},
        {'category_id': category_ids[2], 'name': 'Flow'},
    ])

    # Store category_ids for downgrade
    op.execute("CREATE TEMPORARY TABLE temp_category_ids (category_id VARCHAR);")
    for category_id in category_ids:
        op.execute(f"INSERT INTO temp_category_ids (category_id) VALUES ('{category_id}');")

    # role table (no schema specified, assuming default/public)
    role_table = sa.table(
        'role',
        sa.column('role_id', sa.String),
        sa.column('name', sa.String),
        sa.column('description', sa.Text),
        sa.column('permission',sa.JSON),
        schema = 'meta'
    )
    role_ids = [str(uuid.uuid4()) for _ in range(3)]
    op.bulk_insert(role_table, [
        {
            'role_id': role_ids[0],
            'name': 'admin',
            'description': "Admin can handle the application with all rights but can't edit permissions or create users",
            'permissions': {"is_view": True, "is_write": True, "is_edit": True, "is_support": False}
        },
        {
            'role_id': role_ids[1],
            'name': 'support',
            'description': "Support has all access; activities tracked by audit log and mailed to admin",
            'permissions': {"is_view": True, "is_write": True, "is_edit": True, "is_support": True}
        },
        {
            'role_id': role_ids[2],
            'name': 'viewer',
            'description': "Viewer can only view the application",
            'permissions': {"is_view": True, "is_write": False, "is_edit": False, "is_support": False}
        }
    ])

    # Store role_ids for downgrade
    op.execute("CREATE TEMPORARY TABLE temp_role_ids (role_id VARCHAR);")
    for role_id in role_ids:
        op.execute(f"INSERT INTO temp_role_ids (role_id) VALUES ('{role_id}');")


def downgrade() -> None:
    """Downgrade schema."""
    # Delete HouseItem entries
    op.execute("DELETE FROM meta.\"HouseItem\" WHERE item_id IN (SELECT item_id FROM temp_item_ids);")
    op.execute("DROP TABLE temp_item_ids;")

    # Delete Category entries
    op.execute("DELETE FROM meta.\"Category\" WHERE category_id IN (SELECT category_id FROM temp_category_ids);")
    op.execute("DROP TABLE temp_category_ids;")

    # Delete role entries
    op.execute("DELETE FROM role WHERE role_id IN (SELECT role_id FROM temp_role_ids);")
    op.execute("DROP TABLE temp_role_ids;")

    # Delete UserPermission entries (cascade deletes role if FK exists, otherwise manual)
    op.execute("DELETE FROM user_permission WHERE permission_id IN (1, 2, 3);")