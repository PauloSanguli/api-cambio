import requests
from Extrair_Tag import extrair_tag
from Extrair_Tag import Formate_String
from bs4 import BeautifulSoup

 
class BCI():
  """html_text = requests.get('https://www.bci.ao/').text"""
  html_text = """
  From: <Saved by Blink>
Snapshot-Content-Location: https://www.bci.ao/
Subject: Banco BCI
Date: Sat, 7 Jan 2023 13:34:35 -0000
MIME-Version: 1.0
Content-Type: multipart/related;
	type="text/html";
	boundary="----MultipartBoundary--B35gv9hf8GVvnlqnSn2OQfMwBE5Ga2VECPMKOPmjLS----"


------MultipartBoundary--B35gv9hf8GVvnlqnSn2OQfMwBE5Ga2VECPMKOPmjLS----
Content-Type: text/html
Content-ID: <frame-D3FA16A8B342B7A029BDAC0AD3F58730@mhtml.blink>
Content-Transfer-Encoding: binary
Content-Location: https://www.bci.ao/

<!DOCTYPE html><html lang=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Banco BCI</title>
        
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        
    <!-- OPEN GRAPH TAGS -->
    <meta property="og:title" content="">
    <meta property="og:description" content="">
    
    <meta property="og:url" content="http://www.bci.ao:8081/">
    <meta property="og:site_name" content="BCI Angola">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="pt_PT">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <!-- TWITTER TAGS -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="">
    <meta name="twitter:description" content="">
    
    <meta name="twitter:url" content="http://www.bci.ao:8081/">
    <meta name="twitter:creator" content="djomba">

    <title></title>
    <meta name="description" content="">
    <meta name="keywords" content="">

        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="theme-color" content="">
        <meta name="msapplication-navbutton-color" content="">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

        <meta name="application-name" content="">
        <meta name="msapplication-TileColor" content="#FFFFFF">

        <link rel="apple-touch-icon-precomposed" sizes="57x57" href="https://www.bci.ao/media/1180/apple-touch-icon-57x57.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://www.bci.ao/media/1184/apple-touch-icon-114x114.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://www.bci.ao/media/1182/apple-touch-icon-72x72.png">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://www.bci.ao/media/1186/apple-touch-icon-144x144.png">
        <link rel="apple-touch-icon-precomposed" sizes="60x60" href="https://www.bci.ao/media/1181/apple-touch-icon-60x60.png">
        <link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://www.bci.ao/media/1185/apple-touch-icon-120x120.png">
        <link rel="apple-touch-icon-precomposed" sizes="76x76" href="https://www.bci.ao/media/1183/apple-touch-icon-76x76.png">
        <link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://www.bci.ao/media/1187/apple-touch-icon-152x152.png">
        <link rel="icon" href="https://www.bci.ao/media/1188/favicon.ico" type="image/x-icon">
        <link rel="icon" type="image/png" href="https://www.bci.ao/media/1193/favicon-196x196.png" sizes="196x196">
        <link rel="icon" type="image/png" href="https://www.bci.ao/media/1191/favicon-96x96.png" sizes="96x96">
        <link rel="icon" type="image/png" href="https://www.bci.ao/media/1190/favicon-32x32.png" sizes="32x32">
        <link rel="icon" type="image/png" href="https://www.bci.ao/media/1189/favicon-16x16.png" sizes="16x16">
        <link rel="icon" type="image/png" href="https://www.bci.ao/media/1192/favicon-128.png" sizes="128x128">
        <meta name="msapplication-TileImage" content="/media/1195/mstile-144x144.png">
        <meta name="msapplication-square70x70logo" content="/media/1194/mstile-70x70.png">
        <meta name="msapplication-square150x150logo" content="/media/1196/mstile-150x150.png">
        <meta name="msapplication-wide310x150logo" content="/media/1197/mstile-310x150.png">
        <meta name="msapplication-square310x310logo" content="/media/1198/mstile-310x310.png">
        
        <link type="text/css" rel="stylesheet" href="https://www.bci.ao/css/font-awesome-572.css">
        <link type="text/css" rel="stylesheet" href="https://www.bci.ao/css/applibs.css">
        <link type="text/css" rel="stylesheet" href="https://www.bci.ao/css/app.css">
            
        

    </head>
    <body class="particulares active">
        <div class="global-container">
            





<header class="header-nav min" style="">
    <nav class="sections-nav">
        <div class="content">
            <div class="menu-left">
                <ul class="sections-links">
                       
                
                    <li class="particulares active">
                        <a href="https://www.bci.ao/pt/particulares/" id="menuTopLevel10"><span>Particulares</span></a>
                    </li>
                
                
                    <li class="empresas">
                        <a href="https://www.bci.ao/pt/empresas/" id="menuTopLevel11"><span>Empresas</span></a>
                    </li>
                
                
                    <li class="institucional">
                        <a href="https://www.bci.ao/pt/institucional/" id="menuTopLevel12"><span>Institucional</span></a>
                    </li>
                

    

                </ul>
            </div>
            <div class="menu-right">
                
                <ul class="contactos-links">
                    <li><a href="https://www.bci.ao/pt/contactos"><span>Contactos e Balcões</span></a></li>
                </ul>
                <button class="search-button">
                     

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15.9 16.1" enable-background="new 0 0 15.9 16.1" xml:space="preserve">
                	<circle fill="none" stroke="#212121" stroke-miterlimit="10" cx="9.1" cy="6.8" r="6.3"></circle>
                	<line fill="none" stroke="#212121" stroke-miterlimit="10" x1="4.8" y1="11.4" x2="0.4" y2="15.8"></line>
                </svg>
            


                </button>
            </div>
        </div>
    </nav>
    <nav class="menu-nav">
        <div class="content">
            <div class="menu-left">
                <div class="logo">
                    <a href="https://www.bci.ao/"><img src="https://www.bci.ao/media/1101/logo.svg"></a>
                </div>
                        
            <ul class="menu-links show-menu" data-menu-id="menuTopLevel10"> <!-- Parent id container -->
                        
                            <li><a href="https://www.bci.ao/pt/particulares/" id="menuTopLevel20"><span>Início</span></a></li>

                        
                        
                            <li><a href="https://www.bci.ao/pt/particulares/conta-%C3%A0-ordem/" id="menuTopLevel21"><span>Conta à ordem</span></a></li>

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel22"><span>Poupança</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Poupança</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/conta-poupan%C3%A7a-monami/" id="menuTopLevel30">Conta Poupança MONAMI</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/poupan%C3%A7a-bankita-crescer/" id="menuTopLevel31">Poupança Bankita Crescer</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/dep%C3%B3sito-a-prazo/" id="menuTopLevel32">Depósito a Prazo</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/dp-bci-cl%C3%A1ssico-moeda-nacional/" id="menuTopLevel33">DP BCI Clássico Moeda Nacional</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/dp-bci-cl%C3%A1ssico-moeda-estrangeira/" id="menuTopLevel34">DP BCI Clássico Moeda Estrangeira</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel23"><span>Crédito</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Crédito</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-geral/" target="_top" id="menuTopLevel30">Crédito Geral</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-sal%C3%A1rio/" id="menuTopLevel31">Crédito Salário</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cria-condi%C3%A7%C3%B5es/" target="_top" id="menuTopLevel32">Cria Condições</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-autom%C3%B3vel/" target="_top" id="menuTopLevel33">Crédito Automóvel</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-seguro-autom%C3%B3vel/" target="_top" id="menuTopLevel34">Crédito Seguro Automóvel</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/bci-adiantamento-de-sal%C3%A1rio-mais/" id="menuTopLevel35">BCI Adiantamento de Salário Mais</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/bci-adiantamento-de-sal%C3%A1rio/" id="menuTopLevel36">BCI Adiantamento de Salário</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/bci-adiantamento-de-sal%C3%A1rio-funcion%C3%A1rio-publico/" id="menuTopLevel37">BCI Adiantamento de Salário Funcionário Publico</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel24"><span>Serviços</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Serviços</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/opera%C3%A7%C3%B5es-sobre-o-estrangeiro/" id="menuTopLevel30">Operações sobre o Estrangeiro</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/western-union/" id="menuTopLevel31">Western Union</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/carta-de-cr%C3%A9dito/" id="menuTopLevel32">Carta de Crédito</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/bcinet/" id="menuTopLevel33">BCINet</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/tpa-terminal-de-pagamento-autom%C3%A1tico/" id="menuTopLevel34">TPA - Terminal de Pagamento Automático</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/pagou-activou/" id="menuTopLevel35">Pagou Activou</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel25"><span>Cartões</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Cartões</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cart%C3%B5es/cart%C3%A3o-multicaixa-d%C3%A9bito/" id="menuTopLevel30">Cartão Multicaixa Débito</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cart%C3%B5es/cart%C3%A3o-pr%C3%A9-pago-moxi/" target="_blank" id="menuTopLevel31">Cartão pré-pago Moxi</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li><a href="https://www.bci.ao/#/" id="menuTopLevel26"><span>Seguros</span></a></li>

                        
                        
                            <li><a href="https://www.bci.ao/pt/particulares/seguran%C3%A7a/" target="_blank" id="menuTopLevel27"><span>Segurança</span></a></li>

                        

            </ul>
        
        
            <ul class="menu-links" data-menu-id="menuTopLevel11"> <!-- Parent id container -->
                        
                            <li><a href="https://www.bci.ao/pt/empresas/" id="menuTopLevel20"><span>Início</span></a></li>

                        
                        
                            <li><a href="https://www.bci.ao/pt/empresas/contas/" id="menuTopLevel21"><span>Contas</span></a></li>

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel22"><span>Crédito</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Crédito</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/cr%C3%A9dito/conta-corrente-caucionada/" id="menuTopLevel30">Conta corrente caucionada</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/cr%C3%A9dito/cr%C3%A9dito-geral/" id="menuTopLevel31">Crédito Geral</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/cr%C3%A9dito/carta-de-cr%C3%A9dito/" id="menuTopLevel32">Carta de Crédito</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li><a href="https://www.bci.ao/pt/empresas/dep%C3%B3sitos/" id="menuTopLevel23"><span>Depósitos</span></a></li>

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel24"><span>Investimento</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Investimento</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/aplica%C3%A7%C3%B5es-a-prazo/" id="menuTopLevel30">Aplicações a prazo</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/aplica%C3%A7%C3%B5es-de-tesouraria/" id="menuTopLevel31">Aplicações de Tesouraria</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/aplica%C3%A7%C3%B5es-em-t%C3%ADtulos/" id="menuTopLevel32">Aplicações em títulos</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/dp-bci-tesouraria-fortificada/" id="menuTopLevel33">DP BCI Tesouraria Fortificada</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel25"><span>Estado</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Estado</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-agr%C3%ADcola-de-investimento/" id="menuTopLevel30">Crédito Agrícola de Investimento</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-de-campanha-agr%C3%ADcola/" target="_top" id="menuTopLevel31">Crédito de Campanha Agrícola</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-pr%C3%B3jovem/" id="menuTopLevel32">Crédito PróJovem</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-ao-sector-real-da-economia/" id="menuTopLevel33">Crédito ao Sector Real da Economia</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li><a href="https://www.bci.ao/pt/empresas/pagamento-de-impostos/" id="menuTopLevel26"><span>Pagamento de impostos</span></a></li>

                        
                        
                            <li><a href="https://www.bci.ao/#/" id="menuTopLevel27"><span>Seguros</span></a></li>

                        
                        
                            <li><a href="https://www.bci.ao/pt/empresas/seguran%C3%A7a-empresas/" id="menuTopLevel28"><span>Segurança</span></a></li>

                        

            </ul>
        
        
            <ul class="menu-links" data-menu-id="menuTopLevel12"> <!-- Parent id container -->
                        
                            <li><a href="https://www.bci.ao/pt/institucional/" id="menuTopLevel20"><span>Início</span></a></li>

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel21"><span>Conheça o BCI</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Conheça o BCI</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/conhe%C3%A7a-o-bci/quem-somos/" id="menuTopLevel30">Quem somos</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/conhe%C3%A7a-o-bci/org%C3%A3os-sociais/" id="menuTopLevel31">Orgãos Sociais</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/conhe%C3%A7a-o-bci/informa%C3%A7%C3%B5es-corporativas/" id="menuTopLevel32">Informações corporativas</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li class="with_sub"><a href="https://www.bci.ao/#/" id="menuTopLevel22"><span>Informação Financeira</span></a></li>
                                    
                                        <div class="sub_header">
                                            <div class="content">
                                                <div class="text">
                                                    <h3>Informação Financeira</h3>
                                                </div>
                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/contas/" id="menuTopLevel30">Demonstrações Financeiras</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/relat%C3%B3rios-e-contas/" id="menuTopLevel31">Relatórios e contas</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/balancetes/" id="menuTopLevel32">Balancetes</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/cr%C3%A9dito-a-economia-real/" target="" id="menuTopLevel33">Crédito a Economia Real</a></li>
                                                            

                                                </ul>
                                            </div>
                                        </div>
                                    

                        
                        
                            <li><a href="https://www.bci.ao/pt/institucional/not%C3%ADcias/" id="menuTopLevel23"><span>Notícias</span></a></li>

                        
                        
                            <li><a href="https://www.bci.ao/pt/institucional/clipping/" id="menuTopLevel24"><span>Clipping</span></a></li>

                        

            </ul>
        

            </div>

            <div class="menu-right">
                <div class="login-menu">
                    <a href="https://ib.bci.ao/" target="_blank">
                        <div class="header">
                             <strong>BCI NET</strong> <span class="sep"></span> Login
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </nav>
</header>

<header class="header-mobile-nav">
    <div class="content">

        <div class="menu-left">
            <div class="logo">
                <a href="https://www.bci.ao/"><img src="https://www.bci.ao/media/1101/logo.svg"></a>
            </div>
        </div>

        <div class="menu-right">
            <button class="search-button">
                 

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 15.9 16.1" enable-background="new 0 0 15.9 16.1" xml:space="preserve">
                	<circle fill="none" stroke="#212121" stroke-miterlimit="10" cx="9.1" cy="6.8" r="6.3"></circle>
                	<line fill="none" stroke="#212121" stroke-miterlimit="10" x1="4.8" y1="11.4" x2="0.4" y2="15.8"></line>
                </svg>
            


            </button>
            <button class="menu-button">
                <div class="wrapper">
                    <span class="line"></span>
                    <span class="line"></span>
                    <span class="line"></span>
                </div>
            </button>
        </div>
    </div>
    <div class="menu-wrapper">
        <div class="login-menu">
            <a href="https://ib.bci.ao/" target="_blank">
                <div class="header">
                    <strong>BCI NET</strong> <span class="sep"></span> Login
                </div>
            </a>
        </div>
        <div class="mobile-links-container">
                    
            <div class="mobile-links-section">   
                <div class="header">
                    <h6>Particulares</h6> <div class="seta"></div>
                </div>
                <ul class="menu-mobile-links">
                            
                                <li data-menu-id="1310"><a href="https://www.bci.ao/pt/particulares/">Início</a>

                                </li>

                            
                            
                                <li data-menu-id="0"><a href="https://www.bci.ao/pt/particulares/conta-%C3%A0-ordem/">Conta à ordem</a>

                                </li>

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Poupança</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/conta-poupan%C3%A7a-monami/" id="menuTop1661">Conta Poupança MONAMI</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/poupan%C3%A7a-bankita-crescer/" id="menuTop1694">Poupança Bankita Crescer</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/dep%C3%B3sito-a-prazo/" id="menuTop1692">Depósito a Prazo</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/dp-bci-cl%C3%A1ssico-moeda-nacional/" id="menuTop1964">DP BCI Clássico Moeda Nacional</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/dp-bci-cl%C3%A1ssico-moeda-estrangeira/" id="menuTop1966">DP BCI Clássico Moeda Estrangeira</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Crédito</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-geral/" target="_top" id="menuTop1313">Crédito Geral</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-sal%C3%A1rio/" id="menuTop1318">Crédito Salário</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cria-condi%C3%A7%C3%B5es/" target="_top" id="menuTop1319">Cria Condições</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-autom%C3%B3vel/" target="_top" id="menuTop1320">Crédito Automóvel</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/cr%C3%A9dito-seguro-autom%C3%B3vel/" target="_top" id="menuTop1321">Crédito Seguro Automóvel</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/bci-adiantamento-de-sal%C3%A1rio-mais/" id="menuTop1704">BCI Adiantamento de Salário Mais</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/bci-adiantamento-de-sal%C3%A1rio/" id="menuTop1705">BCI Adiantamento de Salário</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cr%C3%A9dito/bci-adiantamento-de-sal%C3%A1rio-funcion%C3%A1rio-publico/" id="menuTop1708">BCI Adiantamento de Salário Funcionário Publico</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Serviços</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/opera%C3%A7%C3%B5es-sobre-o-estrangeiro/" id="menuTop1697">Operações sobre o Estrangeiro</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/western-union/" id="menuTop1698">Western Union</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/carta-de-cr%C3%A9dito/" id="menuTop1700">Carta de Crédito</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/bcinet/" id="menuTop1701">BCINet</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/tpa-terminal-de-pagamento-autom%C3%A1tico/" id="menuTop1706">TPA - Terminal de Pagamento Automático</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/servi%C3%A7os/pagou-activou/" id="menuTop1718">Pagou Activou</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Cartões</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cart%C3%B5es/cart%C3%A3o-multicaixa-d%C3%A9bito/" id="menuTop1703">Cartão Multicaixa Débito</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/particulares/cart%C3%B5es/cart%C3%A3o-pr%C3%A9-pago-moxi/" target="_blank" id="menuTop1709">Cartão pré-pago Moxi</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li data-menu-id="0"><a href="https://www.bci.ao/#/">Seguros</a>

                                </li>

                            
                            
                                <li data-menu-id="1309"><a href="https://www.bci.ao/pt/particulares/seguran%C3%A7a/">Segurança</a>

                                </li>

                            

                </ul>
            </div>
        
        
            <div class="mobile-links-section">   
                <div class="header">
                    <h6>Empresas</h6> <div class="seta"></div>
                </div>
                <ul class="menu-mobile-links">
                            
                                <li data-menu-id="0"><a href="https://www.bci.ao/pt/empresas/">Início</a>

                                </li>

                            
                            
                                <li data-menu-id="1356"><a href="https://www.bci.ao/pt/empresas/contas/">Contas</a>

                                </li>

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Crédito</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/cr%C3%A9dito/conta-corrente-caucionada/" id="menuTop1317">Conta corrente caucionada</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/cr%C3%A9dito/cr%C3%A9dito-geral/" id="menuTop1366">Crédito Geral</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/cr%C3%A9dito/carta-de-cr%C3%A9dito/" id="menuTop1367">Carta de Crédito</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li data-menu-id="1368"><a href="https://www.bci.ao/pt/empresas/dep%C3%B3sitos/">Depósitos</a>

                                </li>

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Investimento</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/aplica%C3%A7%C3%B5es-a-prazo/" id="menuTop1358">Aplicações a prazo</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/aplica%C3%A7%C3%B5es-de-tesouraria/" id="menuTop1359">Aplicações de Tesouraria</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/aplica%C3%A7%C3%B5es-em-t%C3%ADtulos/" id="menuTop1360">Aplicações em títulos</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/investimento/dp-bci-tesouraria-fortificada/" id="menuTop1969">DP BCI Tesouraria Fortificada</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Estado</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-agr%C3%ADcola-de-investimento/" id="menuTop1365">Crédito Agrícola de Investimento</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-de-campanha-agr%C3%ADcola/" target="_top" id="menuTop1353">Crédito de Campanha Agrícola</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-pr%C3%B3jovem/" id="menuTop1295">Crédito PróJovem</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/empresas/estado/cr%C3%A9dito-ao-sector-real-da-economia/" id="menuTop1972">Crédito ao Sector Real da Economia</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li data-menu-id="1281"><a href="https://www.bci.ao/pt/empresas/pagamento-de-impostos/">Pagamento de impostos</a>

                                </li>

                            
                            
                                <li data-menu-id="0"><a href="https://www.bci.ao/#/">Seguros</a>

                                </li>

                            
                            
                                <li data-menu-id="1370"><a href="https://www.bci.ao/pt/empresas/seguran%C3%A7a-empresas/">Segurança</a>

                                </li>

                            

                </ul>
            </div>
        
        
            <div class="mobile-links-section">   
                <div class="header">
                    <h6>Institucional</h6> <div class="seta"></div>
                </div>
                <ul class="menu-mobile-links">
                            
                                <li data-menu-id="0"><a href="https://www.bci.ao/pt/institucional/">Início</a>

                                </li>

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Conheça o BCI</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/conhe%C3%A7a-o-bci/quem-somos/" id="menuTop1374">Quem somos</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/conhe%C3%A7a-o-bci/org%C3%A3os-sociais/" id="menuTop1791">Orgãos Sociais</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/conhe%C3%A7a-o-bci/informa%C3%A7%C3%B5es-corporativas/" id="menuTop1376">Informações corporativas</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li class="with_sub" data-menu-id="0"><a href="https://www.bci.ao/#/">Informação Financeira</a>
                                            
                                                <div class="seta"></div>
                                            

                                </li>
                                        
                                            <div class="sub_header">

                                                <ul class="links">
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/contas/" id="menuTop1833">Demonstrações Financeiras</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/relat%C3%B3rios-e-contas/" id="menuTop1413">Relatórios e contas</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/balancetes/" id="menuTop1414">Balancetes</a></li>
                                                            
                                                            
                                                                <li><a href="https://www.bci.ao/pt/institucional/informa%C3%A7%C3%A3o-financeira/cr%C3%A9dito-a-economia-real/" target="" id="menuTop1836">Crédito a Economia Real</a></li>
                                                            

                                                </ul>
                                            </div>
                                        

                            
                            
                                <li data-menu-id="1259"><a href="https://www.bci.ao/pt/institucional/not%C3%ADcias/">Notícias</a>

                                </li>

                            
                            
                                <li data-menu-id="1395"><a href="https://www.bci.ao/pt/institucional/clipping/">Clipping</a>

                                </li>

                            

                </ul>
            </div>
        

            <div class="mobile-others">
                <ul class="contactos-links">
                    <li><a href="https://www.bci.ao/#"><span>Contactos e Balcões</span></a></li>
                </ul>
                <ul class="languages-links">
                    <li><a href="https://www.bci.ao/#"><span>PT</span></a></li>
                    <li><a href="https://www.bci.ao/#"><span>ENG</span></a></li>
                </ul>
            </div>
        </div>
    </div>
</header> 
             
            <div class="search-container">
                <div class="content">
                    <form method="" action="https://www.bci.ao/">
                        <div class="salwrap">
                            <input type="text" name="search" placeholder="Pesquisar..." autocomplete="off">
                        </div>
                        <button class="square-btn" disabled="">
                            

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 22.9 15.4" enable-background="new 0 0 22.9 15.4" xml:space="preserve">
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="0.5" y1="7.7" x2="22.4" y2="7.7"></line>
                	<polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="15.1,0.5
                		22.4,7.8 15.2,14.9 	"></polyline>
                </svg>
            


                        </button>
                        <button class="btn" disabled="">
                            <span>Pesquisar</span>
                        </button>
                    </form>
                </div>
            </div>
            
            <div class="page-container min">


<div class="homepage-header">
    <div class="shadow-layer"></div>
    
            
                <div class="slide" data-photo="1" style="background-image: url('/media/1447/abertura-sabados-banner.jpg')">
                    <a href="https://www.bci.ao/pt/institucional/not%C3%ADcias/abertura-das-ag%C3%AAncias-e-dos-balc%C3%B5es-aos-s%C3%A1bados/">
                        <div class="inner">
                            <div class="content">
                                <div class="desc">
                                    <h6>Abertura dos Balcões aos Sábados</h6>
                                    <h1>.</h1>
                                    <p> 
                                        </p><div class="see-more">
                                            Saber Mais
                                            

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 22.9 15.4" enable-background="new 0 0 22.9 15.4" xml:space="preserve">
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="0.5" y1="7.7" x2="22.4" y2="7.7"></line>
                	<polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="15.1,0.5
                		22.4,7.8 15.2,14.9 	"></polyline>
                </svg>
            


                                        </div>
                                    <p></p>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            
            
                <div class="slide active" data-photo="2" style="background-image: url('/media/1359/soluções-de-crédito.png')">
                    <a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/conta-poupan%C3%A7a-monami/">
                        <div class="inner">
                            <div class="content">
                                <div class="desc">
                                    <h6>Soluções de Crédito</h6>
                                    <h1>.</h1>
                                    <p> 
                                        </p><div class="see-more">
                                            Saber Mais
                                            

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 22.9 15.4" enable-background="new 0 0 22.9 15.4" xml:space="preserve">
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="0.5" y1="7.7" x2="22.4" y2="7.7"></line>
                	<polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="15.1,0.5
                		22.4,7.8 15.2,14.9 	"></polyline>
                </svg>
            


                                        </div>
                                    <p></p>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            
            
                <div class="slide " data-photo="3" style="background-image: url('/media/1437/886928171-outbound-relaunch-angola-3410x1301-v1.jpg')">
                    <a href="https://www.bci.ao/">
                        <div class="inner">
                            <div class="content">
                                <div class="desc">
                                    <h6>WESTERN UNION</h6>
                                    <h1>.</h1>
                                    <p> 
                                        </p><div class="see-more">
                                            Saber Mais
                                            

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 22.9 15.4" enable-background="new 0 0 22.9 15.4" xml:space="preserve">
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="0.5" y1="7.7" x2="22.4" y2="7.7"></line>
                	<polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="15.1,0.5
                		22.4,7.8 15.2,14.9 	"></polyline>
                </svg>
            


                                        </div>
                                    <p></p>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            
            
                <div class="slide " data-photo="4" style="background-image: url('')">
                    <a href="https://www.bci.ao/media/1486/comunicado-pre%C3%A7%C3%A1rio-bci.pdf">
                        <div class="inner">
                            <div class="content">
                                <div class="desc">
                                    <h6>Comunicado Preçário BCI</h6>
                                    <h1>Preçário II 10 de Novembro de 2022</h1>
                                    <p> 
                                        </p><div class="see-more">
                                            Saber Mais
                                            

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 22.9 15.4" enable-background="new 0 0 22.9 15.4" xml:space="preserve">
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="0.5" y1="7.7" x2="22.4" y2="7.7"></line>
                	<polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="15.1,0.5
                		22.4,7.8 15.2,14.9 	"></polyline>
                </svg>
            


                                        </div>
                                    <p></p>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            

</div>

<div class="homepage-header-menu">
            
                <div class="square" data-photo="1">
                    <div class="inner">
                        <a href="https://www.bci.ao/pt/institucional/not%C3%ADcias/abertura-das-ag%C3%AAncias-e-dos-balc%C3%B5es-aos-s%C3%A1bados/">
                            <div class="wrapper">
                            </div>
                            <div class="content">
                                

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 96.9 82.4" enable-background="new 0 0 96.9 82.4" xml:space="preserve">
                	<rect class="stroke" x="43.2" y="22.8" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" width="11.5" height="45.6"></rect>
                	<rect class="stroke" x="72" y="22.8" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" width="11.5" height="45.6"></rect>
                	<polygon class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="
                	48.5,1.2 95.7,22.8 1.2,22.8"></polygon>
                	<rect class="stroke" x="14.3" y="22.8" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" width="11.5" height="45.6"></rect>
                	<rect class="stroke" x="6.9" y="68.4" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" width="83.1" height="5.7"></rect>
                	<rect class="stroke" x="1.2" y="74.1" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" width="94.5" height="7.1"></rect>
                </svg>
            


                                <h5>Abertura dos Balcões aos Sábados</h5>
                            </div>
                        </a>
                    </div>
                </div>
            
            
                <div class="square active" data-photo="2">
                    <div class="inner">
                        <a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/conta-poupan%C3%A7a-monami/">
                            <div class="wrapper">
                            </div>
                            <div class="content">
                                

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100.2 82.4" enable-background="new 0 0 100.2 82.4" xml:space="preserve">
                    <path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                    M46.2,14.6h-7.1C23.1,14.6,10,27.6,10,43.7c0,10.7,5.8,20.5,15.2,25.6c0.7,0.4,1.1,1.1,1.1,1.8v8.2c0,1,0.8,1.9,1.9,1.9h12.2
                    c1,0,1.9-0.8,1.9-1.9v-4.4c0-1.2,0.9-2.1,2.1-2.1H62c1.2,0,2.1,0.9,2.1,2.1v4.4c0,1,0.8,1.9,1.9,1.9h12.2c1,0,1.9-0.8,1.9-1.9
                    V67.7c0-0.6,0.3-1.2,0.8-1.6c4.4-3.6,7.6-8.4,9.2-13.7c0.2-0.8,0.9-1.4,1.7-1.5l5.7-0.7c1-0.1,1.7-0.9,1.7-1.9V37.8
                    c0-1-0.7-1.8-1.7-1.9l-6.1-0.8c-0.8-0.1-1.4-0.6-1.7-1.4c-1.4-3.9-3.6-7.3-6.3-10.2c-0.2-0.1-0.4-0.3-0.5-0.5
                    c-0.9-0.9-1.8-1.9-2.8-2.8l0,0L82,9c-3.6,0.8-6.5,3.8-7.8,7.3l0,0c-2.5-1.1-5.7-1.8-10.1-1.8h-2.9"></path>
                    <path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                    M78.6,32.1c-0.2-0.2-0.4-0.3-0.7-0.3c-0.3,0-0.5,0.1-0.7,0.3c-0.2,0.2-0.3,0.4-0.3,0.7s0.1,0.5,0.3,0.7c0.2,0.2,0.4,0.3,0.7,0.3
                    c0.3,0,0.5-0.1,0.7-0.3c0.2-0.2,0.3-0.4,0.3-0.7S78.8,32.3,78.6,32.1z"></path>
                    <path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                    M53.7,1.2c-4.9,0-8.8,3.9-8.8,8.8s3.9,8.8,8.8,8.8s8.8-3.9,8.8-8.8S58.5,1.2,53.7,1.2z"></path>
                    <path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                    M1.2,35.6c0,4.9,3.9,8.8,8.8,8.8"></path>
                    <line class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="44.3" y1="22.8" x2="62.1" y2="22.8"></line>
                </svg>
            


                                <h5>Soluções de Crédito</h5>
                            </div>
                        </a>
                    </div>
                </div>
            
            
                <div class="square " data-photo="3">
                    <div class="inner">
                        <a href="https://www.bci.ao/">
                            <div class="wrapper">
                            </div>
                            <div class="content">
                                

            
               <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 93.5 68" enable-background="new 0 0 93.5 68" xml:space="preserve">
                	<path class="fill" fill="#FFFFFF" d="M91.1,2.4v63.2H2.4V2.4H91.1 M93.5,0H0v68h93.5V0L93.5,0z"></path>
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="2.8" y1="65.7" x2="34.8" y2="34.1"></line>
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="57.7" y1="33.9" x2="91.1" y2="65.4"></line>
                	<polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="
                	2.1,2.6 45.7,44.6 91.1,2.3"></polyline>
                </svg>
            


                                <h5>WESTERN UNION</h5>
                            </div>
                        </a>
                    </div>
                </div>
            
            
                <div class="square " data-photo="4">
                    <div class="inner">
                        <a href="https://www.bci.ao/media/1486/comunicado-pre%C3%A7%C3%A1rio-bci.pdf">
                            <div class="wrapper">
                            </div>
                            <div class="content">
                                

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 81.9 81.9" enable-background="new 0 0 81.9 81.9" xml:space="preserve">
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                		M27.5,28.1C13,28.1,1.2,39.9,1.2,54.4S13,80.7,27.5,80.7s26.3-11.8,26.3-26.3S42,28.1,27.5,28.1z"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                		M54.4,53.8c14.5,0,26.3-11.8,26.3-26.3S68.9,1.2,54.4,1.2S28.1,13,28.1,27.5"></path>
                	<path class="fill" fill="#FFFFFF" d="M18.6,49.6c0-0.3,0.1-0.6,0.3-0.8c0.2-0.2,0.5-0.3,0.7-0.3s0.5,0.1,0.7,0.3c0.2,0.2,0.3,0.5,0.3,0.8v4.1
                		h0l2.5-4.5c0.1-0.3,0.3-0.4,0.4-0.5c0.1-0.1,0.3-0.1,0.5-0.1c0.3,0,0.5,0.1,0.7,0.3c0.2,0.2,0.3,0.4,0.3,0.6c0,0.1,0,0.2-0.1,0.4
                		c-0.1,0.1-0.1,0.3-0.2,0.4l-2,3.3l2.4,5c0.1,0.3,0.2,0.5,0.2,0.7c0,0.3-0.1,0.5-0.3,0.6c-0.2,0.2-0.5,0.3-0.8,0.3
                		c-0.3,0-0.5-0.1-0.7-0.2c-0.2-0.1-0.3-0.3-0.4-0.7l-1.8-3.7l-0.9,1.3v2.2c0,0.3-0.1,0.6-0.3,0.8c-0.2,0.2-0.5,0.3-0.7,0.3
                		s-0.5-0.1-0.7-0.3c-0.2-0.2-0.3-0.5-0.3-0.8V49.6z"></path>
                    <path class="fill" fill="#FFFFFF" d="M30.4,50.6c-0.4,0-0.7-0.1-0.8-0.3c-0.2-0.2-0.3-0.4-0.3-0.7c0-0.3,0.1-0.5,0.3-0.7
                		c0.2-0.2,0.5-0.3,0.8-0.3h4.8c0.7,0,1.1,0.3,1.1,0.9c0,0.3-0.1,0.7-0.4,1.1l-4.3,7.3h3.7c0.4,0,0.7,0.1,0.8,0.3
                		c0.2,0.2,0.3,0.4,0.3,0.7c0,0.3-0.1,0.5-0.3,0.7C36,59.9,35.7,60,35.3,60h-5.2c-0.3,0-0.6-0.1-0.8-0.3C29.1,59.5,29,59.3,29,59
                		c0-0.1,0-0.3,0.1-0.4c0-0.1,0.1-0.3,0.3-0.5l4.3-7.4H30.4z"></path>
                	<path class="fill" fill="#FFFFFF" d="M46.6,23.4c0-0.3,0.1-0.5,0.3-0.7c0.2-0.2,0.4-0.3,0.6-0.3s0.5,0.1,0.6,0.3c0.2,0.2,0.3,0.4,0.3,0.7V27h0
                		l2.2-4c0.1-0.2,0.2-0.4,0.4-0.5c0.1-0.1,0.3-0.1,0.5-0.1c0.3,0,0.5,0.1,0.6,0.2c0.2,0.2,0.3,0.3,0.3,0.6c0,0.1,0,0.2-0.1,0.3
                		c0,0.1-0.1,0.3-0.2,0.4l-1.8,2.9l2.1,4.4c0.1,0.3,0.2,0.5,0.2,0.6c0,0.2-0.1,0.4-0.3,0.6c-0.2,0.2-0.4,0.2-0.7,0.2
                		c-0.3,0-0.5-0.1-0.6-0.2c-0.1-0.1-0.3-0.3-0.4-0.6l-1.6-3.3l-0.8,1.1v1.9c0,0.3-0.1,0.5-0.3,0.7c-0.2,0.2-0.4,0.3-0.6,0.3
                		s-0.5-0.1-0.6-0.3c-0.2-0.2-0.3-0.4-0.3-0.7V23.4z"></path>
                	<path class="fill" fill="#FFFFFF" d="M56.9,24.2c-0.3,0-0.6-0.1-0.7-0.2c-0.2-0.2-0.2-0.3-0.2-0.6c0-0.2,0.1-0.4,0.2-0.6
                		c0.2-0.2,0.4-0.2,0.7-0.2h4.2c0.6,0,1,0.3,1,0.8c0,0.3-0.1,0.6-0.3,1L58,30.8h3.2c0.3,0,0.6,0.1,0.7,0.2s0.2,0.3,0.2,0.6
                		c0,0.2-0.1,0.4-0.2,0.6s-0.4,0.2-0.7,0.2h-4.6c-0.3,0-0.5-0.1-0.7-0.3c-0.2-0.2-0.3-0.4-0.3-0.6c0-0.1,0-0.2,0.1-0.4
                		c0-0.1,0.1-0.3,0.2-0.5l3.7-6.5H56.9z"></path>
                </svg>
            


                                <h5>Comunicado Preçário BCI</h5>
                            </div>
                        </a>
                    </div>
                </div>
            

</div>
<div class="mouse animated">
    

            
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 30">
                    <path class="fill" fill="#ffffff" d="M10,2a8,8,0,0,1,8,8V20A8,8,0,1,1,2,20V10a8,8,0,0,1,8-8m0-2h0A10,10,0,0,0,0,10V20A10,10,0,0,0,10,30h0A10,10,0,0,0,20,20V10A10,10,0,0,0,10,0Z M10,8.5a2,2,0,1,0,2,2,2,2,0,0,0-2-2Z"></path>
                </svg>
            


    

            
                <svg version="1.1" class="st" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 16.3 8.6" style="enable-background:new 0 0 16.3 8.6;" xml:space="preserve">
            	    <polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="1,1.1 8.2,7.6 15.3,1 "></polyline>
                </svg>
            


</div>
                






        
            <div class="banner-section">
                        
                            <div class="banner-container image-left">
                                <div class="image">
                                            
                                                <img src="https://www.bci.ao/media/1357/af-bci-net-post-1200x1200-01.jpg" alt="">
                                            

                                </div>
                                <div class="info">
                                    <div class="content">
                                        <div class="desc">
                                            <h2>Ter o seu banco no smartphone? Nada mais simples.</h2>
                                            <p></p><p>Disponível para iOs e Android</p><p></p>
                                        </div>
                                                
                                                    <div class="btn-container align-left">
                                                                
                                                                    <a class="btn" href="https://play.google.com/store/apps/details?id=com.exictos.mbanka.bci.ao&amp;hl=en_US">
                                                                        <span>
                                                                            

            
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 22.21 25">
                    <polygon class="fill" points="16.1 8.44 1.42 0 13.01 11.53 16.1 8.44" fill="#fff" fill-rule="evenodd"></polygon>
                    <path class="fill" d="M.09.09A.67.67,0,0,0,0,.43V24.32a.66.66,0,0,0,0,.21L12.31,12.24Z" fill="#fff" fill-rule="evenodd"></path>
                    <path class="fill" d="M13,13,1,25,1.09,25l15.2-8.75Z" fill="#fff" fill-rule="evenodd"></path>
                    <path class="fill" d="M21.85,11.75,17,9l-3.27,3.28,3.47,3.45L21.85,13A.73.73,0,0,0,21.85,11.75Z" fill="#fff" fill-rule="evenodd"></path>
                </svg>
            


                                                                            Google Play
                                                                        </span>
                                                                    </a>
                                                                
                                                                
                                                                    <a class="btn" href="https://itunes.apple.com/ao/app/bci-mobile/id1113648161?mt=8">
                                                                        <span>
                                                                            

            
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20.34 25">
                    <path class="fill" d="M17,13.29a5.67,5.67,0,0,1,2.7-4.76,5.8,5.8,0,0,0-4.58-2.48c-1.93-.2-3.8,1.15-4.78,1.15S7.82,6.07,6.19,6.1A6.13,6.13,0,0,0,1.05,9.24c-2.22,3.84-.56,9.49,1.57,12.6,1.06,1.52,2.3,3.22,3.93,3.16s2.19-1,4.11-1,2.46,1,4.12,1,2.79-1.53,3.82-3.06a12.71,12.71,0,0,0,1.74-3.55A5.51,5.51,0,0,1,17,13.29Z" fill="#fff"></path>
                    <path class="fill" d="M13.85,4a5.59,5.59,0,0,0,1.28-4,5.66,5.66,0,0,0-3.68,1.91,5.26,5.26,0,0,0-1.31,3.85A4.68,4.68,0,0,0,13.85,4Z" fill="#fff"></path>
                 </svg>
            


                                                                            App Store
                                                                        </span>
                                                                    </a>
                                                                

                                                    </div>
                                                

                                    </div>
                                </div>
                            </div>
                        

            </div>
        
                    
                        <div class="contactos-squares-section">
                            <div class="contactos-squares-container thirds">
                                <div class="title">
                                    <h2>Precisa de apoio? <br>
                                    Fale connosco</h2>
                                </div>
                                <div class="squares">
                                    <div class="row">
                                        <div class="square">
                                            <a href="https://www.bci.ao/pt/apoio-ao-cliente">
                                                <div class="inner">
                                                    <div class="wrapper">
                                                    </div>
                                                    <div class="content">
                                                        

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 60.5 82.4" enable-background="new 0 0 60.5 82.4" xml:space="preserve">
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M32.7,49.2h-5c-9.1,0-16.5-7.4-16.5-16.5V17.7c0-9.1,7.4-16.5,16.5-16.5h5c9.1,0,16.5,7.4,16.5,16.5v14.9
                	C49.3,41.8,41.9,49.2,32.7,49.2z"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M39,48.1v4.7c0,1,0.8,1.9,1.8,2c10.3,0.9,18.5,9.7,18.5,20.3v6.1"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M21.6,48.1v4.7c0,1-0.8,1.9-1.8,2C9.4,55.7,1.2,64.5,1.2,75.1v6.1"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M21,54.2C21,54.2,21,54.2,21,54.2"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M21,54.7c5.1,5.1,13.4,5.1,18.5,0"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M22,26.5c-0.2-0.2-0.4-0.3-0.7-0.3s-0.5,0.1-0.7,0.3c-0.2,0.2-0.3,0.4-0.3,0.7c0,0.3,0.1,0.5,0.3,0.7
                	c0.2,0.2,0.4,0.3,0.7,0.3s0.5-0.1,0.7-0.3c0.2-0.2,0.3-0.4,0.3-0.7C22.3,26.9,22.2,26.7,22,26.5z"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M40,26.5c-0.2-0.2-0.4-0.3-0.7-0.3c-0.3,0-0.5,0.1-0.7,0.3s-0.3,0.4-0.3,0.7c0,0.3,0.1,0.5,0.3,0.7c0.2,0.2,0.4,0.3,0.7,0.3
                	c0.3,0,0.5-0.1,0.7-0.3c0.2-0.2,0.3-0.4,0.3-0.7C40.2,26.9,40.1,26.7,40,26.5z"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                		M22.3,36.9c4.4,4.4,11.6,4.4,16,0"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M11.2,25.2L16,14.8c0.6-1.2,1.8-1.9,3.1-1.8l8.3,0.6c1.9,0.1,3.8,0.1,5.6,0l8.3-0.6c1.3-0.1,2.6,0.6,3.1,1.8l4.9,10.5"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M49.3,25.5L49.3,25.5c1.3-1.3,3.6-0.4,3.6,1.5v0.4c0,0.6-0.2,1.1-0.6,1.5l-2.7,2.7"></path>
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M11.2,25.5L11.2,25.5c-1.3-1.3-3.6-0.4-3.6,1.5v0.4c0,0.6,0.2,1.1,0.6,1.5l2.7,2.7"></path>
                </svg>
            


                                                        <h5>
                                                            <span>Apoio ao cliente</span>
                                                        </h5>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <div class="square">
                                            <a href="tel:923166911" target="_blank">
                                                <div class="inner">
                                                    <div class="wrapper">
                                                    </div>
                                                    <div class="content">
                                                        

            
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 82.5 82.4" enable-background="new 0 0 82.5 82.4" xml:space="preserve">
                	<path class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="
                	M81.2,64.3c0.2,1.3-0.2,2.4-1.2,3.4L68.8,78.9c-0.5,0.6-1.2,1-2,1.4c-0.8,0.4-1.6,0.6-2.4,0.8c-0.1,0-0.2,0-0.5,0
                	c-0.3,0-0.6,0-1.1,0c-1.1,0-2.8-0.2-5.2-0.6c-2.4-0.4-5.3-1.3-8.8-2.7c-3.5-1.4-7.4-3.6-11.8-6.5c-4.4-2.9-9.1-6.8-14.1-11.9
                	c-4-3.9-7.2-7.6-9.8-11.2c-2.6-3.6-4.7-6.9-6.3-9.9c-1.6-3-2.8-5.8-3.6-8.2S1.8,25.7,1.6,24c-0.3-1.8-0.4-3.2-0.3-4.2
                	c0.1-1,0.1-1.6,0.1-1.7c0.1-0.8,0.4-1.6,0.8-2.4c0.4-0.8,0.9-1.5,1.4-2L14.8,2.4c0.8-0.8,1.7-1.2,2.7-1.2c0.7,0,1.4,0.2,1.9,0.6
                	c0.6,0.4,1,0.9,1.4,1.6l9.1,17.2c0.5,0.9,0.6,1.9,0.4,3s-0.7,2-1.4,2.7l-4.2,4.2c-0.1,0.1-0.2,0.3-0.3,0.6s-0.1,0.5-0.1,0.6
                	c0.2,1.2,0.7,2.5,1.5,4.1c0.7,1.4,1.7,3,3.1,5c1.4,1.9,3.4,4.2,6,6.7c2.5,2.6,4.8,4.6,6.8,6.1c2,1.4,3.6,2.5,5,3.2
                	s2.3,1.1,3.1,1.2l1.1,0.2c0.1,0,0.3,0,0.6-0.1c0.3-0.1,0.4-0.2,0.6-0.3l4.8-4.9c1-0.9,2.2-1.4,3.6-1.4c1,0,1.7,0.2,2.3,0.5h0.1
                	l16.4,9.7C80.3,62.3,81,63.2,81.2,64.3z"></path>
                </svg>
            


                                                        <h5>
                                                            <span>Telefone:</span>
                                                            923166911
                                                        </h5>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                        <div class="square">
                                            <a href="mailto:apoioaocliente@bci.ao" target="_blank">
                                                <div class="inner">
                                                    <div class="wrapper">
                                                    </div>
                                                    <div class="content">
                                                        

            
               <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 93.5 68" enable-background="new 0 0 93.5 68" xml:space="preserve">
                	<path class="fill" fill="#FFFFFF" d="M91.1,2.4v63.2H2.4V2.4H91.1 M93.5,0H0v68h93.5V0L93.5,0z"></path>
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="2.8" y1="65.7" x2="34.8" y2="34.1"></line>
                	<line class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="57.7" y1="33.9" x2="91.1" y2="65.4"></line>
                	<polyline class="stroke" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" points="
                	2.1,2.6 45.7,44.6 91.1,2.3"></polyline>
                </svg>
            


                                                        <h5>
                                                            <span>Email:</span>
                                                            geral@bci.ao
                                                        </h5>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    


        
            <div class="banner-section">
                        
                            <div class="banner-container image-left">
                                <div class="image">
                                            
                                                <img src="https://www.bci.ao/media/1173/bci-guia-particulares.png" alt="">
                                            

                                </div>
                                <div class="info">
                                    <div class="content">
                                        <div class="desc">
                                            <h2>Nada como um bom guia para tudo ficar mais simples.</h2>
                                            <p></p><p>Este Guia, elaborado pelo Banco Nacional de Angola, vai tornar ainda mais simples a sua relação com o BCI. Descarregue aqui embaixo</p><p></p>
                                        </div>
                                                
                                                    <div class="btn-container align-left">
                                                                
                                                                    <a class="btn" href="https://www.bci.ao/media/1215/guiaconsumidor.pdf">
                                                                        <span>
                                                                            



                                                                            Descarregar
                                                                        </span>
                                                                    </a>
                                                                

                                                    </div>
                                                

                                    </div>
                                </div>
                            </div>
                        

            </div>
        


        
             <div class="default-half-section">
                <div class="content">
                            
                                <div class="half">
                                    <h3>TV BCI Angola</h3>
                                    <div class="iframe-container"><iframe src="cid:frame-3F2CAF4BE950543E5824147AFE00994E@mhtml.blink" frameborder="0"></iframe></div>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>

                                </div>
                                <div class="half">
                                    <h3>Taxas de câmbio do dia</h3>
                                            
                                                <div class="tabelas-container">
                                                    <div class="tabelas-wrapper">
                                                    
                <div class="tabelas-half">
                    <div class="tabelas-moeda">
                        <h4>Divisas</h4>
                        <h4>100 Kwanzas (AOA)</h4>
                    </div>
                    <div class="tabelas">
                        <div class="header">

                                <div class="cell">
                                    Moedas
                                </div>
                                <div class="cell">
                                    Compra
                                </div>
                                <div class="cell">
                                    Venda
                                </div>

                        </div>
                        <div class="body">
                                <div class="line">
                                    <div class="cell">
                                        EUR
                                    </div>
                                    <div class="cell">
                                        534.462

                                    </div>
                                    <div class="cell">
                                        548.600
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        USD
                                    </div>
                                    <div class="cell">
                                        503.496

                                    </div>
                                    <div class="cell">
                                        515.773
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        CAD
                                    </div>
                                    <div class="cell">
                                        373.098

                                    </div>
                                    <div class="cell">
                                        380.703
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        GBP
                                    </div>
                                    <div class="cell">
                                        605.857

                                    </div>
                                    <div class="cell">
                                        618.206
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        ZAR
                                    </div>
                                    <div class="cell">
                                        29.548

                                    </div>
                                    <div class="cell">
                                        30.150
                                    </div>
                                </div>
                        </div>
                    </div>
                </div>
            
                <div class="tabelas-half">
                    <div class="tabelas-moeda">
                        <h4>Notas</h4>
                        <h4>100 Kwanzas (AOA)</h4>
                    </div>
                    <div class="tabelas">
                        <div class="header">

                                <div class="cell">
                                    Moedas
                                </div>
                                <div class="cell">
                                    Compra
                                </div>
                                <div class="cell">
                                    Venda
                                </div>

                        </div>
                        <div class="body">
                                <div class="line">
                                    <div class="cell">
                                        EUR
                                    </div>
                                    <div class="cell">
                                        534.462

                                    </div>
                                    <div class="cell">
                                        548.600
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        USD
                                    </div>
                                    <div class="cell">
                                        503.496

                                    </div>
                                    <div class="cell">
                                        515.773
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        CAD
                                    </div>
                                    <div class="cell">
                                        373.098

                                    </div>
                                    <div class="cell">
                                        380.703
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        GBP
                                    </div>
                                    <div class="cell">
                                        605.857

                                    </div>
                                    <div class="cell">
                                        618.206
                                    </div>
                                </div>
                                <div class="line">
                                    <div class="cell">
                                        ZAR
                                    </div>
                                    <div class="cell">
                                        29.548

                                    </div>
                                    <div class="cell">
                                        30.150
                                    </div>
                                </div>
                        </div>
                    </div>
                </div>
            </div>
                                                    <p class="tabela-fonte">Actualizado em <span class="update-currency-time">2023-01-06T12:00:00.000Z</span></p>
                                                </div>
                                            

                                </div>
                            

                </div>
            </div>
        


        
            <div class="banner-section">
                        
                            <div class="banner-container image-left">
                                <div class="image">

                                </div>
                                <div class="info">
                                    <div class="content">
                                        <div class="desc">
                                            <h2>Preçário</h2>
                                            <p></p>
                                        </div>
                                                
                                                    <div class="btn-container align-left">
                                                                
                                                                    <a class="btn" href="https://www.bci.ao/media/1429/bci_pre_outros-clientes-09102022.pdf">
                                                                        <span>
                                                                            



                                                                            Empresas
                                                                        </span>
                                                                    </a>
                                                                
                                                                
                                                                    <a class="btn" href="https://www.bci.ao/media/1428/particulares-20221009.pdf">
                                                                        <span>
                                                                            



                                                                            Particulares
                                                                        </span>
                                                                    </a>
                                                                

                                                    </div>
                                                

                                    </div>
                                </div>
                            </div>
                        

            </div>
        


            </div>
        </div>
        <footer class="footer">
            <div class="footer-upper">
                <div class="content">
                    <div class="footer-logo">
                       <a href="https://www.bci.ao/"> <img src="https://www.bci.ao/media/1102/logo_grey.svg"></a>
                    </div>
                    <div class="footer-upper-links">
                        







        
            <div data-menu-id="0"> <!-- Parent id container -->
                <h6>Particulares</h6>
                <ul>
                            
                                <li><a href="https://www.bci.ao/pt/conta-a-ordem/" id="menuTop0">Conta à Ordem</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/particulares/poupan%C3%A7a/" id="menuTop1306">Poupança</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/particulares/seguran%C3%A7a/" id="menuTop1309">Segurança</a></li>
                            

                </ul>
            </div>
        
        
            <div data-menu-id="0"> <!-- Parent id container -->
                <h6>Empresas</h6>
                <ul>
                            
                                <li><a href="https://www.bci.ao/pt/empresas/contas/" id="menuTop0">Contas</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/empresas/dep%C3%B3sitos/" id="menuTop1368">Depósitos</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/empresas/investimento/" id="menuTop1357">Investimento</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/empresas/pagamento-de-impostos/" id="menuTop1281">Pagamento de Impostos</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/empresas/seguran%C3%A7a-empresas/" id="menuTop1370">Segurança</a></li>
                            

                </ul>
            </div>
        
        
            <div data-menu-id="1833"> <!-- Parent id container -->
                <h6>Institucional</h6>
                <ul>
                            
                                <li><a href="https://www.bci.ao/pt/institucional/noticias/" id="menuTop0">Notícias</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/institucional/clipping/" id="menuTop1395">Clipping</a></li>
                            
                            
                                <li><a href="https://www.bci.ao/pt/institucional/dicion%C3%A1rio-financeiro/" id="menuTop1429">Dicionário Financeiro</a></li>
                            

                </ul>
            </div>
        

 
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <div class="content">
                    <p class="all-rights-reserved">BCI © Todos os direitos reservados</p>
        
                    <ul class="footer-bottom-links">
                        <li><a href="https://www.bci.ao/">Início</a></li>
                        <li><a href="https://www.bci.ao/pt/mapa-de-site">Mapa do Site</a></li>
                        <li><a href="https://www.bci.ao/pt/termos-e-condi%C3%A7%C3%B5es/">Termos e condições</a></li>
                        <li><a href="https://www.bci.ao/media/1430/bci_pre_cliente-particulares-e-outros-clientes-20230105.pdf" target="_blank">Preçário</a></li>
                    </ul>
        
                    <ul class="footer-social-links">
                        <li><a href="https://www.facebook.com/bciangola/" target="_blank"><i class="fab fa-facebook-square"></i></a></li>
                        <li><a href="https://www.youtube.com/channel/UCOOhBqKFT5jR3aTHIQVm8mA" target="_blank"><i class="fab fa-youtube"></i></a></li>
                        <li><a href="https://www.linkedin.com/in/bci-angola-a8127612a" target="_blank"><i class="fab fa-linkedin"></i></a></li>
                        <li><a href="https://www.instagram.com/bciangola" target="_blank"><i class="fab fa-instagram"></i></a></li>
                        <li><a href="https://twitter.com/VGerviz" target="_blank"><i class="fab fa-twitter"></i></a></li>
                    </ul>
                   
                </div>
            </div>
        </footer>

        
        
        
        
            
        

    


    
</body></html>
------MultipartBoundary--B35gv9hf8GVvnlqnSn2OQfMwBE5Ga2VECPMKOPmjLS----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.bci.ao/css/font-awesome-572.css

@charset "utf-8";

.fa, .fas, .far, .fal, .fab { -webkit-font-smoothing: antialiased; display: inline-block; font-style: normal; font-variant: normal; text-rendering: auto; line-height: 1; }

.fa-lg { font-size: 1.33333em; line-height: 0.75em; vertical-align: -0.0667em; }

.fa-xs { font-size: 0.75em; }

.fa-sm { font-size: 0.875em; }

.fa-1x { font-size: 1em; }

.fa-2x { font-size: 2em; }

.fa-3x { font-size: 3em; }

.fa-4x { font-size: 4em; }

.fa-5x { font-size: 5em; }

.fa-6x { font-size: 6em; }

.fa-7x { font-size: 7em; }

.fa-8x { font-size: 8em; }

.fa-9x { font-size: 9em; }

.fa-10x { font-size: 10em; }

.fa-fw { text-align: center; width: 1.25em; }

.fa-ul { list-style-type: none; margin-left: 2.5em; padding-left: 0px; }

.fa-ul > li { position: relative; }

.fa-li { left: -2em; position: absolute; text-align: center; width: 2em; line-height: inherit; }

.fa-border { border: 0.08em solid rgb(238, 238, 238); border-radius: 0.1em; padding: 0.2em 0.25em 0.15em; }

.fa-pull-left { float: left; }

.fa-pull-right { float: right; }

.fa.fa-pull-left, .fas.fa-pull-left, .far.fa-pull-left, .fal.fa-pull-left, .fab.fa-pull-left { margin-right: 0.3em; }

.fa.fa-pull-right, .fas.fa-pull-right, .far.fa-pull-right, .fal.fa-pull-right, .fab.fa-pull-right { margin-left: 0.3em; }

.fa-spin { animation: 2s linear 0s infinite normal none running fa-spin; }

.fa-pulse { animation: 1s steps(8) 0s infinite normal none running fa-spin; }

@-webkit-keyframes fa-spin { 
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes fa-spin { 
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.fa-rotate-90 { transform: rotate(90deg); }

.fa-rotate-180 { transform: rotate(180deg); }

.fa-rotate-270 { transform: rotate(270deg); }

.fa-flip-horizontal { transform: scale(-1, 1); }

.fa-flip-vertical { transform: scale(1, -1); }

.fa-flip-both, .fa-flip-horizontal.fa-flip-vertical { transform: scale(-1, -1); }

:root .fa-rotate-90, :root .fa-rotate-180, :root .fa-rotate-270, :root .fa-flip-horizontal, :root .fa-flip-vertical, :root .fa-flip-both { filter: none; }

.fa-stack { display: inline-block; height: 2em; line-height: 2em; position: relative; vertical-align: middle; width: 2.5em; }

.fa-stack-1x, .fa-stack-2x { left: 0px; position: absolute; text-align: center; width: 100%; }

.fa-stack-1x { line-height: inherit; }

.fa-stack-2x { font-size: 2em; }

.fa-inverse { color: rgb(255, 255, 255); }

.fa-500px::before { content: ""; }

.fa-accessible-icon::before { content: ""; }

.fa-accusoft::before { content: ""; }

.fa-acquisitions-incorporated::before { content: ""; }

.fa-ad::before { content: ""; }

.fa-address-book::before { content: ""; }

.fa-address-card::before { content: ""; }

.fa-adjust::before { content: ""; }

.fa-adn::before { content: ""; }

.fa-adobe::before { content: ""; }

.fa-adversal::before { content: ""; }

.fa-affiliatetheme::before { content: ""; }

.fa-air-freshener::before { content: ""; }

.fa-algolia::before { content: ""; }

.fa-align-center::before { content: ""; }

.fa-align-justify::before { content: ""; }

.fa-align-left::before { content: ""; }

.fa-align-right::before { content: ""; }

.fa-alipay::before { content: ""; }

.fa-allergies::before { content: ""; }

.fa-amazon::before { content: ""; }

.fa-amazon-pay::before { content: ""; }

.fa-ambulance::before { content: ""; }

.fa-american-sign-language-interpreting::before { content: ""; }

.fa-amilia::before { content: ""; }

.fa-anchor::before { content: ""; }

.fa-android::before { content: ""; }

.fa-angellist::before { content: ""; }

.fa-angle-double-down::before { content: ""; }

.fa-angle-double-left::before { content: ""; }

.fa-angle-double-right::before { content: ""; }

.fa-angle-double-up::before { content: ""; }

.fa-angle-down::before { content: ""; }

.fa-angle-left::before { content: ""; }

.fa-angle-right::before { content: ""; }

.fa-angle-up::before { content: ""; }

.fa-angry::before { content: ""; }

.fa-angrycreative::before { content: ""; }

.fa-angular::before { content: ""; }

.fa-ankh::before { content: ""; }

.fa-app-store::before { content: ""; }

.fa-app-store-ios::before { content: ""; }

.fa-apper::before { content: ""; }

.fa-apple::before { content: ""; }

.fa-apple-alt::before { content: ""; }

.fa-apple-pay::before { content: ""; }

.fa-archive::before { content: ""; }

.fa-archway::before { content: ""; }

.fa-arrow-alt-circle-down::before { content: ""; }

.fa-arrow-alt-circle-left::before { content: ""; }

.fa-arrow-alt-circle-right::before { content: ""; }

.fa-arrow-alt-circle-up::before { content: ""; }

.fa-arrow-circle-down::before { content: ""; }

.fa-arrow-circle-left::before { content: ""; }

.fa-arrow-circle-right::before { content: ""; }

.fa-arrow-circle-up::before { content: ""; }

.fa-arrow-down::before { content: ""; }

.fa-arrow-left::before { content: ""; }

.fa-arrow-right::before { content: ""; }

.fa-arrow-up::before { content: ""; }

.fa-arrows-alt::before { content: ""; }

.fa-arrows-alt-h::before { content: ""; }

.fa-arrows-alt-v::before { content: ""; }

.fa-artstation::before { content: ""; }

.fa-assistive-listening-systems::before { content: ""; }

.fa-asterisk::before { content: ""; }

.fa-asymmetrik::before { content: ""; }

.fa-at::before { content: ""; }

.fa-atlas::before { content: ""; }

.fa-atlassian::before { content: ""; }

.fa-atom::before { content: ""; }

.fa-audible::before { content: ""; }

.fa-audio-description::before { content: ""; }

.fa-autoprefixer::before { content: ""; }

.fa-avianex::before { content: ""; }

.fa-aviato::before { content: ""; }

.fa-award::before { content: ""; }

.fa-aws::before { content: ""; }

.fa-baby::before { content: ""; }

.fa-baby-carriage::before { content: ""; }

.fa-backspace::before { content: ""; }

.fa-backward::before { content: ""; }

.fa-bacon::before { content: ""; }

.fa-balance-scale::before { content: ""; }

.fa-ban::before { content: ""; }

.fa-band-aid::before { content: ""; }

.fa-bandcamp::before { content: ""; }

.fa-barcode::before { content: ""; }

.fa-bars::before { content: ""; }

.fa-baseball-ball::before { content: ""; }

.fa-basketball-ball::before { content: ""; }

.fa-bath::before { content: ""; }

.fa-battery-empty::before { content: ""; }

.fa-battery-full::before { content: ""; }

.fa-battery-half::before { content: ""; }

.fa-battery-quarter::before { content: ""; }

.fa-battery-three-quarters::before { content: ""; }

.fa-bed::before { content: ""; }

.fa-beer::before { content: ""; }

.fa-behance::before { content: ""; }

.fa-behance-square::before { content: ""; }

.fa-bell::before { content: ""; }

.fa-bell-slash::before { content: ""; }

.fa-bezier-curve::before { content: ""; }

.fa-bible::before { content: ""; }

.fa-bicycle::before { content: ""; }

.fa-bimobject::before { content: ""; }

.fa-binoculars::before { content: ""; }

.fa-biohazard::before { content: ""; }

.fa-birthday-cake::before { content: ""; }

.fa-bitbucket::before { content: ""; }

.fa-bitcoin::before { content: ""; }

.fa-bity::before { content: ""; }

.fa-black-tie::before { content: ""; }

.fa-blackberry::before { content: ""; }

.fa-blender::before { content: ""; }

.fa-blender-phone::before { content: ""; }

.fa-blind::before { content: ""; }

.fa-blog::before { content: ""; }

.fa-blogger::before { content: ""; }

.fa-blogger-b::before { content: ""; }

.fa-bluetooth::before { content: ""; }

.fa-bluetooth-b::before { content: ""; }

.fa-bold::before { content: ""; }

.fa-bolt::before { content: ""; }

.fa-bomb::before { content: ""; }

.fa-bone::before { content: ""; }

.fa-bong::before { content: ""; }

.fa-book::before { content: ""; }

.fa-book-dead::before { content: ""; }

.fa-book-medical::before { content: ""; }

.fa-book-open::before { content: ""; }

.fa-book-reader::before { content: ""; }

.fa-bookmark::before { content: ""; }

.fa-bowling-ball::before { content: ""; }

.fa-box::before { content: ""; }

.fa-box-open::before { content: ""; }

.fa-boxes::before { content: ""; }

.fa-braille::before { content: ""; }

.fa-brain::before { content: ""; }

.fa-bread-slice::before { content: ""; }

.fa-briefcase::before { content: ""; }

.fa-briefcase-medical::before { content: ""; }

.fa-broadcast-tower::before { content: ""; }

.fa-broom::before { content: ""; }

.fa-brush::before { content: ""; }

.fa-btc::before { content: ""; }

.fa-bug::before { content: ""; }

.fa-building::before { content: ""; }

.fa-bullhorn::before { content: ""; }

.fa-bullseye::before { content: ""; }

.fa-burn::before { content: ""; }

.fa-buromobelexperte::before { content: ""; }

.fa-bus::before { content: ""; }

.fa-bus-alt::before { content: ""; }

.fa-business-time::before { content: ""; }

.fa-buysellads::before { content: ""; }

.fa-calculator::before { content: ""; }

.fa-calendar::before { content: ""; }

.fa-calendar-alt::before { content: ""; }

.fa-calendar-check::before { content: ""; }

.fa-calendar-day::before { content: ""; }

.fa-calendar-minus::before { content: ""; }

.fa-calendar-plus::before { content: ""; }

.fa-calendar-times::before { content: ""; }

.fa-calendar-week::before { content: ""; }

.fa-camera::before { content: ""; }

.fa-camera-retro::before { content: ""; }

.fa-campground::before { content: ""; }

.fa-canadian-maple-leaf::before { content: ""; }

.fa-candy-cane::before { content: ""; }

.fa-cannabis::before { content: ""; }

.fa-capsules::before { content: ""; }

.fa-car::before { content: ""; }

.fa-car-alt::before { content: ""; }

.fa-car-battery::before { content: ""; }

.fa-car-crash::before { content: ""; }

.fa-car-side::before { content: ""; }

.fa-caret-down::before { content: ""; }

.fa-caret-left::before { content: ""; }

.fa-caret-right::before { content: ""; }

.fa-caret-square-down::before { content: ""; }

.fa-caret-square-left::before { content: ""; }

.fa-caret-square-right::before { content: ""; }

.fa-caret-square-up::before { content: ""; }

.fa-caret-up::before { content: ""; }

.fa-carrot::before { content: ""; }

.fa-cart-arrow-down::before { content: ""; }

.fa-cart-plus::before { content: ""; }

.fa-cash-register::before { content: ""; }

.fa-cat::before { content: ""; }

.fa-cc-amazon-pay::before { content: ""; }

.fa-cc-amex::before { content: ""; }

.fa-cc-apple-pay::before { content: ""; }

.fa-cc-diners-club::before { content: ""; }

.fa-cc-discover::before { content: ""; }

.fa-cc-jcb::before { content: ""; }

.fa-cc-mastercard::before { content: ""; }

.fa-cc-paypal::before { content: ""; }

.fa-cc-stripe::before { content: ""; }

.fa-cc-visa::before { content: ""; }

.fa-centercode::before { content: ""; }

.fa-centos::before { content: ""; }

.fa-certificate::before { content: ""; }

.fa-chair::before { content: ""; }

.fa-chalkboard::before { content: ""; }

.fa-chalkboard-teacher::before { content: ""; }

.fa-charging-station::before { content: ""; }

.fa-chart-area::before { content: ""; }

.fa-chart-bar::before { content: ""; }

.fa-chart-line::before { content: ""; }

.fa-chart-pie::before { content: ""; }

.fa-check::before { content: ""; }

.fa-check-circle::before { content: ""; }

.fa-check-double::before { content: ""; }

.fa-check-square::before { content: ""; }

.fa-cheese::before { content: ""; }

.fa-chess::before { content: ""; }

.fa-chess-bishop::before { content: ""; }

.fa-chess-board::before { content: ""; }

.fa-chess-king::before { content: ""; }

.fa-chess-knight::before { content: ""; }

.fa-chess-pawn::before { content: ""; }

.fa-chess-queen::before { content: ""; }

.fa-chess-rook::before { content: ""; }

.fa-chevron-circle-down::before { content: ""; }

.fa-chevron-circle-left::before { content: ""; }

.fa-chevron-circle-right::before { content: ""; }

.fa-chevron-circle-up::before { content: ""; }

.fa-chevron-down::before { content: ""; }

.fa-chevron-left::before { content: ""; }

.fa-chevron-right::before { content: ""; }

.fa-chevron-up::before { content: ""; }

.fa-child::before { content: ""; }

.fa-chrome::before { content: ""; }

.fa-church::before { content: ""; }

.fa-circle::before { content: ""; }

.fa-circle-notch::before { content: ""; }

.fa-city::before { content: ""; }

.fa-clinic-medical::before { content: ""; }

.fa-clipboard::before { content: ""; }

.fa-clipboard-check::before { content: ""; }

.fa-clipboard-list::before { content: ""; }

.fa-clock::before { content: ""; }

.fa-clone::before { content: ""; }

.fa-closed-captioning::before { content: ""; }

.fa-cloud::before { content: ""; }

.fa-cloud-download-alt::before { content: ""; }

.fa-cloud-meatball::before { content: ""; }

.fa-cloud-moon::before { content: ""; }

.fa-cloud-moon-rain::before { content: ""; }

.fa-cloud-rain::before { content: ""; }

.fa-cloud-showers-heavy::before { content: ""; }

.fa-cloud-sun::before { content: ""; }

.fa-cloud-sun-rain::before { content: ""; }

.fa-cloud-upload-alt::before { content: ""; }

.fa-cloudscale::before { content: ""; }

.fa-cloudsmith::before { content: ""; }

.fa-cloudversify::before { content: ""; }

.fa-cocktail::before { content: ""; }

.fa-code::before { content: ""; }

.fa-code-branch::before { content: ""; }

.fa-codepen::before { content: ""; }

.fa-codiepie::before { content: ""; }

.fa-coffee::before { content: ""; }

.fa-cog::before { content: ""; }

.fa-cogs::before { content: ""; }

.fa-coins::before { content: ""; }

.fa-columns::before { content: ""; }

.fa-comment::before { content: ""; }

.fa-comment-alt::before { content: ""; }

.fa-comment-dollar::before { content: ""; }

.fa-comment-dots::before { content: ""; }

.fa-comment-medical::before { content: ""; }

.fa-comment-slash::before { content: ""; }

.fa-comments::before { content: ""; }

.fa-comments-dollar::before { content: ""; }

.fa-compact-disc::before { content: ""; }

.fa-compass::before { content: ""; }

.fa-compress::before { content: ""; }

.fa-compress-arrows-alt::before { content: ""; }

.fa-concierge-bell::before { content: ""; }

.fa-confluence::before { content: ""; }

.fa-connectdevelop::before { content: ""; }

.fa-contao::before { content: ""; }

.fa-cookie::before { content: ""; }

.fa-cookie-bite::before { content: ""; }

.fa-copy::before { content: ""; }

.fa-copyright::before { content: ""; }

.fa-couch::before { content: ""; }

.fa-cpanel::before { content: ""; }

.fa-creative-commons::before { content: ""; }

.fa-creative-commons-by::before { content: ""; }

.fa-creative-commons-nc::before { content: ""; }

.fa-creative-commons-nc-eu::before { content: ""; }

.fa-creative-commons-nc-jp::before { content: ""; }

.fa-creative-commons-nd::before { content: ""; }

.fa-creative-commons-pd::before { content: ""; }

.fa-creative-commons-pd-alt::before { content: ""; }

.fa-creative-commons-remix::before { content: ""; }

.fa-creative-commons-sa::before { content: ""; }

.fa-creative-commons-sampling::before { content: ""; }

.fa-creative-commons-sampling-plus::before { content: ""; }

.fa-creative-commons-share::before { content: ""; }

.fa-creative-commons-zero::before { content: ""; }

.fa-credit-card::before { content: ""; }

.fa-critical-role::before { content: ""; }

.fa-crop::before { content: ""; }

.fa-crop-alt::before { content: ""; }

.fa-cross::before { content: ""; }

.fa-crosshairs::before { content: ""; }

.fa-crow::before { content: ""; }

.fa-crown::before { content: ""; }

.fa-crutch::before { content: ""; }

.fa-css3::before { content: ""; }

.fa-css3-alt::before { content: ""; }

.fa-cube::before { content: ""; }

.fa-cubes::before { content: ""; }

.fa-cut::before { content: ""; }

.fa-cuttlefish::before { content: ""; }

.fa-d-and-d::before { content: ""; }

.fa-d-and-d-beyond::before { content: ""; }

.fa-dashcube::before { content: ""; }

.fa-database::before { content: ""; }

.fa-deaf::before { content: ""; }

.fa-delicious::before { content: ""; }

.fa-democrat::before { content: ""; }

.fa-deploydog::before { content: ""; }

.fa-deskpro::before { content: ""; }

.fa-desktop::before { content: ""; }

.fa-dev::before { content: ""; }

.fa-deviantart::before { content: ""; }

.fa-dharmachakra::before { content: ""; }

.fa-dhl::before { content: ""; }

.fa-diagnoses::before { content: ""; }

.fa-diaspora::before { content: ""; }

.fa-dice::before { content: ""; }

.fa-dice-d20::before { content: ""; }

.fa-dice-d6::before { content: ""; }

.fa-dice-five::before { content: ""; }

.fa-dice-four::before { content: ""; }

.fa-dice-one::before { content: ""; }

.fa-dice-six::before { content: ""; }

.fa-dice-three::before { content: ""; }

.fa-dice-two::before { content: ""; }

.fa-digg::before { content: ""; }

.fa-digital-ocean::before { content: ""; }

.fa-digital-tachograph::before { content: ""; }

.fa-directions::before { content: ""; }

.fa-discord::before { content: ""; }

.fa-discourse::before { content: ""; }

.fa-divide::before { content: ""; }

.fa-dizzy::before { content: ""; }

.fa-dna::before { content: ""; }

.fa-dochub::before { content: ""; }

.fa-docker::before { content: ""; }

.fa-dog::before { content: ""; }

.fa-dollar-sign::before { content: ""; }

.fa-dolly::before { content: ""; }

.fa-dolly-flatbed::before { content: ""; }

.fa-donate::before { content: ""; }

.fa-door-closed::before { content: ""; }

.fa-door-open::before { content: ""; }

.fa-dot-circle::before { content: ""; }

.fa-dove::before { content: ""; }

.fa-download::before { content: ""; }

.fa-draft2digital::before { content: ""; }

.fa-drafting-compass::before { content: ""; }

.fa-dragon::before { content: ""; }

.fa-draw-polygon::before { content: ""; }

.fa-dribbble::before { content: ""; }

.fa-dribbble-square::before { content: ""; }

.fa-dropbox::before { content: ""; }

.fa-drum::before { content: ""; }

.fa-drum-steelpan::before { content: ""; }

.fa-drumstick-bite::before { content: ""; }

.fa-drupal::before { content: ""; }

.fa-dumbbell::before { content: ""; }

.fa-dumpster::before { content: ""; }

.fa-dumpster-fire::before { content: ""; }

.fa-dungeon::before { content: ""; }

.fa-dyalog::before { content: ""; }

.fa-earlybirds::before { content: ""; }

.fa-ebay::before { content: ""; }

.fa-edge::before { content: ""; }

.fa-edit::before { content: ""; }

.fa-egg::before { content: ""; }

.fa-eject::before { content: ""; }

.fa-elementor::before { content: ""; }

.fa-ellipsis-h::before { content: ""; }

.fa-ellipsis-v::before { content: ""; }

.fa-ello::before { content: ""; }

.fa-ember::before { content: ""; }

.fa-empire::before { content: ""; }

.fa-envelope::before { content: ""; }

.fa-envelope-open::before { content: ""; }

.fa-envelope-open-text::before { content: ""; }

.fa-envelope-square::before { content: ""; }

.fa-envira::before { content: ""; }

.fa-equals::before { content: ""; }

.fa-eraser::before { content: ""; }

.fa-erlang::before { content: ""; }

.fa-ethereum::before { content: ""; }

.fa-ethernet::before { content: ""; }

.fa-etsy::before { content: ""; }

.fa-euro-sign::before { content: ""; }

.fa-exchange-alt::before { content: ""; }

.fa-exclamation::before { content: ""; }

.fa-exclamation-circle::before { content: ""; }

.fa-exclamation-triangle::before { content: ""; }

.fa-expand::before { content: ""; }

.fa-expand-arrows-alt::before { content: ""; }

.fa-expeditedssl::before { content: ""; }

.fa-external-link-alt::before { content: ""; }

.fa-external-link-square-alt::before { content: ""; }

.fa-eye::before { content: ""; }

.fa-eye-dropper::before { content: ""; }

.fa-eye-slash::before { content: ""; }

.fa-facebook::before { content: ""; }

.fa-facebook-f::before { content: ""; }

.fa-facebook-messenger::before { content: ""; }

.fa-facebook-square::before { content: ""; }

.fa-fantasy-flight-games::before { content: ""; }

.fa-fast-backward::before { content: ""; }

.fa-fast-forward::before { content: ""; }

.fa-fax::before { content: ""; }

.fa-feather::before { content: ""; }

.fa-feather-alt::before { content: ""; }

.fa-fedex::before { content: ""; }

.fa-fedora::before { content: ""; }

.fa-female::before { content: ""; }

.fa-fighter-jet::before { content: ""; }

.fa-figma::before { content: ""; }

.fa-file::before { content: ""; }

.fa-file-alt::before { content: ""; }

.fa-file-archive::before { content: ""; }

.fa-file-audio::before { content: ""; }

.fa-file-code::before { content: ""; }

.fa-file-contract::before { content: ""; }

.fa-file-csv::before { content: ""; }

.fa-file-download::before { content: ""; }

.fa-file-excel::before { content: ""; }

.fa-file-export::before { content: ""; }

.fa-file-image::before { content: ""; }

.fa-file-import::before { content: ""; }

.fa-file-invoice::before { content: ""; }

.fa-file-invoice-dollar::before { content: ""; }

.fa-file-medical::before { content: ""; }

.fa-file-medical-alt::before { content: ""; }

.fa-file-pdf::before { content: ""; }

.fa-file-powerpoint::before { content: ""; }

.fa-file-prescription::before { content: ""; }

.fa-file-signature::before { content: ""; }

.fa-file-upload::before { content: ""; }

.fa-file-video::before { content: ""; }

.fa-file-word::before { content: ""; }

.fa-fill::before { content: ""; }

.fa-fill-drip::before { content: ""; }

.fa-film::before { content: ""; }

.fa-filter::before { content: ""; }

.fa-fingerprint::before { content: ""; }

.fa-fire::before { content: ""; }

.fa-fire-alt::before { content: ""; }

.fa-fire-extinguisher::before { content: ""; }

.fa-firefox::before { content: ""; }

.fa-first-aid::before { content: ""; }

.fa-first-order::before { content: ""; }

.fa-first-order-alt::before { content: ""; }

.fa-firstdraft::before { content: ""; }

.fa-fish::before { content: ""; }

.fa-fist-raised::before { content: ""; }

.fa-flag::before { content: ""; }

.fa-flag-checkered::before { content: ""; }

.fa-flag-usa::before { content: ""; }

.fa-flask::before { content: ""; }

.fa-flickr::before { content: ""; }

.fa-flipboard::before { content: ""; }

.fa-flushed::before { content: ""; }

.fa-fly::before { content: ""; }

.fa-folder::before { content: ""; }

.fa-folder-minus::before { content: ""; }

.fa-folder-open::before { content: ""; }

.fa-folder-plus::before { content: ""; }

.fa-font::before { content: ""; }

.fa-font-awesome::before { content: ""; }

.fa-font-awesome-alt::before { content: ""; }

.fa-font-awesome-flag::before { content: ""; }

.fa-font-awesome-logo-full::before { content: ""; }

.fa-fonticons::before { content: ""; }

.fa-fonticons-fi::before { content: ""; }

.fa-football-ball::before { content: ""; }

.fa-fort-awesome::before { content: ""; }

.fa-fort-awesome-alt::before { content: ""; }

.fa-forumbee::before { content: ""; }

.fa-forward::before { content: ""; }

.fa-foursquare::before { content: ""; }

.fa-free-code-camp::before { content: ""; }

.fa-freebsd::before { content: ""; }

.fa-frog::before { content: ""; }

.fa-frown::before { content: ""; }

.fa-frown-open::before { content: ""; }

.fa-fulcrum::before { content: ""; }

.fa-funnel-dollar::before { content: ""; }

.fa-futbol::before { content: ""; }

.fa-galactic-republic::before { content: ""; }

.fa-galactic-senate::before { content: ""; }

.fa-gamepad::before { content: ""; }

.fa-gas-pump::before { content: ""; }

.fa-gavel::before { content: ""; }

.fa-gem::before { content: ""; }

.fa-genderless::before { content: ""; }

.fa-get-pocket::before { content: ""; }

.fa-gg::before { content: ""; }

.fa-gg-circle::before { content: ""; }

.fa-ghost::before { content: ""; }

.fa-gift::before { content: ""; }

.fa-gifts::before { content: ""; }

.fa-git::before { content: ""; }

.fa-git-square::before { content: ""; }

.fa-github::before { content: ""; }

.fa-github-alt::before { content: ""; }

.fa-github-square::before { content: ""; }

.fa-gitkraken::before { content: ""; }

.fa-gitlab::before { content: ""; }

.fa-gitter::before { content: ""; }

.fa-glass-cheers::before { content: ""; }

.fa-glass-martini::before { content: ""; }

.fa-glass-martini-alt::before { content: ""; }

.fa-glass-whiskey::before { content: ""; }

.fa-glasses::before { content: ""; }

.fa-glide::before { content: ""; }

.fa-glide-g::before { content: ""; }

.fa-globe::before { content: ""; }

.fa-globe-africa::before { content: ""; }

.fa-globe-americas::before { content: ""; }

.fa-globe-asia::before { content: ""; }

.fa-globe-europe::before { content: ""; }

.fa-gofore::before { content: ""; }

.fa-golf-ball::before { content: ""; }

.fa-goodreads::before { content: ""; }

.fa-goodreads-g::before { content: ""; }

.fa-google::before { content: ""; }

.fa-google-drive::before { content: ""; }

.fa-google-play::before { content: ""; }

.fa-google-plus::before { content: ""; }

.fa-google-plus-g::before { content: ""; }

.fa-google-plus-square::before { content: ""; }

.fa-google-wallet::before { content: ""; }

.fa-gopuram::before { content: ""; }

.fa-graduation-cap::before { content: ""; }

.fa-gratipay::before { content: ""; }

.fa-grav::before { content: ""; }

.fa-greater-than::before { content: ""; }

.fa-greater-than-equal::before { content: ""; }

.fa-grimace::before { content: ""; }

.fa-grin::before { content: ""; }

.fa-grin-alt::before { content: ""; }

.fa-grin-beam::before { content: ""; }

.fa-grin-beam-sweat::before { content: ""; }

.fa-grin-hearts::before { content: ""; }

.fa-grin-squint::before { content: ""; }

.fa-grin-squint-tears::before { content: ""; }

.fa-grin-stars::before { content: ""; }

.fa-grin-tears::before { content: ""; }

.fa-grin-tongue::before { content: ""; }

.fa-grin-tongue-squint::before { content: ""; }

.fa-grin-tongue-wink::before { content: ""; }

.fa-grin-wink::before { content: ""; }

.fa-grip-horizontal::before { content: ""; }

.fa-grip-lines::before { content: ""; }

.fa-grip-lines-vertical::before { content: ""; }

.fa-grip-vertical::before { content: ""; }

.fa-gripfire::before { content: ""; }

.fa-grunt::before { content: ""; }

.fa-guitar::before { content: ""; }

.fa-gulp::before { content: ""; }

.fa-h-square::before { content: ""; }

.fa-hacker-news::before { content: ""; }

.fa-hacker-news-square::before { content: ""; }

.fa-hackerrank::before { content: ""; }

.fa-hamburger::before { content: ""; }

.fa-hammer::before { content: ""; }

.fa-hamsa::before { content: ""; }

.fa-hand-holding::before { content: ""; }

.fa-hand-holding-heart::before { content: ""; }

.fa-hand-holding-usd::before { content: ""; }

.fa-hand-lizard::before { content: ""; }

.fa-hand-middle-finger::before { content: ""; }

.fa-hand-paper::before { content: ""; }

.fa-hand-peace::before { content: ""; }

.fa-hand-point-down::before { content: ""; }

.fa-hand-point-left::before { content: ""; }

.fa-hand-point-right::before { content: ""; }

.fa-hand-point-up::before { content: ""; }

.fa-hand-pointer::before { content: ""; }

.fa-hand-rock::before { content: ""; }

.fa-hand-scissors::before { content: ""; }

.fa-hand-spock::before { content: ""; }

.fa-hands::before { content: ""; }

.fa-hands-helping::before { content: ""; }

.fa-handshake::before { content: ""; }

.fa-hanukiah::before { content: ""; }

.fa-hard-hat::before { content: ""; }

.fa-hashtag::before { content: ""; }

.fa-hat-wizard::before { content: ""; }

.fa-haykal::before { content: ""; }

.fa-hdd::before { content: ""; }

.fa-heading::before { content: ""; }

.fa-headphones::before { content: ""; }

.fa-headphones-alt::before { content: ""; }

.fa-headset::before { content: ""; }

.fa-heart::before { content: ""; }

.fa-heart-broken::before { content: ""; }

.fa-heartbeat::before { content: ""; }

.fa-helicopter::before { content: ""; }

.fa-highlighter::before { content: ""; }

.fa-hiking::before { content: ""; }

.fa-hippo::before { content: ""; }

.fa-hips::before { content: ""; }

.fa-hire-a-helper::before { content: ""; }

.fa-history::before { content: ""; }

.fa-hockey-puck::before { content: ""; }

.fa-holly-berry::before { content: ""; }

.fa-home::before { content: ""; }

.fa-hooli::before { content: ""; }

.fa-hornbill::before { content: ""; }

.fa-horse::before { content: ""; }

.fa-horse-head::before { content: ""; }

.fa-hospital::before { content: ""; }

.fa-hospital-alt::before { content: ""; }

.fa-hospital-symbol::before { content: ""; }

.fa-hot-tub::before { content: ""; }

.fa-hotdog::before { content: ""; }

.fa-hotel::before { content: ""; }

.fa-hotjar::before { content: ""; }

.fa-hourglass::before { content: ""; }

.fa-hourglass-end::before { content: ""; }

.fa-hourglass-half::before { content: ""; }

.fa-hourglass-start::before { content: ""; }

.fa-house-damage::before { content: ""; }

.fa-houzz::before { content: ""; }

.fa-hryvnia::before { content: ""; }

.fa-html5::before { content: ""; }

.fa-hubspot::before { content: ""; }

.fa-i-cursor::before { content: ""; }

.fa-ice-cream::before { content: ""; }

.fa-icicles::before { content: ""; }

.fa-id-badge::before { content: ""; }

.fa-id-card::before { content: ""; }

.fa-id-card-alt::before { content: ""; }

.fa-igloo::before { content: ""; }

.fa-image::before { content: ""; }

.fa-images::before { content: ""; }

.fa-imdb::before { content: ""; }

.fa-inbox::before { content: ""; }

.fa-indent::before { content: ""; }

.fa-industry::before { content: ""; }

.fa-infinity::before { content: ""; }

.fa-info::before { content: ""; }

.fa-info-circle::before { content: ""; }

.fa-instagram::before { content: ""; }

.fa-intercom::before { content: ""; }

.fa-internet-explorer::before { content: ""; }

.fa-invision::before { content: ""; }

.fa-ioxhost::before { content: ""; }

.fa-italic::before { content: ""; }

.fa-itunes::before { content: ""; }

.fa-itunes-note::before { content: ""; }

.fa-java::before { content: ""; }

.fa-jedi::before { content: ""; }

.fa-jedi-order::before { content: ""; }

.fa-jenkins::before { content: ""; }

.fa-jira::before { content: ""; }

.fa-joget::before { content: ""; }

.fa-joint::before { content: ""; }

.fa-joomla::before { content: ""; }

.fa-journal-whills::before { content: ""; }

.fa-js::before { content: ""; }

.fa-js-square::before { content: ""; }

.fa-jsfiddle::before { content: ""; }

.fa-kaaba::before { content: ""; }

.fa-kaggle::before { content: ""; }

.fa-key::before { content: ""; }

.fa-keybase::before { content: ""; }

.fa-keyboard::before { content: ""; }

.fa-keycdn::before { content: ""; }

.fa-khanda::before { content: ""; }

.fa-kickstarter::before { content: ""; }

.fa-kickstarter-k::before { content: ""; }

.fa-kiss::before { content: ""; }

.fa-kiss-beam::before { content: ""; }

.fa-kiss-wink-heart::before { content: ""; }

.fa-kiwi-bird::before { content: ""; }

.fa-korvue::before { content: ""; }

.fa-landmark::before { content: ""; }

.fa-language::before { content: ""; }

.fa-laptop::before { content: ""; }

.fa-laptop-code::before { content: ""; }

.fa-laptop-medical::before { content: ""; }

.fa-laravel::before { content: ""; }

.fa-lastfm::before { content: ""; }

.fa-lastfm-square::before { content: ""; }

.fa-laugh::before { content: ""; }

.fa-laugh-beam::before { content: ""; }

.fa-laugh-squint::before { content: ""; }

.fa-laugh-wink::before { content: ""; }

.fa-layer-group::before { content: ""; }

.fa-leaf::before { content: ""; }

.fa-leanpub::before { content: ""; }

.fa-lemon::before { content: ""; }

.fa-less::before { content: ""; }

.fa-less-than::before { content: ""; }

.fa-less-than-equal::before { content: ""; }

.fa-level-down-alt::before { content: ""; }

.fa-level-up-alt::before { content: ""; }

.fa-life-ring::before { content: ""; }

.fa-lightbulb::before { content: ""; }

.fa-line::before { content: ""; }

.fa-link::before { content: ""; }

.fa-linkedin::before { content: ""; }

.fa-linkedin-in::before { content: ""; }

.fa-linode::before { content: ""; }

.fa-linux::before { content: ""; }

.fa-lira-sign::before { content: ""; }

.fa-list::before { content: ""; }

.fa-list-alt::before { content: ""; }

.fa-list-ol::before { content: ""; }

.fa-list-ul::before { content: ""; }

.fa-location-arrow::before { content: ""; }

.fa-lock::before { content: ""; }

.fa-lock-open::before { content: ""; }

.fa-long-arrow-alt-down::before { content: ""; }

.fa-long-arrow-alt-left::before { content: ""; }

.fa-long-arrow-alt-right::before { content: ""; }

.fa-long-arrow-alt-up::before { content: ""; }

.fa-low-vision::before { content: ""; }

.fa-luggage-cart::before { content: ""; }

.fa-lyft::before { content: ""; }

.fa-magento::before { content: ""; }

.fa-magic::before { content: ""; }

.fa-magnet::before { content: ""; }

.fa-mail-bulk::before { content: ""; }

.fa-mailchimp::before { content: ""; }

.fa-male::before { content: ""; }

.fa-mandalorian::before { content: ""; }

.fa-map::before { content: ""; }

.fa-map-marked::before { content: ""; }

.fa-map-marked-alt::before { content: ""; }

.fa-map-marker::before { content: ""; }

.fa-map-marker-alt::before { content: ""; }

.fa-map-pin::before { content: ""; }

.fa-map-signs::before { content: ""; }

.fa-markdown::before { content: ""; }

.fa-marker::before { content: ""; }

.fa-mars::before { content: ""; }

.fa-mars-double::before { content: ""; }

.fa-mars-stroke::before { content: ""; }

.fa-mars-stroke-h::before { content: ""; }

.fa-mars-stroke-v::before { content: ""; }

.fa-mask::before { content: ""; }

.fa-mastodon::before { content: ""; }

.fa-maxcdn::before { content: ""; }

.fa-medal::before { content: ""; }

.fa-medapps::before { content: ""; }

.fa-medium::before { content: ""; }

.fa-medium-m::before { content: ""; }

.fa-medkit::before { content: ""; }

.fa-medrt::before { content: ""; }

.fa-meetup::before { content: ""; }

.fa-megaport::before { content: ""; }

.fa-meh::before { content: ""; }

.fa-meh-blank::before { content: ""; }

.fa-meh-rolling-eyes::before { content: ""; }

.fa-memory::before { content: ""; }

.fa-mendeley::before { content: ""; }

.fa-menorah::before { content: ""; }

.fa-mercury::before { content: ""; }

.fa-meteor::before { content: ""; }

.fa-microchip::before { content: ""; }

.fa-microphone::before { content: ""; }

.fa-microphone-alt::before { content: ""; }

.fa-microphone-alt-slash::before { content: ""; }

.fa-microphone-slash::before { content: ""; }

.fa-microscope::before { content: ""; }

.fa-microsoft::before { content: ""; }

.fa-minus::before { content: ""; }

.fa-minus-circle::before { content: ""; }

.fa-minus-square::before { content: ""; }

.fa-mitten::before { content: ""; }

.fa-mix::before { content: ""; }

.fa-mixcloud::before { content: ""; }

.fa-mizuni::before { content: ""; }

.fa-mobile::before { content: ""; }

.fa-mobile-alt::before { content: ""; }

.fa-modx::before { content: ""; }

.fa-monero::before { content: ""; }

.fa-money-bill::before { content: ""; }

.fa-money-bill-alt::before { content: ""; }

.fa-money-bill-wave::before { content: ""; }

.fa-money-bill-wave-alt::before { content: ""; }

.fa-money-check::before { content: ""; }

.fa-money-check-alt::before { content: ""; }

.fa-monument::before { content: ""; }

.fa-moon::before { content: ""; }

.fa-mortar-pestle::before { content: ""; }

.fa-mosque::before { content: ""; }

.fa-motorcycle::before { content: ""; }

.fa-mountain::before { content: ""; }

.fa-mouse-pointer::before { content: ""; }

.fa-mug-hot::before { content: ""; }

.fa-music::before { content: ""; }

.fa-napster::before { content: ""; }

.fa-neos::before { content: ""; }

.fa-network-wired::before { content: ""; }

.fa-neuter::before { content: ""; }

.fa-newspaper::before { content: ""; }

.fa-nimblr::before { content: ""; }

.fa-nintendo-switch::before { content: ""; }

.fa-node::before { content: ""; }

.fa-node-js::before { content: ""; }

.fa-not-equal::before { content: ""; }

.fa-notes-medical::before { content: ""; }

.fa-npm::before { content: ""; }

.fa-ns8::before { content: ""; }

.fa-nutritionix::before { content: ""; }

.fa-object-group::before { content: ""; }

.fa-object-ungroup::before { content: ""; }

.fa-odnoklassniki::before { content: ""; }

.fa-odnoklassniki-square::before { content: ""; }

.fa-oil-can::before { content: ""; }

.fa-old-republic::before { content: ""; }

.fa-om::before { content: ""; }

.fa-opencart::before { content: ""; }

.fa-openid::before { content: ""; }

.fa-opera::before { content: ""; }

.fa-optin-monster::before { content: ""; }

.fa-osi::before { content: ""; }

.fa-otter::before { content: ""; }

.fa-outdent::before { content: ""; }

.fa-page4::before { content: ""; }

.fa-pagelines::before { content: ""; }

.fa-pager::before { content: ""; }

.fa-paint-brush::before { content: ""; }

.fa-paint-roller::before { content: ""; }

.fa-palette::before { content: ""; }

.fa-palfed::before { content: ""; }

.fa-pallet::before { content: ""; }

.fa-paper-plane::before { content: ""; }

.fa-paperclip::before { content: ""; }

.fa-parachute-box::before { content: ""; }

.fa-paragraph::before { content: ""; }

.fa-parking::before { content: ""; }

.fa-passport::before { content: ""; }

.fa-pastafarianism::before { content: ""; }

.fa-paste::before { content: ""; }

.fa-patreon::before { content: ""; }

.fa-pause::before { content: ""; }

.fa-pause-circle::before { content: ""; }

.fa-paw::before { content: ""; }

.fa-paypal::before { content: ""; }

.fa-peace::before { content: ""; }

.fa-pen::before { content: ""; }

.fa-pen-alt::before { content: ""; }

.fa-pen-fancy::before { content: ""; }

.fa-pen-nib::before { content: ""; }

.fa-pen-square::before { content: ""; }

.fa-pencil-alt::before { content: ""; }

.fa-pencil-ruler::before { content: ""; }

.fa-penny-arcade::before { content: ""; }

.fa-people-carry::before { content: ""; }

.fa-pepper-hot::before { content: ""; }

.fa-percent::before { content: ""; }

.fa-percentage::before { content: ""; }

.fa-periscope::before { content: ""; }

.fa-person-booth::before { content: ""; }

.fa-phabricator::before { content: ""; }

.fa-phoenix-framework::before { content: ""; }

.fa-phoenix-squadron::before { content: ""; }

.fa-phone::before { content: ""; }

.fa-phone-slash::before { content: ""; }

.fa-phone-square::before { content: ""; }

.fa-phone-volume::before { content: ""; }

.fa-php::before { content: ""; }

.fa-pied-piper::before { content: ""; }

.fa-pied-piper-alt::before { content: ""; }

.fa-pied-piper-hat::before { content: ""; }

.fa-pied-piper-pp::before { content: ""; }

.fa-piggy-bank::before { content: ""; }

.fa-pills::before { content: ""; }

.fa-pinterest::before { content: ""; }

.fa-pinterest-p::before { content: ""; }

.fa-pinterest-square::before { content: ""; }

.fa-pizza-slice::before { content: ""; }

.fa-place-of-worship::before { content: ""; }

.fa-plane::before { content: ""; }

.fa-plane-arrival::before { content: ""; }

.fa-plane-departure::before { content: ""; }

.fa-play::before { content: ""; }

.fa-play-circle::before { content: ""; }

.fa-playstation::before { content: ""; }

.fa-plug::before { content: ""; }

.fa-plus::before { content: ""; }

.fa-plus-circle::before { content: ""; }

.fa-plus-square::before { content: ""; }

.fa-podcast::before { content: ""; }

.fa-poll::before { content: ""; }

.fa-poll-h::before { content: ""; }

.fa-poo::before { content: ""; }

.fa-poo-storm::before { content: ""; }

.fa-poop::before { content: ""; }

.fa-portrait::before { content: ""; }

.fa-pound-sign::before { content: ""; }

.fa-power-off::before { content: ""; }

.fa-pray::before { content: ""; }

.fa-praying-hands::before { content: ""; }

.fa-prescription::before { content: ""; }

.fa-prescription-bottle::before { content: ""; }

.fa-prescription-bottle-alt::before { content: ""; }

.fa-print::before { content: ""; }

.fa-procedures::before { content: ""; }

.fa-product-hunt::before { content: ""; }

.fa-project-diagram::before { content: ""; }

.fa-pushed::before { content: ""; }

.fa-puzzle-piece::before { content: ""; }

.fa-python::before { content: ""; }

.fa-qq::before { content: ""; }

.fa-qrcode::before { content: ""; }

.fa-question::before { content: ""; }

.fa-question-circle::before { content: ""; }

.fa-quidditch::before { content: ""; }

.fa-quinscape::before { content: ""; }

.fa-quora::before { content: ""; }

.fa-quote-left::before { content: ""; }

.fa-quote-right::before { content: ""; }

.fa-quran::before { content: ""; }

.fa-r-project::before { content: ""; }

.fa-radiation::before { content: ""; }

.fa-radiation-alt::before { content: ""; }

.fa-rainbow::before { content: ""; }

.fa-random::before { content: ""; }

.fa-raspberry-pi::before { content: ""; }

.fa-ravelry::before { content: ""; }

.fa-react::before { content: ""; }

.fa-reacteurope::before { content: ""; }

.fa-readme::before { content: ""; }

.fa-rebel::before { content: ""; }

.fa-receipt::before { content: ""; }

.fa-recycle::before { content: ""; }

.fa-red-river::before { content: ""; }

.fa-reddit::before { content: ""; }

.fa-reddit-alien::before { content: ""; }

.fa-reddit-square::before { content: ""; }

.fa-redhat::before { content: ""; }

.fa-redo::before { content: ""; }

.fa-redo-alt::before { content: ""; }

.fa-registered::before { content: ""; }

.fa-renren::before { content: ""; }

.fa-reply::before { content: ""; }

.fa-reply-all::before { content: ""; }

.fa-replyd::before { content: ""; }

.fa-republican::before { content: ""; }

.fa-researchgate::before { content: ""; }

.fa-resolving::before { content: ""; }

.fa-restroom::before { content: ""; }

.fa-retweet::before { content: ""; }

.fa-rev::before { content: ""; }

.fa-ribbon::before { content: ""; }

.fa-ring::before { content: ""; }

.fa-road::before { content: ""; }

.fa-robot::before { content: ""; }

.fa-rocket::before { content: ""; }

.fa-rocketchat::before { content: ""; }

.fa-rockrms::before { content: ""; }

.fa-route::before { content: ""; }

.fa-rss::before { content: ""; }

.fa-rss-square::before { content: ""; }

.fa-ruble-sign::before { content: ""; }

.fa-ruler::before { content: ""; }

.fa-ruler-combined::before { content: ""; }

.fa-ruler-horizontal::before { content: ""; }

.fa-ruler-vertical::before { content: ""; }

.fa-running::before { content: ""; }

.fa-rupee-sign::before { content: ""; }

.fa-sad-cry::before { content: ""; }

.fa-sad-tear::before { content: ""; }

.fa-safari::before { content: ""; }

.fa-sass::before { content: ""; }

.fa-satellite::before { content: ""; }

.fa-satellite-dish::before { content: ""; }

.fa-save::before { content: ""; }

.fa-schlix::before { content: ""; }

.fa-school::before { content: ""; }

.fa-screwdriver::before { content: ""; }

.fa-scribd::before { content: ""; }

.fa-scroll::before { content: ""; }

.fa-sd-card::before { content: ""; }

.fa-search::before { content: ""; }

.fa-search-dollar::before { content: ""; }

.fa-search-location::before { content: ""; }

.fa-search-minus::before { content: ""; }

.fa-search-plus::before { content: ""; }

.fa-searchengin::before { content: ""; }

.fa-seedling::before { content: ""; }

.fa-sellcast::before { content: ""; }

.fa-sellsy::before { content: ""; }

.fa-server::before { content: ""; }

.fa-servicestack::before { content: ""; }

.fa-shapes::before { content: ""; }

.fa-share::before { content: ""; }

.fa-share-alt::before { content: ""; }

.fa-share-alt-square::before { content: ""; }

.fa-share-square::before { content: ""; }

.fa-shekel-sign::before { content: ""; }

.fa-shield-alt::before { content: ""; }

.fa-ship::before { content: ""; }

.fa-shipping-fast::before { content: ""; }

.fa-shirtsinbulk::before { content: ""; }

.fa-shoe-prints::before { content: ""; }

.fa-shopping-bag::before { content: ""; }

.fa-shopping-basket::before { content: ""; }

.fa-shopping-cart::before { content: ""; }

.fa-shopware::before { content: ""; }

.fa-shower::before { content: ""; }

.fa-shuttle-van::before { content: ""; }

.fa-sign::before { content: ""; }

.fa-sign-in-alt::before { content: ""; }

.fa-sign-language::before { content: ""; }

.fa-sign-out-alt::before { content: ""; }

.fa-signal::before { content: ""; }

.fa-signature::before { content: ""; }

.fa-sim-card::before { content: ""; }

.fa-simplybuilt::before { content: ""; }

.fa-sistrix::before { content: ""; }

.fa-sitemap::before { content: ""; }

.fa-sith::before { content: ""; }

.fa-skating::before { content: ""; }

.fa-sketch::before { content: ""; }

.fa-skiing::before { content: ""; }

.fa-skiing-nordic::before { content: ""; }

.fa-skull::before { content: ""; }

.fa-skull-crossbones::before { content: ""; }

.fa-skyatlas::before { content: ""; }

.fa-skype::before { content: ""; }

.fa-slack::before { content: ""; }

.fa-slack-hash::before { content: ""; }

.fa-slash::before { content: ""; }

.fa-sleigh::before { content: ""; }

.fa-sliders-h::before { content: ""; }

.fa-slideshare::before { content: ""; }

.fa-smile::before { content: ""; }

.fa-smile-beam::before { content: ""; }

.fa-smile-wink::before { content: ""; }

.fa-smog::before { content: ""; }

.fa-smoking::before { content: ""; }

.fa-smoking-ban::before { content: ""; }

.fa-sms::before { content: ""; }

.fa-snapchat::before { content: ""; }

.fa-snapchat-ghost::before { content: ""; }

.fa-snapchat-square::before { content: ""; }

.fa-snowboarding::before { content: ""; }

.fa-snowflake::before { content: ""; }

.fa-snowman::before { content: ""; }

.fa-snowplow::before { content: ""; }

.fa-socks::before { content: ""; }

.fa-solar-panel::before { content: ""; }

.fa-sort::before { content: ""; }

.fa-sort-alpha-down::before { content: ""; }

.fa-sort-alpha-up::before { content: ""; }

.fa-sort-amount-down::before { content: ""; }

.fa-sort-amount-up::before { content: ""; }

.fa-sort-down::before { content: ""; }

.fa-sort-numeric-down::before { content: ""; }

.fa-sort-numeric-up::before { content: ""; }

.fa-sort-up::before { content: ""; }

.fa-soundcloud::before { content: ""; }

.fa-sourcetree::before { content: ""; }

.fa-spa::before { content: ""; }

.fa-space-shuttle::before { content: ""; }

.fa-speakap::before { content: ""; }

.fa-spider::before { content: ""; }

.fa-spinner::before { content: ""; }

.fa-splotch::before { content: ""; }

.fa-spotify::before { content: ""; }

.fa-spray-can::before { content: ""; }

.fa-square::before { content: ""; }

.fa-square-full::before { content: ""; }

.fa-square-root-alt::before { content: ""; }

.fa-squarespace::before { content: ""; }

.fa-stack-exchange::before { content: ""; }

.fa-stack-overflow::before { content: ""; }

.fa-stamp::before { content: ""; }

.fa-star::before { content: ""; }

.fa-star-and-crescent::before { content: ""; }

.fa-star-half::before { content: ""; }

.fa-star-half-alt::before { content: ""; }

.fa-star-of-david::before { content: ""; }

.fa-star-of-life::before { content: ""; }

.fa-staylinked::before { content: ""; }

.fa-steam::before { content: ""; }

.fa-steam-square::before { content: ""; }

.fa-steam-symbol::before { content: ""; }

.fa-step-backward::before { content: ""; }

.fa-step-forward::before { content: ""; }

.fa-stethoscope::before { content: ""; }

.fa-sticker-mule::before { content: ""; }

.fa-sticky-note::before { content: ""; }

.fa-stop::before { content: ""; }

.fa-stop-circle::before { content: ""; }

.fa-stopwatch::before { content: ""; }

.fa-store::before { content: ""; }

.fa-store-alt::before { content: ""; }

.fa-strava::before { content: ""; }

.fa-stream::before { content: ""; }

.fa-street-view::before { content: ""; }

.fa-strikethrough::before { content: ""; }

.fa-stripe::before { content: ""; }

.fa-stripe-s::before { content: ""; }

.fa-stroopwafel::before { content: ""; }

.fa-studiovinari::before { content: ""; }

.fa-stumbleupon::before { content: ""; }

.fa-stumbleupon-circle::before { content: ""; }

.fa-subscript::before { content: ""; }

.fa-subway::before { content: ""; }

.fa-suitcase::before { content: ""; }

.fa-suitcase-rolling::before { content: ""; }

.fa-sun::before { content: ""; }

.fa-superpowers::before { content: ""; }

.fa-superscript::before { content: ""; }

.fa-supple::before { content: ""; }

.fa-surprise::before { content: ""; }

.fa-suse::before { content: ""; }

.fa-swatchbook::before { content: ""; }

.fa-swimmer::before { content: ""; }

.fa-swimming-pool::before { content: ""; }

.fa-synagogue::before { content: ""; }

.fa-sync::before { content: ""; }

.fa-sync-alt::before { content: ""; }

.fa-syringe::before { content: ""; }

.fa-table::before { content: ""; }

.fa-table-tennis::before { content: ""; }

.fa-tablet::before { content: ""; }

.fa-tablet-alt::before { content: ""; }

.fa-tablets::before { content: ""; }

.fa-tachometer-alt::before { content: ""; }

.fa-tag::before { content: ""; }

.fa-tags::before { content: ""; }

.fa-tape::before { content: ""; }

.fa-tasks::before { content: ""; }

.fa-taxi::before { content: ""; }

.fa-teamspeak::before { content: ""; }

.fa-teeth::before { content: ""; }

.fa-teeth-open::before { content: ""; }

.fa-telegram::before { content: ""; }

.fa-telegram-plane::before { content: ""; }

.fa-temperature-high::before { content: ""; }

.fa-temperature-low::before { content: ""; }

.fa-tencent-weibo::before { content: ""; }

.fa-tenge::before { content: ""; }

.fa-terminal::before { content: ""; }

.fa-text-height::before { content: ""; }

.fa-text-width::before { content: ""; }

.fa-th::before { content: ""; }

.fa-th-large::before { content: ""; }

.fa-th-list::before { content: ""; }

.fa-the-red-yeti::before { content: ""; }

.fa-theater-masks::before { content: ""; }

.fa-themeco::before { content: ""; }

.fa-themeisle::before { content: ""; }

.fa-thermometer::before { content: ""; }

.fa-thermometer-empty::before { content: ""; }

.fa-thermometer-full::before { content: ""; }

.fa-thermometer-half::before { content: ""; }

.fa-thermometer-quarter::before { content: ""; }

.fa-thermometer-three-quarters::before { content: ""; }

.fa-think-peaks::before { content: ""; }

.fa-thumbs-down::before { content: ""; }

.fa-thumbs-up::before { content: ""; }

.fa-thumbtack::before { content: ""; }

.fa-ticket-alt::before { content: ""; }

.fa-times::before { content: ""; }

.fa-times-circle::before { content: ""; }

.fa-tint::before { content: ""; }

.fa-tint-slash::before { content: ""; }

.fa-tired::before { content: ""; }

.fa-toggle-off::before { content: ""; }

.fa-toggle-on::before { content: ""; }

.fa-toilet::before { content: ""; }

.fa-toilet-paper::before { content: ""; }

.fa-toolbox::before { content: ""; }

.fa-tools::before { content: ""; }

.fa-tooth::before { content: ""; }

.fa-torah::before { content: ""; }

.fa-torii-gate::before { content: ""; }

.fa-tractor::before { content: ""; }

.fa-trade-federation::before { content: ""; }

.fa-trademark::before { content: ""; }

.fa-traffic-light::before { content: ""; }

.fa-train::before { content: ""; }

.fa-tram::before { content: ""; }

.fa-transgender::before { content: ""; }

.fa-transgender-alt::before { content: ""; }

.fa-trash::before { content: ""; }

.fa-trash-alt::before { content: ""; }

.fa-trash-restore::before { content: ""; }

.fa-trash-restore-alt::before { content: ""; }

.fa-tree::before { content: ""; }

.fa-trello::before { content: ""; }

.fa-tripadvisor::before { content: ""; }

.fa-trophy::before { content: ""; }

.fa-truck::before { content: ""; }

.fa-truck-loading::before { content: ""; }

.fa-truck-monster::before { content: ""; }

.fa-truck-moving::before { content: ""; }

.fa-truck-pickup::before { content: ""; }

.fa-tshirt::before { content: ""; }

.fa-tty::before { content: ""; }

.fa-tumblr::before { content: ""; }

.fa-tumblr-square::before { content: ""; }

.fa-tv::before { content: ""; }

.fa-twitch::before { content: ""; }

.fa-twitter::before { content: ""; }

.fa-twitter-square::before { content: ""; }

.fa-typo3::before { content: ""; }

.fa-uber::before { content: ""; }

.fa-ubuntu::before { content: ""; }

.fa-uikit::before { content: ""; }

.fa-umbrella::before { content: ""; }

.fa-umbrella-beach::before { content: ""; }

.fa-underline::before { content: ""; }

.fa-undo::before { content: ""; }

.fa-undo-alt::before { content: ""; }

.fa-uniregistry::before { content: ""; }

.fa-universal-access::before { content: ""; }

.fa-university::before { content: ""; }

.fa-unlink::before { content: ""; }

.fa-unlock::before { content: ""; }

.fa-unlock-alt::before { content: ""; }

.fa-untappd::before { content: ""; }

.fa-upload::before { content: ""; }

.fa-ups::before { content: ""; }

.fa-usb::before { content: ""; }

.fa-user::before { content: ""; }

.fa-user-alt::before { content: ""; }

.fa-user-alt-slash::before { content: ""; }

.fa-user-astronaut::before { content: ""; }

.fa-user-check::before { content: ""; }

.fa-user-circle::before { content: ""; }

.fa-user-clock::before { content: ""; }

.fa-user-cog::before { content: ""; }

.fa-user-edit::before { content: ""; }

.fa-user-friends::before { content: ""; }

.fa-user-graduate::before { content: ""; }

.fa-user-injured::before { content: ""; }

.fa-user-lock::before { content: ""; }

.fa-user-md::before { content: ""; }

.fa-user-minus::before { content: ""; }

.fa-user-ninja::before { content: ""; }

.fa-user-nurse::before { content: ""; }

.fa-user-plus::before { content: ""; }

.fa-user-secret::before { content: ""; }

.fa-user-shield::before { content: ""; }

.fa-user-slash::before { content: ""; }

.fa-user-tag::before { content: ""; }

.fa-user-tie::before { content: ""; }

.fa-user-times::before { content: ""; }

.fa-users::before { content: ""; }

.fa-users-cog::before { content: ""; }

.fa-usps::before { content: ""; }

.fa-ussunnah::before { content: ""; }

.fa-utensil-spoon::before { content: ""; }

.fa-utensils::before { content: ""; }

.fa-vaadin::before { content: ""; }

.fa-vector-square::before { content: ""; }

.fa-venus::before { content: ""; }

.fa-venus-double::before { content: ""; }

.fa-venus-mars::before { content: ""; }

.fa-viacoin::before { content: ""; }

.fa-viadeo::before { content: ""; }

.fa-viadeo-square::before { content: ""; }

.fa-vial::before { content: ""; }

.fa-vials::before { content: ""; }

.fa-viber::before { content: ""; }

.fa-video::before { content: ""; }

.fa-video-slash::before { content: ""; }

.fa-vihara::before { content: ""; }

.fa-vimeo::before { content: ""; }

.fa-vimeo-square::before { content: ""; }

.fa-vimeo-v::before { content: ""; }

.fa-vine::before { content: ""; }

.fa-vk::before { content: ""; }

.fa-vnv::before { content: ""; }

.fa-volleyball-ball::before { content: ""; }

.fa-volume-down::before { content: ""; }

.fa-volume-mute::before { content: ""; }

.fa-volume-off::before { content: ""; }

.fa-volume-up::before { content: ""; }

.fa-vote-yea::before { content: ""; }

.fa-vr-cardboard::before { content: ""; }

.fa-vuejs::before { content: ""; }

.fa-walking::before { content: ""; }

.fa-wallet::before { content: ""; }

.fa-warehouse::before { content: ""; }

.fa-water::before { content: ""; }

.fa-weebly::before { content: ""; }

.fa-weibo::before { content: ""; }

.fa-weight::before { content: ""; }

.fa-weight-hanging::before { content: ""; }

.fa-weixin::before { content: ""; }

.fa-whatsapp::before { content: ""; }

.fa-whatsapp-square::before { content: ""; }

.fa-wheelchair::before { content: ""; }

.fa-whmcs::before { content: ""; }

.fa-wifi::before { content: ""; }

.fa-wikipedia-w::before { content: ""; }

.fa-wind::before { content: ""; }

.fa-window-close::before { content: ""; }

.fa-window-maximize::before { content: ""; }

.fa-window-minimize::before { content: ""; }

.fa-window-restore::before { content: ""; }

.fa-windows::before { content: ""; }

.fa-wine-bottle::before { content: ""; }

.fa-wine-glass::before { content: ""; }

.fa-wine-glass-alt::before { content: ""; }

.fa-wix::before { content: ""; }

.fa-wizards-of-the-coast::before { content: ""; }

.fa-wolf-pack-battalion::before { content: ""; }

.fa-won-sign::before { content: ""; }

.fa-wordpress::before { content: ""; }

.fa-wordpress-simple::before { content: ""; }

.fa-wpbeginner::before { content: ""; }

.fa-wpexplorer::before { content: ""; }

.fa-wpforms::before { content: ""; }

.fa-wpressr::before { content: ""; }

.fa-wrench::before { content: ""; }

.fa-x-ray::before { content: ""; }

.fa-xbox::before { content: ""; }

.fa-xing::before { content: ""; }

.fa-xing-square::before { content: ""; }

.fa-y-combinator::before { content: ""; }

.fa-yahoo::before { content: ""; }

.fa-yandex::before { content: ""; }

.fa-yandex-international::before { content: ""; }

.fa-yarn::before { content: ""; }

.fa-yelp::before { content: ""; }

.fa-yen-sign::before { content: ""; }

.fa-yin-yang::before { content: ""; }

.fa-yoast::before { content: ""; }

.fa-youtube::before { content: ""; }

.fa-youtube-square::before { content: ""; }

.fa-zhihu::before { content: ""; }

.sr-only { border: 0px; clip: rect(0px, 0px, 0px, 0px); height: 1px; margin: -1px; overflow: hidden; padding: 0px; position: absolute; width: 1px; }

.sr-only-focusable:active, .sr-only-focusable:focus { clip: auto; height: auto; margin: 0px; overflow: visible; position: static; width: auto; }

@font-face { font-family: "Font Awesome 5 Brands"; font-style: normal; font-weight: normal; font-display: auto; src: url("/media/1409/font-awesome-5-brands-regular.woff"); }

@font-face { font-family: "Font Awesome 5 Free"; font-style: normal; font-weight: 400; font-display: auto; }
------MultipartBoundary--B35gv9hf8GVvnlqnSn2OQfMwBE5Ga2VECPMKOPmjLS----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.bci.ao/css/applibs.css

@charset "utf-8";

html { line-height: 1.15; text-size-adjust: 100%; }

body { margin: 0px; }

main { display: block; }

h1 { font-size: 2em; margin: 0.67em 0px; }

hr { box-sizing: content-box; height: 0px; overflow: visible; }

pre { font-family: monospace, monospace; font-size: 1em; }

a { background-color: transparent; }

abbr[title] { border-bottom: none; text-decoration: underline dotted; }

b, strong { font-weight: bolder; }

code, kbd, samp { font-family: monospace, monospace; font-size: 1em; }

small { font-size: 80%; }

sub, sup { font-size: 75%; line-height: 0; position: relative; vertical-align: baseline; }

sub { bottom: -0.25em; }

sup { top: -0.5em; }

img { border-style: none; }

button, input, optgroup, select, textarea { font-family: inherit; font-size: 100%; line-height: 1.15; margin: 0px; }

button, input { overflow: visible; }

button, select { text-transform: none; }

[type="button"], [type="reset"], [type="submit"], button { -webkit-appearance: button; }

fieldset { padding: 0.35em 0.75em 0.625em; }

legend { box-sizing: border-box; color: inherit; display: table; max-width: 100%; padding: 0px; white-space: normal; }

progress { vertical-align: baseline; }

textarea { overflow: auto; }

[type="checkbox"], [type="radio"] { box-sizing: border-box; padding: 0px; }

[type="number"]::-webkit-inner-spin-button, [type="number"]::-webkit-outer-spin-button { height: auto; }

[type="search"] { -webkit-appearance: textfield; outline-offset: -2px; }

[type="search"]::-webkit-search-decoration { -webkit-appearance: none; }

::-webkit-file-upload-button { -webkit-appearance: button; font: inherit; }

details { display: block; }

summary { display: list-item; }

[hidden], template { display: none; }

.slick-slider { box-sizing: border-box; user-select: none; touch-action: pan-y; -webkit-tap-highlight-color: transparent; }

.slick-list, .slick-slider { position: relative; display: block; }

.slick-list { overflow: hidden; margin: 0px; padding: 0px; }

.slick-list:focus { outline: none; }

.slick-list.dragging { cursor: pointer; }

.slick-slider .slick-list, .slick-slider .slick-track { transform: translateZ(0px); }

.slick-track { position: relative; left: 0px; top: 0px; display: block; margin-left: auto; margin-right: auto; }

.slick-track::after, .slick-track::before { content: ""; display: table; }

.slick-track::after { clear: both; }

.slick-loading .slick-track { visibility: hidden; }

.slick-slide { float: left; height: 100%; min-height: 1px; display: none; }

[dir="rtl"] .slick-slide { float: right; }

.slick-slide img { display: block; }

.slick-slide.slick-loading img { display: none; }

.slick-slide.dragging img { pointer-events: none; }

.slick-initialized .slick-slide { display: block; }

.slick-loading .slick-slide { visibility: hidden; }

.slick-vertical .slick-slide { display: block; height: auto; border: 1px solid transparent; }

.slick-arrow.slick-hidden { display: none; }

.selectric-wrapper { position: relative; cursor: pointer; }

.selectric-responsive { width: 100%; }

.selectric { border: 1px solid rgb(255, 255, 255); background: rgb(255, 255, 255); position: relative; }

.selectric .label { display: block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin: 0px 38px 0px 10px; line-height: 38px; color: rgb(68, 68, 68); height: 38px; user-select: none; }

.selectric .button { display: block; position: absolute; right: 0px; top: 0px; width: 38px; height: 38px; color: rgb(255, 255, 255); text-align: center; font: 0px / 0 a; }

.selectric .button::after { content: " "; position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; margin: auto; width: 0px; height: 0px; border-top: 4px solid rgb(255, 255, 255); border-right: 4px solid transparent; border-left: 4px solid transparent; border-image: initial; border-bottom: none; }

.selectric-focus .selectric { border-color: rgb(204, 204, 204); }

.selectric-hover .selectric { border-color: rgb(230, 230, 230); }

.selectric-hover .selectric .button { color: rgb(230, 230, 230); }

.selectric-hover .selectric .button::after { border-top-color: rgb(230, 230, 230); }

.selectric-open { z-index: 9999; }

.selectric-open .selectric { border-color: rgb(230, 230, 230); }

.selectric-open .selectric-items { display: block; }

.selectric-disabled { opacity: 0.5; cursor: default; user-select: none; }

.selectric-hide-select { position: relative; overflow: hidden; width: 0px; height: 0px; }

.selectric-hide-select select { position: absolute; left: -100%; display: none; }

.selectric-input { position: absolute !important; top: 0px !important; left: 0px !important; overflow: hidden !important; clip: rect(0px, 0px, 0px, 0px) !important; margin: 0px !important; padding: 0px !important; width: 1px !important; height: 1px !important; outline: none !important; border: none !important; background: none !important; }

.selectric-temp-show { position: absolute !important; visibility: hidden !important; display: block !important; }

.selectric-items { display: none; position: absolute; top: 100%; left: 0px; background: rgb(255, 255, 255); border: 1px solid rgb(230, 230, 230); z-index: -1; box-shadow: 0px 0px 10px -6px; }

.selectric-items .selectric-scroll { height: 100%; overflow: auto; }

.selectric-above .selectric-items { top: auto; bottom: 100%; }

.selectric-items li, .selectric-items ul { list-style: none; padding: 0px; margin: 0px; line-height: 20px; min-height: 20px; }

.selectric-items li { display: block; padding: 10px; color: rgb(102, 102, 102); cursor: pointer; }

.selectric-items li.selected { background: rgb(224, 224, 224); color: rgb(68, 68, 68); }

.selectric-items li:hover { background: rgb(213, 213, 213); color: rgb(68, 68, 68); }

.selectric-items .disabled { opacity: 0.5; cursor: default !important; background: none !important; color: rgb(102, 102, 102) !important; }

.selectric-items .disabled, .selectric-items .selectric-group .selectric-group-label { user-select: none; }

.selectric-items .selectric-group .selectric-group-label { font-weight: 700; padding-left: 10px; cursor: default; background: none; color: rgb(68, 68, 68); }

.selectric-items .selectric-group.disabled li { opacity: 1; }

.selectric-items .selectric-group li { padding-left: 25px; }
------MultipartBoundary--B35gv9hf8GVvnlqnSn2OQfMwBE5Ga2VECPMKOPmjLS----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.bci.ao/css/app.css

@charset "utf-8";

@font-face { font-family: "PT Sans"; src: local("PT Sans Italic"), local("PTSans-Italic"), url("/media/1407/ptsans-italic.woff") format("woff"); font-weight: normal; font-style: italic; font-display: swap; }

@font-face { font-family: "PT Sans"; src: local("PT Sans Bold Italic"), local("PTSans-BoldItalic"), url("/media/1406/ptsans-bolditalic.woff") format("woff"); font-weight: bold; font-style: italic; font-display: swap; }

@font-face { font-family: "PT Sans"; src: local("PT Sans Bold"), local("PTSans-Bold"), url("/media/1405/ptsans-bold.woff") format("woff"); font-weight: bold; font-style: normal; font-display: swap; }

@font-face { font-family: "PT Sans"; src: local("PT Sans"), local("PTSans-Regular"), url("/media/1408/ptsans-regular.woff") format("woff"); font-weight: normal; font-style: normal; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans Bold"), local("OpenSans-Bold"), url("/media/1412/opensans-bold.woff") format("woff"); font-weight: bold; font-style: normal; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans Bold Italic"), local("OpenSans-BoldItalic"), url("/media/1413/opensans-bolditalic.woff") format("woff"); font-weight: bold; font-style: italic; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans ExtraBold"), local("OpenSans-ExtraBold"), url("/media/1414/opensans-extrabold.woff") format("woff"); font-weight: 800; font-style: normal; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans ExtraBold Italic"), local("OpenSans-ExtraBoldItalic"), url("/media/1415/opensans-extrabolditalic.woff") format("woff"); font-weight: 800; font-style: italic; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans Italic"), local("OpenSans-Italic"), url("/media/1416/opensans-italic.woff") format("woff"); font-weight: normal; font-style: italic; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans Light"), local("OpenSans-Light"), url("/media/1417/opensans-light.woff") format("woff"); font-weight: 300; font-style: normal; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans Light Italic"), local("OpenSans-LightItalic"), url("/fonts/OpenSans-LightItalic.woff") format("woff"); font-weight: 300; font-style: italic; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans Regular"), local("OpenSans-Regular"), url("/media/1419/opensans-regular.woff") format("woff"); font-weight: normal; font-style: normal; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans SemiBold"), local("OpenSans-SemiBold"), url("/media/1403/opensans-semibold.woff") format("woff"); font-weight: 600; font-style: normal; font-display: swap; }

@font-face { font-family: "Open Sans"; src: local("Open Sans SemiBold Italic"), local("OpenSans-SemiBoldItalic"), url("/media/1404/opensans-semibolditalic.woff") format("woff"); font-weight: 600; font-style: italic; font-display: swap; }

*, ::after, ::before { box-sizing: border-box; margin: 0px; padding: 0px; }

html { font-size: 16px; text-size-adjust: 100%; -webkit-font-smoothing: antialiased !important; text-rendering: optimizelegibility !important; }

h1, h2, h3, h4, h5, h6 { font-size: 100%; font-weight: inherit; }

h1, h2, h3, h4, h5, h6, li, p { margin: 0px; line-height: 1; }

ul { list-style: none; padding: 0px; margin: 0px; }

li { display: inline-block; }

a { text-decoration: none; color: inherit; }

a[href]:not([href="#"]) { cursor: pointer; }

button, input, textarea { outline: none; background-color: transparent; }

input:not([type="checkbox"]), input:not([type="radio"]), select { -webkit-appearance: none; padding: 0px; margin: 0px; border: none; box-shadow: none; }

input:not([type="checkbox"]):focus, input:not([type="radio"]):focus, select:focus { outline: none; }

button { -webkit-appearance: none; padding: 0px; margin: 0px; border: none; background-color: transparent; }

button:not(:disabled) { cursor: pointer; }

.clr { clear: both; }

.column-half, .documentos-links, .downloads-links, .homepage-header-menu, .homepage-header .slide, .links-404-container, .row:not(.row-flex) { zoom: 1; }

.column-half::after, .column-half::before, .documentos-links::after, .documentos-links::before, .downloads-links::after, .downloads-links::before, .homepage-header-menu::after, .homepage-header-menu::before, .homepage-header .slide::after, .homepage-header .slide::before, .links-404-container::after, .links-404-container::before, .row:not(.row-flex)::after, .row:not(.row-flex)::before { content: ""; display: table; }

.column-half::after, .documentos-links::after, .downloads-links::after, .homepage-header-menu::after, .homepage-header .slide::after, .links-404-container::after, .row:not(.row-flex)::after { clear: both; }

.selectric { display: inline-flex; border: none; }

.selectric:hover .button { width: 50px; }

.selectric:hover .button::after, .selectric:hover .button::before { width: auto; height: auto; transform: none; position: relative; left: 10px; background-color: transparent !important; }

.selectric:hover .button::before { content: none; }

.selectric:hover .button::after { font-family: "PT Sans", sans-serif; text-transform: uppercase; content: "Trocar"; font-size: 12px; font-weight: 600; }

.selectric, .selectric-hover .selectric, .selectric-open .selectric { border: transparent; }

.selectric-hover .selectric .button, .selectric-open .selectric .button, .selectric .button { color: inherit; }

.selectric .label { height: auto; line-height: normal; margin: 0px auto; font-size: 1.125rem; padding: 0.46875rem; }

@media (max-width: 767px) {
  .selectric .label { font-size: 1rem; }
}

.selectric .button { position: relative; display: inline-block; width: 38px; height: 38px; right: auto; top: auto; }

.selectric .button::after, .selectric .button::before { content: ""; position: absolute; top: 50%; left: 50%; width: 2px; height: 10px; }

.selectric .button::before { transform: rotate(45deg) translateY(-50%); }

.selectric .button::after { right: auto; bottom: auto; margin: 0px; border-width: initial; border-right-style: none; border-bottom-style: none; border-left-style: none; border-right-color: initial; border-bottom-color: initial; border-left-color: initial; border-image: initial; border-top-style: initial; border-top-color: transparent; transform: rotate(-45deg) translateY(-50%); }

.selectric-items li.selected { background-color: rgb(242, 242, 242); }

.selectric-open .selectric-items { display: inline-block; min-width: auto !important; width: auto !important; }

@media (max-width: 767px) {
  .selectric-open .selectric-items { font-size: 1rem; }
}

.selectric-items li:hover { background: rgb(242, 242, 242); }

body.particulares svg .fill { fill: rgb(106, 63, 36); }

body.particulares svg .stroke { stroke: rgb(106, 63, 36); }

body.particulares .btn { border: 2px solid rgb(106, 63, 36); }

@media (min-width: 993px) {
  body.particulares .btn:hover { background-color: rgb(106, 63, 36); }
}

body.particulares .noticia-detalhe-container li a, body.particulares .noticia-detalhe-container p a, body.particulares .page-content li a, body.particulares .page-content p a { color: rgb(106, 63, 36); }

body.particulares .contactos-squares-container .square .inner::after, body.particulares .homepage-header-menu .square.active, body.particulares .menu-links > li.active::before { background-color: rgb(106, 63, 36); }

body.particulares .contactos-squares-container .square h5 { color: rgb(106, 63, 36); }

body.particulares .tabelas-half:not(:last-child) .tabelas { border-right: 1px solid rgb(106, 63, 36); }

@media (max-width: 767px) {
  body.particulares .tabelas-half:not(:last-child) .tabelas { border-bottom: 1px solid rgb(106, 63, 36); }
}

body.particulares .page-content li::before, body.particulares .sub_header li::before { background-image: url("data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" x=\"0px\" y=\"0px\" width=\"6.937px\" height=\"10.795px\" viewBox=\"0 0 6.937 10.795\" enable-background=\"new 0 0 6.937 10.795\" xml:space=\"preserve\"><path fill=\"%236a3f24\" d=\"M1.84,10.669c-0.167,0.167-0.435,0.167-0.603,0L0.125,9.557c-0.167-0.167-0.167-0.435,0-0.603l3.557-3.557L0.125,1.84c-0.167-0.167-0.167-0.435,0-0.603l1.112-1.112c0.167-0.167,0.435-0.167,0.603,0l4.971,4.971 c0.167,0.167,0.167,0.435,0,0.603L1.84,10.669z\"/></svg>"); }

body.particulares .results-wrapper .highlight { color: rgb(106, 63, 36); }

body.particulares .pagination .square { border: 2px solid rgb(106, 63, 36); }

body.particulares .pagination .next::after, body.particulares .pagination .next::before, body.particulares .pagination .prev::after, body.particulares .pagination .prev::before, body.particulares .pagination .square:hover { background-color: rgb(106, 63, 36); }

body.particulares .tipos-negocio-adesao .links a { color: rgb(106, 63, 36); }

body.particulares .tipos-negocio-adesao .links a:not(.download-link)::after { background-image: url("data:image/svg+xml;utf8,<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 20.5 10\" enable-background=\"new 0 0 20.5 10\" xml:space=\"preserve\"><path class=\"stroke\" fill=\"none\" stroke=\"%236a3f24\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" d=\"M20,5,c0,0-2.6,4.5-9.8,4.5S0.5,5,0.5,5s2.6-4.5,9.8-4.5S20,5,20,5z\"/><circle class=\"stroke\" fill=\"none\" stroke=\"%236a3f24\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" cx=\"10.3\" cy=\"5\" r=\"3.8\"/></svg>"); }

body.particulares .tipos-negocio-adesao .links a:not(.download-link)::before { background-color: rgb(106, 63, 36); }

body.particulares .download-link { color: rgb(106, 63, 36); }

body.particulares .download-link::before { background-color: rgb(106, 63, 36); }

body.particulares .download-link::after { background-image: url("data:image/svg+xml;utf8,<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 25.9 23.1\" enable-background=\"new 0 0 25.9 23.1\" xml:space=\"preserve\"><path class=\"stroke\" fill=\"none\" stroke=\"%236a3f24\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" d=\"M25.4,22.6H0.5\"/><line class=\"stroke\" fill=\"none\" stroke=\"%236a3f24\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" x1=\"13\" y1=\"0.5\" x2=\"13\" y2=\"19.4\"/><polyline class=\"stroke\" fill=\"none\" stroke=\"%236a3f24\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" points=\"20.2,12.1,12.9,19.4 5.7,12.2 \"/></svg>"); }

body.particulares .documentos-links a, body.particulares .tipos-negocio-adesao .link a { color: rgb(106, 63, 36); }

body.particulares .documentos-links a::before { background-color: rgb(106, 63, 36); }

body.particulares .faq .header { color: rgb(106, 63, 36); }

body.particulares .faq .seta::after, body.particulares .faq .seta::before { background-color: rgb(106, 63, 36); }

body.particulares .balcao-resultado .ver-mapa { color: rgb(106, 63, 36); }

body.particulares .checkbox input[type="checkbox"] + label .square, body.particulares .checkbox input[type="radio"] + label .square, body.particulares .radio input[type="checkbox"] + label .square, body.particulares .radio input[type="radio"] + label .square { border: 2px solid rgb(106, 63, 36); }

body.particulares .noticias-back { color: rgb(106, 63, 36); }

body.particulares .menu-button .line { background-color: rgb(106, 63, 36); }

body.particulares .mapa-list-container > ul > li > a + ul > li > a + ul > li > a::before { background-image: url("data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" x=\"0px\" y=\"0px\" width=\"6.937px\" height=\"10.795px\" viewBox=\"0 0 6.937 10.795\" enable-background=\"new 0 0 6.937 10.795\" xml:space=\"preserve\"><path fill=\"%236a3f24\" d=\"M1.84,10.669c-0.167,0.167-0.435,0.167-0.603,0L0.125,9.557c-0.167-0.167-0.167-0.435,0-0.603l3.557-3.557L0.125,1.84c-0.167-0.167-0.167-0.435,0-0.603l1.112-1.112c0.167-0.167,0.435-0.167,0.603,0l4.971,4.971 c0.167,0.167,0.167,0.435,0,0.603L1.84,10.669z\"/></svg>"); }

body.particulares .form-input-salwrap input[type="email"], body.particulares .form-input-salwrap input[type="text"], body.particulares .selectric { border-bottom: 1px solid rgb(106, 63, 36); }

body.particulares .selectric:hover .button::after { color: rgb(106, 63, 36) !important; }

body.particulares .selectric-items li, body.particulares .selectric .label { color: rgb(106, 63, 36); }

body.particulares .selectric .button::after, body.particulares .selectric .button::before { background-color: rgb(106, 63, 36); }

body.particulares .form-success-message a { color: rgb(106, 63, 36); }

body.empresas svg .fill { fill: rgb(178, 26, 18); }

body.empresas svg .stroke { stroke: rgb(178, 26, 18); }

body.empresas .btn { border: 2px solid rgb(178, 26, 18); }

@media (min-width: 993px) {
  body.empresas .btn:hover { background-color: rgb(178, 26, 18); }
}

body.empresas .noticia-detalhe-container li a, body.empresas .noticia-detalhe-container p a, body.empresas .page-content li a, body.empresas .page-content p a { color: rgb(178, 26, 18); }

body.empresas .contactos-squares-container .square .inner::after, body.empresas .homepage-header-menu .square.active, body.empresas .menu-links > li.active::before { background-color: rgb(178, 26, 18); }

body.empresas .contactos-squares-container .square h5 { color: rgb(178, 26, 18); }

body.empresas .tabelas-half:not(:last-child) .tabelas { border-right: 1px solid rgb(178, 26, 18); }

@media (max-width: 767px) {
  body.empresas .tabelas-half:not(:last-child) .tabelas { border-bottom: 1px solid rgb(178, 26, 18); }
}

body.empresas .page-content li::before, body.empresas .sub_header li::before { background-image: url("data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" x=\"0px\" y=\"0px\" width=\"6.937px\" height=\"10.795px\" viewBox=\"0 0 6.937 10.795\" enable-background=\"new 0 0 6.937 10.795\" xml:space=\"preserve\"><path fill=\"%23b21a12\" d=\"M1.84,10.669c-0.167,0.167-0.435,0.167-0.603,0L0.125,9.557c-0.167-0.167-0.167-0.435,0-0.603l3.557-3.557L0.125,1.84c-0.167-0.167-0.167-0.435,0-0.603l1.112-1.112c0.167-0.167,0.435-0.167,0.603,0l4.971,4.971 c0.167,0.167,0.167,0.435,0,0.603L1.84,10.669z\"/></svg>"); }

body.empresas .results-wrapper .highlight { color: rgb(178, 26, 18); }

body.empresas .pagination .square { border: 2px solid rgb(178, 26, 18); }

body.empresas .pagination .next::after, body.empresas .pagination .next::before, body.empresas .pagination .prev::after, body.empresas .pagination .prev::before, body.empresas .pagination .square:hover { background-color: rgb(178, 26, 18); }

body.empresas .tipos-negocio-adesao .links a { color: rgb(178, 26, 18); }

body.empresas .tipos-negocio-adesao .links a:not(.download-link)::after { background-image: url("data:image/svg+xml;utf8,<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 20.5 10\" enable-background=\"new 0 0 20.5 10\" xml:space=\"preserve\"><path class=\"stroke\" fill=\"none\" stroke=\"%23b21a12\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" d=\"M20,5,c0,0-2.6,4.5-9.8,4.5S0.5,5,0.5,5s2.6-4.5,9.8-4.5S20,5,20,5z\"/><circle class=\"stroke\" fill=\"none\" stroke=\"%23b21a12\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" cx=\"10.3\" cy=\"5\" r=\"3.8\"/></svg>"); }

body.empresas .tipos-negocio-adesao .links a:not(.download-link)::before { background-color: rgb(178, 26, 18); }

body.empresas .download-link { color: rgb(178, 26, 18); }

body.empresas .download-link::before { background-color: rgb(178, 26, 18); }

body.empresas .download-link::after { background-image: url("data:image/svg+xml;utf8,<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 25.9 23.1\" enable-background=\"new 0 0 25.9 23.1\" xml:space=\"preserve\"><path class=\"stroke\" fill=\"none\" stroke=\"%23b21a12\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" d=\"M25.4,22.6H0.5\"/><line class=\"stroke\" fill=\"none\" stroke=\"%23b21a12\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" x1=\"13\" y1=\"0.5\" x2=\"13\" y2=\"19.4\"/><polyline class=\"stroke\" fill=\"none\" stroke=\"%23b21a12\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" points=\"20.2,12.1,12.9,19.4 5.7,12.2 \"/></svg>"); }

body.empresas .documentos-links a, body.empresas .tipos-negocio-adesao .link a { color: rgb(178, 26, 18); }

body.empresas .documentos-links a::before { background-color: rgb(178, 26, 18); }

body.empresas .faq .header { color: rgb(178, 26, 18); }

body.empresas .faq .seta::after, body.empresas .faq .seta::before { background-color: rgb(178, 26, 18); }

body.empresas .balcao-resultado .ver-mapa { color: rgb(178, 26, 18); }

body.empresas .checkbox input[type="checkbox"] + label .square, body.empresas .checkbox input[type="radio"] + label .square, body.empresas .radio input[type="checkbox"] + label .square, body.empresas .radio input[type="radio"] + label .square { border: 2px solid rgb(178, 26, 18); }

body.empresas .noticias-back { color: rgb(178, 26, 18); }

body.empresas .menu-button .line { background-color: rgb(178, 26, 18); }

body.empresas .mapa-list-container > ul > li > a + ul > li > a + ul > li > a::before { background-image: url("data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" x=\"0px\" y=\"0px\" width=\"6.937px\" height=\"10.795px\" viewBox=\"0 0 6.937 10.795\" enable-background=\"new 0 0 6.937 10.795\" xml:space=\"preserve\"><path fill=\"%23b21a12\" d=\"M1.84,10.669c-0.167,0.167-0.435,0.167-0.603,0L0.125,9.557c-0.167-0.167-0.167-0.435,0-0.603l3.557-3.557L0.125,1.84c-0.167-0.167-0.167-0.435,0-0.603l1.112-1.112c0.167-0.167,0.435-0.167,0.603,0l4.971,4.971 c0.167,0.167,0.167,0.435,0,0.603L1.84,10.669z\"/></svg>"); }

body.empresas .form-input-salwrap input[type="email"], body.empresas .form-input-salwrap input[type="text"], body.empresas .selectric { border-bottom: 1px solid rgb(178, 26, 18); }

body.empresas .selectric:hover .button::after { color: rgb(178, 26, 18) !important; }

body.empresas .selectric-items li, body.empresas .selectric .label { color: rgb(178, 26, 18); }

body.empresas .selectric .button::after, body.empresas .selectric .button::before { background-color: rgb(178, 26, 18); }

body.empresas .form-success-message a { color: rgb(178, 26, 18); }

body.institucional svg .fill { fill: rgb(102, 10, 25); }

body.institucional svg .stroke { stroke: rgb(102, 10, 25); }

body.institucional .btn { border: 2px solid rgb(102, 10, 25); }

@media (min-width: 993px) {
  body.institucional .btn:hover { background-color: rgb(102, 10, 25); }
}

body.institucional .noticia-detalhe-container li a, body.institucional .noticia-detalhe-container p a, body.institucional .page-content li a, body.institucional .page-content p a { color: rgb(102, 10, 25); }

body.institucional .contactos-squares-container .square .inner::after, body.institucional .homepage-header-menu .square.active, body.institucional .menu-links > li.active::before { background-color: rgb(102, 10, 25); }

body.institucional .contactos-squares-container .square h5 { color: rgb(102, 10, 25); }

body.institucional .tabelas-half:not(:last-child) .tabelas { border-right: 1px solid rgb(102, 10, 25); }

@media (max-width: 767px) {
  body.institucional .tabelas-half:not(:last-child) .tabelas { border-bottom: 1px solid rgb(102, 10, 25); }
}

body.institucional .page-content li::before, body.institucional .sub_header li::before { background-image: url("data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" x=\"0px\" y=\"0px\" width=\"6.937px\" height=\"10.795px\" viewBox=\"0 0 6.937 10.795\" enable-background=\"new 0 0 6.937 10.795\" xml:space=\"preserve\"><path fill=\"%23660a19\" d=\"M1.84,10.669c-0.167,0.167-0.435,0.167-0.603,0L0.125,9.557c-0.167-0.167-0.167-0.435,0-0.603l3.557-3.557L0.125,1.84c-0.167-0.167-0.167-0.435,0-0.603l1.112-1.112c0.167-0.167,0.435-0.167,0.603,0l4.971,4.971 c0.167,0.167,0.167,0.435,0,0.603L1.84,10.669z\"/></svg>"); }

body.institucional .results-wrapper .highlight { color: rgb(102, 10, 25); }

body.institucional .pagination .square { border: 2px solid rgb(102, 10, 25); }

body.institucional .pagination .next::after, body.institucional .pagination .next::before, body.institucional .pagination .prev::after, body.institucional .pagination .prev::before, body.institucional .pagination .square:hover { background-color: rgb(102, 10, 25); }

body.institucional .tipos-negocio-adesao .links a { color: rgb(102, 10, 25); }

body.institucional .tipos-negocio-adesao .links a:not(.download-link)::after { background-image: url("data:image/svg+xml;utf8,<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 20.5 10\" enable-background=\"new 0 0 20.5 10\" xml:space=\"preserve\"><path class=\"stroke\" fill=\"none\" stroke=\"%23660a19\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" d=\"M20,5,c0,0-2.6,4.5-9.8,4.5S0.5,5,0.5,5s2.6-4.5,9.8-4.5S20,5,20,5z\"/><circle class=\"stroke\" fill=\"none\" stroke=\"%23660a19\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" cx=\"10.3\" cy=\"5\" r=\"3.8\"/></svg>"); }

body.institucional .tipos-negocio-adesao .links a:not(.download-link)::before { background-color: rgb(102, 10, 25); }

body.institucional .download-link { color: rgb(102, 10, 25); }

body.institucional .download-link::before { background-color: rgb(102, 10, 25); }

body.institucional .download-link::after { background-image: url("data:image/svg+xml;utf8,<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 25.9 23.1\" enable-background=\"new 0 0 25.9 23.1\" xml:space=\"preserve\"><path class=\"stroke\" fill=\"none\" stroke=\"%23660a19\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" d=\"M25.4,22.6H0.5\"/><line class=\"stroke\" fill=\"none\" stroke=\"%23660a19\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" x1=\"13\" y1=\"0.5\" x2=\"13\" y2=\"19.4\"/><polyline class=\"stroke\" fill=\"none\" stroke=\"%23660a19\" stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-miterlimit=\"10\" points=\"20.2,12.1,12.9,19.4 5.7,12.2 \"/></svg>"); }

body.institucional .documentos-links a, body.institucional .tipos-negocio-adesao .link a { color: rgb(102, 10, 25); }

body.institucional .documentos-links a::before { background-color: rgb(102, 10, 25); }

body.institucional .faq .header { color: rgb(102, 10, 25); }

body.institucional .faq .seta::after, body.institucional .faq .seta::before { background-color: rgb(102, 10, 25); }

body.institucional .balcao-resultado .ver-mapa { color: rgb(102, 10, 25); }

body.institucional .checkbox input[type="checkbox"] + label .square, body.institucional .checkbox input[type="radio"] + label .square, body.institucional .radio input[type="checkbox"] + label .square, body.institucional .radio input[type="radio"] + label .square { border: 2px solid rgb(102, 10, 25); }

body.institucional .noticias-back { color: rgb(102, 10, 25); }

body.institucional .menu-button .line { background-color: rgb(102, 10, 25); }

body.institucional .mapa-list-container > ul > li > a + ul > li > a + ul > li > a::before { background-image: url("data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" x=\"0px\" y=\"0px\" width=\"6.937px\" height=\"10.795px\" viewBox=\"0 0 6.937 10.795\" enable-background=\"new 0 0 6.937 10.795\" xml:space=\"preserve\"><path fill=\"%23660a19\" d=\"M1.84,10.669c-0.167,0.167-0.435,0.167-0.603,0L0.125,9.557c-0.167-0.167-0.167-0.435,0-0.603l3.557-3.557L0.125,1.84c-0.167-0.167-0.167-0.435,0-0.603l1.112-1.112c0.167-0.167,0.435-0.167,0.603,0l4.971,4.971 c0.167,0.167,0.167,0.435,0,0.603L1.84,10.669z\"/></svg>"); }

body.institucional .form-input-salwrap input[type="email"], body.institucional .form-input-salwrap input[type="text"], body.institucional .selectric { border-bottom: 1px solid rgb(102, 10, 25); }

body.institucional .selectric:hover .button::after { color: rgb(102, 10, 25) !important; }

body.institucional .selectric-items li, body.institucional .selectric .label { color: rgb(102, 10, 25); }

body.institucional .selectric .button::after, body.institucional .selectric .button::before { background-color: rgb(102, 10, 25); }

body.institucional .form-success-message a { color: rgb(102, 10, 25); }

html { font-family: "PT Sans", sans-serif; color: rgb(33, 33, 33); }

.global-container, .page-container { position: relative; width: 100%; overflow: hidden; }

.content, .wrapper { position: relative; width: 100%; margin: 0px auto; }

.half { width: 50%; }

.homepage-header h1 { font-size: 72px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .homepage-header h1 { font-size: 54px; }
}

@media (max-width: 992px) {
  .homepage-header h1 { font-size: 36px; }
}

.banner-container h2, .contactos-squares-container h2 { font-size: 48px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .banner-container h2, .contactos-squares-container h2 { font-size: 36px; }
}

@media (max-width: 992px) {
  .banner-container h2, .contactos-squares-container h2 { font-size: 24px; }
}

@media (max-width: 767px) {
  .banner-container h2, .contactos-squares-container h2 { font-size: 28px; }
}

.default-half-section h3 { font-size: 36px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .default-half-section h3 { font-size: 27px; }
}

@media (max-width: 992px) {
  .default-half-section h3 { font-size: 20px; }
}

@media (max-width: 767px) {
  .default-half-section h3 { font-size: 24px; }
}

.banner-container p, .homepage-header p { font-size: 18px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .banner-container p, .homepage-header p { font-size: 14px; }
}

@media (max-width: 767px) {
  .banner-container p, .homepage-header p { font-size: 15px; }
}

.tabelas .header { font-size: 12px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tabelas .header { font-size: 9px; }
}

@media (max-width: 992px) {
  .tabelas .header { font-size: 12px; }
}

.tabelas .body { font-size: 16px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tabelas .body { font-size: 13px; }
}

@media (max-width: 767px) {
  .tabelas .body { font-size: 16px; }
}

.tabela-fonte { font-size: 12px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tabela-fonte { font-size: 10px; }
}

@media (max-width: 767px) {
  .tabela-fonte { font-size: 12px; }
}

.page-header h1 { font-size: 72px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .page-header h1 { font-size: 54px; }
}

@media (max-width: 992px) {
  .page-header h1 { font-size: 36px; }
}

.balcoes-resultados-container h2, .contactos-page-content h2, .form-page-content h2, .mapa-page-content h2, .page-content h2, .results-page-content h1 { font-size: 48px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .balcoes-resultados-container h2, .contactos-page-content h2, .form-page-content h2, .mapa-page-content h2, .page-content h2, .results-page-content h1 { font-size: 36px; }
}

@media (max-width: 992px) {
  .balcoes-resultados-container h2, .contactos-page-content h2, .form-page-content h2, .mapa-page-content h2, .page-content h2, .results-page-content h1 { font-size: 24px; }
}

.balcoes-resultados-container h3, .balcoes-resultados-container h4, .contactos-page-content h3, .contactos-page-content h4, .noticia-detalhe-container h3, .page-content h3, .page-content h4 { font-size: 36px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .balcoes-resultados-container h3, .balcoes-resultados-container h4, .contactos-page-content h3, .contactos-page-content h4, .noticia-detalhe-container h3, .page-content h3, .page-content h4 { font-size: 27px; }
}

@media (max-width: 992px) {
  .balcoes-resultados-container h3, .balcoes-resultados-container h4, .contactos-page-content h3, .contactos-page-content h4, .noticia-detalhe-container h3, .page-content h3, .page-content h4 { font-size: 20px; }
}

@media (max-width: 767px) {
  .balcoes-resultados-container h3, .balcoes-resultados-container h4, .contactos-page-content h3, .contactos-page-content h4, .noticia-detalhe-container h3, .page-content h3, .page-content h4 { font-size: 24px; }
}

.download-link, .faq .header { font-size: 28px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .download-link, .faq .header { font-size: 21px; }
}

@media (max-width: 992px) {
  .download-link, .faq .header { font-size: 18px; }
}

@media (max-width: 767px) {
  .download-link, .faq .header { font-size: 20px; }
}

.tipos-negocio-adesao .link a:not(.download-link) { font-size: 16px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tipos-negocio-adesao .link a:not(.download-link) { font-size: 12px; }
}

@media (max-width: 992px) {
  .tipos-negocio-adesao .link a:not(.download-link) { font-size: 14px; }
}

@media (max-width: 767px) {
  .tipos-negocio-adesao .link a:not(.download-link) { font-size: 15px; }
}

.noticias-square h4, .page-content h5 { font-size: 24px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .noticias-square h4, .page-content h5 { font-size: 18px; }
}

.contactos-page-content li, .contactos-page-content p, .mapa-list-container > ul > li > a + ul > li > a, .mapa-list-container > ul > li > a + ul > li > a + ul > li > a, .noticia-detalhe-container p, .noticia-detalhe-container ul, .noticias-square p, .page-content li, .page-content p, .page-header p { font-size: 18px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .contactos-page-content li, .contactos-page-content p, .mapa-list-container > ul > li > a + ul > li > a, .mapa-list-container > ul > li > a + ul > li > a + ul > li > a, .noticia-detalhe-container p, .noticia-detalhe-container ul, .noticias-square p, .page-content li, .page-content p, .page-header p { font-size: 14px; }
}

@media (max-width: 767px) {
  .contactos-page-content li, .contactos-page-content p, .mapa-list-container > ul > li > a + ul > li > a, .mapa-list-container > ul > li > a + ul > li > a + ul > li > a, .noticia-detalhe-container p, .noticia-detalhe-container ul, .noticias-square p, .page-content li, .page-content p, .page-header p { font-size: 15px; }
}

.contactos-page-content blockquote, .page-content blockquote { font-size: 36px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .contactos-page-content blockquote, .page-content blockquote { font-size: 27px; }
}

@media (max-width: 992px) {
  .contactos-page-content blockquote, .page-content blockquote { font-size: 20px; }
}

@media (max-width: 767px) {
  .contactos-page-content blockquote, .page-content blockquote { font-size: 24px; }
}

.download-link:hover::after, .mapa-list-container > ul > li > a, .noticia-detalhe-container h6, .noticias-square h6, .results-page-content h6, .tipos-negocio-adesao h6 { font-size: 14px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .download-link:hover::after, .mapa-list-container > ul > li > a, .noticia-detalhe-container h6, .noticias-square h6, .results-page-content h6, .tipos-negocio-adesao h6 { font-size: 10px; }
}

@media (max-width: 767px) {
  .download-link:hover::after, .mapa-list-container > ul > li > a, .noticia-detalhe-container h6, .noticias-square h6, .results-page-content h6, .tipos-negocio-adesao h6 { font-size: 12px; }
}

.contactos-squares-container h5 span { font-size: 18px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .contactos-squares-container h5 span { font-size: 14px; }
}

@media (max-width: 767px) {
  .contactos-squares-container h5 span { font-size: 15px; }
}

.balcoes-form input { font-size: 24px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .balcoes-form input { font-size: 18px; }
}

@media (max-width: 992px) {
  .balcoes-form input { font-size: 15px; }
}

.balcao-resultado .line { font-size: 18px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .balcao-resultado .line { font-size: 14px; }
}

@media (max-width: 767px) {
  .balcao-resultado .line { font-size: 15px; }
}

.result h4 { font-size: 24px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .result h4 { font-size: 28px; }
}

@media (max-width: 992px) {
  .result h4 { font-size: 18px; }
}

.results-page-content p { font-size: 18px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .results-page-content p { font-size: 14px; }
}

@media (max-width: 767px) {
  .results-page-content p { font-size: 15px; }
}

.page-404-container h6 { font-size: 14px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .page-404-container h6 { font-size: 10px; }
}

@media (max-width: 767px) {
  .page-404-container h6 { font-size: 12px; }
}

.page-404-container h2 { font-size: 48px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .page-404-container h2 { font-size: 36px; }
}

@media (max-width: 992px) {
  .page-404-container h2 { font-size: 24px; }
}

.page-404-container p { font-size: 18px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .page-404-container p { font-size: 14px; }
}

@media (max-width: 767px) {
  .page-404-container p { font-size: 15px; }
}

.contactos-squares-container h5, .homepage-header-menu h5, .links-404-container h5 { font-size: 24px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .contactos-squares-container h5, .homepage-header-menu h5, .links-404-container h5 { font-size: 18px; }
}

@media (max-width: 992px) {
  .contactos-squares-container h5, .homepage-header-menu h5, .links-404-container h5 { font-size: 16px; }
}

@media (max-width: 767px) {
  .contactos-squares-container h5, .homepage-header-menu h5, .links-404-container h5 { font-size: 14px; }
}

.btn { position: relative; display: inline-block; width: 195px; height: 50px; line-height: 46px; font-size: 1.125rem; font-weight: 700; text-align: center; }

@media (max-width: 992px) {
  .btn { width: 120px; height: 35px; line-height: 31px; font-size: 0.75rem; }
}

@media (max-width: 767px) {
  .btn { display: block; max-width: 320px; width: 100%; }
}

@media (min-width: 993px) {
  .btn:hover { color: rgb(255, 255, 255); }
}

.btn:hover svg .fill { fill: rgb(255, 255, 255) !important; }

.btn:hover svg .stroke { stroke: rgb(255, 255, 255) !important; }

.btn[disabled] { color: rgb(157, 157, 157) !important; border: 2px solid rgb(157, 157, 157) !important; }

.btn[disabled] svg .fill { fill: rgb(157, 157, 157) !important; }

.btn[disabled] svg .stroke { stroke: rgb(157, 157, 157) !important; }

.btn.error { margin-bottom: 60px; }

.btn.error::after { position: absolute; top: calc(100% + 25px); left: 0px; width: 100%; line-height: 140%; content: attr(data-error); color: red; text-align: center; font-size: 0.875rem; font-weight: 300; }

.btn > span { line-height: normal; }

.btn > span, .btn svg { display: inline-block; }

.btn svg { width: 25px; height: 25px; margin-right: 0.625rem; vertical-align: middle; margin-top: -0.3125rem; }

@media (max-width: 992px) {
  .btn svg { width: 15px; height: 15px; margin-right: 0.15625rem; }
}

.salwrap { display: inline-block; }

.btn-container { display: flex; }

.btn-container.align-left { justify-content: flex-start; }

@media (max-width: 767px) {
  .btn-container.align-left { justify-content: center; }
}

@media (min-width: 768px) {
  .btn-container.align-left .btn:not(.error) { margin: 0px 0.9375rem; }
}

@media (max-width: 767px) {
  .btn-container.align-left .btn:not(.error) { margin: 0px auto 0.9375rem; }
}

@media (min-width: 768px) {
  .btn-container.align-left .btn:not(.error):not(:only-child):first-child { margin-left: 0px; }
}

@media (min-width: 768px) {
  .btn-container.align-left .btn:not(.error):not(:only-child):last-child { margin-right: 0px; }
}

@media (min-width: 768px) {
  .btn-container.align-left .btn:not(.error):only-child { margin: 0px; }
}

.btn-container.align-left .btn:not(.error):last-child { margin-bottom: 0px; }

.btn-container.align-right { justify-content: flex-end; }

@media (max-width: 767px) {
  .btn-container.align-right { justify-content: center; }
}

@media (min-width: 768px) {
  .btn-container.align-right .btn:not(.error) { margin: 0px 0.9375rem; }
}

@media (max-width: 767px) {
  .btn-container.align-right .btn:not(.error) { margin: 0px auto 0.9375rem; }
}

@media (min-width: 768px) {
  .btn-container.align-right .btn:not(.error):not(:only-child):first-child { margin-left: 0px; }
}

@media (min-width: 768px) {
  .btn-container.align-right .btn:not(.error):not(:only-child):last-child { margin-right: 0px; }
}

@media (min-width: 768px) {
  .btn-container.align-right .btn:not(.error):only-child { margin: 0px; }
}

.btn-container.align-right .btn:not(.error):last-child { margin-bottom: 0px; }

.menu-nav, .sections-nav { width: 100%; }

.menu-nav > .content, .sections-nav > .content { max-width: 1400px; padding: 0px 2.5rem; display: flex; justify-content: space-between; }

.sections-nav { background-color: rgb(242, 242, 242); height: 50px; }

.sections-nav .menu-left { padding-left: 160px; }

.sections-nav .menu-right { display: flex; align-items: center; }

.menu-nav { background-color: rgb(255, 255, 255); height: 100px; border-bottom: 1px solid rgb(242, 242, 242); transition: height 0.35s ease-in-out 0s; }

.menu-nav .menu-left { display: flex; align-items: center; }

.header-mobile-nav, .header-nav { position: fixed; top: 0px; left: 0px; width: 100%; z-index: 10; height: auto; }

@media (max-width: 992px) {
  .header-nav { display: none; }
}

@media (min-width: 993px) {
  .header-nav.min .logo img { width: 70px; }
}

@media (min-width: 993px) {
  .header-nav.min .menu-links, .header-nav.min .menu-nav { height: 50px; }
}

@media (min-width: 993px) {
  .header-nav.min .menu-links > li.with_sub, .header-nav.min .menu-links > li a { line-height: 50px; }
}

@media (min-width: 993px) {
  .header-nav.min .login-menu, .header-nav.min .login-menu .header { height: 50px; }
}

@media (min-width: 993px) {
  .header-nav.min .sub_header { top: 100px; }
}

.header-mobile-nav { display: none; padding: 0px 0.625rem 0px 1.5625rem; background-color: rgb(255, 255, 255); }

@media (max-width: 992px) {
  .header-mobile-nav { display: block; }
}

.header-mobile-nav > .content { display: flex; justify-content: space-between; align-items: center; height: 70px; }

.header-mobile-nav .logo, .header-mobile-nav .logo img { width: 90px; }

.header-mobile-nav .menu-right { display: flex; align-items: center; }

.sub_header { display: block; position: fixed; width: 100%; top: 149px; left: 0px; background-color: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.15) 5px 5px 5px; overflow: hidden; opacity: 0; height: 0px; pointer-events: none; transition: height 0.4s ease-in-out 0s, opacity 0.01s ease-in-out 0.5s, top 0.35s ease-in-out 0s; }

@media (max-width: 992px) {
  .sub_header { position: relative; top: auto; left: auto; background-color: transparent; box-shadow: none; }
}

.sub_header.open { height: 230px; transition: height 0.4s ease-in-out 0s; }

@media (max-width: 992px) {
  .sub_header.open { height: auto; margin-top: -0.3125rem; margin-bottom: 1.875rem; }
}

.sub_header.active { opacity: 1; pointer-events: all; }

.sub_header > .content { max-width: 1320px; margin: 0px auto; display: flex; justify-content: space-between; flex-wrap: wrap; padding: 2.8125rem 2.5rem 2.8125rem 10.9375rem; }

@media (max-width: 992px) {
  .sub_header > .content { padding: 0px 2.5rem; }
}

.sub_header .text { width: 33.333%; }

@media (max-width: 992px) {
  .sub_header .text { display: none; }
}

.sub_header .text h3 { font-size: 2.5rem; font-weight: 700; }

.sub_header .links { width: 66.666%; height: 140px; display: flex; flex-flow: column wrap; align-items: flex-start; }

@media (max-width: 992px) {
  .sub_header .links { width: 100%; flex-direction: row; height: auto; }
}

.sub_header .links li { padding-left: 1.25rem; break-inside: avoid; font-size: 1.125rem; margin-bottom: 1.09375rem; }

@media (max-width: 992px) {
  .sub_header .links li { width: 100%; padding-left: 0.9375rem; color: rgb(157, 157, 157); }
}

.sub_header .links li.active { font-weight: 700; }

@media (min-width: 993px) {
  .sub_header .links li:hover { font-weight: 600; }
}

@media (max-width: 992px) {
  .sub_header .links li::before { content: none; }
}

@media (min-width: 993px) {
  .sub_header .links li:nth-child(4n) { margin-bottom: 0px; }
}

.sub_header .links li:last-child { margin-bottom: 0px; }

.page-content li, .sub_header li { position: relative; display: inline-block; }

.page-content li::before, .sub_header li::before { content: ""; width: 8px; height: 12px; position: absolute; left: 0px; transform: translateY(-50%); background-size: cover; background-position: 50% center; background-repeat: no-repeat; }

.sub_header li::before { top: 9px; }

.page-content li { width: 100%; }

.page-container { width: 100%; margin-top: 150px; transition: margin 0.35s ease-in-out 0s; }

@media (max-width: 992px) {
  .page-container { margin-top: 70px; }
}

@media (min-width: 993px) {
  .page-container.min { margin-top: 100px; }
}

.logo { display: inline-block; width: 135px; margin-right: 1.5625rem; align-items: center; }

.logo img { width: 135px; transition: width 0.35s ease-in-out 0s; }

.contactos-links, .languages-links, .menu-links, .sections-links { display: inline-block; }

.contactos-links li, .languages-links li, .menu-links li, .sections-links li { display: inline-block; cursor: pointer; float: left; }

.contactos-links li span, .languages-links li span, .menu-links li span, .sections-links li span { display: inline-block; vertical-align: middle; line-height: normal; }

.contactos-links, .languages-links { border-right: 1px solid rgb(157, 157, 157); }

.contactos-links li, .languages-links li { font-size: 0.875rem; }

.contactos-links li:hover a, .languages-links li:hover a { color: rgb(33, 33, 33); }

.contactos-links li a, .languages-links li a { color: rgb(178, 178, 178); }

.contactos-links { padding: 0.3125rem 1.875rem; }

.languages-links li { font-weight: 700; padding: 0.3125rem 0.9375rem; }

.languages-links li:last-child { padding-right: 1.875rem; }

.languages-links li.active a { color: rgb(33, 33, 33); }

.menu-links > li, .menu-mobile-links > li { position: relative; font-weight: 700; font-size: 1.125rem; }

.menu-links > li.active a, .menu-mobile-links > li.active a { color: rgb(33, 33, 33); }

.menu-links { display: none; height: 100px; transition: height 0.35s ease-in-out 0s; }

.menu-links.show-menu { display: inline-block; }

.menu-links > li { padding: 0px 0.9375rem; font-weight: 700; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .menu-links > li { font-size: 1rem; padding: 0px 0.625rem; }
}

.menu-links > li:hover a { color: rgb(33, 33, 33); }

.menu-links > li.active::before { content: ""; }

.menu-links > li.with_sub { line-height: 100px; color: rgb(178, 178, 178); transition: line-height 0.35s ease-in-out 0s; }

.menu-links > li.with_sub.active { color: rgb(33, 33, 33); }

@media (max-width: 992px) {
  .menu-links > li.with_sub { line-height: normal; }
}

.menu-links > li::before { position: absolute; bottom: 0px; left: 0px; width: 100%; height: 3px; }

.menu-links > li a { display: inline-block; color: rgb(178, 178, 178); line-height: 100px; transition: line-height 0.35s ease-in-out 0s; }

.menu-mobile-links { height: 0px; overflow: hidden; }

.menu-mobile-links > li { width: 100%; color: rgb(157, 157, 157); margin-bottom: 1.5625rem; }

.menu-mobile-links > li:last-child { margin-bottom: 0px; }

.menu-mobile-links > li.active { color: rgb(33, 33, 33); }

.menu-mobile-links > li.with_sub.active .seta { transform: translateY(-50%) rotateX(180deg); }

.menu-mobile-links .seta { right: 0px; }

.menu-mobile-links .seta::after, .menu-mobile-links .seta::before { background-color: rgb(157, 157, 157); }

.sections-links li { font-weight: 700; font-size: 0.75rem; text-transform: uppercase; padding: 0px 1.25rem; }

.sections-links li.active.institucional a, .sections-links li:hover.institucional a { color: rgb(102, 10, 25); }

.sections-links li.active.particulares a, .sections-links li:hover.particulares a { color: rgb(106, 63, 36); }

.sections-links li.active.empresas a, .sections-links li:hover.empresas a { color: rgb(178, 26, 18); }

.sections-links li.active { background-color: rgb(255, 255, 255); }

.sections-links li a { display: inline-block; color: rgb(157, 157, 157); line-height: 50px; }

.search-button { position: relative; display: inline-block; width: 50px; height: 50px; margin-left: 0.9375rem; }

@media (max-width: 992px) {
  .search-button { margin-left: 0px; }
}

.search-button.open { background-color: rgb(255, 255, 255); }

.search-button.open svg { display: none; }

.search-button.open::after, .search-button.open::before { content: ""; }

.search-button svg { width: 18px; height: 18px; }

.search-button::after, .search-button::before { display: block; position: absolute; top: 50%; left: 50%; width: 1px; height: 18px; background-color: rgb(33, 33, 33); transform-origin: center center; }

.search-button::before { transform: translate(-50%, -50%) rotate(45deg); }

.search-button::after { transform: translate(-50%, -50%) rotate(-45deg); }

.login-menu .header .seta, .menu-mobile-links li.with_sub .seta, .mobile-links-section .header .seta { position: absolute; top: 50%; width: 15px; height: 10px; transform: translateY(-50%); }

.login-menu .header .seta::after, .login-menu .header .seta::before, .menu-mobile-links li.with_sub .seta::after, .menu-mobile-links li.with_sub .seta::before, .mobile-links-section .header .seta::after, .mobile-links-section .header .seta::before { position: absolute; content: ""; left: 50%; bottom: 0px; width: 2px; height: 10px; }

.login-menu .header .seta::before, .menu-mobile-links li.with_sub .seta::before, .mobile-links-section .header .seta::before { transform: translateX(-50%) rotate(45deg); transform-origin: right bottom; }

.login-menu .header .seta::after, .menu-mobile-links li.with_sub .seta::after, .mobile-links-section .header .seta::after { transform: translateX(-50%) rotate(-45deg); transform-origin: left bottom; }

.login-menu { position: relative; overflow: hidden; width: 195px; height: 100px; transition: overflow 0s linear 0.4s, height 0.35s ease-in-out 0s; }

@media (max-width: 992px) {
  .login-menu { width: 100%; height: auto; }
}

.login-menu.open { overflow: visible; }

@media (min-width: 993px) {
  .login-menu.open .login-links { visibility: visible; opacity: 1; }
}

@media (max-width: 992px) {
  .login-menu.open .login-links { height: auto; }
}

.login-menu .header { background-color: rgb(218, 92, 9); color: rgb(255, 255, 255); height: 100px; display: flex; align-items: center; justify-content: center; padding: 0px 1.25rem; cursor: pointer; transition: height 0.35s ease-in-out 0s; }

@media (max-width: 992px) {
  .login-menu .header { height: auto; justify-content: flex-start; padding: 0.9375rem 1.5625rem; }
}

.login-menu .header .sep { position: relative; display: inline-block; margin: 0px 0.9375rem; }

.login-menu .header .sep::before { content: ""; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); height: 25px; width: 1px; background-color: rgb(255, 255, 255); }

.login-menu .header .seta { right: 25px; }

.login-menu .header .seta::after, .login-menu .header .seta::before { background-color: rgb(255, 255, 255); }

.login-menu svg .stroke { stroke: rgb(218, 92, 9) !important; }

.login-menu svg .fill { fill: rgb(218, 92, 9) !important; }

.login-links { position: absolute; top: 100%; width: 100%; left: 0px; padding: 1.875rem 1.25rem; background-color: rgb(255, 255, 255); visibility: hidden; opacity: 0; z-index: 2; box-shadow: rgba(33, 33, 33, 0.15) 10px 10px 25px; transition: visibility 0.35s ease-out 0.25s, opacity 0.35s ease-out 0.25s; }

@media (max-width: 992px) {
  .login-links { position: relative; top: auto; left: auto; visibility: visible; opacity: 1; padding: 0px 1.5625rem; box-shadow: none; transition: none 0s ease 0s; height: 0px; }
}

.login-links li { width: 100%; margin-bottom: 0.625rem; }

@media (max-width: 992px) {
  .login-links li { margin-bottom: 0px; padding: 0.9375rem 0px; border-bottom: 1px solid rgb(242, 242, 242); }
}

.login-links li:last-child { margin-bottom: 0px; }

@media (max-width: 992px) {
  .login-links li:last-child { border-bottom: none; }
}

.login-links li a { color: rgb(157, 157, 157); }

.login-links li svg { position: relative; float: right; width: 20px; top: -3px; }

.footer-bottom > .content, .footer-upper > .content { max-width: 1320px; display: flex; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .footer-bottom > .content, .footer-upper > .content { max-width: 1050px; }
}

.footer-logo { width: 43%; }

@media (max-width: 992px) {
  .footer-logo { width: 100%; text-align: center; }
}

.footer-logo img { width: 200px; }

@media (max-width: 992px) {
  .footer-logo img { width: 105px; }
}

.footer-upper-links { width: 57%; min-width: 540px; font-family: "Open Sans", sans-serif; display: flex; justify-content: space-between; }

@media (max-width: 992px) {
  .footer-upper-links { display: none; }
}

.footer-upper-links > div { display: inline-block; min-width: 180px; }

.footer-upper-links h6 { display: inline-block; font-weight: 700; font-size: 0.875rem; text-transform: uppercase; margin-bottom: 1.875rem; color: rgb(157, 157, 157); float: left; clear: both; }

.footer-upper-links li { width: 100%; font-weight: 300; margin-bottom: 1.25rem; font-size: 1rem; line-height: 140%; float: left; clear: both; }

.footer-upper-links li:hover a { color: rgb(33, 33, 33); }

.footer-upper-links li:last-child { margin-bottom: 0px; }

.footer-upper-links li a { color: rgb(157, 157, 157); }

.footer-upper { padding: 3.75rem 2.5rem 5.625rem; background-color: rgb(242, 242, 242); }

@media (max-width: 992px) {
  .footer-upper { padding: 3.125rem 2.5rem; }
}

.footer-bottom { padding: 3.125rem 2.5rem; background-color: rgb(216, 216, 216); border-bottom: 5px solid rgb(218, 92, 9); font-size: 0.875rem; }

.footer-bottom > .content { justify-content: space-between; }

@media (max-width: 992px) {
  .footer-bottom > .content { justify-content: center; flex-wrap: wrap; }
}

.all-rights-reserved { color: rgb(157, 157, 157); }

@media (max-width: 992px) {
  .all-rights-reserved { order: 3; }
}

.footer-bottom-links, .footer-social-links { display: inline-block; }

.footer-bottom-links li, .footer-social-links li { display: inline-block; margin: 0px 0.78125rem; }

@media (min-width: 993px) {
  .footer-bottom-links li:first-child, .footer-social-links li:first-child { margin-left: 0px; }
}

@media (min-width: 993px) {
  .footer-bottom-links li:last-child, .footer-social-links li:last-child { margin-right: 0px; }
}

.footer-bottom-links { display: inline-block; }

@media (max-width: 992px) {
  .footer-bottom-links { order: 2; text-align: center; margin-bottom: 0.9375rem; }
}

@media (max-width: 992px) {
  .footer-bottom-links li { margin-bottom: 1.5625rem; }
}

.footer-bottom-links li a { color: rgb(33, 33, 33); }

@media (max-width: 992px) {
  .footer-social-links { order: 1; margin-bottom: 2.5rem; }
}

.footer-social-links li { font-size: 1.25rem; }

.footer-social-links li a { color: rgb(157, 157, 157); }

.homepage-header, .page-header { position: relative; width: 100%; }

.homepage-header .content, .page-header .content { color: rgb(255, 255, 255); z-index: 2; }

.homepage-header .desc, .page-header .desc { text-shadow: rgba(0, 0, 0, 0.5) 0px 2px 3px; }

.homepage-header { height: 540px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .homepage-header { height: 400px; }
}

@media (max-width: 992px) {
  .homepage-header { height: 335px; }
}

@media (max-width: 767px) {
  .homepage-header { height: 320px; }
}

.homepage-header .slide { display: none; position: absolute; top: 0px; left: 0px; width: 100%; overflow: hidden; background-size: cover; background-position: 50% center; background-repeat: no-repeat; justify-content: flex-start; }

.homepage-header .slide.active { display: block; }

.homepage-header .slide .inner { width: 100%; display: flex; align-items: center; height: 540px; padding-bottom: 7.9375rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .homepage-header .slide .inner { height: 400px; padding-bottom: 6.25rem; }
}

@media (max-width: 992px) {
  .homepage-header .slide .inner { height: 335px; padding-bottom: 4.125rem; }
}

@media (max-width: 767px) {
  .homepage-header .slide .inner { height: 320px; padding-bottom: 0px; }
}

.homepage-header .slide .content { max-width: 1410px; padding: 1.875rem 2.8125rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .homepage-header .slide .content { max-width: 1110px; }
}

@media (max-width: 992px) {
  .homepage-header .slide .content { max-width: 620px; padding: 1.875rem 1.5625rem; }
}

.homepage-header .desc { max-width: 530px; }

@media (max-width: 992px) {
  .homepage-header .desc { max-width: 315px; }
}

.homepage-header h6 { display: none; text-transform: uppercase; font-weight: 600; font-size: 0.875rem; margin-bottom: 0.9375rem; }

@media (max-width: 767px) {
  .homepage-header h6 { display: block; }
}

.homepage-header h1 { font-weight: 700; margin-bottom: 2.1875rem; }

@media (max-width: 992px) {
  .homepage-header h1 { margin-bottom: 1.25rem; }
}

.homepage-header svg { position: relative; display: inline-block; margin-left: 0.625rem; filter: drop-shadow(rgba(0, 0, 0, 0.5) 0px 2px 3px); top: 3px; }

.homepage-header svg .stroke { stroke: rgb(255, 255, 255) !important; }

.homepage-header svg .fill { fill: rgb(255, 255, 255) !important; }

.see-more { display: inline-block; }

.page-header { height: 400px; display: flex; justify-content: flex-start; align-items: center; background-size: cover; background-position: 50% center; background-repeat: no-repeat; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .page-header { height: 350px; }
}

@media (max-width: 992px) {
  .page-header { height: 250px; }
}

@media (max-width: 767px) {
  .page-header { height: 200px; }
}

.page-header > .content { max-width: 960px; }

@media (max-width: 992px) {
  .page-header > .content { max-width: 620px; padding: 0px 1.5625rem; }
}

.page-header h1 { font-weight: 700; }

.homepage-header-menu { position: relative; max-width: 1320px; width: calc(100% - 80px); margin: -7.9375rem auto 0px; box-shadow: rgba(33, 33, 33, 0.15) 10px 10px 25px; z-index: 3; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .homepage-header-menu { margin: -6.25rem auto 0px; max-width: 1050px; }
}

@media (max-width: 992px) {
  .homepage-header-menu { width: 100%; max-width: 570px; margin: -4.125rem auto 0px; }
}

@media (max-width: 767px) {
  .homepage-header-menu { max-width: none; margin: 0px auto; }
}

.homepage-header-menu .square { width: 25%; float: left; background-color: rgb(255, 255, 255); }

@media (max-width: 767px) {
  .homepage-header-menu .square { background-color: rgba(242, 242, 242, 0.5); }
}

.homepage-header-menu .square.active::after, .homepage-header-menu .square:last-child::after { content: none; }

.homepage-header-menu .square.active { color: rgb(255, 255, 255); }

.homepage-header-menu .square.active svg .fill { fill: rgb(255, 255, 255) !important; }

.homepage-header-menu .square.active svg .stroke { stroke: rgb(255, 255, 255) !important; }

.homepage-header-menu .square::after { content: ""; position: absolute; top: 17.5781%; right: 0px; width: 2px; height: 47.2656%; background-color: rgb(242, 242, 242); z-index: 3; }

@media (max-width: 767px) {
  .homepage-header-menu .square::after { top: 50%; transform: translateY(-50%); }
}

.homepage-header-menu .square .wrapper { padding-top: 78.0488%; }

@media (max-width: 992px) {
  .homepage-header-menu .square .wrapper { padding-top: 85.7143%; }
}

@media (max-width: 767px) {
  .homepage-header-menu .square .wrapper { padding-top: 112.5%; }
}

@media (max-width: 767px) {
  .homepage-header-menu .square h5 { display: none; }
}

.homepage-header-menu svg { width: auto; height: 85px; margin-bottom: 2.1875rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .homepage-header-menu svg { height: 50px; margin-bottom: 1.5625rem; }
}

@media (max-width: 992px) {
  .homepage-header-menu svg { height: 35px; margin-bottom: 0.9375rem; }
}

@media (max-width: 767px) {
  .homepage-header-menu svg { margin-bottom: 0px; }
}

.contactos-squares-container .square, .homepage-header-menu .square { position: relative; text-align: center; }

.contactos-squares-container .square .content, .homepage-header-menu .square .content { position: absolute; top: 50%; left: 50%; width: 100%; transform: translate(-50%, -50%); }

.contactos-squares-container h5, .homepage-header-menu h5 { font-weight: 700; }

.shadow-layer { position: absolute; width: 100%; height: 100%; z-index: 2; top: 0px; left: 0px; background-image: linear-gradient(45deg, rgba(0, 0, 0, 0.25), rgba(255, 255, 255, 0)); pointer-events: none; }

@media (max-width: 992px) {
  .shadow-layer { background-image: linear-gradient(45deg, rgba(0, 0, 0, 0.5), rgba(255, 255, 255, 0)); }
}

.banner-section { padding: 5.625rem 2.5rem; }

@media (max-width: 992px) {
  .banner-section { padding: 4.0625rem 1.25rem; }
}

.banner-container { max-width: 1320px; width: 100%; margin: 0px auto; display: flex; flex-wrap: wrap; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .banner-container { max-width: 1050px; }
}

@media (max-width: 992px) {
  .banner-container { max-width: 570px; }
}

.banner-container.image-left .image { order: 1; }

.banner-container.image-left .info { order: 2; justify-content: flex-end; }

@media (max-width: 767px) {
  .banner-container.image-left .info { justify-content: flex-start; }
}

.banner-container.image-right .image { order: 2; }

@media (max-width: 767px) {
  .banner-container.image-right .image { order: 1; }
}

.banner-container.image-right .info { order: 1; justify-content: flex-start; }

@media (max-width: 767px) {
  .banner-container.image-right .info { order: 2; }
}

.banner-container .info { width: 45%; display: flex; align-items: center; }

@media (max-width: 992px) {
  .banner-container .info { width: 52%; }
}

@media (max-width: 767px) {
  .banner-container .info { width: 100%; }
}

.banner-container .desc { margin-bottom: 2.1875rem; }

.banner-container .content { max-width: 425px; margin: 0px; }

@media (max-width: 767px) {
  .banner-container .content { max-width: none; margin: 0px auto; }
}

.banner-container .image { width: 55%; }

@media (max-width: 992px) {
  .banner-container .image { width: 48%; }
}

@media (max-width: 767px) {
  .banner-container .image { width: 100%; margin-bottom: 1.875rem; }
}

.banner-container .image img { width: 100%; height: auto; }

.banner-container h2 { font-weight: 700; margin-bottom: 2.1875rem; }

.banner-container p { color: rgb(157, 157, 157); line-height: 140%; }

.contactos-squares-section { padding: 7.1875rem 2.5rem; background-color: rgb(242, 242, 242); }

@media (max-width: 992px) {
  .contactos-squares-section { padding: 2.5rem 1.5625rem; }
}

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .contactos-squares-section .contactos-squares-container { max-width: 1050px; }
}

@media (max-width: 992px) {
  .contactos-squares-section .contactos-squares-container { max-width: 425px; flex-wrap: wrap; }
}

@media (max-width: 767px) {
  .contactos-squares-section .contactos-squares-container { max-width: none; }
}

@media (max-width: 767px) {
  .contactos-squares-section .contactos-squares-container .row { width: 150% !important; }
}

@media (max-width: 767px) {
  .contactos-squares-section .contactos-squares-container.thirds .square { padding: 0px 0.46875rem; margin-top: 0.1875rem; margin-bottom: 0.9375rem; }
}

.contactos-squares-section .contactos-squares-container.thirds .square .wrapper { padding-top: 100%; }

.contactos-squares-section .contactos-squares-container.thirds:last-child { margin-bottom: 0px; }

.contactos-squares-section .squares { width: 65%; }

@media (max-width: 992px) {
  .contactos-squares-section .squares { width: 100%; }
}

@media (max-width: 767px) {
  .contactos-squares-section .squares { width: calc(100% + 50px); margin: 0px -1.5625rem; overflow: auto; }
}

@media (max-width: 767px) {
  .contactos-squares-section .squares .row { width: 100%; padding: 0px 0.625rem; margin: 0px !important; }
}

.contactos-squares-container { max-width: 1320px; width: 100%; margin: 0px auto; display: flex; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .contactos-squares-container { max-width: 1050px; }
}

.contactos-squares-container.half .square { width: 50%; }

.contactos-squares-container.thirds .square { width: 33.333%; }

.contactos-squares-container .title { width: 35%; display: flex; align-items: center; }

@media (max-width: 992px) {
  .contactos-squares-container .title { width: 100%; margin-bottom: 1.875rem; }
}

.contactos-squares-container .squares .row { margin: 0px -0.78125rem; }

.contactos-squares-container .square { position: relative; float: right; padding: 0px 0.78125rem; top: 0px; transition: top 0.15s ease-in-out 0s; }

@media (min-width: 993px) {
  .contactos-squares-container .square:hover { top: 5px; }
}

@media (min-width: 993px) {
  .contactos-squares-container .square:hover .inner { box-shadow: rgba(0, 0, 0, 0.3) 0px 1px 3px; }
}

.contactos-squares-container .square .inner { position: relative; background-color: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.3) 0px 3px 5px; transition: box-shadow 0.15s ease-in-out 0s; }

.contactos-squares-container .square .inner::after { content: ""; position: absolute; left: 50%; transform: translateX(-50%); width: 120px; height: 7px; bottom: 0px; }

@media (max-width: 992px) {
  .contactos-squares-container .square .inner::after { width: 50px; height: 3px; }
}

.contactos-squares-container h2 { width: 100%; font-weight: 700; }

@media (max-width: 992px) {
  .contactos-squares-container h2 { text-align: center; }
}

.contactos-squares-container svg { width: auto; height: 85px; margin-bottom: 2.1875rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .contactos-squares-container svg { height: 50px; margin-bottom: 1.25rem; }
}

@media (max-width: 992px) {
  .contactos-squares-container svg { height: 35px; }
}

.contactos-squares-container h5 span { display: block; color: rgb(33, 33, 33); margin-bottom: 0.3125rem; }

.default-half-section { padding: 7.5rem 2.5rem; }

@media (max-width: 992px) {
  .default-half-section { padding: 2.5rem 1.5625rem; }
}

.default-half-section > .content { max-width: 1320px; display: flex; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .default-half-section > .content { max-width: 1050px; }
}

@media (max-width: 992px) {
  .default-half-section > .content { max-width: 570px; flex-wrap: wrap; }
}

@media (max-width: 992px) {
  .default-half-section .half { width: 100%; }
}

@media (min-width: 993px) {
  .default-half-section .half:first-child { padding-right: 3.125rem; }
}

@media (max-width: 992px) {
  .default-half-section .half:first-child { padding-right: 0px; order: 2; }
}

@media (min-width: 993px) {
  .default-half-section .half:nth-child(2) { padding-left: 3.125rem; }
}

@media (max-width: 992px) {
  .default-half-section .half:nth-child(2) { padding-left: 0px; order: 1; margin-bottom: 2.5rem; }
}

.default-half-section h3 { font-weight: 700; margin-bottom: 2.5rem; }

.iframe-container { position: relative; width: 100%; padding-top: 56.25%; }

@media (max-width: 992px) {
  .iframe-container { max-width: 570px; width: calc(100% + 50px); }
}

@media (max-width: 620px) {
  .iframe-container { max-width: none; margin-left: -1.5625rem; padding-top: calc(56.25% + 25px); }
}

.iframe-container iframe { position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; }

.tabelas-container { width: 100%; }

.tabelas-wrapper { display: flex; margin-bottom: 1.5625rem; }

@media (max-width: 767px) {
  .tabelas-wrapper { flex-wrap: wrap; }
}

.tabelas-moeda { margin-bottom: 1.5625rem; }

.tabelas-moeda h4 { font-weight: 700; font-size: 1.125rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tabelas-moeda h4 { font-size: 1rem; }
}

.tabelas-moeda h4:first-child { color: rgb(157, 157, 157); margin-bottom: 1.25rem; }

.tabelas-moeda h4:last-child { color: rgb(33, 33, 33); }

@media (max-width: 767px) {
  .tabelas-half { width: 100%; }
}

.tabelas-half:last-child { margin-bottom: 0px; }

@media (min-width: 768px) {
  .tabelas-half:last-child .tabelas { width: 210px; padding-right: 0px; margin-right: 0px; }
}

@media (max-width: 767px) {
  .tabelas-half:last-child .tabelas { width: 100%; margin-bottom: 0px; border-right: none !important; border-bottom: none !important; }
}

.tabelas-half:last-child .tabelas .line:last-child { padding-bottom: 0px; }

.tabelas { color: rgb(157, 157, 157); }

@media (min-width: 993px) {
  .tabelas { width: 230px; padding-right: 1.875rem; margin-right: 3.125rem; }
}

@media (max-width: 992px) {
  .tabelas { width: 230px; padding-right: 1.875rem; margin-right: 3.125rem; }
}

@media (max-width: 767px) {
  .tabelas { width: 100%; padding-right: 0px; margin-right: 0px; margin-bottom: 1.875rem; border-right: none !important; }
}

.tabelas .header, .tabelas .line { display: flex; padding-bottom: 1.875rem; }

@media (max-width: 767px) {
  .tabelas .header, .tabelas .line { padding-bottom: 1.5625rem; }
}

@media (min-width: 768px) {
  .tabelas .header:last-child, .tabelas .line:last-child { padding-bottom: 0px; }
}

.tabelas .header .cell:first-child, .tabelas .line .cell:first-child { width: 33.333%; }

@media (min-width: 768px) {
  .tabelas .header .cell:first-child, .tabelas .line .cell:first-child { max-width: 90px; }
}

.tabelas .header .cell:nth-child(2), .tabelas .line .cell:nth-child(2) { width: 33.333%; }

@media (min-width: 768px) {
  .tabelas .header .cell:nth-child(2), .tabelas .line .cell:nth-child(2) { max-width: 90px; }
}

.tabelas .header .cell:nth-child(3), .tabelas .line .cell:nth-child(3) { width: 33.333%; }

@media (min-width: 768px) {
  .tabelas .header .cell:nth-child(3), .tabelas .line .cell:nth-child(3) { max-width: 70px; }
}

.tabelas .header { text-transform: uppercase; font-weight: 700; }

.tabela-fonte { color: rgb(157, 157, 157); line-height: 125%; }

.tabela-fonte br { display: none; }

@media (max-width: 767px) {
  .tabela-fonte br { display: block; }
}

.balcoes-resultados-container h2, .contactos-page-content h2, .form-page-content h2, .mapa-page-content h2, .page-content h2 { font-weight: 700; margin-bottom: 2.1875rem; }

.form-page-content h4 { font-size: 1.5rem; margin-bottom: 1.875rem; }

.form-page-content .btn-container { margin-top: 3.125rem; }

.balcoes-resultados-container > .content, .contactos-page-content > .content, .page-content > .content { max-width: 960px; }

@media (max-width: 992px) {
  .balcoes-resultados-container > .content, .contactos-page-content > .content, .page-content > .content { max-width: 570px; }
}

.balcoes-resultados-container h3, .contactos-page-content h3, .page-content h3 { font-weight: 700; }

.balcoes-resultados-container h4, .contactos-page-content h4, .page-content h4 { font-weight: 100; }

.contactos-page-content blockquote, .page-content blockquote { font-family: "Open Sans", sans-serif; font-weight: 100; margin-bottom: 0.3125rem; }

.contactos-page-content li, .contactos-page-content p, .page-content li, .page-content p { font-family: "PT Sans", sans-serif; line-height: 140%; color: rgb(157, 157, 157); }

.contactos-page-content p + h2, .contactos-page-content ul + h2, .page-content p + h2, .page-content ul + h2 { margin-top: 6.25rem; }

@media (max-width: 992px) {
  .contactos-page-content p + h2, .contactos-page-content ul + h2, .page-content p + h2, .page-content ul + h2 { margin-top: 3.125rem; }
}

.contactos-page-content p, .page-content p { margin-bottom: 1.25rem; }

.contactos-page-content p:last-child, .page-content p:last-child { margin-bottom: 0px; }

.contactos-page-content li, .page-content li { position: relative; padding-left: 1.875rem; margin-bottom: 0.9375rem; }

.contactos-page-content li:last-child, .page-content li:last-child { margin-bottom: 0px; }

.page-content { padding: 4.6875rem 2.5rem 10.625rem; }

@media (max-width: 992px) {
  .page-content { padding: 3.125rem 1.25rem; }
}

.page-content :last-child { margin-bottom: 0px !important; }

.page-content p + .column-half, .page-content p + .downloads-links, .page-content p + .tipos-negocio-adesao-container, .page-content ul + .column-half, .page-content ul + .downloads-links, .page-content ul + .tipos-negocio-adesao-container { margin-top: 4.375rem; }

@media (max-width: 992px) {
  .page-content p + .column-half, .page-content p + .downloads-links, .page-content p + .tipos-negocio-adesao-container, .page-content ul + .column-half, .page-content ul + .downloads-links, .page-content ul + .tipos-negocio-adesao-container { margin-top: 2.1875rem; }
}

.page-content p + .documentos-links, .page-content ul + .documentos-links { margin-top: 1.875rem; }

.page-content p + h3, .page-content p + h4, .page-content p + h5, .page-content ul + h3, .page-content ul + h4, .page-content ul + h5 { margin-top: 3.125rem; }

@media (max-width: 992px) {
  .page-content p + h3, .page-content p + h4, .page-content p + h5, .page-content ul + h3, .page-content ul + h4, .page-content ul + h5 { margin-top: 1.5625rem; }
}

.page-content p + p, .page-content p + ul, .page-content ul + p, .page-content ul + ul { margin-top: 1.5625rem; }

@media (max-width: 992px) {
  .page-content p + p, .page-content p + ul, .page-content ul + p, .page-content ul + ul { margin-top: 1.25rem; }
}

.page-content .column-half + :not(.column-half) { clear: both; margin-top: 0px; padding-top: 6.25rem; }

@media (max-width: 992px) {
  .page-content .column-half + :not(.column-half) { padding-top: 3.125rem; float: none; }
}

.page-content .column-half + .column-half { margin-top: 4.375rem; }

@media (max-width: 992px) {
  .page-content .column-half + .column-half { margin-top: 2.1875rem; }
}

.page-content .column-half + .column-half.right { border-left: 2px solid rgba(157, 157, 157, 0.2); }

@media (max-width: 992px) {
  .page-content .column-half + .column-half.right { border-left: none; }
}

.page-content li::before { top: 12px; }

.page-content h5 { color: rgb(33, 33, 33); font-weight: 700; margin-bottom: 0.46875rem; }

@media (max-width: 992px) {
  .page-content h5 { margin-bottom: 0.3125rem; }
}

.page-content h3 + p, .page-content h3 + ul { margin-top: 1.5625rem; }

@media (max-width: 992px) {
  .page-content h3 + p, .page-content h3 + ul { margin-top: 0.9375rem; }
}

.contactos-page-content > .content { padding: 5.625rem 2.5rem 5rem; }

@media (max-width: 767px) {
  .contactos-page-content > .content { padding: 3.125rem 1.5625rem; }
}

.contactos-page-content .contactos-squares-container { margin: 5rem auto 8.125rem; }

.contactos-page-content .contactos-squares-container .squares { width: 100%; }

@media (max-width: 767px) {
  .contactos-page-content .contactos-squares-container .square { width: 100%; margin-bottom: 1.875rem; }
}

.contactos-page-content .contactos-squares-container .square .wrapper { padding-top: 60%; }

.mapa-page-content { padding: 7.1875rem 2.5rem; }

@media (max-width: 992px) {
  .mapa-page-content { padding: 3.125rem 1.5625rem; }
}

.mapa-page-content > .content { max-width: 1320px; }

.mapa-page-content .wrapper { padding-left: 1.25rem; }

@media (max-width: 767px) {
  .mapa-page-content .wrapper { padding-left: 0px; }
}

.mapa-page-content h2 { margin-bottom: 5.9375rem; }

@media (max-width: 767px) {
  .mapa-page-content h2 { margin-bottom: 2.5rem; }
}

.noticias-page-content { padding: 5.9375rem 2.5rem 0px; }

@media (max-width: 767px) {
  .noticias-page-content { padding: 3.75rem 2.5rem 0px; }
}

.noticias-page-content > .content { max-width: 960px; }

@media (max-width: 992px) {
  .noticias-page-content > .content { max-width: 570px; }
}

.form-page-content { padding: 5.9375rem 2.5rem 3.75rem; }

@media (max-width: 767px) {
  .form-page-content { padding: 3.75rem 1.25rem 1.875rem; }
}

.form-page-content > .content { max-width: 1020px; }

@media (max-width: 992px) {
  .form-page-content > .content { max-width: 570px; }
}

@media (max-width: 767px) {
  .form-page-content h2 { font-size: 1.875rem; }
}

.results-page-content { padding: 7.1875rem 2.5rem; }

@media (max-width: 992px) {
  .results-page-content { padding: 3.125rem 1.5625rem; }
}

.results-page-content > .content { max-width: 1020px; }

.results-page-content .highlight { font-weight: 700; }

.results-page-content h1 { margin-bottom: 2.5rem; }

@media (max-width: 992px) {
  .results-page-content h1 { margin-bottom: 1.875rem; }
}

.results-page-content h6 { color: rgb(157, 157, 157); font-weight: 700; margin-bottom: 2.8125rem; }

@media (max-width: 992px) {
  .results-page-content h6 { margin-bottom: 1.875rem; }
}

.results-page-content p { color: rgb(157, 157, 157); line-height: 125%; }

.results-page-content svg { width: 85px; margin-bottom: 3.125rem; }

@media (max-width: 992px) {
  .results-page-content svg { width: 45px; margin-bottom: 1.875rem; }
}

.column-half { width: 50%; display: block; }

@media (max-width: 767px) {
  .column-half { width: 100%; margin-bottom: 2.1875rem; }
}

.column-half svg { width: auto; height: 90px; margin-bottom: 1.875rem; }

.column-half.left { float: left; padding-right: 4.6875rem; }

@media (max-width: 767px) {
  .column-half.left { float: none; padding-right: 0px; }
}

.column-half.right { float: right; padding-left: 4.6875rem; }

@media (max-width: 767px) {
  .column-half.right { float: none; padding-left: 0px; }
}

.column-half h3 { margin-bottom: 2.5rem; }

@media (max-width: 992px) {
  .column-half h3 { margin-bottom: 1.25rem; }
}

.column-half + h2, .column-half + li, .column-half + p, .column-half + ul { width: 100%; padding-top: 6.25rem; }

@media (max-width: 992px) {
  .column-half + h2, .column-half + li, .column-half + p, .column-half + ul { padding-top: 3.125rem; }
}

.balcoes-form .salwrap, .search-container .salwrap { border-bottom: 2px solid rgb(157, 157, 157); }

.balcoes-form input, .search-container input { width: 100%; font-style: italic; padding-bottom: 0.3125rem; }

.balcoes-form input::-webkit-input-placeholder, .search-container input::-webkit-input-placeholder { color: rgb(157, 157, 157); }

.balcoes-form .bottom { display: flex; justify-content: space-between; }

@media (max-width: 767px) {
  .balcoes-form .bottom { flex-direction: column; }
}

@media (max-width: 767px) {
  .balcoes-form .btn { align-self: center; }
}

.balcoes-form-container { padding-bottom: 6.25rem; }

.balcoes-form { margin-top: 4.6875rem; }

.balcoes-form .salwrap { width: 100%; margin-bottom: 1.875rem; }

.balcoes-resultados-container { width: 100%; height: 0px; overflow: hidden; }

.balcoes-resultados-container.open { padding-bottom: 7.5rem; height: auto; }

.balcoes-resultados-container > .content { padding: 5.625rem 2.5rem 7.8125rem; }

.balcoes-resultados-container h6 { color: rgb(157, 157, 157); font-weight: 700; margin-bottom: 2.8125rem; font-size: 1.125rem; }

.balcoes-resultados-container h6:last-child { margin-bottom: 0px; }

.balcao-resultado { margin-bottom: 5.625rem; }

.balcao-resultado:last-child { margin-bottom: 0px; }

.balcao-resultado .ver-mapa { font-size: 1.125rem; line-height: normal; align-items: center; font-weight: 700; }

@media (max-width: 767px) {
  .balcao-resultado .ver-mapa { display: none; font-size: 0.875rem; }
}

.balcao-resultado svg { width: 30px; height: 25px; margin-right: 0.625rem; }

.balcao-resultado h3 { margin-bottom: 1.5625rem; }

.balcao-resultado h3 .ver-mapa { display: inline-flex; margin-left: 4.6875rem; }

@media (max-width: 767px) {
  .balcao-resultado h3 .ver-mapa { display: none; }
}

.balcao-resultado .line { color: rgb(157, 157, 157); margin-bottom: 0.9375rem; }

.balcao-resultado .line:last-child { margin-bottom: 0px; }

.balcao-resultado .line:nth-last-child(2) + .ver-mapa { display: none; }

@media (max-width: 767px) {
  .balcao-resultado .line:nth-last-child(2) + .ver-mapa { display: flex; }
}

.balcao-resultado .param { display: inline-block; width: 180px; font-weight: 600; color: rgb(33, 33, 33); }

@media (max-width: 992px) {
  .balcao-resultado .param { width: 100px; }
}

@media (max-width: 767px) {
  .balcao-resultado .param { width: 55px; }
}

.search-container { display: block; position: fixed; width: 100%; top: 149px; left: 0px; background-color: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.15) 5px 5px 5px; overflow: hidden; opacity: 0; height: 0px; pointer-events: none; transition: height 0.4s ease-in-out 0s, opacity 0.01s ease-in-out 0.5s; z-index: 12; }

@media (max-width: 992px) {
  .search-container { top: 69px; box-shadow: none; }
}

.search-container.open { height: 230px; opacity: 1; pointer-events: all; transition: height 0.4s ease-in-out 0s; }

@media (max-width: 992px) {
  .search-container.open { height: 70px; }
}

.search-container > .content { max-width: 1400px; padding: 5.3125rem 2.5rem; }

@media (max-width: 992px) {
  .search-container > .content { padding: 0.9375rem 1.5625rem; }
}

.search-container form { display: flex; align-items: center; }

.search-container .salwrap { position: relative; width: calc(100% - 285px); padding-left: 4.6875rem; margin-right: 5.625rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .search-container .salwrap { width: calc(100% - 255px); padding-left: 3.125rem; margin-right: 3.75rem; }
}

@media (max-width: 992px) {
  .search-container .salwrap { width: 100%; margin-right: 0px; padding: 0px 2.5rem 0px 0.625rem; border-bottom: 1px solid rgb(157, 157, 157); }
}

.search-container .salwrap::before { content: ""; position: absolute; bottom: 10px; left: 0px; width: 40px; height: 41px; background-image: url("data:image/svg+xml;utf8,<svg version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\" viewBox=\"0 0 39.8 39.8\" enable-background=\"new 0 0 39.8 39.8\" xml:space=\"preserve\"><circle fill=\"none\" stroke=\"%23B2B2B2\" stroke-width=\"2\" stroke-miterlimit=\"10\" cx=\"26\" cy=\"13.7\" r=\"12.7\"/><path fill=\"none\" stroke=\"%23B2B2B2\" stroke-width=\"2\" stroke-miterlimit=\"10\" d=\"M2.2,38.3l-0.7-0.7c-0.6-0.6-0.6-1.7,0-2.4l7.3-7.3c0.6-0.6,1.7-0.6,2.4,0l0.7,0.7c0.6,0.6,0.6,1.7,0,2.4l-7.3,7.3C3.9,38.9,2.8,38.9,2.2,38.3z\"/><line fill=\"none\" stroke=\"%23B2B2B2\" stroke-width=\"2\" stroke-miterlimit=\"10\" x1=\"17\" y1=\"22.8\" x2=\"11.5\" y2=\"28.3\"/></svg>"); background-size: contain; background-position: 50% center; background-repeat: no-repeat; z-index: 3; }

@media (max-width: 992px) {
  .search-container .salwrap::before { content: none; }
}

.search-container input { font-size: 3rem; padding-bottom: 0.3125rem; float: left; margin-top: -0.75rem; }

@media (max-width: 992px) {
  .search-container input { margin-top: auto; font-size: 1rem; }
}

@media (max-width: 992px) {
  .search-container .btn { display: none; }
}

.search-container .square-btn { position: relative; display: none; width: 20px; height: 40px; margin-left: -40px; z-index: 2; cursor: pointer; }

@media (max-width: 992px) {
  .search-container .square-btn { display: inline-block; top: -3px; }
}

.search-container .square-btn svg .stroke { stroke: rgb(33, 33, 33); }

.search-container .square-btn svg .fill { fill: rgb(33, 33, 33); }

.results-wrapper { width: 100%; margin-bottom: 5.9375rem; }

@media (max-width: 992px) {
  .results-wrapper { margin-bottom: 3.125rem; }
}

.result { margin-bottom: 3.4375rem; }

@media (max-width: 992px) {
  .result { margin-bottom: 1.875rem; }
}

.result:last-child { margin-bottom: 0px; }

.result p { line-height: 140%; }

.result h4 { color: rgb(33, 33, 33); font-weight: 700; margin-bottom: 0.625rem; }

.result h4:last-child, .result svg { margin-bottom: 0px; }

.result svg { width: 20px; margin-left: 0.9375rem; }

@media (max-width: 992px) {
  .result svg { margin-left: 0.625rem; }
}

.pagination { width: 100%; display: flex; justify-content: center; }

.pagination .next, .pagination .prev, .pagination .square { position: relative; display: inline-block; width: 50px; height: 50px; line-height: 46px; text-align: center; margin: 0px 0.625rem; }

@media (max-width: 992px) {
  .pagination .next, .pagination .prev, .pagination .square { width: 30px; height: 30px; line-height: 26px; margin: 0px 0.3125rem; }
}

.pagination .square { font-weight: 700; font-size: 1.25rem; }

@media (max-width: 992px) {
  .pagination .square { font-size: 1rem; }
}

.pagination .square:hover { color: rgb(255, 255, 255); }

.pagination .next::after, .pagination .next::before, .pagination .prev::after, .pagination .prev::before { content: ""; position: absolute; top: 50%; left: 50%; width: 15px; height: 1px; }

.pagination .next.disabled::after, .pagination .next.disabled::before, .pagination .prev.disabled::after, .pagination .prev.disabled::before { background-color: rgb(157, 157, 157) !important; }

.pagination .prev::before { transform-origin: left bottom; transform: translate(-50%, -50%) rotate(45deg); }

.pagination .prev::after { transform-origin: left top; transform: translate(-50%, -50%) rotate(-45deg); }

.pagination .next::before { transform-origin: right bottom; transform: translate(-50%, -50%) rotate(45deg); }

.pagination .next::after { transform-origin: right top; transform: translate(-50%, -50%) rotate(-45deg); }

.chatbot-square { position: fixed; top: 50%; right: 0px; width: 200px; height: 200px; transform: translateY(-50%); border-top-left-radius: 15px; border-bottom-left-radius: 15px; background-color: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.15) -5px 3px 10px; cursor: pointer; text-align: center; padding: 1.25rem; display: flex; align-items: center; z-index: 5; }

@media (max-width: 992px) {
  .chatbot-square { display: none; }
}

.chatbot-square svg { display: inline-block; width: auto; height: 80px; margin-bottom: 1.875rem; }

.chatbot-square h5 { font-weight: 700; font-size: 1.375rem; }

.tipos-negocio-adesao-container { margin-bottom: 6.25rem; }

.tipos-negocio-adesao { display: flex; }

@media (max-width: 767px) {
  .tipos-negocio-adesao { flex-wrap: wrap; }
}

.tipos-negocio-adesao .icon { width: 140px; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tipos-negocio-adesao .icon { width: 110px; }
}

@media (max-width: 992px) {
  .tipos-negocio-adesao .icon { width: 100px; }
}

@media (max-width: 767px) {
  .tipos-negocio-adesao .icon { width: 100%; margin-bottom: 1.25rem; }
}

.tipos-negocio-adesao .desc { width: calc(100% - 520px); padding-right: 1.875rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tipos-negocio-adesao .desc { width: calc(100% - 385px); }
}

@media (max-width: 992px) {
  .tipos-negocio-adesao .desc { width: calc(100% - 360px); padding-right: 0.9375rem; }
}

@media (max-width: 767px) {
  .tipos-negocio-adesao .desc { width: 100%; margin-bottom: 1.875rem; }
}

.tipos-negocio-adesao .links { width: 380px; }

@media (max-width: 992px) {
  .tipos-negocio-adesao .links { width: 260px; }
}

@media (max-width: 767px) {
  .tipos-negocio-adesao .links { width: 100%; }
}

.tipos-negocio-adesao .link { margin-bottom: 2.1875rem; }

.tipos-negocio-adesao .link:last-child { margin-bottom: 0px; }

.tipos-negocio-adesao .link a:not(.download-link) { position: relative; display: block; float: left; clear: both; }

.tipos-negocio-adesao .link a:not(.download-link):hover::before { width: 100%; }

.tipos-negocio-adesao .link a:not(.download-link)::before { content: ""; position: absolute; left: 0px; bottom: -1px; width: 0px; height: 1px; transition: width 0.35s ease-in-out 0s; }

.tipos-negocio-adesao .link a:not(.download-link)::after { content: ""; display: inline-block; width: 20px; height: 12px; margin-left: 10px; background-size: contain; background-position: 50% center; background-repeat: no-repeat; }

.tipos-negocio-adesao h6 { text-transform: uppercase; color: rgb(135, 135, 135); font-weight: 700; margin-bottom: 0.3125rem; }

.tipos-negocio-adesao h3 { margin-bottom: 1.25rem; }

.tipos-negocio-adesao svg { width: 115px; height: auto; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .tipos-negocio-adesao svg { width: 85px; }
}

@media (max-width: 992px) {
  .tipos-negocio-adesao svg { width: 80px; }
}

.download-link { position: relative; font-weight: 300; clear: both; padding-right: 50px; }

@media (max-width: 992px) {
  .download-link { padding-right: 2.1875rem; }
}

.download-link::before { content: ""; position: absolute; left: 0px; bottom: 2px; width: 0px; height: 1px; transition: width 0.35s ease-in-out 0s; }

.download-link::after { position: absolute; bottom: 4px; right: 0px; content: ""; display: inline-block; width: 25px; height: 26px; margin-left: 1.875rem; background-size: cover; background-position: 50% center; background-repeat: no-repeat; line-height: 1; }

@media (max-width: 992px) {
  .download-link::after { margin-left: 0.9375rem; width: 18px; height: 18px; }
}

.download-link:hover { padding-right: 7.4375rem; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .download-link:hover { padding-right: 5.625rem; }
}

@media (max-width: 767px) {
  .download-link:hover { padding-right: 6.25rem; }
}

.download-link:hover::before { width: 100%; }

.download-link:hover::after { content: attr(data-after-text); width: 90px; height: 12px; text-transform: uppercase; font-weight: 700; bottom: 10px; margin-left: 0.9375rem; background-image: none !important; }

@media (max-width: 1400px), (max-height: 850px) and (min-width: 1401px) {
  .download-link:hover::after { bottom: 0.1875rem; width: 65px; }
}

@media (max-width: 767px) {
  .download-link:hover::after { bottom: 6px; width: 76px; }
}

.documentos-links, .downloads-links { margin-bottom: 6.25rem; }

.documentos-links a, .downloads-links a { display: block; float: left; clear: both; margin-bottom: 0.1875rem; line-height: 125%; }

.documentos-links a { position: relative; }

.documentos-links a:hover::before { width: 100%; }

.documentos-links a::before { content: ""; position: absolute; left: 0px; bottom: -1px; width: 0px; height: 1px; transition: width 0.35s ease-in-out 0s; }

.downloads-links a { margin-bottom: 2.5rem; }

@media (max-width: 767px) {
  .downloads-links a { padding-right: 1.25rem; }
}

.faqs-group { margin-bottom: 5.625rem; }

@media (max-width: 992px) {
  .faqs-group { margin-bottom: 3.125rem; }
}

.faqs-group:last-child { margin-bottom: 0px; }

.faqs-group h3 { margin-bottom: 1.875rem; }

.faq { margin-bottom: 3.125rem; }

@media (max-width: 992px) {
  .faq { margin-bottom: 1.875rem; }
}

.faq:last-child { margin-bottom: 0px; }

.faq.open .seta { transform: rotateX(180deg); }

.faq .header { position: relative; padding-right: 2.5rem; cursor: pointer; }

.faq .body { height: 0px; overflow: hidden; }

.faq .body .content { padding-top: 1.875rem; }

@media (max-width: 992px) {
  .faq .body .content { padding-top: 0.9375rem; }
}

.faq .seta { position: absolute; bottom: 5px; right: 5px; display: inline-block; margin-left: 1.25rem; width: 20px; height: 12.5px; transition: transform 0.25s ease-in-out 0s, -webkit-transform 0.25s ease-in-out 0s; }

.faq .seta::after, .faq .seta::before { content: ""; position: absolute; top: 50%; left: 50%; width: 2px; height: 15px; }

.faq .seta::before { transform-origin: right bottom; transform: translate(-50%, -50%) rotate(45deg); }

.faq .seta::after { transform-origin: left bottom; transform: translate(-50%, -50%) rotate(-45deg); }

#map { width: calc(100% + 80px); height: 56.25vw; max-height: 600px; margin-left: -2.5rem; border: none; }

.mapa-list-container > ul { width: 100%; display: flex; flex-wrap: wrap; }

.mapa-list-container > ul > li { display: block; float: left; width: 33.333%; }

@media (max-width: 767px) {
  .mapa-list-container > ul > li { width: 100%; margin-bottom: 2.5rem; }
}

.mapa-list-container > ul > li:nth-child(n+4) { width: 100%; }

.mapa-list-container > ul > li:last-child { margin-bottom: 0px; }

.mapa-list-container > ul > li + li { margin-top: 2.5rem; }

@media (max-width: 767px) {
  .mapa-list-container > ul > li + li { margin-top: 1.875rem; }
}

.mapa-list-container > ul > li + li:first-child, .mapa-list-container > ul > li + li:nth-child(2), .mapa-list-container > ul > li + li:nth-child(3) { margin-top: 0px; }

@media (max-width: 767px) {
  .mapa-list-container > ul > li + li:first-child, .mapa-list-container > ul > li + li:nth-child(2), .mapa-list-container > ul > li + li:nth-child(3) { margin-top: 1.875rem; }
}

.mapa-list-container > ul > li > a { width: 100%; color: rgb(157, 157, 157); text-transform: uppercase; font-weight: 700; }

.mapa-list-container > ul > li > a + ul { width: 100%; padding-left: 1.25rem; margin-top: 2.8125rem; }

@media (max-width: 767px) {
  .mapa-list-container > ul > li > a + ul { margin-top: 1.875rem; }
}

.mapa-list-container > ul > li > a + ul > li { display: inline-block; width: 100%; }

.mapa-list-container > ul > li > a + ul > li + li { margin-top: 1.875rem; }

@media (max-width: 767px) {
  .mapa-list-container > ul > li > a + ul > li + li { margin-top: 1.25rem; }
}

.mapa-list-container > ul > li > a + ul > li > a { display: inline-block; position: relative; width: 100%; font-weight: 700; }

.mapa-list-container > ul > li > a + ul > li > a + ul { margin-top: 1.25rem; width: 100%; }

.mapa-list-container > ul > li > a + ul > li > a + ul > li { display: inline-block; width: 100%; }

.mapa-list-container > ul > li > a + ul > li > a + ul > li + li { margin-top: 1.25rem; }

@media (max-width: 767px) {
  .mapa-list-container > ul > li > a + ul > li > a + ul > li + li { margin-top: 0.9375rem; }
}

.mapa-list-container > ul > li > a + ul > li > a + ul > li > a { width: 100%; position: relative; display: inline-block; padding-left: 1.25rem; }

.mapa-list-container > ul > li > a + ul > li > a + ul > li > a::before { content: ""; top: 9px; width: 8px; height: 12px; position: absolute; left: 0px; transform: translateY(-50%); background-size: cover; background-position: 50% center; background-repeat: no-repeat; }

.noticias-list-container { width: 100%; padding-bottom: 7.8125rem; }

@media (max-width: 767px) {
  .noticias-list-container { padding-bottom: 3.75rem; }
}

.noticias-list-container .row { margin: 0px -0.9375rem; }

.noticias-list-container .row + .pagination { margin-top: 3.75rem; }

@media (max-width: 767px) {
  .noticias-list-container .row + .pagination { margin-top: 2.5rem; }
}

.noticias-square { width: 50%; float: left; padding: 0px 0.9375rem; margin-bottom: 4.6875rem; }

@media (max-width: 992px) {
  .noticias-square { margin-bottom: 3.125rem; }
}

@media (max-width: 767px) {
  .noticias-square { width: 100%; }
}

@media (min-width: 768px) {
  .noticias-square:nth-last-child(2) { margin-bottom: 0px; }
}

.noticias-square:last-child { margin-bottom: 0px; }

.noticias-square .inner { position: relative; }

.noticias-square .image { width: 100%; padding-top: 60.6061%; background-color: rgb(213, 154, 18); background-size: cover; background-position: 50% center; background-repeat: no-repeat; margin-bottom: 1.875rem; box-shadow: rgba(0, 0, 0, 0.4) 3px 3px 5px; }

.noticias-square h6 { margin-bottom: 0.3125rem; }

.noticias-square h4 { color: rgb(33, 33, 33); margin-bottom: 0.9375rem; font-weight: 600; }

@media (max-width: 767px) {
  .noticias-square h4 { margin-bottom: 0.625rem; }
}

.noticias-square p { color: rgb(157, 157, 157); line-height: 140%; }

.noticias-square svg { margin-left: 0.625rem; }

.homepage-header .desc svg, .noticias-back svg, .noticias-square svg { width: 20px; }

.noticia-detalhe-container h6, .noticias-square h6 { color: rgb(157, 157, 157); font-weight: 700; }

.noticia-detalhe-container { width: 100%; margin-bottom: 4.375rem; }

.noticia-detalhe-container h3 { font-weight: 700; margin-bottom: 1.25rem; }

.noticia-detalhe-container h6 { margin-bottom: 3.4375rem; }

.noticia-detalhe-container p, .noticia-detalhe-container ul { color: rgb(157, 157, 157); line-height: 140%; margin-bottom: 1.875rem; }

.noticia-detalhe-container p:last-child, .noticia-detalhe-container ul:last-child { margin-bottom: 0px; }

.noticia-detalhe-container li { margin-bottom: 0.625rem; }

.noticia-detalhe-container li:last-child { margin-bottom: 0px; }

.noticia-detalhe-container img { margin-bottom: 1.875rem; width: 100% !important; height: auto !important; float: none !important; }

.noticia-slider { width: 100%; position: relative; background-color: rgba(242, 242, 242, 0.5); }

@media (max-width: 992px) {
  .noticia-slider { width: calc(100% + 80px); margin-left: -2.5rem; }
}

.noticia-slider .slide { float: left; }

.noticia-slider .slide .wrapper { width: 100%; padding-top: 70.8333%; background-size: contain; background-position: 50% center; background-repeat: no-repeat; }

.noticia-slider .seta { position: absolute; width: 55px; height: 110px; top: 50%; transform: translateY(-50%); z-index: 3; cursor: pointer; }

@media (max-width: 992px) {
  .noticia-slider .seta { width: 25px; height: 50px; }
}

.noticia-slider .seta.left { left: 20px; }

.noticia-slider .seta.left::after, .noticia-slider .seta.left::before { left: 0px; }

.noticia-slider .seta.left::before { transform-origin: left bottom; transform: translateY(-50%) rotate(45deg); }

.noticia-slider .seta.left::after { transform-origin: left top; transform: translateY(-50%) rotate(-45deg); }

.noticia-slider .seta.right { right: 20px; }

.noticia-slider .seta.right::after, .noticia-slider .seta.right::before { right: 0px; }

.noticia-slider .seta.right::before { transform-origin: right bottom; transform: translateY(-50%) rotate(45deg); }

.noticia-slider .seta.right::after { transform-origin: right top; transform: translateY(-50%) rotate(-45deg); }

.noticia-slider .seta::after, .noticia-slider .seta::before { content: ""; position: absolute; top: 50%; width: 75px; height: 2px; background-color: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.2) 2px 2px 2px; }

@media (max-width: 992px) {
  .noticia-slider .seta::after, .noticia-slider .seta::before { width: 30px; }
}

.noticias-back { display: inline-block; margin-bottom: 4.0625rem; }

.noticias-back svg { margin-right: 0.625rem; transform: rotate(180deg); }

.page-404-container { width: 100%; min-height: 100vh; display: flex; justify-content: center; align-items: center; background-color: rgb(242, 242, 242); padding: 2.5rem; text-align: center; }

.page-404-container > .content { width: 930px; }

.page-404-container h6 { margin-bottom: 1.5625rem; color: rgb(157, 157, 157); font-weight: 700; text-transform: uppercase; }

.page-404-container h2 { font-weight: 700; color: rgb(33, 33, 33); margin-bottom: 5rem; }

.page-404-container p { color: rgb(157, 157, 157); margin-bottom: 3.75rem; }

.logo-404 { display: block; width: 140px; margin: 0px auto 5.625rem; }

.links-404-container { width: 100%; }

.links-404-container .square { position: relative; width: 33.333%; float: left; }

.links-404-container .square:last-child::after { content: none; }

.links-404-container .square::after { content: ""; position: absolute; top: 0px; right: 0px; width: 1px; height: 125px; background-color: rgb(157, 157, 157); z-index: 3; }

@media (max-width: 992px) {
  .links-404-container .square::after { height: 90px; }
}

.links-404-container .inner { padding: 0.9375rem; }

.links-404-container svg { display: inline-block; width: auto; height: 85px; margin-bottom: 2.1875rem; }

@media (max-width: 992px) {
  .links-404-container svg { height: 55px; }
}

.links-404-container h5 { font-weight: 700; color: rgb(33, 33, 33); }

.menu-button { position: relative; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; }

.menu-button .wrapper { width: 30px; height: 17px; }

.menu-button.open .line:first-child { top: 7px; transform: rotate(45deg); transition: top 0.25s ease-in-out 0s, transform 0.25s ease-in-out 0.25s, -webkit-transform 0.25s ease-in-out 0.25s; }

.menu-button.open .line:nth-child(2) { opacity: 0; transition: opacity 0.25s ease-in-out 0s; }

.menu-button.open .line:nth-child(3) { top: 7px; transform: rotate(-45deg); transition: top 0.25s ease-in-out 0s, transform 0.25s ease-in-out 0.25s, -webkit-transform 0.25s ease-in-out 0.25s; }

.menu-button .line { position: absolute; display: inline-block; left: 0px; width: 30px; height: 2px; }

.menu-button .line:first-child { top: 0px; transition: top 0.25s ease-in-out 0.25s, transform 0.25s ease-in-out 0s, -webkit-transform 0.25s ease-in-out 0s; }

.menu-button .line:nth-child(2) { top: 7px; opacity: 1; transition: opacity 0.25s ease-in-out 0.25s; }

.menu-button .line:nth-child(3) { top: 14px; transition: top 0.25s ease-in-out 0.25s, transform 0.25s ease-in-out 0s, -webkit-transform 0.25s ease-in-out 0s; }

.menu-wrapper { position: fixed; top: 70px; right: 0px; width: 100%; transform: translateX(100%); background-color: rgb(242, 242, 242); height: calc(100vh - 70px); transition: transform 0.25s ease-in-out 0s, -webkit-transform 0.25s ease-in-out 0s; overflow: auto; }

.menu-wrapper.open { transform: translateX(0px); }

.mobile-links-container { overflow: hidden; min-height: calc(100vh - 115px); padding: 1.875rem 1.5625rem 1.875rem 1.25rem; }

.mobile-links-container.login { min-height: calc(100vh - 224px); }

.mobile-links-section { padding: 1.40625rem 0.9375rem; border-bottom: 1px solid rgb(157, 157, 157); }

.mobile-links-section:first-child { padding-top: 0px; }

.mobile-links-section.active .menu-mobile-links { margin-top: 1.5625rem; height: auto; }

.mobile-links-section.active .header h6 { color: rgb(33, 33, 33); }

.mobile-links-section.active .header .seta { transform: translateY(-50%) rotateX(180deg); }

.mobile-links-section .header { position: relative; }

.mobile-links-section .header .seta { right: 0px; }

.mobile-links-section .header .seta::after, .mobile-links-section .header .seta::before { background-color: rgb(218, 92, 9); }

.mobile-links-section h6 { font-weight: 700; text-transform: uppercase; font-size: 0.875rem; color: rgb(157, 157, 157); }

.infowindow-modal { padding: 0.5rem 1.125rem; }

.infowindow-modal .title-line { text-transform: uppercase; font-weight: 600; }

.infowindow-modal .desc-line, .infowindow-modal .title-line { color: rgb(157, 157, 157); font-size: 1rem; margin-bottom: 0.46875rem; }

.infowindow-modal .desc-line:last-child { margin-bottom: 0px; }

.mouse { width: 25px; margin: 2.5rem auto 0px; text-align: center; }

@media (max-height: 850px) and (min-width: 993px) {
  .mouse { bottom: 20px; }
}

@media (max-width: 992px) {
  .mouse { display: none; }
}

.mouse span { width: 100%; font-size: 0.8125rem; margin-bottom: 0.46875rem; color: rgb(255, 255, 255); text-transform: uppercase; letter-spacing: -1px; font-weight: 700; }

.mouse span, .mouse svg { display: inline-block; }

.mouse svg:not(.st) { width: 25px; }

.mouse svg.st { width: 15px; }

.mobile-others { width: 100%; padding: 1.40625rem 0.9375rem; display: flex; justify-content: space-between; align-items: center; }

.mobile-others .contactos-links, .mobile-others .languages-links { width: auto; border-right: none; }

.mobile-others .contactos-links { padding: 0px; }

.mobile-others .contactos-links li a { color: rgb(33, 33, 33); }

.mobile-others .languages-links li:first-child { padding-left: 0px; }

.mobile-others .languages-links li:last-child { padding-right: 0px; }

.checkbox, .radio { display: flex; align-items: center; color: rgb(157, 157, 157); }

@media (max-width: 767px) {
  .checkbox, .radio { margin-bottom: 1.875rem; }
}

.checkbox input[type="checkbox"], .checkbox input[type="radio"], .radio input[type="checkbox"], .radio input[type="radio"] { -webkit-appearance: none; width: 0px; height: 0px; overflow: hidden; opacity: 0; }

.checkbox input[type="checkbox"]:checked + label .square::after, .checkbox input[type="radio"]:checked + label .square::after, .radio input[type="checkbox"]:checked + label .square::after, .radio input[type="radio"]:checked + label .square::after { content: ""; }

.checkbox input[type="checkbox"] + label, .checkbox input[type="radio"] + label, .radio input[type="checkbox"] + label, .radio input[type="radio"] + label { display: flex; align-items: center; cursor: pointer; }

.checkbox input[type="checkbox"] + label .square, .checkbox input[type="radio"] + label .square, .radio input[type="checkbox"] + label .square, .radio input[type="radio"] + label .square { position: relative; display: inline-block; width: 50px; height: 50px; margin-right: 0.9375rem; }

@media (max-width: 992px) {
  .checkbox input[type="checkbox"] + label .square, .checkbox input[type="radio"] + label .square, .radio input[type="checkbox"] + label .square, .radio input[type="radio"] + label .square { width: 35px; height: 35px; }
}

@media (max-width: 767px) {
  .checkbox input[type="checkbox"] + label .square, .checkbox input[type="radio"] + label .square, .radio input[type="checkbox"] + label .square, .radio input[type="radio"] + label .square { width: 20px; height: 20px; }
}

.checkbox input[type="checkbox"] + label .square::after, .checkbox input[type="radio"] + label .square::after, .radio input[type="checkbox"] + label .square::after, .radio input[type="radio"] + label .square::after { position: absolute; top: 50%; left: 50%; width: 25px; height: 12.5px; border-left: 2px solid rgb(33, 33, 33); border-bottom: 2px solid rgb(33, 33, 33); transform: translate(-50%, -70%) rotate(-45deg); }

@media (max-width: 767px) {
  .checkbox input[type="checkbox"] + label .square::after, .checkbox input[type="radio"] + label .square::after, .radio input[type="checkbox"] + label .square::after, .radio input[type="radio"] + label .square::after { width: 12.5px; height: 6.25px; border-left: 1px solid rgb(33, 33, 33); border-bottom: 1px solid rgb(33, 33, 33); }
}

.checkbox input[type="checkbox"] + label span, .checkbox input[type="radio"] + label span, .radio input[type="checkbox"] + label span, .radio input[type="radio"] + label span { font-weight: 700; }

@media (max-width: 767px) {
  .checkbox input[type="checkbox"] + label span, .checkbox input[type="radio"] + label span, .radio input[type="checkbox"] + label span, .radio input[type="radio"] + label span { font-size: 0.875rem; }
}

.form-input-salwrap, .form-select-salwrap { position: relative; margin-bottom: 3.125rem; }

@media (max-width: 767px) {
  .form-input-salwrap, .form-select-salwrap { margin-bottom: 1.875rem; }
}

.form-input-salwrap.error label, .form-select-salwrap.error label { color: red !important; }

.form-input-salwrap.focusfilled label, .form-select-salwrap.focusfilled label { text-transform: uppercase; transform: translateY(-20px); font-size: 0.75rem; color: rgb(158, 158, 158); font-weight: 600; }

.form-input-salwrap label, .form-select-salwrap label { display: inline-block; position: absolute; font-size: 1.125rem; top: 0px; left: 0px; padding: 0.46875rem; pointer-events: none; transform: translate(0px); transition: transform 0.35s ease-in-out 0s, opacity 0.35s ease-in-out 0s, visibility 0.35s ease-in-out 0s, font-weight 0.35s ease-in-out 0s, color 0.35s ease-in-out 0s, font-size 0.35s ease-in-out 0s, -webkit-transform 0.35s ease-in-out 0s; }

@media (max-width: 767px) {
  .form-input-salwrap label, .form-select-salwrap label { font-size: 1rem; }
}

.form-check-radio-container p.error, .form-input-salwrap p.error, .form-select-salwrap p.error { width: 100%; font-size: 0.875rem; padding: 0.46875rem; color: red; font-weight: 400; }

.form-check-radio-container p.error:empty, .form-input-salwrap p.error:empty, .form-select-salwrap p.error:empty { display: none; }

.form-select-salwrap label { opacity: 0; visibility: hidden; z-index: 2; }

.form-select-salwrap.focusfilled label { opacity: 1; visibility: visible; }

.form-select-salwrap.error .selectric { border-bottom: 1px solid red; }

.form-select-salwrap.error .selectric:hover .button::after { color: red !important; }

.form-input-salwrap.error input[type="email"], .form-input-salwrap.error input[type="text"] { border-bottom: 1px solid red !important; }

.form-input-salwrap.error textarea { border: 1px solid red !important; }

.form-input-salwrap input[type="email"], .form-input-salwrap input[type="text"] { padding: 0.46875rem; width: 100%; font-size: 1.125rem; }

@media (max-width: 767px) {
  .form-input-salwrap input[type="email"], .form-input-salwrap input[type="text"] { font-size: 1rem; }
}

.form-input-salwrap textarea { width: 100%; resize: none; border: 1px solid rgb(33, 33, 33); padding: 1.25rem; font-size: 1.125rem; }

@media (max-width: 767px) {
  .form-input-salwrap textarea { font-size: 1rem; }
}

.form-check-radio-container { display: flex; flex-wrap: wrap; margin-bottom: 4.0625rem; }

@media (max-width: 767px) {
  .form-check-radio-container { margin-bottom: 1.875rem; }
}

.form-check-radio-container.error .checkbox input[type="checkbox"] + label .square, .form-check-radio-container.error .checkbox input[type="radio"] + label .square, .form-check-radio-container.error .radio input[type="checkbox"] + label .square, .form-check-radio-container.error .radio input[type="radio"] + label .square { border: 2px solid red !important; }

.form-check-radio-container .checkbox, .form-check-radio-container .radio { width: 50%; margin-bottom: 3.125rem; }

@media (max-width: 992px) {
  .form-check-radio-container .checkbox, .form-check-radio-container .radio { margin-bottom: 1.25rem; }
}

.form-check-radio-container .checkbox:nth-last-child(2), .form-check-radio-container .checkbox:nth-last-child(3):nth-child(2n+1), .form-check-radio-container .radio:nth-last-child(2), .form-check-radio-container .radio:nth-last-child(3):nth-child(2n+1) { margin-bottom: 0px; }

.form-helper { color: rgb(157, 157, 157); }

#apoio-cliente-form.hide, .form-success-message.hide { display: none; }

.form-success-message { text-align: center; }

.form-success-message p { line-height: 140%; margin-bottom: 5rem; }

.mouse.animated .st { animation-name: movingMouse; animation-duration: 4s; animation-direction: alternate; animation-iteration-count: infinite; animation-timing-function: linear; }

@-webkit-keyframes movingMouse { 
  0% { transform: translateY(0px); }
  12.5% { transform: translateY(80%); }
  25% { transform: translateY(0px); }
  37.5% { transform: translateY(80%); }
  50% { transform: translateY(0px); }
  100% { transform: translateY(0px); }
}

@keyframes movingMouse { 
  0% { transform: translateY(0px); }
  12.5% { transform: translateY(80%); }
  25% { transform: translateY(0px); }
  37.5% { transform: translateY(80%); }
  50% { transform: translateY(0px); }
  100% { transform: translateY(0px); }
}
------MultipartBoundary--B35gv9hf8GVvnlqnSn2OQfMwBE5Ga2VECPMKOPmjLS----
Content-Type: application/x-font-woff
Content-Transfer-Encoding: binary
Content-Location: https://www.bci.ao/media/1407/ptsans-italic.woff

wOFF"""


  lista_paises = list()
  lista_compra = list()
  lista_venda = list()
  Tabela_Cambio = list()
  lista_paises_2 = list()
  lista_compra_2 = list()
  lista_venda_2 = list()
  Tabela_Cambio_2 = list()
  Banco_BCI = dict()

  Soup = BeautifulSoup(html_text, 'html.parser')
  #table_1 = Soup.f('div',attrs={'class':'body'})
  table = Soup.select('div.body')

  lista_paises = table[0].select('div.line div:nth-of-type(1)')
  lista_compra = table[0].select('div.line div:nth-of-type(2)')
  lista_venda = table[0].select('div.line div:nth-of-type(3)')

  lista_paises_2 = table[1].select('div.line div:nth-of-type(1)')
  lista_compra_2 = table[1].select('div.line div:nth-of-type(2)')
  lista_venda_2 = table[1].select('div.line div:nth-of-type(3)')

  for c in range(0, len(lista_compra)):
    Banco_BCI['pais'] = Formate_String.formate_string(extrair_tag(lista_paises[c]))
    Banco_BCI['compra'] = Formate_String.formate_string(extrair_tag(lista_compra[c]))
    Banco_BCI['venda'] = Formate_String.formate_string(extrair_tag(lista_venda[c]))

    Tabela_Cambio.append(Banco_BCI.copy())

    Banco_BCI['pais'] = Formate_String.formate_string(extrair_tag(lista_paises_2[c]))
    Banco_BCI['compra'] = Formate_String.formate_string(extrair_tag(lista_compra_2[c]))
    Banco_BCI['venda'] = Formate_String.formate_string(extrair_tag(lista_venda_2[c]))

    Tabela_Cambio_2.append(Banco_BCI.copy())
