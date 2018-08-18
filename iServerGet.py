#!/usr/bin/env python2
# Original file GitHubGet.py
# Modified for iServer
# Create a new folder and paste this script into it, the GitHub repo will be downloaded into a folder created iServer-master
import urllib,zipfile,sys, clipboard, functools, re, os, tempfile

def extract_git_id(git):
    print git
    m = re.match((r'^http(s?)://([\w-]*\.)?github\.com/(?P<user>[\w-]+)/(?P<repo>[\w-]*)'
                 '((/tree|/blob)/(?P<branch>[\w-]*))?'), git)
#    print m.groupdict()
    return m
    
def git_download_from_args(args):
    url = "https://github.com/GoDzM4TT3O/iServer"
    git_download(url)


def dlProgress(filename, count, blockSize, totalSize):
    if count*blockSize > totalSize:
        percent=100
    else:
        percent = max(min(int(count*blockSize*100/totalSize),100),0)
    sys.stdout.write("\r" + filename + "...%d%%" % percent)
    sys.stdout.flush()

def git_download(url):
    base='https://codeload.github.com'
    archive='zip'
    m=extract_git_id(url)
    if m:
        g=m.groupdict()
        if not g['branch']:
            g['branch']='master'

        u=   '/'.join((base,g['user'],g['repo'],archive, g['branch']))
        #print u
        try:
            with tempfile.NamedTemporaryFile(mode='w+b',suffix='.zip') as f:
                urllib.urlretrieve(u,f.name,reporthook=functools.partial(dlProgress,u))
                z=zipfile.ZipFile(f)
                z.extractall()
                print z.namelist()
        except:
            print('git url did not return zip file')
    else:
        print('could not determine repo url from clipboard or argv')
        
if __name__=='__main__':
    git_download_from_args(sys.argv)
