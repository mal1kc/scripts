import os
import argparse


parser = argparse.ArgumentParser(description='Rename files in a directory')
parser.add_argument('-e','--echo', help='echo the string you use here')
parser.add_argument('--verbose', help='increase output verbosity', action='store_true')
parser.add_argument('-u','--username', help='specify the github username',required=True)
parser.add_argument('-n','--repo-name',help='specify the repository name',required=True)
parser.add_argument('-d','--repo-desc',help='specify the repository description if not given description same as name')

if __name__=='__main__':
    print('operation started')
    parsed_args = parser.parse_args()
    token = os.getenv('GHUB_TOKEN')
    print(f' username - {parsed_args.username}\n repo name - {parsed_args.repo_name}\n repo description - {parsed_args.repo_desc}')
    # os.system(f'echo '{parsed_args.username} hello'')
    # command = 'curl -u \"{{0}}\" https://api.github.com/user/repos -d \"{{\"name\":{1}},{\"description\":{2}}}\"'.format(parsed_args.username,parsed_args.repo_name,parsed_args.repo_desc if parsed_args!=None else parsed_args.repo_name)
    command = f'curl -u \"{parsed_args.username}:{token}\" https://api.github.com/user/repos --data \'{{\"name\":"{parsed_args.repo_name}",\"description\":"{(parsed_args.repo_desc if parsed_args!=None else parsed_args.repo_name)}"}}\''
    print(command)
    os.system(command)
# curl -H -u '{$1}' https://api.github.com/user/repos -d '{'name':'repository name'}'
# git remote add origin git@github.com:user/repository_name.git && git push origin master