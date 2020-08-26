from github import Github
from slugify import slugify
import sys, os

# conecta no repositorio
g = Github('ff0c99f2894c6eee83faf57f033cd5dd3b158baa')
repo = g.get_repo('cfloriani/create-branch-assign-issue-based-on-milestone')

repo.create_pull(title='teste de pr', body='OI', head="cfloriani:feature-teste", base='master')