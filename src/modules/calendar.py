from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle
from datetime import datetime, timedelta, timezone

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_calendar_service():
    creds = None
    if os.path.exists("calendar_token.pickle"):
        with open("calendar_token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("calendar_token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("calendar", "v3", credentials=creds)

def get_upcoming_events(max_results: int = 10, days_ahead: int = 7):
    service = get_calendar_service()
    now_utc = datetime.now(timezone.utc)
    now = now_utc.isoformat()
    end_time = (now_utc + timedelta(days=days_ahead)).isoformat()

    events_result = service.events().list(
        calendarId="primary",
        timeMin=now,
        timeMax=end_time,
        maxResults=max_results * 2,  # fetch extra in case some are filtered out
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])
    event_summaries = []

    for event in events:
        start_raw = event["start"].get("dateTime", event["start"].get("date"))
        start_dt = datetime.fromisoformat(start_raw.replace("Z", "+00:00")) if "T" in start_raw else datetime.fromisoformat(start_raw)
        if start_dt < now_utc:
            continue  # skip past events
        start_str = start_dt.strftime("%b %d, %I:%M %p") if "T" in start_raw else start_dt.strftime("%b %d")
        summary = event.get("summary", "No title")
        event_summaries.append(f"{start_str} - {summary}")
        if len(event_summaries) >= max_results:
            break

    return event_summaries
