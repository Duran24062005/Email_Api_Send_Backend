from fastapi import FastAPI
from routes.auth.auth_routes import auth_router
from routes.home.home_routes import home_routes
from routes.profile.profile_routes import profile_routes
from routes.emails.email_routes import email_routes


app = FastAPI(
    title="Send email Back-End",
    description="This application was built to be able to send messages from a user created in the system.",
    version="0.0.1"
)


@app.get('/', response_model=str, status_code=200)
async def root():
    return "Welcome to Platform"

# TODO
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(home_routes, prefix="/home", tags=["Home"])
app.include_router(profile_routes, prefix="/profile", tags=["Profile"])
app.include_router(email_routes, prefix="/emails", tags=["Emails"])