from fastapi import FastAPI
from sqlalchemy.orm import Session

from app.database import engine, Base, SessionLocal
from app.models import Role, Permission
from app.routes import auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RBAC Authorization System", version="1.0.0")

app.include_router(auth.router)
app.include_router(users.router)

DEFAULT_PERMISSIONS = [
    "user:read", "user:create", "user:update", "user:delete",
]

DEFAULT_ROLES = {
    "admin": DEFAULT_PERMISSIONS,
    "manager": ["user:read", "user:create", "user:update"],
    "user": ["user:read"],
}


def seed_defaults():
    db = SessionLocal()
    try:
        if db.query(Permission).count() == 0:
            for perm_name in DEFAULT_PERMISSIONS:
                db.add(Permission(name=perm_name))
            db.commit()

        if db.query(Role).count() == 0:
            for role_name, perm_names in DEFAULT_ROLES.items():
                role = Role(name=role_name)
                perms = db.query(Permission).filter(Permission.name.in_(perm_names)).all()
                role.permissions = perms
                db.add(role)
            db.commit()
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    seed_defaults()


@app.get("/")
def root():
    return {"message": "RBAC Authorization System is running. Visit /docs for API documentation."}
