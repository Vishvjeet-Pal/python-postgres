from database import engine, Base, SessionLocal
from crud import get_user, get_users, create_user, update_user, delete_user

Base.metadata.create_all(bind=engine)

db=SessionLocal()

# Create a new user
new_user=create_user(db, name="Alice", course="Btech", age=22)
print(f"Created User: {new_user.s_id}, {new_user.name}, {new_user.course}, {new_user.age}")
# Get all users
users=get_users(db)
print("All Users:")
for user in users:
    print(f"{user.s_id}, {user.name}, {user.course}, {user.age}")
# Get a specific user
user=get_user(db, user_id=new_user.s_id)
print(f"Fetched User: {user.s_id}, {user.name}, {user.course}, {user.age}")
# Update a user
updated_user=update_user(db, user_id=new_user.s_id, name="Alice Smith", age=23)
print(f"Updated User: {updated_user.s_id}, {updated_user.name}, {updated_user.course}, {updated_user.age}")
# Delete a user 
delete_user(db, user_id=new_user.s_id) 
print("Deleted User")

db.close()