import os
import argparse


parser = argparse.ArgumentParser(description='Rename files in a directory')
parser.add_argument('-t', '--token', type=str,
                    help='specify github user token')
parser.add_argument('-u', '--username', type=str,
                    help='specify the github username', required=True)
parser.add_argument('-n', '--repo-name', type=str,
                    help='specify the repository name', required=True)
parser.add_argument('-d', '--repo-desc', type=str,
                    help='specify the repository description if not given description same as name')
parser.add_argument('-p', '--is_private',
                    help='repository visibility status:[True/False]', type=bool)

def get_token():
    if parsed_args.token != None:
        return parsed_args.token
    return os.getenv('GHUB_TOKEN')


if __name__ == '__main__':
    print('operation started')
    parsed_args = parser.parse_args()

    # print(f' username - {parsed_args.username}\n repo name - {parsed_args.repo_name}\n repo description - {parsed_args.repo_desc}')
    # os.system(f'echo '{parsed_args.username} hello'')
    token = get_token()
    command = f'curl -u \"{parsed_args.username}:{token}\" https://api.github.com/user/repos --data \'{{\"name\":"{parsed_args.repo_name}",\"description\":"{(parsed_args.repo_desc if parsed_args!=None else parsed_args.repo_name)}",\"private\":"{str(parsed_args.is_private).lower()}"}}\''
    print(command)
    os.system(command)

# curl -H -u '{$1}' https://api.github.com/user/repos -d '{'name':'repository name'}'
# git remote add origin git@github.com:user/repository_name.git && git push origin master
