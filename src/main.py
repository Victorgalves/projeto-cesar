import Cadastro.cadastro as c
import Quizz.quizz as q

cadastro= c.Cadastro()
quizz=q.Quizz()

opcoes={
    'Cadastro':{
        cadastro.criar_cadastroProf(),
        cadastro.cadastro_turma(),
    },
    'Quizz':{
        quizz.quizz_inicial(),
    }
}