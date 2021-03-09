#!/usr/bin/python3

import shutil, os, cgi, subprocess, cgitb, time
cgitb.enable()
fs = cgi.FieldStorage()
fileitem = fs['flag1']
fileitem2 = fs['flag2']

print("Content-type: text/html")
print("\n")
print("<html>")
print("Please do not attempt to hack the CGI - this is NOT part of the challenge.<br>")

folder = str(time.time())


if not os.path.exists('/tmp/' + folder):
    try:
        os.makedirs('/tmp/' + folder)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            os.exit()


# Test if the file was uploaded
if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + folder + '/file1', 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
else:
    message = 'No file was uploaded'
    print(message)
    os.exit()

if fileitem2.filename:
    fn = os.path.basename(fileitem2.filename)
    open('/tmp/' + folder + '/file2', 'wb').write(fileitem2.file.read())
else:
    message1 = 'No file was uploaded'
    print(message1)
    os.exit()


args = ("/ctfbin/crackme_flag",'/tmp/' + folder + '/file1', '/tmp/' + folder + '/file2')
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()

#shutil.rmtree('/tmp/' + folder)

print(output.decode("utf-8"))

print("</html>")
