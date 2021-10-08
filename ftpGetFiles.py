from ftplib import FTP
import os

class FTPDownloadFiles :

  __ftpClient = None

  def __init__(self, ftpUrl) -> None:
      self.__ftpUrl = ftpUrl

  def Login(self, user, password) :
     try:
      self.__ftpClient  = FTP(self.__ftpUrl) 

      resultLogin = self.__ftpClient.login(user, password)# Efetuo o login e verifico.
      
      if resultLogin[0:3] != "230" :
        raise ValueError("Usuário ou senha incorreto.")

      return True
     except Exception as e:
      print('Ocorreu um erro durante o download dos seus arquivo.')
      print(e)
      return False

  def DownloadFiles(self, pathFtp, pathLocal, fileMatch = '*.*') -> bool:
    """
    Função responsavel por baixar arquivos de FTP
    :param ftpUrl: str
    :param user: str
    :param password: str
    :param pathFtp: str (exemplo: /public_html)
    :param pathLocal: str (exemplo: c:\\temp)
    :param fileMatch: str = '*.*'
    :return bool
    """
    try:
      
      resultChangPathFtp = self.__ftpClient.cwd(pathFtp); #Chamo a função de troca de diretório e pego retorno
      if resultChangPathFtp[0:3] != "250" : #Caso o retorno venha código diferente de 250, forço erro 
        raise ValueError("Diretório do FTP incorreto.")

      self.__ftpClient.encoding = "utf-8"
      downloaded = []
      skipped = 0

      for filename in self.__ftpClient.nlst(fileMatch): #Loop para buscar todos os arquivo que batem com o fileMatch informado
          if  filename not in downloaded: #Verifico se o arquivo já está no array de arquivos baixados
              fhandle = open(os.path.join(pathLocal,filename), 'wb') #Crio um handle do para escrever o arquivo físico na maquina
              print('Iniciando download do arquivo ' + filename)
              self.__ftpClient.retrbinary('RETR ' + filename, fhandle.write) #Passo o handle do arquivo para que o FTP possa fazer o download e savar no arquivo local
              fhandle.close() #Fecho o arquivo local
              downloaded.append(filename) #Adiciono o arquivo baixado no array
          else:
              skipped += 1 #Se por acaso o arquivo já estiver na lista de download não baixo novamente

      print('Baixados %s, não baixados %d arquivos' % (len(downloaded), skipped))
      return True
    except Exception as e:
      print('Ocorreu um erro durante o download dos seus arquivo.')
      print(e)
      return False
    finally:
      if self.__ftpClient != None :
        self.__ftpClient.quit()  


