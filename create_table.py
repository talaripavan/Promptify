"""
I am creating 3 tables [category , keyword , template] , 
In keyword table , I am storing category_id
In Template table , I am storing category_id , keyword_id .
"""

import psycopg2
import os

# SQL statements for creating tables
create_category_table = """
CREATE TABLE IF NOT EXISTS test_schema.category(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_keyword_table = """
CREATE TABLE IF NOT EXISTS test_schema.keyword(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id UUID REFERENCES test_schema.category(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

create_template_table = """
CREATE TABLE IF NOT EXISTS test_schema.template(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    keyword_id UUID REFERENCES test_schema.keyword(id),
    category_id UUID REFERENCES test_schema.category(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Database connection parameters
hostname = os.getenv('HOSTNAME')
db_name = os.getenv('DB_NAME')
username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
port = os.getenv('PORT')

# Connect to the database and create tables
try:
    with psycopg2.connect(
        host=hostname,
        database=db_name,
        user=username,
        password=password,
        port=port
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(create_category_table)
            cur.execute(create_keyword_table)
            cur.execute(create_template_table)
        conn.commit()
    print("Tables created successfully.")
except (Exception, psycopg2.Error) as error:
    print("Error while creating tables:", error)

# Function to insert sample data
def insert_sample_data(cur):
    try:
        cur.execute(
            "INSERT INTO test_schema.category(content) VALUES (%s) RETURNING id;",
            ("general",)
        )
        category_id = cur.fetchone()[0]
        print(f"Inserted category_id: {category_id}")

        cur.execute(
            "INSERT INTO test_schema.keyword(category_id, content) VALUES (%s, %s) RETURNING id;",
            (category_id, "explain, describe, what is")
        )
        keyword_id = cur.fetchone()[0]
        print(f"Inserted keyword_id: {keyword_id}")

        cur.execute(
            "INSERT INTO test_schema.template(keyword_id, category_id, content) VALUES (%s, %s, %s);",
            (keyword_id, category_id,
             """Based on the retrieved information, please provide a comprehensive answer to the query: {query_str}
                Retrieved context {context_str}:
                Please structure your response as follows:
                Response:
                1. Brief Answer (1-2 sentences)
                2. Detailed Explanation
                3. Key Takeaways (bullet points)
            """)
        )
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting sample data:", error)

try:
    with psycopg2.connect(
        host=hostname,
        database=db_name,
        user=username,
        password=password,
        port=port
    ) as conn:
        with conn.cursor() as cur:
            insert_sample_data(cur)
        conn.commit()
    print("Sample data inserted successfully.")
except (Exception, psycopg2.Error) as error:
    print("Error while inserting sample data:", error)
