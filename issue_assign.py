from github import Github
from slugify import slugify
import sys, os

# conecta no repositorio
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

# cria uma branch para a issue
nome_branch = slugify(os.getenv('issue'))
repo.create_git_ref('refs/heads/{nome_branch}'.format(**locals()),repo.get_branch('master').commit.sha)
print('Criada a branch ', nome_branch ,' para a Issue')

# cria uma branch extra para a issue com milestone feature:
if str(os.getenv('milestone'))[0:7].lower() == "feature":
    nome_branch = slugify(os.getenv('milestone'))
    print('Criada a branch ', nome_branch ,' para a Milestone')
    repo.create_git_ref('refs/heads/{nome_branch}'.format(**locals()),repo.get_branch('master').commit.sha)
