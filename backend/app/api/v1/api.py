from fastapi import APIRouter

from app.api.v1.endpoints import users, login, profile, jobs, applications, optimus, resume_analysis, agent, task, feedback, learning

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(applications.router, prefix="/applications", tags=["applications"])
api_router.include_router(optimus.router, prefix="/optimus", tags=["optimus"])
api_router.include_router(resume_analysis.router, prefix="/resume-analysis", tags=["resume-analysis"])

# New AI agent-related endpoints
api_router.include_router(agent.router, prefix="/agent", tags=["agent"])
api_router.include_router(task.router, prefix="/task", tags=["task"])
api_router.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
api_router.include_router(learning.router, prefix="/learning", tags=["learning"])
