import uuid
import os



os.system('git add .')
os.system('git commit -m "d"')
os.system('git tag submit-'+str(uuid.uuid4())+' -m " "')
os.system('git push --follow-tags')
