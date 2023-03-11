while True:
    RES = input('Téorema(1) ou Réciproque(2): ')

    if RES == '1':
            X1: float = float(input('Côté opposé: '))
            X2 = float(input('côté adjacent: '))

            P0 = (X2 ** 2 + X1 ** 2) ** (1 / 2)

            print("....................................................")

            print("O valor da hypoténuse é: {}".format(P0))

    elif RES == '2':

            X1: float = float(input('Côté opposé: '))
            X2 = float(input('hypoténuse: '))

            P0 = (X2 ** 2 - X1 ** 2) ** (1/2)

            print("....................................................")

            print("La valeur de l'hypoténuse est: {}".format(P0))

    else:
            Souo = str(input('réponse invalide voulez-vous réessayer (O/N)'))
            if Souo =='O':
                    continue
            elif Souo =='N':
                    break
            else:
                    print("option invalide!")

