import glob
import json
import os
from typing import List


import psycopg2



def get_files(filepath: str) -> List[str]:
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    return all_files


def process(cur, conn, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    
    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                
                if each["type"] == "IssueCommentEvent":
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                        
                    )
                else:
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                    )

                #Insert data into tables here
                insert_statement_actors = f"""
                    INSERT INTO actors (
                        actor_id, 
                        actor_login, 
                        actor_display_login, 
                        actor_gravatar_id, 
                        actor_url, 
                        actor_avatar_url
                    ) VALUES (  
                        '{each["actor"]["id"]}', 
                        '{each["actor"]["login"]}',
                        '{each["actor"]["display_login"]}',
                        '{each["actor"]["gravatar_id"]}',
                        '{each["actor"]["url"]}',
                        '{each["actor"]["avatar_url"]}'
                        )
                        ON CONFLICT (actor_id) DO NOTHING
                    """
                # print(insert_statement_actors)
                cur.execute(insert_statement_actors)
                
                insert_statement_repo = f"""
                    INSERT INTO repo (
                        repo_id, 
                        repo_name, 
                        repo_url
                    ) VALUES (  
                        '{each["repo"]["id"]}', 
                        '{each["repo"]["name"]}',
                        '{each["repo"]["url"]}'
                        )
                        ON CONFLICT (repo_id) DO NOTHING
                    """
                cur.execute(insert_statement_repo)

                try:
                    insert_statement_payload = f"""
                    INSERT INTO payload (
                        push_id, 
                        size, 
                        distinct_size, 
                        ref, 
                        head, 
                        before, 
                        commits
                    ) VALUES (  
                        '{each["payload"]["push_id"]}', 
                        '{each["payload"]["size"]}',
                        '{each["payload"]["distinct_size"]}',
                        '{each["payload"]["ref"]}',
                        '{each["payload"]["head"]}',
                        '{each["payload"]["before"]}',
                        '{each["payload"]["commits"]}'
                        )
                        ON CONFLICT (push_id) DO NOTHING
                    """
                    cur.execute(insert_statement_payload)

                except:
                    pass
                
                try:
                    insert_statement_org = f"""
                    INSERT INTO org (
                        org_id, 
                        org_login, 
                        org_gravatar_id, 
                        org_url, 
                        org_avatar_url
                    ) VALUES (  
                        '{each["org"]["id"]}', 
                        '{each["org"]["login"]}',
                        '{each["org"]["gravatar_id"]}',
                        '{each["org"]["url"]}',
                        '{each["org"]["avatar_url"]}'
                        )
                        ON CONFLICT (org_id) DO NOTHING
                    """
                    cur.execute(insert_statement_org)

                except:
                    pass

                try:
                    insert_statement_events = f"""
                    INSERT INTO events (
                        event_id, 
                        event_type, 
                        actor_id, 
                        repo_id, 
                        payload_action, 
                        payload_push_id, 
                        public, 
                        created_at, 
                        org_id, 
                        event_time
                    ) VALUES (  
                        '{each["event"]["id"]}', 
                        '{each["event"]["type"]}',
                        '{each["actor"]["id"]}',
                        '{each["repo"]["id"]}',
                        '{each["payload"]["action"]}',
                        '{each["payload"]["push_id"]}',
                        '{each["public"]}',
                        '{each["create_at"]}',
                        '{each["org"]["id"]}',
                        '{each["event"]["time"]}'
                        )
                        ON CONFLICT (event_id) DO NOTHING
                    """
                    cur.execute(insert_statement_events)

                except:
                    pass 

                conn.commit()


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )

    cur = conn.cursor()

    process(cur, conn, filepath="../data")


    conn.close()
   

if __name__ == "__main__":
    main()