while True:
    a = print("""
      **   *******       **      ********
     /**  **/////**     ****    **////// 
     /** **     //**   **//**  /**       
     /**/**      /**  **  //** /*********
     /**/**      /** **********////////**
 **  /**//**     ** /**//////**       /**
//*****  //*******  /**     /** ******** 
 /////    ///////   //      // ////////  
    """)
    print(a)
    print("Bem vindo a Ferramenta de Stalk Facebook v1.0")
    print("Para o uso da ferramenta só coloque o link do perfil, /numerodoperfil")
    print("\n1 - Posts Curtidos \n2 - Fotos Comentadas\n3 - Videos Comentados")
    menu = input("Digite a opção desejada: ")
    if menu == "1":
        print("Posts curtidos")
        foto = input("Digite o número do perfil: ")
        print(f"https://www.facebook.com/search/{foto}/stories-liked?epa=SEARCH_BOX")
    if menu == "2":
        print("Comentários de fotos")
        comentario = input("Digite o número do perfil: ")
        print(f"https://www.facebook.com/search/{comentario}/photos-commented/")
    if menu == "3":
        print("Comentários de videos")
        videos = input("Digite o número do perfil: ")
        print(f"https://www.facebook.com/search/{videos}/videos-commented/")