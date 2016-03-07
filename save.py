import os

for root,dirs,files in os.walk("./init/"):
  for ffile in files:
    if ffile.endswith(".html"):
      if root[-1] != '/':
        root += '/'
      f = open(root+ffile, 'r+')
      text = f.read()
      new_root = '.' + root[6:]
      text = text.replace(r'''../index.html''',r"""javascript:localStorage.setItem('mypage','"""+new_root+ffile+"""');""")
      text = text.replace(r'index.html',r'javascript:if (localStorage.mypage != undefined){window.location.href=localStorage.mypage};')
      f.seek(0)
      f.write(text)
      f.truncate()
      f.close()