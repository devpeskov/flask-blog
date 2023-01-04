# Flask project

To run:

- `git clone https://github.com/devpeskov/flask-blog.git`
- `cd flask blog`
- Create `.env` file (and substitute your values if necessary):
```
echo 'POSTGRES_USER="postgres"
POSTGRES_PASSWORD="paSsw0rdExam91e"
POSTGRES_DB="flask_blog"
FLASK_SECRET_KEY="flask-secure-r&+q;(a!#37goqw,er2/.[aktt2&5e#%hegx-13o((=uz^o"

SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}"' > .env
```
- `docker-compose up --build`
