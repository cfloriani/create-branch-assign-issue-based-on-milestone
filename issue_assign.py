from github import Github
from slugify import slugify
import sys, os

# connet in repository
g = Github(sys.argv[1])
repo = g.get_repo(os.getenv('repository'))

# creade a branch for issue
branch_issue = os.getenv('issue_num') + '-' + slugify(os.getenv('issue'))
repo.create_git_ref('refs/heads/{branch_issue}'.format(**locals()),repo.get_branch('master').commit.sha)

# create extra branch for milestone feature:
if str(os.getenv('milestone'))[0:7].lower() == "feature":
    branch_milestone = slugify(os.getenv('milestone'))
    repo.create_git_ref('refs/heads/{branch_milestone}'.format(**locals()),repo.get_branch('master').commit.sha)
