from app.application.interfaces.user_repo_factory import IUserRepoFactory
from app.application.user.dtos.user_requests import UserCreateRequest
from app.domain.user.user_factory import UserFactory


class CreateUserCommand:
    def __init__(self, repo_factory: IUserRepoFactory):
        self.repo_factory = repo_factory

    def execute(self, request: UserCreateRequest):
        # 1. Create Domain Entity
        user = UserFactory.create(request.user_type, request.model_dump())
        print('test')

        # 2. Get the specific repo from the factory based on the request
        # 'request.target_database' would be "mongo" or "postgres"
        repo = self.repo_factory.get_repository(request.target_database)

        # 3. Save
        repo.save(user)
        return user
