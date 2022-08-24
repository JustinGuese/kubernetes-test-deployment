a quick kubernetes test deployment if i quickly need something to test

using my often used tools python, postgresql, fastapi

a simple application that accepts new users and returns them

check out the swagger ui at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

needs the manual kubernetes secret

- POSTGRES_PASSWORD
- PSQL_URL

`kubectl create secret generic psql-password --from-literal=POSTGRES_PASSWORD="changeme"`

`kubectl create secret generic psql-url --from-literal=PSQL_URL="postgres:changeme@postgresql/postgres"`