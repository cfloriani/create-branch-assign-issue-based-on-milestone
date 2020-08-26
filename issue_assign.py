from github import Github
from slugify import slugify
import sys, os

# conecta no repositorio
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

print(os.getenv('repository'))
print(os.getenv('issue'))
print(os.getenv('milestone'))

# cria uma branch para a issue
nome_branch = slugify(os.getenv('issue'))
repo.create_git_ref('refs/heads/{nome_branch}'.format(**locals()),repo.get_branch('master').commit.sha)

# cria uma branch extra para a issue com milestone feature:
if str(os.getenv('milestone'))[0:7].lower() == "feature":
    nome_branch = slugify(os.getenv('milestone'))
    repo.create_git_ref('refs/heads/{nome_branch}'.format(**locals()),repo.get_branch('master').commit.sha)
