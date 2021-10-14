import os
import platform


def get_md5(file_path):
    sys = platform.platform()
    if sys.find("indows") > 0:
        md5 = os.popen("certutil -hashfile " + file_path + " MD5").readlines()[1].rstrip()
    else:
        md5 = os.popen("md5sum " + file_path).readlines()[0].split()[0]
    return md5


def get_string_md5(string_body):
    cmd = 'echo -n {}| md5sum'.format(string_body)
    md5 = os.popen(cmd).readlines()[0].split()[0]
    return md5
