# LCM:: Database

PostGIS runs in Docker. Start it with `docker compose up -d`, then connect on `localhost:5432` (db, user and password are all `lcm` for local dev).

On first start, anything in `db/init/` runs automatically. Right now that just creates three empty schemas: `staging` (raw stuff lands here), `published` (cleaned and ready to serve) and `catalog` (what we've got and where it came from).

Init scripts only run against a fresh volume. If you change them, run `docker compose down -v && docker compose up -d` to rebuild. Heads up: that wipes the data.