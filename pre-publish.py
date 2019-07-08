import requests, zipfile, platform, subprocess, os, StringIO, shutil

class FileInfo(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

def download(url, files):
	print (url)
	result = requests.get(url, stream=True)
	zip = zipfile.ZipFile(StringIO.StringIO(result.content))
	tmp_dir = "./tmp"
	if not os.path.exists(tmp_dir):
		os.makedirs(tmp_dir)
	zip.extractall(tmp_dir)
	for file in files:
		shutil.copyfile(tmp_dir+ "/"+ file.src, file.dest)

def main():
	print("Downloading LexActivator library ...")

	base_url = 'https://dl.cryptlex.com/downloads/'
	base_path = './cryptlex/lexactivator/libs'
	version = 'v3.7.1'

	files = [FileInfo('libs/clang/x86_64/libLexActivator.dylib', base_path + '/macos/x86_64/libLexActivator.dylib')]
	url = '/LexActivator-Mac.zip'
	download(base_url + version + url, files)

	files = [
		FileInfo('libs/vc14/x86/LexActivator.dll', base_path + '/win32/x86/LexActivator.dll'),
		FileInfo('libs/vc14/x64/LexActivator.dll', base_path + '/win32/x86_64/LexActivator.dll')
	]
	url = '/LexActivator-Win.zip'
	download(base_url + version + url, files)

	files = [
		FileInfo('libs/gcc/amd64/libLexActivator.so', base_path + '/linux/gcc/x86_64/libLexActivator.so'),
		FileInfo('libs/gcc/i386/libLexActivator.so', base_path + '/linux/gcc/x86/libLexActivator.so'),
		FileInfo('libs/musl/amd64/libLexActivator.so', base_path + '/linux/musl/x86_64/libLexActivator.so'),
	]
	url = '/LexActivator-Linux.zip'	
	download(base_url + version + url, files)

	print("Lexactivator library successfully downloaded!")

main()