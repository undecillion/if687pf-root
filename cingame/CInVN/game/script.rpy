
define a = Character("Aluno", color="#8e9aaf")
define p = Character("Personal Support Daemon", color="#e71d34", voice_tag="personalsd")
image bg entrance = "images/entrance.jpg"
image bg classroom = "images/sala1.jpg"
image bg ccensaida = "images/ccensaida.jpg"
image bg hallway1 = "images/hallway1.jpg"
image bg hallway2 = "images/hallway2.jpg"
image bg openarea = "images/openarea.jpg"
image bg garden1 = "images/garden1.jpg"
image bg bedroom = "images/bedroom.jpg"
image bg bibliot = "images/bibliot.jpg"
image bg sala2 = "images/sala2.jpg"
image bg copa1 = "images/copa1.jpg"
image bg roam = "images/roam.jpg"
image bg garden1 = "images/garden1.jpg"
image bg desolate = "images/desolate.jpg"

label start:

    scene bg entrance

    a "Oi, ouvi dizer que preciso de um crachá para acessar certas áreas aqui no CIn. Você pode me ajudar com isso?"

    show sprite_psd_01_reduced at truecenter
    with dissolve

    voice "voices/cena1/voice_line_0_cena1.wav"
    p "Claro! Vamos por partes, para a primeira via e para as demais vias do seu crachá, os processos são um pouco diferentes."

    voice "voices/cena1/voice_line_1_cena1.wav"
    p "Para a {b}{i}{color=#f00}primeira via{/color}{/i}{/b} do crachá:"

    voice "voices/cena1/voice_line_2_cena1.wav"
    p "{size=-7}{b}Envio de Foto:{/b} Você deve enviar para o e-mail cracha@cin.ufpe.br uma foto de rosto com fundo claro. É importante que a foto esteja numa proporção de 3:4 para evitar distorções na impressão. O arquivo da foto deve ser nomeado seguindo o formato \"pessoa_CPF.jpg\", com o CPF contendo apenas dígitos.{/size}"

    voice "voices/cena1/voice_line_3_cena1.wav"
    p "{size=-5}{b}Aguardar E-mail de Confirmação:{/b} depois de enviar a foto, você receberá um e-mail informando que o crachá foi emitido.{/size}"

    voice "voices/cena1/voice_line_4_cena1.wav"
    p "{size=-5}{b}Retirada:{/b} com o e-mail de confirmação em mãos, vá até a Secretaria de Graduação com um documento oficial com foto para retirar seu crachá.{/size}"

    voice "voices/cena1/voice_line_5_cena1.wav"
    p "Para a emissão da {b}{i}{color=#f00}2ª via{/color}{/i}{/b} ou {b}{i}{color=#f00}demais{/color}{/i}{/b} vias:"

    voice "voices/cena1/voice_line_6_cena1.wav"
    p "{size=-5}{b}Formulário:{/b} primeiro, baixe o formulário de solicitação de remissão de crachá e termo de responsabilidade disponível online.{/size}"

    voice "voices/cena1/voice_line_7_cena1.wav"
    p "{size=-5}{b}Preenchimento:{/b} preencha o formulário corretamente, date e assine.{/size}"

    voice "voices/cena1/voice_line_8_cena1.wav"
    p "{size=-5}{b}Envio do Formulário:{/b} escaneie o formulário preenchido e envie-o para cracha2via@cin.ufpe.br.{/size}"

    voice "voices/cena1/voice_line_9_cena1.wav"
    p "{size=-5}{b}Aguardar E-mail de Confirmação:{/b} assim como na primeira via, você receberá um e-mail informando que o crachá foi emitido.{/size}"

    voice "voices/cena1/voice_line_10_cena1.wav"
    p "{size=-5}{b}Retirada:{/b} Com o e-mail de confirmação, vá até a Secretaria de Graduação para retirar seu crachá.{/size}"

    voice "voices/cena1/voice_line_11_cena1.wav"
    p "É essencial garantir que os dados preenchidos no formulário estejam legíveis e corretos, especialmente seus dados pessoais como nome, CPF, login e vínculo. Isso facilitará o processo e evitará atrasos na emissão do seu crachá."

    a "Obrigado! Isso parece simples. Vou começar o processo agora mesmo."

    voice "voices/cena1/voice_line_12_cena1.wav"
    "Sem problemas! Se precisar de mais alguma coisa ou tiver dúvidas, estou aqui para ajudar. Boa sorte com a sua jornada aqui no CIn!"

    hide sprite_psd_01_reduced with dissolve


    jump classroomscene

    # This ends the game.

label classroomscene:

    scene bg classroom with fade

    a "Eu estive pensndo em como os softwares e ferramentas são importantes para o nosso aprendizado e projetos. Existe algum apoio do CIn nesse aspecto?"

    show sprite_psd_01_reduced at truecenter
    with dissolve

    voice "voices/cena2/voice_line_0_cena2.wav"
    p "Com certeza! O CIn, em parceria com várias empresas que apoiam a educação na área de computação, oferece diversos descontos e acessos gratuitos a softwares e plataformas essenciais. Vamos ver o que temos disponível..."

    voice "voices/cena2/voice_line_1_cena2.wav"
    "{size=-5}{color=#f09}GitHub Education:{/color} uma iniciativa do GitHub que oferece o Student Developer Pack, dando acesso ilimitado a mais de 20 ferramentas de programação, além de repositórios privados ilimitados no GitHub até você se formar.{/size}"

    voice "voices/cena2/voice_line_2_cena2.wav"
    "{size=-5}{color=#f09}JetBrains:{/color} disponibiliza o All Products Pack gratuitamente para estudantes, incluindo licenças para todas as IDEs da empresa, como IntelliJ IDEA Ultimate, CLion e PyCharm Professional.{/size}"

    voice "voices/cena2/voice_line_3_cena2.wav"
    "{size=-5}{color=#f09}Microsoft Azure Dev Tools:{/color} em parceria com a Microsoft, oferecemos através da plataforma Microsoft Azure acesso a uma grande seleção de softwares da Microsoft, como Windows 10, Windows Server e Visual Studio, sem custos normalmente associados.{/size}"

    voice "voices/cena2/voice_line_4_cena2.wav"
    "{size=-5}{color=#f09}InVision:{/color} plataforma de design de produto digital oferece ferramentas intuitivas para criação de ideias, design, protótipos e gerenciamento de design. Com um cadastro simples, você tem acesso à versão educacional da plataforma.{/size}"

    voice "voices/cena2/voice_line_5_cena2.wav"
    "{size=-8}{color=#f09}Dell e Apple:{/color} oferecem descontos em notebooks e outros equipamentos. Para a Dell, os descontos variam conforme o valor da compra e podem ser cumulativos às promoções do site. Para a Apple, há preços especiais em Macs, iPads e acessórios para o público acadêmico, com descontos que variam de 2\% a 3\%.{/size}"

    a "Isso é incrível! Vai ajudar muito durante a graduação."

    voice "voices/cena2/voice_line_6_cena2.wav"
    p "Exatamente! Essas parcerias são uma ótima maneira de acessar recursos que podem fazer uma grande diferença na sua educação e projetos. Não esqueça de aproveitar essas oportunidades."

    ## [O aluno acena, parecendo motivado e pronto para explorar os recursos disponíveis.]

    a "Obrigado por me informar sobre isso. Vou verificar cada uma dessas opções."

    voice "voices/cena2/voice_line_7_cena2.wav"
    p "Sempre à disposição para ajudar! Se tiver mais dúvidas ou precisar de mais informações, é só chamar."

    hide sprite_psd_01_reduced with dissolve

    #? Este diálogo detalhado explora a opção 2 sobre descontos acadêmicos, fornecendo informações específicas sobre os recursos disponíveis para os alunos do CIn, conforme descrito no manual.

    jump libraryscene

label libraryscene:

    scene bg bibliot with fade

    a "Estou tentando entender como funciona o SIGAA para gerenciar meus estudos e matrículas. Você pode me ajudar?"

    show sprite_psd_01_reduced at truecenter
    with dissolve

    voice "voices/cena3/voice_line_0_cena3.wav"
    p "Claro! O SIGAA é o Sistema de Informações e Gestão Acadêmica da UFPE, um portal essencial para a sua jornada acadêmica. Ele gerencia desde sua matrícula até o acompanhamento do seu progresso. Vou te guiar pelas funcionalidades principais."

    voice "voices/cena3/voice_line_1_cena3.wav"
    p "Em relação ao {b}{i}{color=#f00}primeiro acesso:{/color}{/i}{/b}"

    voice "voices/cena3/voice_line_2_cena3.wav"
    "{size=-5}Acesse o site do SIGAA: acesse o site sigaa.ufpe.br e clique em \"Login\" e subsequentemente \"Cadastre-se\".{/size}"
    voice "voices/cena3/voice_line_3_cena3.wav"
    "{size=-5}Preencha o Formulário: preencha o formulário com seus dados pessoais. O cadastro só será validado se os dados digitados forem iguais aos dados informados no processo seletivo.{/size}"

    voice "voices/cena3/voice_line_4_cena3.wav"
    p "Após o cadastro, você terá acesso a diversas funcionalidades, como:"

    voice "voices/cena3/voice_line_5_cena3.wav"
    p "{size=-5}{color=#f99}Matrícula:{/color} você pode realizar sua matrícula em disciplinas, consultar o histórico escolar e visualizar o plano de ensino das disciplinas.{/size}"

    voice "voices/cena3/voice_line_6_cena3.wav"
    p "{size=-5}{color=#f99}Acompanhamento:{/color} você pode acompanhar o seu desempenho acadêmico, consultar o calendário acadêmico e visualizar o seu plano de estudos.{/size}"

    voice "voices/cena3/voice_line_7_cena3.wav"
    p "{size=-5}{color=#f99}Documentos:{/color} você pode acessar documentos importantes, bem como solicitar suas emissões.{/size}"
    voice "voices/cena3/voice_line_8_cena3.wav"
    p "Além disso, o SIGAA é uma ferramenta essencial para a comunicação entre alunos e professores, pois é por meio dele que você terá acesso a informações sobre eventos, notícias e comunicados."

    voice "voices/cena3/voice_line_9_cena3.wav"
    p "Alguns detalhes sobre o SIGAA que podem ser úteis:"

    voice "voices/cena3/voice_line_10_cena3.wav"
    p "{size=-5}Se você for um aluno blocado (cumprindo o currículo dentro do prazo esperado), o SIGAA montará automaticamente sua grade horária com as disciplinas obrigatórias do seu período atual. Confirmar essa grade significa que sua matrícula nesses componentes está assegurada.{/size}"

    voice "voices/cena3/voice_line_11_cena3.wav"
    p "{size=-5}Para alunos não blocados, o sistema tenta montar uma grade horária com disciplinas pendentes, mas você competirá (em prioridade) por vagas com outros alunos, o que significa que sua matrícula pode ou não ser confirmada, dependendo da disponibilidade.{/size}"

    voice "voices/cena3/voice_line_12_cena3.wav"
    p "{size=-5}O aluno também é livre para montar sua grade horária manualmente, escolhendo disciplinas e horários de acordo com sua preferência e disponibilidade.{/size}"

    voice "voices/cena3/voice_line_13_cena3.wav"
    p "{size=-8}A prioridade é determinada pela sua situação acadêmica e ranking. Alunos concluintes blocados têm a maior prioridade, seguidos por alunos blocados, concluintes não blocados, e, por último, alunos não blocados. Em caso de empate, prevalece o aluno com maior ranking.{/size}"

    voice "voices/cena3/voice_line_14_cena3.wav"
    p "Após o período de matrícula inicial, você entra no período de modificação, onde pode adicionar ou cancelar disciplinas conforme necessário."

    a "Entendi! Parece ser uma ferramenta muito útil para o meu dia a dia."

    voice "voices/cena3/voice_line_15_cena3.wav"
    p "Lembre-se de que o SIGAA é uma ferramenta poderosa para gerenciar sua vida acadêmica, então explore-o e familiarize-se com suas funcionalidades. Se tiver mais dúvidas, estou aqui para ajudar!"

    hide sprite_psd_01_reduced with dissolve

    #? Essa resposta detalhada abrange a funcionalidade e o uso do SIG@, seguindo as informações fornecidas, para garantir que o aluno tenha uma compreensão clara de como navegar e utilizar o sistema efetivamente.

    jump frarea

label frarea:

    scene bg openarea with fade

    a "Estou pensando em onde almoçar hoje. Você sabe se tem algum lugar para comer aqui no CIn?"

    show sprite_psd_01_reduced at truecenter
    with dissolve

    voice "voices/cena4/voice_line_0_cena4.wav"
    p "Na verdade, o CIn não possui lanchonetes ou restaurantes internamente. Mas não se preocupe, há opções próximas para você explorar!"

    voice "voices/cena4/voice_line_1_cena4.wav"
    "{b}{color=#00a188}Almir Refeições{/color}{/b} oferece refeições completas e variadas. Você pode conferir o menu do dia e fazer pedidos pelo WhatsApp. O contato é (81) 99568-6578."

    voice "voices/cena4/voice_line_2_cena4.wav"
    "Conhecido pelos seus salgados variados e refeições rápidas, {b}{color=#aa001e}Marcelinho dos Salgados{/color}{/b} é uma ótima escolha para um lanche entre as aulas."

    voice "voices/cena4/voice_line_3_cena4.wav"
    "Para mais informações, acesse {a=https://www.salgadoscin.com.br/}Marcelinho dos Salgados{/a}."

    voice "voices/cena4/voice_line_4_cena4.wav"
    p "Além dessas opções, algumas dicas..."

    voice "voices/cena4/voice_line_5_cena4.wav"
    p "Cantina da Área II e Restaurante da ASSIF: São locais próximos para almoço, oferecendo uma variedade de pratos a preços acessíveis."

    voice "voices/cena4/voice_line_6_cena4.wav"
    p "Existem várias lanchonetes e restaurantes dentro e nos arredores da universidade. Vale a pena explorar e encontrar seus favoritos."

    voice "voices/cena4/voice_line_7_cena4.wav"
    p "{size=-6}Considere o uso de delivery para receber suas refeições no CIn. Algumas plataformas de entrega, como o iFood, entregam no CIn. Para endereço de entrega, use {color=#c9f}\"Av. Jornalista Aníbal Fernandes, 500 - Cidade Universitária, CEP 50740-560\"{/color}, indicando o Centro de Informática como ponto de referência.{/size}"

    a "Ótimas sugestões! Vou experimentar uma dessas opções hoje. Obrigado!"

    voice "voices/cena4/voice_line_8_cena4.wav"
    p "De nada! Se tiver mais alguma dúvida ou precisar de sugestões, estou aqui para ajudar. Bom apetite!"

    hide sprite_psd_01_reduced with dissolve

    #? Este diálogo aborda a opção de alimentação, detalhando as principais alternativas disponíveis para os alunos do Centro de Informática da UFPE, conforme as informações do manual.

    jump blocosscene

label blocosscene:

    scene bg garden1 with fade

    a "Estou um pouco perdido. Preciso encontrar algumas salas, mas não sei por onde começar."

    show sprite_psd_01_reduced at truecenter
    with dissolve

    voice "voices/cena5/voice_line_0_cena5.wav"
    p "Sem problemas! O CIn é dividido em blocos, cada um com suas próprias salas e laboratórios. Vou te dar uma visão geral."

    voice "voices/cena5/voice_line_1_cena5.wav"
    p "Blocos A, B e C - O Prédio Vermelho"

    voice "voices/cena5/voice_line_2_cena5.wav"
    p "Térreo: Aqui você encontra principalmente laboratórios e algumas salas administrativas. É um bom ponto de referência para começar a explorar o CIn."

    voice "voices/cena5/voice_line_3_cena5.wav"
    p "1º andar: Este andar abriga mais laboratórios de pesquisa e salas de professores. Se você está procurando por um professor específico, é provável que a sala dele esteja aqui."

    voice "voices/cena5/voice_line_4_cena5.wav"
    p "2º andar: Similar ao primeiro, com salas de professores e alguns laboratórios. É aqui que muitas reuniões acadêmicas acontecem."

    voice "voices/cena5/voice_line_5_cena5.wav"
    p "Bloco D - Parte do CCEN"

    voice "voices/cena5/voice_line_6_cena5.wav"
    p "Este bloco é um pouco separado dos demais e tem uma conexão direta com o Centro de Ciências Exatas e da Natureza (CCEN). Geralmente, é utilizado para aulas teóricas de matemática e estatística."

    voice "voices/cena5/voice_line_7_cena5.wav"
    p "Bloco E - O Prédio Branco"

    voice "voices/cena5/voice_line_8_cena5.wav"
    p "Térreo e Mezanino: O térreo tem algumas salas de aula grandes e laboratórios de ensino. O mezanino é um espaço aberto para estudos e projetos."

    voice "voices/cena5/voice_line_9_cena5.wav"
    p "1º, 2º, 3º e 4º andares: Esses andares possuem uma mistura de salas de aula, laboratórios de pesquisa e espaços de estudo."

    voice "voices/cena5/voice_line_10_cena5.wav"
    p "O 4º andar é particularmente conhecido pelos seus laboratórios de pesquisa avançada."


    a "E como eu faço para saber onde cada sala ou laboratório está localizado?"

    voice "voices/cena5/voice_line_11_cena5.wav"
    p "No site do CIn, você pode encontrar mapas detalhados de cada bloco e andar. Esses mapas te darão uma visão clara de onde tudo está localizado. Além disso, sempre há placas informativas espalhadas pelos corredores."

    a "Isso vai ser muito útil, obrigado!"

    voice "voices/cena5/voice_line_12_cena5.wav"
    p "De nada! E lembre-se, se você se perder, não hesite em perguntar. Todos aqui estão dispostos a ajudar."

    hide sprite_psd_01_reduced with dissolve

    jump oarea

label oarea:

    scene bg sala2 with fade

    a "Ouvi dizer que o CIn é cheio de oportunidades além das aulas. O que você pode me dizer sobre isso?"

    show sprite_psd_01_reduced at truecenter with dissolve

    voice "voices/cena6/voice_line_0_cena6.wav"
    p "Sim, o CIn é um centro de excelência que oferece várias oportunidades para expandir seus conhecimentos e habilidades. Vamos detalhar algumas delas..."

    voice "voices/cena6/voice_line_1_cena6.wav"
    p "{size=-3}{b}{color=#00a188}PET-Informática{/color}{/b}{/size}"

    voice "voices/cena6/voice_line_2_cena6.wav"
    p "{size=-3}O que é:\n Programa de Educação Tutorial financiado pela SESu/MEC, visando a melhoria do ensino de graduação e a formação ampla do aluno através de ensino, pesquisa e extensão.{/size}"

    voice "voices/cena6/voice_line_3_cena6.wav"
    p "{size=-3}Atividades:\n Olimpíada Pernambucana de Informática, Curso de Férias em Python, CIn Salva Vidas em parceria com o HEMOPE, HackaPET, SharePET para workshops, e manutenção da CInWiki e do Manual de Sobrevivência.{/size}"

    voice "voices/cena6/voice_line_4_cena6.wav"
    p "{size=-3}Como participar:\nO processo seletivo ocorre anualmente e inclui análise de currículo, entrevistas e dinâmicas em grupo. Monitoria e Iniciação Científica são valorizadas, mas não obrigatórias.{/size}"

    voice "voices/cena6/voice_line_5_cena6.wav"
    p "{size=-3}{b}{color=#00a188}Maratona de Programação{/color}{/b}{/size}"

    voice "voices/cena6/voice_line_6_cena6.wav"
    p "{size=-3}Descrição:\nCompetição de programação que desafia os alunos a resolver problemas complexos no menor tempo possível. O CIn tem um histórico de excelência na maratona, com múltiplos títulos regionais e participações em mundiais.{/size}"

    voice "voices/cena6/voice_line_7_cena6.wav"
    p "{size=-3}Benefícios:\nDesenvolve habilidades em lógica, programação e trabalho em equipe. É uma grande porta de entrada para o mercado de trabalho na área de tecnologia.{/size}"

    voice "voices/cena6/voice_line_8_cena6.wav"
    p "{size=-3}{b}{color=#00a188}Voxar Labs{/color}{/b}{/size}"

    voice "voices/cena6/voice_line_9_cena6.wav"
    p "{size=-3}Foco:\nPesquisa em realidade aumentada, realidade virtual, computação gráfica e inteligência artificial. Envolve projetos com cooperação internacional e com a indústria.{/size}"

    voice "voices/cena6/voice_line_10_cena6.wav"
    p "{size=-3}Oportunidades:\nIdeal para quem tem interesse em pesquisa aplicada e desenvolvimento de novas tecnologias.{/size}"

    voice "voices/cena6/voice_line_11_cena6.wav"
    p "{size=-3}{b}{color=#00a188}Apple Developer Academy{/color}{/b}{/size}"

    voice "voices/cena6/voice_line_12_cena6.wav"
    p "{size=-3}O que é:\nCentro de treinamento em parceria com a Apple, oferecendo formação interdisciplinar em desenvolvimento para iOS, watchOS e tvOS.{/size}"

    voice "voices/cena6/voice_line_13_cena6.wav"
    p "{size=-3}Para quem:\nAberto a estudantes de qualquer curso da UFPE, é uma excelente oportunidade para aprender a resolver problemas reais usando tecnologia.{/size}"

    voice "voices/cena6/voice_line_14_cena6.wav"
    p "{size=-3}{b}{color=#00a188}E.S.T.U.F.A.{/color}{/b}{/size}"

    voice "voices/cena6/voice_line_15_cena6.wav"
    p "{size=-3}Descrição:\nFoco em sistemas embarcados, oferecendo um ambiente colaborativo para desenvolvimento de projetos e pesquisa aplicada.{/size}"

    voice "voices/cena6/voice_line_16_cena6.wav"
    p "{size=-3}Como participar:\nAcompanhe chamadas para projetos e desenvolvedores, principalmente via Instagram.{/size}"

    voice "voices/cena6/voice_line_17_cena6.wav"
    p "{size=-3}{b}{color=#00a188}RobôCIn{/color}{/b}{/size}"

    voice "voices/cena6/voice_line_18_cena6.wav"
    p "{size=-3}Áreas:\nInteligência Artificial, Visão Computacional, Mecânica e Eletrônica aplicada à robótica.{/size}"

    voice "voices/cena6/voice_line_19_cena6.wav"
    p "{size=-3}Benefícios:\nParticipação em competições nacionais e internacionais, desenvolvimento de projetos inovadores em robótica.{/size}"

    voice "voices/cena6/voice_line_20_cena6.wav"
    p "{size=-3}{b}{color=#00a188}CITi e DACin{/color}{/b}{/size}"

    voice "voices/cena6/voice_line_21_cena6.wav"
    p "{size=-3}CITi:\nEmpresa júnior que oferece serviços de TI e desenvolvimento de software, com oportunidades de aprendizado prático em projetos reais.{/size}"

    voice "voices/cena6/voice_line_22_cena6.wav"
    p "{size=-3}DACin:\nDiretório Acadêmico que representa os alunos do CIn, organizando eventos, debates e atividades culturais.{/size}"

    a "Isso é incrível! Há tantas coisas para fazer aqui além das aulas."

    voice "voices/cena6/voice_line_23_cena6.wav"
    p "Exatamente! E essas são apenas algumas das oportunidades disponíveis. O CIn é um lugar onde você pode realmente mergulhar na computação e descobrir sua paixão."

    hide sprite_psd_01_reduced with dissolve

    #? Esta resposta detalhada abrange as oportunidades disponíveis para os alunos do Centro de Informática da UFPE, ajudando a formar uma visão ampla das atividades de ensino, pesquisa, e extensão ofertadas pelo centro.

    jump larea

label larea:

    scene bg ccensaida with fade

    a "Preciso acessar alguns serviços exclusivos do CIn de casa. Ouvi falar sobre a VPN, mas não sei como configurá-la."

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena7/voice_line_0_cena7.wav"
    p "Entendi, vou te explicar! A VPN do CIn permite que você acesse serviços restritos à rede interna da UFPE remotamente, como artigos científicos, hospedagem de sites e serviços de impressão."

    voice "voices/cena7/voice_line_1_cena7.wav"
    p "Primeiro, você precisa visitar a {a=https://helpdesk.cin.ufpe.br/servicos/conectividade/vpn}página{/a} do HelpDesk sobre a VPN. Lá, você encontrará instruções detalhadas específicas para o seu sistema operacional."

    voice "voices/cena7/voice_line_2_cena7.wav"
    p "Dependendo do seu dispositivo, o processo de configuração da VPN pode variar. Geralmente, você precisará baixar e instalar um software VPN, como o OpenVPN ou qualquer cliente VPN recomendado pela página do HelpDesk."

    voice "voices/cena7/voice_line_3_cena7.wav"
    p "Para se conectar, use seu login e senha do CIn. Certifique-se de seguir as instruções de configuração para inserir os dados corretamente."

    voice "voices/cena7/voice_line_4_cena7.wav"
    p "{size=-7}Essa conexão permite o acesso a diversos recursos, como artigos científicos e bases de dados que normalmente requerem uma subscrição. Também é possível fazer upload de arquivos para seu espaço de hospedagem web usando uma conexão SFTP segura. Para imprimir documentos nos laboratórios do CIn de seu computador pessoal, você também precisará estar conectado à VPN.{/size}"

    a "Entendi! Vou verificar as instruções e configurar a VPN no meu laptop agora mesmo."

    voice "voices/cena7/voice_line_5_cena7.wav"
    p "Excelente! Se tiver alguma dúvida ou dificuldade, não hesite em consultar a página do HelpDesk ou entrar em contato com o suporte técnico do CIn. Estamos aqui para ajudar!"

    hide sprite_psd_01_reduced with dissolve

    #? Esta resposta detalhada fornece uma visão clara sobre como acessar e utilizar a VPN do Centro de Informática da UFPE, permitindo ao aluno acessar serviços exclusivos de qualquer lugar.

    jump classroommanual

label classroommanual:

    scene bg ccensaida with fade

    a "Estou tentando planejar meu curso para garantir que cumpro todas as exigências de carga horária. Você pode me ajudar a entender melhor isso?"

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena8/voice_line_0_cena8.wav"
    p "{size=-4}Claro! Cada curso no Centro de Informática possui uma carga horária determinada para a integralização curricular. Isso significa que, para você se formar, precisa cumprir uma carga horária mínima, que é composta de cadeiras obrigatórias, cadeiras eletivas de perfil, e cadeiras eletivas livres.{/size}"

    voice "voices/cena8/voice_line_1_cena8.wav"
    p "As chamadas Cadeiras Obrigatórias são disciplinas fundamentais para a formação no seu curso, com uma periodização indicada no perfil curricular. Sua aprovação é obrigatória para todos que pretendem concluir o curso."

    voice "voices/cena8/voice_line_2_cena8.wav"
    p "{size=-7}As Eletivas de Perfil são disciplinas listadas no perfil curricular do curso que não têm uma periodização específica. A escolha de cursá-las fica a critério do aluno (tendo os requisitos sido atendidos), sendo requerida apenas a carga horária de aprovação igual ou superior à requerida pelo curso.{/size}"

    voice "voices/cena8/voice_line_3_cena8.wav"
    p "{size=-8}Já as Eletivas Livres são disciplinas que não estão listadas no perfil curricular do curso, mas que podem ser cursadas para completar a carga horária mínima. Elas podem ser de qualquer área do conhecimento, desde que aprovadas pelo colegiado do curso. É possível cursar estas cadeiras em outras instituições de ensino superior, tanto no Brasil quanto no exterior.{/size}"

    a "E como isso se aplica a estágios ou atividades extracurriculares?"

    voice "voices/cena8/voice_line_4_cena8.wav"
    p "{size=-9}Boa pergunta! Para os estágios não-obrigatórios, é necessário que você tenha cursado pelo menos 1515 horas de disciplinas, obrigatórias ou eletivas. Além disso, a carga horária do estágio deve ser de 4 horas por dia. Em relação às empresas dentro do CIn, como a Samsung, Motorola e OKI Brasil, elas frequentemente oferecem oportunidades de estágio que podem contribuir para a sua carga horária de formação.{/size}"

    a "Isso ajuda muito no planejamento. Obrigado por esclarecer!"

    voice "voices/cena8/voice_line_5_cena8.wav"
    p "Sempre à disposição para ajudar! Lembre-se de consultar frequentemente o perfil curricular do seu curso e o SIGAA para um planejamento eficiente. Qualquer dúvida, a Secretaria de Graduação também pode oferecer suporte."

    hide sprite_psd_01_reduced with dissolve

    #? Este diálogo detalha a composição da carga horária necessária para a graduação no Centro de Informática da UFPE, incluindo a distinção entre cadeiras obrigatórias, eletivas de perfil e livres, e como os estágios se encaixam nesse contexto.

    jump labscene

label labscene:

    scene bg hallway1 with fade

    a "Estou tentando acessar alguns serviços do CIn, mas estou enfrentando problemas. Eu ouvi que há um Help Desk que pode ajudar. Você sabe como funciona?"

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena9/voice_line_0_cena9.wav"
    p " Claro! O Help Desk é sua linha de suporte para qualquer problema ou dúvida sobre os recursos tecnológicos oferecidos pelo CIn. Aqui está como você pode obter ajuda:"

    voice "voices/cena9/voice_line_3_cena9.wav"
    p "{color=#af00ff}Como Entrar Em Contato:{/color}\nTodas as solicitações de suporte devem ser enviadas para o e-mail {color=#f00}helpdesk@cin.ufpe.br{/color}. Isso inclui desde dúvidas sobre como conectar-se à rede Wi-Fi até problemas mais complexos com os serviços de hospedagem."

    voice "voices/cena9/voice_line_5_cena9.wav"
    p "{size=-7}O Help Desk pode ajudá-lo com uma ampla gama de questões, como acesso à rede interna, problemas de login, configuração de VPN, utilização de impressoras no centro, entre outros. Eles também fornecem suporte para problemas relacionados à G Suite disponibilizada para os alunos.{/size}"

    voice "voices/cena9/voice_line_6_cena9.wav"
    p "Para uma lista completa dos serviços e orientações sobre como utilizá-los, você pode visitar o {a=https://helpdesk.cin.ufpe.br/}site{/a}. Lá, você encontrará guias detalhados e FAQs que podem resolver sua dúvida rapidamente."

    voice "voices/cena9/voice_line_8_cena9.wav"
    p "Lembre-se de que o uso indevido dos recursos tecnológicos do CIn pode resultar no bloqueio ou suspensão do seu acesso, incluindo computadores e serviços online. Portanto, é importante seguir as políticas de uso adequado."

    a "Isso é ótimo! Vou enviar um e-mail agora mesmo para solucionar meu problema."

    voice "voices/cena9/voice_line_9_cena9.wav"
    p " Excelente! Eles são bastante responsivos e vão ajudar você a resolver qualquer questão. Se tiver mais alguma dúvida ou precisar de ajuda com outra coisa, estou aqui."

    hide sprite_psd_01_reduced with dissolve

    #? Esta resposta detalhada fornece uma visão clara do Help Desk no Centro de Informática da UFPE, incluindo como acessar o serviço, o tipo de ajuda disponível, e lembretes importantes sobre o uso responsável dos recursos tecnológicos.

    jump corridor

label corridor:

    scene bg hallway2 with fade

    a "Estou com algumas dúvidas sobre minha grade curricular e ouvi dizer que a Secretaria de Graduação pode me ajudar. Você sabe como eles funcionam?"

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena10/voice_line_0_cena10.wav"
    p "Claro, a Secretaria de Graduação é um ótimo recurso para os alunos! Eles são responsáveis por todo o acompanhamento acadêmico dos alunos de graduação no CIn. Vou te explicar melhor como você pode utilizar os serviços deles."

    voice "voices/cena10/voice_line_1_cena10.wav"
    p "A Secretaria de Graduação fica no primeiro andar do Bloco E (após o mezanino.) Você pode visitar a secretaria pessoalmente ou, se preferir, entrar em contato através do e-mail secgrad@cin.ufpe.br."

    voice "voices/cena10/voice_line_2_cena10.wav"
    p "Eles podem te ajudar com uma variedade de questões, como:"

    voice "voices/cena10/voice_line_3_cena10.wav"
    p "{size=-5}{color=#f00}Alteração de Matrícula:{/color} se você precisar alterar sua matrícula depois do período regular, a Secretaria pode ajudar.{/size}"

    voice "voices/cena10/voice_line_4_cena10.wav"
    p "{size=-5}{color=#f00}Matrícula em Disciplinas Isoladas e Eletivas de Outros Centros:{/color} Para explorar disciplinas fora do seu curso ou centro, a Secretaria orienta como proceder.{/size}"

    voice "voices/cena10/voice_line_5_cena10.wav"
    p "{size=-5}{color=#f00}Cancelamento de Disciplina e Trancamento de Período:{/color}\nSe você estiver passando por dificuldades e precisar ajustar sua carga horária, eles podem orientar sobre os procedimentos necessários.{/size}"

    voice "voices/cena10/voice_line_6_cena10.wav"
    p "{size=-5}{color=#f00}Pedido de Segunda Chamada de Provas e Revisão de Provas:{/color}\nCaso haja necessidade, a Secretaria gerencia esses pedidos.{/size}"

    voice "voices/cena10/voice_line_7_cena10.wav"
    p "{size=-5}{color=#f00}Declarações e Documentos:{/color} Para obtenção de declarações acadêmicas e outros documentos, é só solicitar.{/size}"

    a "Isso é muito útil! Vou entrar em contato com eles para esclarecer minhas dúvidas."

    voice "voices/cena10/voice_line_8_cena10.wav"
    p "{size=-5}{color=#f00}Esclarecimentos sobre Regras, Disciplinas, Horários, Matrículas, e o SIGAA:{/color} Qualquer dúvida acadêmica, a Secretaria está pronta para ajudar.{/size}"

    voice "voices/cena10/voice_line_10_cena10.wav"
    p "No {a=https://cin.ufpe.br/~secgrad}site{/a}, você pode encontrar uma vasta quantidade de informações úteis, como listas de docentes, grades curriculares, horários do semestre, alocações das salas de aulas, códigos das disciplinas, e o calendário acadêmico da UFPE."

    a "Isso é muito útil! Vou entrar em contato com eles para esclarecer minhas dúvidas."

    voice "voices/cena10/voice_line_11_cena10.wav"
    p "Ótimo! Eles estão lá para ajudar, então não hesite em procurá-los sempre que precisar. Lembre-se que manter uma boa comunicação com a Secretaria de Graduação pode facilitar muito sua vida acadêmica no CIn."

    hide sprite_psd_01_reduced with dissolve

    #? Esta resposta detalha o papel da Secretaria de Graduação no Centro de Informática da UFPE, explicando sua localização, como entrar em contato, os serviços oferecidos, e onde encontrar recursos online.

    jump rulesofgoodbehavior

label rulesofgoodbehavior:

    scene bg desolate with fade

    a "Estou tentando me adaptar ao CIn e ouvi dizer que existem algumas regras de convivência importantes. Você pode me explicar melhor sobre elas?"

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena11/voice_line_0_cena11.wav"
    p " Com certeza! O CIn oferece muitos recursos aos alunos, e é importante usá-los com responsabilidade. Vou te passar um resumo das regras mais importantes para garantir um ambiente acadêmico saudável e produtivo para todos."


    voice "voices/cena11/voice_line_1_cena11.wav"
    p "{size=-3}{color=#a0a}Uso dos Laboratórios: {/color}Jogar nos laboratórios é proibido, exceto para atividades acadêmicas que o exijam. Os recursos computacionais são prioritariamente para estudo e pesquisa.{/size}"

    voice "voices/cena11/voice_line_2_cena11.wav"
    p "{size=-4}{color=#b2b}Softwares e Recursos: {/color}Instalar softwares ilegais, que afetem a performance dos computadores após o uso, ou que causem degradação no hardware, como mineradores de criptomoedas, é estritamente proibido.{/size}"

    voice "voices/cena11/voice_line_3_cena11.wav"
    p "{size=-5}{color=#c3c}Atividades Ilegais ou Mal-Intencionadas: {/color}Usar os recursos tecnológicos do CIn para atividades ilegais, como disseminação de vírus, phishing, ou ataques a computadores, é proibido. Ataques permitidos apenas em ambientes controlados e com autorização prévia.{/size}"

    voice "voices/cena11/voice_line_4_cena11.wav"
    p "{size=-3}{color=#d4d}Respeito e Assédio: {/color}A rede do CIn não deve ser usada para ameaçar, assediar, ou incomodar terceiros.{/size}"

    voice "voices/cena11/voice_line_5_cena11.wav"
    p "{size=-3}{color=#e5e}Silêncio e Limpeza nos Laboratórios: {/color}Fazer barulho, comer e/ou beber nos laboratórios é proibido para manter um ambiente de estudo adequado e equipamentos limpos.{/size}"

    voice "voices/cena11/voice_line_6_cena11.wav"
    p "{size=-3}{color=#f6f}Venda de Serviços: {/color}Qualquer tipo de comércio dentro do CIn sem autorização prévia é proibido.{/size}"


    a "Entendi, é basicamente usar o bom senso e respeitar os outros."

    stop music

    voice "voices/cena11/voice_line_7_cena11.wav"
    p "Exatamente! Seguir essas regras ajuda a manter o CIn um lugar excelente para aprender e desenvolver novas habilidades. Se você ver alguém desrespeitando essas regras, é importante reportar para que possamos manter um ambiente positivo para todos."

    hide sprite_psd_01_reduced with dissolve

    #? Esta resposta detalhada abrange as principais regras de convivência no Centro de Informática da UFPE, destacando a importância do uso responsável dos recursos e do respeito mútuo para manter um ambiente acadêmico saudável.

    jump foodcourt

label foodcourt:

    scene bg copa1 with fade

    a "Notei que o CIn tem algumas copas disponíveis para os alunos. Você pode me contar mais sobre como podemos usá-las corretamente?"

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena12/voice_line_0_cena12.wav"
    p "Com certeza! As copas são espaços comuns que todos os alunos podem usar, localizadas no térreo do Bloco B e no mezanino do Bloco E."

    voice "voices/cena12/voice_line_1_cena12.wav"
    p "{size=-5}A estrutura das copas geralmente é composta de geladeira, micro-ondas, gelágua, máquina de café em cápsula, e pia para limpeza de utensílios. Como todo espaço comum, é importante seguir algumas diretrizes para garantir que todos possam aproveitar esses espaços da melhor forma possível.{/size}"

    voice "voices/cena12/voice_line_2_cena12.wav"
    p "Use a geladeira para guardar sua comida, mas evite sacos plásticos que ocupam muito espaço. Guarde apenas o necessário e lembre-se de retirar seus itens ao final do dia."

    voice "voices/cena12/voice_line_3_cena12.wav"
    p "Após comer, descarte os restos de comida no lixo e não na pia, evitando entupimentos. Lave, enxugue e guarde seus utensílios. A copa não é um lugar para armazenar itens pessoais."

    voice "voices/cena12/voice_line_4_cena12.wav"
    p "Não coloque garrafas PET no congelador. Elas podem estourar e danificar o refrigerador."

    voice "voices/cena12/voice_line_5_cena12.wav"
    p "É necessário trazer seu próprio copo ou garrafa para beber água. O CIn não fornece copos descartáveis ou cápsulas de café. A responsabilidade de trazer esses itens é dos alunos."

    a "Isso ajuda bastante! Agora sei como usar as copas sem causar problemas. Obrigado!"

    voice "voices/cena12/voice_line_6_cena12.wav"
    p "De nada! Lembre-se, o respeito e a responsabilidade no uso das áreas comuns são essenciais para manter um bom ambiente para todos no CIn. Se tiver mais alguma dúvida, estou aqui para ajudar."

    hide sprite_psd_01_reduced with dissolve

    #? Esta resposta detalhada fornece orientações claras sobre como os alunos devem usar as copas no Centro de Informática da UFPE, enfatizando a importância da limpeza, do cuidado com os alimentos e utensílios, e da responsabilidade individual.

    jump secgrad

label secgrad:

    scene bg bibliot with fade

    a "Ouvi dizer que podemos reservar salas aqui no CIn para estudos em grupo ou reuniões de projeto. Como isso funciona?"

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena13/voice_line_0_cena13.wav"
    p "Sim, é verdade! Todos os alunos têm a possibilidade de reservar salas no CIn, exceto as salas de reunião. Aqui estão os passos que você precisa seguir para fazer uma reserva:"

    voice "voices/cena13/voice_line_1_cena13.wav"
    p "Passo 1: {b}{color=#233}Verificar Disponibilidade{/color}{/b}"

    voice "voices/cena13/voice_line_2_cena13.wav"
    p "Primeiramente acesse o{a=https://helpdesk.cin.ufpe.br/servicos/reservas} site de reservas{/a} para verificar a disponibilidade da sala desejada."

    voice "voices/cena13/voice_line_3_cena13.wav"
    p "Passo 2: {b}{color=#233}Solicitação por E-mail{/color}{/b}"

    voice "voices/cena13/voice_line_4_cena13.wav"
    p "Após escolher a sala e verificar que está disponível para o período desejado, envie um e-mail para secgrad@cin.ufpe.br. No assunto do e-mail, especifique que deseja reservar uma sala."

    voice "voices/cena13/voice_line_5_cena13.wav"
    p "No corpo do e-mail, informe qual sala você deseja reservar, o período da reserva e o motivo da reserva."

    voice "voices/cena13/voice_line_6_cena13.wav"
    p "Passo 3: {b}{color=#233}Esperar Confirmação{/color}{/b}"

    voice "voices/cena13/voice_line_7_cena13.wav"
    p "Aguarde receber um e-mail de confirmação da Secretaria de Graduação, confirmando que sua reserva foi efetuada com sucesso."

    voice "voices/cena13/voice_line_8_cena13.wav"
    p "Passo 4: {b}{color=#233}Retirada da Chave/Cartão{/color}{/b}"

    voice "voices/cena13/voice_line_9_cena13.wav"
    p "No período reservado, você deve ir à portaria ou à Secretaria de Graduação, se identificar e solicitar a chave ou o cartão da sala reservada."

    a "Parece fácil! E tem algum custo envolvido?"

    voice "voices/cena13/voice_line_10_cena13.wav"
    p "Não, o serviço de reserva de salas é gratuito para os alunos. Apenas certifique-se de usar a sala reservada para o fim especificado na sua solicitação e de devolver a chave ou cartão após o uso."

    a "Ótimo, vou organizar uma sessão de estudos com meu grupo então. Obrigado pela ajuda!"

    voice "voices/cena13/voice_line_11_cena13.wav"
    p "De nada! Se precisar de mais alguma coisa ou tiver outras dúvidas, estou à disposição. Boa sorte com seus estudos!"

    hide sprite_psd_01_reduced with dissolve

    #? Este diálogo oferece uma visão detalhada sobre o processo de reserva de salas no Centro de Informática da UFPE, incluindo onde verificar a disponibilidade, como solicitar a reserva e o processo de confirmação e retirada da chave ou cartão da sala.

    jump networkconnection

label networkconnection:

    scene bg roam with fade

    a "Preciso acessar a internet para enviar um trabalho, mas não tenho certeza de como me conectar à rede Wi-Fi aqui no CIn. Você pode me ajudar?"

    show sprite_psd_01_reduced at truecenter

    voice "voices/cena14/voice_line_0_cena14.wav"
    p "Claro, temos algumas opções de rede Wi-Fi aqui no CIn. Vou te explicar sobre cada uma delas para você decidir qual usar."

    voice "voices/cena14/voice_line_1_cena14.wav"
    p "{size=+10}{b}{color=#00a188}Rede CINUFPE{/color}{/b}{/size}"

    voice "voices/cena14/voice_line_2_cena14.wav"
    p "Esta é a rede principal do CIn, destinada a alunos, professores e servidores. Oferece a maior velocidade de transferência entre todas as redes Wi-Fi disponíveis no centro. O uso dessa rede é altamente recomendado para uma conexão rápida e estável."

    voice "voices/cena14/voice_line_3_cena14.wav"
    p "Para se conectar, use seu login e senha do CIn. Essa rede tem pequenos bloqueios para evitar uso indevido."

    voice "voices/cena14/voice_line_4_cena14.wav"
    p "{size=+10}{b}{color=#00a188}Rede CINGUESTS{/color}{/b}{/size}"

    voice "voices/cena14/voice_line_5_cena14.wav"
    p "Essa é a rede para visitantes do CIn. Tem velocidade limitada e diversos bloqueios, o que pode restringir o acesso a certos serviços."

    voice "voices/cena14/voice_line_6_cena14.wav"
    p "A senha para essa rede é {color=#FDD835}acessocin{/color}. É uma boa opção para visitantes ou quando você estiver com dificuldades de acesso à rede principal."

    voice "voices/cena14/voice_line_7_cena14.wav"
    p "{size=+10}{b}{color=#00a188}Rede eduroam{/color}{/b}{/size}"

    voice "voices/cena14/voice_line_8_cena14.wav"
    p "A eduroam é uma rede livre, disponível em todo o campus da UFPE, e não só no CIn. É destinada a alunos, professores e servidores da universidade."

    voice "voices/cena14/voice_line_9_cena14.wav"
    p "Use seu e-mail institucional e a Senha de Serviços Integrados da UFPE para se conectar. O e-mail institucional SIG@ é diferente do seu login do CIn."

    voice "voices/cena14/voice_line_10_cena14.wav"
    p "Importante lembrar que, para acessar a rede eduroam, sua Senha de Serviços Integrados pode ser alterada por meio do SIG@, caso você não a lembre."

    a "Isso ajuda muito! Vou tentar me conectar à rede CINUFPE então. Obrigado pela informação!"

    voice "voices/cena14/voice_line_11_cena14.wav"
    p "De nada! Se tiver mais alguma dúvida ou dificuldade, sinta-se livre para perguntar. Estamos aqui para ajudar."

    hide sprite_psd_01_reduced with dissolve
    #? Este diálogo detalha as opções de rede Wi-Fi disponíveis no Centro de Informática da UFPE, explicando como cada uma funciona e como os alunos podem acessá-las, garantindo que possam se conectar à internet conforme suas necessidades.

    return
