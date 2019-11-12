import pymysql
import cv2
import subprocess as sp
import time

# ========= Parametros ========= #
TIME = 2
#cap = cv2.VideoCapture(0)
nomeBanco = 'nomeBanco'
usuarioBanco = 'usuario'
senhaBanco = 'senha'
ipBanco = '127.0.0.1'

# ============================== #

class BancoDeDados():
        '''Comunicacao com o banco de dados'''

        def __init__(self, nomeBanco, usuarioBanco, senhaBanco, ipBanco):

                self.nomeBanco = nomeBanco
                self.usuarioBanco = usuarioBanco
                self.senhaBanco = senhaBanco
                self.ipBanco = ipBanco


        def inserirPlaca(self, placa):
                '''Insere uma placa no banco'''
                conexao = pymysql.connect(host=self.ipBanco, db=self.nomeBanco, user=self.usuarioBanco, passwd=self.senhaBanco)
                cursor = conexao.cursor()
                #cursor.execute("insert into entradas (placa, hora) values ('{}', current_time)".format(placa))
                cursor.execute("insert into saidas (placa, hora) values ('{}', current_time)".format(placa))
                conexao.commit()
                conexao.close()


        def atualizarStatus(self, placa, status):
                '''Atualiza um o status de uma placa do banco'''
                conexao = pymysql.connect(host=self.ipBanco, db=self.nomeBanco, user=self.usuarioBanco, passwd=self.senhaBanco)
                cursor = conexao.cursor()
                cursor.execute("update placas set hora = CURRENT_TIME, status = {} where placas.placa = '{}'".format(status, placa))
                conexao.commit()
                conexao.close()

        def verificaPlaca(self, placa):
                '''Verifica uma placa no banco de dados'''
                conexao = pymysql.connect(host=self.ipBanco, db=self.nomeBanco, user=self.usuarioBanco, passwd=self.senhaBanco)
                cursor = conexao.cursor()
                #existe = cursor.execute("select en.placa from entradas as en where en.placa = '{}'".format(placa))
                existe = cursor.execute("select en.placa from saidas as en where en.placa = '{}'".format(placa))
                conexao.close()
                if existe == 1:
                        return True
                else:
                        return False


def foto():

        cap = cv2.VideoCapture(0)
        ret, foto = cap.read()
        cv2.imwrite('images/teste.png', foto)


def detectar_placa():

        out = sp.Popen('alpr -c eu images/teste.png', shell=True, stdout=sp.PIPE)
        stdout = out.communicate()[0]
        stdout = stdout.decode('utf-8')
        db = BancoDeDados(nomeBanco, usuarioBanco, senhaBanco, ipBanco)
        try:
                for placa in range(4, 13, 4):
                        if (len(stdout.split()[placa]) == 7):
                                print(stdout.split()[placa])
                                existe = db.verificaPlaca(stdout.split()[placa])
                                if existe == True:
                                        print('Placa ja cadastrada')
                                        break
                                else:
                                        db.inserirPlaca(stdout.split()[placa])
                                        print("placa inserida")
                                        break
                        else:
                                print('placa nao detectada 2')
        except:
                print('placa nao detectada')



def main():
        #foto()
        #detectar_placa()
        teste = 0
        if teste == 0:
                while True:

                        foto()
                        detectar_placa()
                        time.sleep(TIME)
                        if cv2.waitKey(1) == 27:
                                break
                cv2.destroyAllWindows()

        detectar_placa()

if __name__ == '__main__':
        main()
