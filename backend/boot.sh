#!/bin/sh

cmd="$@"

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

flask db upgrade

python -c "from app import app, db, user_datastore
from models import User, Role
app.app_context().push()

is_object_exists = db.session.query(
    db.exists().where(User.email == '$FLASK_ADMIN_EMAIL')
).scalar()
print(f'Is admin exists? -{is_object_exists}')
if not is_object_exists:
    user_datastore.create_user(email='$FLASK_ADMIN_EMAIL', password='$FLASK_ADMIN_PASSWORD')
    user_datastore.create_role(name='admin', description='administrator')
    db.session.commit()
    user = User.query.first()
    role = Role.query.first()
    user_datastore.add_role_to_user(user, role)
    db.session.commit()
    print(f'Admin is created!')"

exec $cmd
