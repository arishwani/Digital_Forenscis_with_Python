import sqlite3
import datetime

def parse_chrome_history():
    # Locate the Chrome history database file
    history_file_path = input("Enter Browser History Location: ")
    # Replace "<Path_to_Chrome_history_file>" with the actual path to the Chrome history file

    # Connect to the Chrome history database
    conn = sqlite3.connect(history_file_path)
    cursor = conn.cursor()

    # Query the browsing history
    cursor.execute("SELECT title, url, last_visit_time FROM urls ORDER BY last_visit_time DESC")

    # Fetch all the results
    results = cursor.fetchall()

    # Print the browsing history
    for title, url, last_visit_time in results:
        visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=last_visit_time)
        print(f"Title: {title}")
        print(f"URL: {url}")
        print(f"Last Visit Time: {visit_time}")
        print()

    # Close the database connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    parse_chrome_history()
