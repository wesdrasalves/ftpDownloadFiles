# Download arquivos FTP Python 🐍 

&nbsp;&nbsp;Class de acesso ao FTP básica, com funções de autenticação e método de download somente de arquivos em um diretório informado.
<br/><br/>
### 🚀 Como usar 
___
<br/>

&nbsp;&nbsp;Baixe o arquivo ftpGetFiles.py no seu diretório e use o código abaixo e pronto. ✨ 
<br/><br/>

```
import ftpGetFiles 

#Chamo a class de download de arquivos passando o caminho
ftp = ftpGetFiles.FTPDownloadFiles('ftp.meuftp.com')

#Chamo o Login para validar se usuário e senha estão corretos
if ftp.Login('user','password') :
  #Inicio o Download dos arquivos
  ftp.DownloadFiles('/public_html','C:\\temp\\ftp')

 ```
