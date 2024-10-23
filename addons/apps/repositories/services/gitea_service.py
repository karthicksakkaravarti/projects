import requests
from django.conf import settings


class GiteaService:
    # Ensure this is set in your settings
    BASE_URL = settings.GITEA['BASE_URL']
    # Admin token with permissions to create users and repos
    ADMIN_TOKEN = settings.GITEA["TOKEN"]

    def __init__(self):
        self.base_url = settings.GITEA['BASE_URL']
        self.headers = {
            'Authorization': f'token {settings.GITEA["TOKEN"]}',
            'Content-Type': 'application/json',
        }

    def get_repositories(self):
        url = f"{self.base_url}/user/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_repository_details(self, repo_owner, repo_name, token=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {token}"
        }
        url = f"{self.base_url}/repos/{repo_owner}/{repo_name}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_branches(self, repo_owner, repo_name, token=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {token}"
        }
        url = f"{self.base_url}/repos/{repo_owner}/{repo_name}/branches"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_commits(self, repo_owner, repo_name, token=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {token}"
        }
        url = f"{self.base_url}/repos/{repo_owner}/{repo_name}/commits"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_all_files(self, repo_owner, repo_name, ref='main', token=None):
        """
        Retrieves all files in a repository.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {token}"
        }
        url = f"{self.base_url}/repos/{repo_owner}/{repo_name}/contents?ref={ref}"
        print(url)
        response = requests.get(url, headers=headers)
        print(response.content)
        response.raise_for_status()
        return response.json()
    
    def get_user_access_token(self, username, password):
        """
        Retrieves an access token for a user.
        """
        url = f"{self.BASE_URL}/users/{username}/tokens"
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, auth=(username, password), json={
            "name": "token",
            "scopes": [
                "read:repository",
                "write:repository",
                "write:user"
            ]
        })
        print(response.content)
        response.raise_for_status()
        return response.json()

    def _encode_credentials(self, username, password):
        """
        Encodes the username and password for basic authentication.
        """
        import base64
        credentials = f"{username}:{password}"
        return base64.b64encode(credentials.encode()).decode()

    def create_user(self, username, password, email):
        """
        Creates a new user in Gitea.
        """
        url = f"{self.BASE_URL}/admin/users"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {self.ADMIN_TOKEN}"
        }

        data = {

            "username": username,
            "full_name": username,
            "login_name": username,
            "password": password,
            "email": email,
            "must_change_password": False,
            "send_notify": False,
            "source_id": 0
        }
        print("data", data)
        response = requests.post(url, json=data, headers=headers)
        print(response.content)
        response.raise_for_status()
        return response.json()

    def create_repository(self, owner, repo_name, private=True, token=None, description="description"):
        """
        Creates a new repository under the specified owner.
        """
        url = f"{self.BASE_URL}/user/repos"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {token}"
        }
        data = {
            "auto_init": True,
            "default_branch": "main",
            "description": description,
            "gitignores": "",
            "issue_labels": "",
            "license": "",
            "name": repo_name,
            "object_format_name": "sha1",
            "private": True,
            "readme": "Default",
            "template": False,
            "trust_model": "default"
        }
        
        response = requests.post(url, json=data, headers=headers)
        print(response.content)
        response.raise_for_status()
        return response.json()

    def add_user_to_repo(self, owner, repo_name, username, permission="write"):
        """
        Adds a user to a repository with specified permissions.
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}/invitations"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"token {self.ADMIN_TOKEN}"
        }
        data = {
            "username": username,
            "permission": permission
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()


    # Add more methods as needed based on Gitea API documentation
