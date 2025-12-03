#!/usr/bin/python3
"""
Function to generate personalized invitations from a template
and a list of attendee dictionaries.
"""

import os


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendees list."""

    # ---- Validate Input Types ----
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # ---- Handle Empty Template ----
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # ---- Handle Empty Attendee List ----
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---- Process Each Attendee ----
    for index, attendee in enumerate(attendees, start=1):
        # Replace missing data with "N/A"
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Fill template
        filled_template = (
            template.replace("{name}", name)
                    .replace("{event_title}", event_title)
                    .replace("{event_date}", event_date)
                    .replace("{event_location}", event_location)
        )

        # Output filename
        filename = f"output_{index}.txt"

        try:
            # Write output
            with open(filename, "w") as outfile:
                outfile.write(filled_template)

        except Exception as e:
            print(f"Error writing to {filename}: {e}")
            return
