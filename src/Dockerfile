FROM python
RUN pip install psycopg2_binary
COPY src/postgres_test.py /tmp
ENTRYPOINT python /tmp/postgres_test.py
