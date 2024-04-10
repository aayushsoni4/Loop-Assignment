import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from datetime import datetime, time
from app import db
from run import app
from app.models.store_status import StoreStatus
from app.models.business_hours import BusinessHours
from app.models.timezone_info import TimezoneInfo


def check_utc(timestamp):
    if "." not in timestamp:
        timestamp = timestamp.replace(" UTC", ".000000 UTC")
    return timestamp


def populate_store_status():
    df = pd.read_csv("data/store_status.csv")
    for _, row in df.iterrows():
        store_id = row["store_id"]
        timestamp_utc = check_utc(row["timestamp_utc"])
        timestamp_utc = datetime.strptime(timestamp_utc, "%Y-%m-%d %H:%M:%S.%f %Z")
        status = row["status"]
        # Check if entry already exists
        existing_entry = StoreStatus.query.filter_by(
            store_id=store_id, timestamp_utc=timestamp_utc, status=status
        ).first()
        if existing_entry is None:
            store_status = StoreStatus(
                store_id=store_id, timestamp_utc=timestamp_utc, status=status
            )
            db.session.add(store_status)


def populate_business_hours():
    df = pd.read_csv("data/business_hours.csv")
    for _, row in df.iterrows():
        store_id = row["store_id"]
        day_of_week = row["day"]
        open_time_str = row["start_time_local"]
        close_time_str = row["end_time_local"]
        open_time = datetime.strptime(open_time_str, "%H:%M:%S").time()
        close_time = datetime.strptime(close_time_str, "%H:%M:%S").time()
        # Check if entry already exists
        existing_entry = BusinessHours.query.filter_by(
            store_id=store_id,
            day_of_week=day_of_week,
            open_time=open_time,
            close_time=close_time,
        ).first()
        if existing_entry is None:
            business_hours = BusinessHours(
                store_id=store_id,
                day_of_week=day_of_week,
                open_time=open_time,
                close_time=close_time,
            )
            db.session.add(business_hours)


def populate_timezone_info():
    df = pd.read_csv("data/timezone.csv")
    for _, row in df.iterrows():
        store_id = row["store_id"]
        timezone = row["timezone_str"]
        timezone_info = TimezoneInfo(store_id=store_id, timezone=timezone)
        # Check if entry already exists
        existing_entry = TimezoneInfo.query.filter_by(
            store_id=store_id, timezone=timezone
        ).first()
        if existing_entry is None:
            timezone_info = TimezoneInfo(store_id=store_id, timezone=timezone)
            db.session.add(timezone_info)


def main():
    with app.app_context():
        populate_store_status()
        populate_business_hours()
        populate_timezone_info()
        db.session.commit()


if __name__ == "__main__":
    main()
