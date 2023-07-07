import win32evtlog
import win32evtlogutil

def parse_event_logs(log_name, num_records):
    # Open the event log
    hand = win32evtlog.OpenEventLog(None, log_name)

    # Read the event records
    total_records = win32evtlog.GetNumberOfEventLogRecords(hand)
    print(f"Total number of records in {log_name}: {total_records}")

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    record_num = total_records
    count = 0

    # Iterate over the event records
    while count < num_records:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            break

        for event in events:
            record_number = event.RecordNumber
            event_id = event.EventID
            event_source = event.SourceName
            event_time = event.TimeGenerated.Format()
            event_category = event.EventCategory
            event_type = event.EventType
            event_description = win32evtlogutil.SafeFormatMessage(event, log_name)

            # Print event details
            print(f"Record Number: {record_number}")
            print(f"Event ID: {event_id}")
            print(f"Source: {event_source}")
            print(f"Time: {event_time}")
            print(f"Category: {event_category}")
            print(f"Type: {event_type}")
           # print(f"Description: {event_description}")
            print("---------------------------------------")

            count += 1
            if count >= num_records:
                break

        record_num -= len(events)
        if record_num <= 0:
            break

    # Close the event log
    win32evtlog.CloseEventLog(hand)

if __name__ == "__main__":
    log_name = "Security"  # Specify the event log name to parse (e.g., "Application", "System")
    num_records = 30000  # Specify the number of records to print
    parse_event_logs(log_name, num_records)
