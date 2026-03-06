# app/dependencies.py
from app.infrastructure.user.persistence.user_repo_factory_impl import UserRepoFactoryImpl
from app.application.user.commands.create_user import CreateUserCommand

# We instantiate the factory here so it's only created once (Singleton)
repo_factory_instance = UserRepoFactoryImpl()


def get_create_user_command() -> CreateUserCommand:
    """
    This is the provider function for FastAPI.
    It resolves the 'Application' command using 'Infrastructure' tools.
    """
    return CreateUserCommand(repo_factory=repo_factory_instance)
