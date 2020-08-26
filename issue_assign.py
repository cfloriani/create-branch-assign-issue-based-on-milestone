from github import Github
from slugify import slugify
import sys, os

# conecta no repositorio
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

print(os.getenv('repository'))
print(os.getenv('issue'))
print(os.getenv('milestone'))

# pega a última milestone criada
# open_milestones = repo.get_milestones(state='open', direction='desc')

# # verifica se inicia com a palavra feature:
# for milestone in open_milestones:
#     # converte o nome em slug para criar a branch
#     nome_milestone = list(str(milestone).split('"'))
#     nome_branch = slugify(nome_milestone[1])
    
#     if str(milestone)[17:25] == 'feature:':
#         repo.create_git_ref('refs/heads/{nome_branch}'.format(**locals()),repo.get_branch('master').commit.sha)
#     break

# issues = repo.get_issues()

# print(issues)
# for issue in issues:
#     print(issue)
