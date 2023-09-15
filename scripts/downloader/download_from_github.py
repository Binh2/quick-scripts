import fsspec
from pathlib import Path

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='Download from github')
    parser.add_argument('-u', '--user', help='Download files from a user')
    parser.add_argument('-r', '--repo', help='Download files from a repo')
    parser.add_argument('-f', '--folder', help='Download files from a folder', default='')
    args = parser.parse_args()
    
    destination = Path('./github') 
    destination.mkdir(exist_ok=True, parents=True)
    fs = fsspec.filesystem("github", org=args.user, repo=args.repo)
    fs.get(fs.ls(args.folder), destination.as_posix(), recursive=True)