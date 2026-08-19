"""
One-time setup script: creates the Databricks secret scope and stores the
Massive API key. Run this locally (with the Databricks CLI configured) or
from a notebook - never commit the resulting secret value anywhere.

Usage:
    python setup_secrets.py
"""
from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace
import getpass

w = WorkspaceClient()

w.secrets.create_scope(scope="massive_2")
w.secrets.put_secret(
    scope="massive_2",
    key="api-key",
    string_value=getpass.getpass("Paste your Massive API key: ")
)

w.secrets.create_scope(scope="database_2")
w.secrets.put_secret(
    scope="database_2",
    key="alpaca-key-id",
    string_value=getpass.getpass("Paste your key id ")
)

w.secrets.put_secret(
    scope="database_2",
    key="alpaca-secret-key",
    string_value=getpass.getpass("Paste secret key ")
)

w.secrets.put_secret(
    scope="database_2",
    key="lakebase-url",
    string_value=getpass.getpass("Paste your lakebase url")
)

w.secrets.put_acl(
    scope="database_2",
    principal="users",
    permission=workspace.AclPermission.READ,
)

w.secrets.put_acl(
    scope="massive_2",
    principal="users",
    permission=workspace.AclPermission.READ,
)
