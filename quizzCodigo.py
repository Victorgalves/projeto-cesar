quant=aprenderam=alunos=c=escolaInicio=escolaFim=0
alunos=int(input("Quantidade de alunos: "))
## antes do jogo
while c<alunos:
    contInicio=contFim=0
    print(f"\nAluno {c+1}")
    print("\nQuizz sobre o manguebeat")

    while True:
        ans1=input("\nVocê sabe quem foi chico science? [S/N]\n").upper()
        if ans1=="S":
            contInicio+=1
            break
        elif ans1=="N":
            break
        else:
            print("Resposta inválida!, digite 'S' para sim ou 'N' para não.")
            continue

    while True:
        ans2=input("Você já ouviu falar no manguebeat? [S/N]\n").upper()
        if ans2=="S":
            contInicio+=1
            break
        elif ans2=="N":
            break
        else:
            print("Resposta inválida!, digite 'S' para sim ou 'N' para não.")
            continue

    while True:
        ans3=input("Já viu algo sobre chico science ou o manguebeat na escola? [S/N]\n").upper()
        if ans3=="S":
            escolaInicio+=1
            break
        elif ans3=="N":
            break
        else:
            print("Resposta inválida!, digite 'S' para sim ou 'N' para não. ")
            continue

    print("Respostas registradas. Obrigado. Bom jogo!")
    quant+=1

    ## depois do jogo

    print("\nObrigado por jogar!\n")
    contFim=0
    print("Feedback\n")

    while True:
        ans4=input("Depois de jogar o jogo, você agora sabe mais sobre quem foi chico science? [S/N]\n").upper()
        if ans4=="S":
            contFim+=1
            break
        elif ans4=="N":
            break
        else:
            print("Resposta inválida!, digite 'S' para sim ou 'N' para não. ")
            continue

    while True:
        ans5=input("E agora sabe mais sobre o que foi o movimento manguebeat? [S/N]\n").upper()
        if ans5=="S":
            contFim+=1
            break
        elif ans5=="N":
            break
        else:
            print("Resposta inválida!, digite 'S' para sim ou 'N' para não. ")
            continue

    while True:
        ans6=input("Gostaria de aprender mais sobre isso na escola? [S/N]\n").upper()
        if ans6=="S":
            escolaFim+=1
            break
        elif ans6=="N":
            break
        else:
            print("Resposta inválida!, digite 'S' para sim ou 'N' para não. ")
            continue

    if contInicio<=contFim:
        aprenderam+=1
    c+=1
print(f"\nDe {quant} alunos que jogaram, {aprenderam} conseguiram adquirir ou aumentar o seu conhecimento sobre o movimento")
print(f"\n{escolaInicio} alunos ouviram falar sobre na escola, {escolaFim} afirmam que gostariam de aprender mais sobre")