FROM python:3.11-slim

WORKDIR /code

RUN pip install "fastapi[standard]"

COPY . /code

# No CMD here, or use:
CMD ["bash"]