#!/usr/bin/python3
import os


def generate_invitations(template_content, attendees):
    if not attendees:
        return "No data provided, no output files generated."
    
    x = 1
    for attendee in attendees:
        if not os.path.exists(f"output_{x}.txt"):
            return "Template is empty, no output files generated."
        with open(f"output_{x}.txt", 'w') as f:
            # try:
            attendee = {k: v if v is not None else "N/A" for k, v in attendee.items()}
            invitation = template_content.format(**attendee)
            f.write(invitation)
            x += 1
            # except Exception as e:
                # print(e)
                # continue
            
            
if __name__ == "__name__":
    attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    with open('template.txt', 'r') as f:
        template_content = f.read()

    generate_invitations(template_content, attendees)
