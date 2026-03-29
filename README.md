# FastAPI Learning - Attempt 1

This project uses a Docker setup where the server is **not started automatically**. Instead, the container stays alive so you can exec into it and run the server manually.

## How it works

- The `dockerfile` uses `CMD ["bash"]` — no server auto-start.
- `docker-compose.yml` sets `tty: true` and `stdin_open: true` to keep the container running without a process to hold it up.

## Usage

**Start the container (stays alive):**
```bash
docker compose up -d
```

**Exec into the container:**
```bash
docker compose exec web bash
```

**Run the server manually inside the container:**
```bash
fastapi dev main.py --host 0.0.0.0 --port 8000
```

**Stop the container:**
```bash
docker compose down
```
