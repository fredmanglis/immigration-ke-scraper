-- A significantly over-engineered database to cater for possibly more than just
-- the current RRI thingies.

CREATE TABLE IF NOT EXISTS stations(
    station_id TEXT NOT NULL,
    station_name TEXT NOT NULL,
    PRIMARY KEY(station_id),
    UNIQUE(station_name)
) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS rri_weeks(
    rri_week_id TEXT NOT NULL,
    week_name TEXT NOT NULL,
    UNIQUE(week_name),
    PRIMARY KEY(rri_week_id)
) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS tracking_numbers(
    station_id TEXT NOT NULL,
    tracking_number TEXT NOT NULL,
    doc_date TEXT NOT NULL,
    UNIQUE(tracking_number),
    FOREIGN KEY(station_id) REFERENCES stations(station_id)
      ON UPDATE CASCADE ON DELETE RESTRICT
    PRIMARY KEY(station_id, tracking_number)
) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS rri_tracking_numbers(
    station_id TEXT NOT NULL,
    tracking_number TEXT NOT NULL,
    rri_week_id TEXT NOT NULL,
    FOREIGN KEY(station_id) REFERENCES stations(station_id)
      ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY(tracking_number) REFERENCES tracking_numbers(tracking_number) 
      ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY(rri_week_id) REFERENCES rri_weeks(rri_week_id)
      ON UPDATE CASCADE ON DELETE RESTRICT
    PRIMARY KEY(station_id, tracking_number, rri_week_id)
) WITHOUT ROWID;
