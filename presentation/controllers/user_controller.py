# app/presentation/controllers/user_controller.py
from fastapi import APIRouter, Depends
from app.application.user.commands.create_user import CreateUserCommand
from app.application.user.dtos.user_requests import UserCreateRequest
from app.dependencies import get_create_user_command  # <-- FIX HERE

router = APIRouter()


@router.post("/users")
def create_user(request: UserCreateRequest, command: CreateUserCommand = Depends(get_create_user_command)):
    return command.execute(request)
