from ftplib import FTP
import os
import fileinput
import smtplib
from os.path import exists as file_exists

varvente = input("Quel a été votre bénéfice ce mois-ci")

ventefile = open("vente.txt", "w")
ventefile.write(f"{varvente}")
ventefile.close()
print("Fichier bien sauvegardé.")

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('<host>', 21) 
ftp.login('<username>','<password>')
ftp.cwd('/<path>')
fp = open("./<file name>", 'rb')
ftp.storbinary('STOR %s' % os.path.basename("./<file name>"), fp, 1024)
fp.close()

ftp.quit()

content = varvente
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
sender = '<mail post address>'
recipient = '<send mail address>'
mail.login('<send mail address>','<password>')
header='To:'+receipient+'\n'+'From:'\
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender,recipient, content)
mail.close()
