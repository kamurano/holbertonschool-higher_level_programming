#!/usr/bin/python3
import os


def generate_invitations(template_content, attendees):
    x = 1
    for attendee in attendees:
        if not (os.path.exists(f"output_{x}.txt")):
            return
        try:
            with open(f"output_{x}.txt", 'w') as f:
                invitation = template_content.format(**attendee)
                f.write(invitation)
                x += 1
        except Exception as e:
            print(f"Error: {e}")
            continue
