from github import Github
from slugify import slugify
import sys, os

# conecta no repositorio
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

# cria uma branch para a issue
branch_issue = os.getenv('issue_num') + '-' + slugify(os.getenv('issue'))
repo.create_git_ref('refs/heads/{branch_issue}'.format(**locals()),repo.get_branch('master').commit.sha)
print('Criada a branch ', branch_issue ,' para a Issue')

# cria uma branch extra para a issue com milestone feature:
if str(os.getenv('milestone'))[0:7].lower() == "feature":
    branch_milestone = slugify(os.getenv('milestone'))
    print('Criada a branch ', branch_milestone ,' para a Milestone')
    repo.create_git_ref('refs/heads/{branch_milestone}'.format(**locals()),repo.get_branch('master').commit.sha)
    repo.create_pull(title='teste de pr', body='OI', head="develop", base=os.getenv('user') + ':' + branch_milestone)
else:
    repo.create_pull(title=branch_issue, head="develop", base=os.getenv('user') + ':' + 'master')