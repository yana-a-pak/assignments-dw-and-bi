from typing import NewType

import psycopg2


PostgresCursor = NewType("PostgresCursor", psycopg2.extensions.cursor)
PostgresConn = NewType("PostgresConn", psycopg2.extensions.connection)

table_drop_actors = "DROP TABLE IF EXISTS actors CASCADE"
table_drop_repo = "DROP TABLE IF EXISTS repo CASCADE"
table_drop_payload = "DROP TABLE IF EXISTS payload CASCADE"
table_drop_org = "DROP TABLE IF EXISTS org CASCADE"
table_drop_events = "DROP TABLE IF EXISTS events"

# Create Tables
table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
        actor_id int,
        actor_login varchar(100),
        actor_display_login varchar(100),
        actor_gravatar_id varchar(100),
        actor_url varchar(255),
        actor_avatar_url varchar(255),
        PRIMARY KEY(actor_id)
    )
"""
table_create_repo = """
    CREATE TABLE IF NOT EXISTS repo (
        repo_id int,
        repo_name varchar(100),
        repo_url varchar(255),
        PRIMARY KEY(repo_id)
    )
"""
table_create_payload = """
    CREATE TABLE IF NOT EXISTS payload (
        push_id BIGINT,
        size int,
        distinct_size int,
        ref varchar(100),
        head varchar(100),
        before varchar(100),
        commits varchar(255),
        PRIMARY KEY(push_id)
    )
"""
table_create_org = """
    CREATE TABLE IF NOT EXISTS org (
        org_id int,
        org_login varchar(100),
        org_gravatar_id varchar(100),
        org_url varchar(255),
        org_avatar_url varchar(255),
        PRIMARY KEY(org_id)
    )
"""
table_create_events = """
    CREATE TABLE IF NOT EXISTS events (
        event_id BIGINT NOT NULL,
        event_type varchar(100) NOT NULL,
        actor_id int,
        repo_id int,
        paylaod_action varchar(100) NOT NULL, -- [None (is 'push'), 'start', 'created', 'published', 'closed']
        payload_push_id BIGINT,
        public boolean NOT NULL,
        created_at varchar(100),
        org_id int,
        event_time timestamp NOT NULL,
        PRIMARY KEY(event_id),
        CONSTRAINT FK_actor FOREIGN KEY (actor_id) REFERENCES actors(actor_id),
        CONSTRAINT FK_repo FOREIGN KEY (repo_id) REFERENCES repo(repo_id),
        CONSTRAINT FK_payload FOREIGN KEY (payload_push_id) REFERENCES payload(push_id),
        CONSTRAINT FK_org FOREIGN KEY (org_id) REFERENCES org(org_id)
    )
"""


# Insert data
actors_insert = ("""
INSERT INTO actors (actor_id, actor_login, actor_display_login, actor_gravatar_id, actor_url, actor_avatar_url)
VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT (actor_id)
DO NOTHING
""")

repo_insert = ("""
INSERT INTO repo (repo_id, repo_name, repo_url)
VALUES (%s, %s, %s)
ON CONFLICT (repo_id)
DO NOTHING
""")

payload_insert = ("""
INSERT INTO payload (push_id, size, distinct_size, ref, head, before, commits)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (push_id)
DO NOTHING
""")

org_insert = ("""
INSERT INTO org (org_id, org_login, org_gravatar_id, org_url, org_avatar_url)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (org_id)
DO NOTHING
""")

events_insert = ("""
INSERT INTO events (event_id, event_type, actor_id, repo_id, payload_action, payload_push_id, public, created_at, org_id, event_time)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (event_id)
DO NOTHING
""")


# Queries
create_table_queries = [
    table_create_actors,
    table_create_repo,
    table_create_payload,
    table_create_org,
    table_create_events,

]
drop_table_queries = [
    table_drop_actors,
    table_drop_repo,
    table_drop_payload,
    table_drop_org,
    table_drop_events,
]


def drop_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
