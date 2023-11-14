import requests
import Extrair_Tag
from bs4 import BeautifulSoup 


class Infomoney():
  """html_text = requests.get('https://www.infomoney.com.br/ferramentas/cambio/').text"""
  html_text = """
  From: <Saved by Blink>
Snapshot-Content-Location: https://www.infomoney.com.br/ferramentas/cambio/
Subject: =?utf-8?Q?C=C3=A2mbio=20de=20Moedas=20-=20Ferramentas=20|=20InfoMoney?=
Date: Sat, 7 Jan 2023 13:33:31 -0000
MIME-Version: 1.0
Content-Type: multipart/related;
	type="text/html";
	boundary="----MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----"


------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/html
Content-ID: <frame-D3FA16A8B342B7A029BDAC0AD3F58730@mhtml.blink>
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/ferramentas/cambio/

<!DOCTYPE html><html lang="pt-BR" class="jetpack-lazy-images-js-enabled"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link rel="stylesheet" type="text/css" href="cid:css-06067961-65bd-4c1d-beb2-6d7a245b4f70@mhtml.blink" /><link rel="stylesheet" type="text/css" href="cid:css-fb73eae7-6ccc-4e01-8217-fdfcc9621bc0@mhtml.blink" /><link rel="stylesheet" type="text/css" href="cid:css-47acedb3-2edf-474c-9ba3-34a5dfb417a3@mhtml.blink" /><link rel="stylesheet" type="text/css" href="cid:css-cf9b1a48-580d-4b26-be19-cf570fb4c7bf@mhtml.blink" /><link rel="stylesheet" type="text/css" href="cid:css-2c23ed12-3da7-4cae-b91d-b027048fcf86@mhtml.blink" /><link rel="stylesheet" type="text/css" href="cid:css-31e41619-27cd-4853-b513-7a402782e2d5@mhtml.blink" /><link rel="stylesheet" type="text/css" href="cid:css-bc2216da-a751-4c2e-8841-7b1b5ecfbe61@mhtml.blink" /> 
    
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    

    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">

	<!-- This site is optimized with the Yoast SEO Premium plugin v19.3 (Yoast SEO v19.7.2) - https://yoast.com/wordpress/plugins/seo/ -->
	<title>Câmbio de Moedas - Ferramentas | InfoMoney</title>
	<meta name="description" content="Acompanhe as taxas de câmbio das principais moedas; Dólar, Euro, Libra, Peso e mais.Aqui você encontra a cotação de hoje, o histórico e uma ferramenta de conversão para o real.">
	<link rel="canonical" href="https://www.infomoney.com.br/ferramentas/cambio/">
	<meta property="og:locale" content="pt_BR">
	<meta property="og:type" content="article">
	<meta property="og:title" content="Câmbio de Moedas - Ferramentas | InfoMoney">
	<meta property="og:description" content="Acompanhe as taxas de câmbio das principais moedas; Dólar, Euro, Libra, Peso e mais.Aqui você encontra a cotação de hoje, o histórico e uma ferramenta de conversão para o real.">
	<meta property="og:url" content="https://www.infomoney.com.br/ferramentas/cambio/">
	<meta property="og:site_name" content="InfoMoney">
	<meta property="article:publisher" content="https://www.facebook.com/InfoMoney/">
	<meta property="article:modified_time" content="2022-12-05T19:20:36+00:00">
	<meta property="og:image" content="https://www.infomoney.com.br/wp-content/uploads/2021/03/Site-thumb-de-materia.png?quality=70">
	<meta property="og:image:width" content="1280">
	<meta property="og:image:height" content="720">
	<meta property="og:image:type" content="image/png">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@infomoney">
	<link rel="preconnect" href="https://na5.thunderhead.com/"><link rel="preload" href="https://na5.cdn.thunderhead.com/one/rt/js/one-tag.js?siteKey=ONE-4YRKC0KWPA-1291" as="script">
	<!-- / Yoast SEO Premium plugin. -->


<link rel="dns-prefetch" href="https://cdnjs.cloudflare.com/">
<link rel="dns-prefetch" href="https://platform.instagram.com/">
<link rel="dns-prefetch" href="https://www.googletagservices.com/">
<link rel="dns-prefetch" href="https://cdn.datatables.net/">
<link rel="dns-prefetch" href="https://fonts.googleapis.com/">
<link rel="dns-prefetch" href="https://v0.wordpress.com/">
<link rel="alternate" type="application/rss+xml" title="Feed para InfoMoney »" href="https://www.infomoney.com.br/feed/">
<link rel="alternate" type="application/rss+xml" title="Feed de comentários para InfoMoney »" href="https://www.infomoney.com.br/comments/feed/">
<link rel="alternate" type="application/rss+xml" title="InfoMoney » Stories Feed" href="https://www.infomoney.com.br/web-stories/feed/">

	<link rel="stylesheet" id="the-neverending-homepage-css" href="https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/infinite-scroll/infinity.css?ver=20140422" media="all">
<link rel="stylesheet" id="infomoney-tools-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/css/templates/tools.css?ver=6.4" media="all">
<link rel="stylesheet" id="infomoney-datatables-css-css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css?ver=6.1.1" media="all">
<link rel="stylesheet" id="infomoney-select2-css-css" href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.7/css/select2.min.css?ver=6.1.1" media="all">
<link rel="stylesheet" id="infomoney-selectize-css" href="https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.6/css/selectize.bootstrap3.min.css?ver=6.1.1" media="all">
<link rel="stylesheet" id="mediaelement-css" href="https://www.infomoney.com.br/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.17" media="all">
<link rel="stylesheet" id="wp-mediaelement-css" href="https://www.infomoney.com.br/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=6.1.1" media="all">
<link rel="stylesheet" id="elasticpress-related-posts-block-css" href="https://www.infomoney.com.br/wp-content/mu-plugins/search/elasticpress/dist/css/related-posts-block-styles.min.css?ver=3.6.5" media="all">
<link rel="stylesheet" id="classic-theme-styles-css" href="https://www.infomoney.com.br/wp-includes/css/classic-themes.min.css?ver=1" media="all">

<link rel="stylesheet" id="livenews_css_main-css" href="https://www.infomoney.com.br/wp-content/plugins/livenews/front/assets/css/component.css?ver=1.1.0" media="all">
<link rel="stylesheet" id="jetpack-carousel-swiper-css-css" href="https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/carousel/swiper-bundle.css?ver=11.6" media="all">
<link rel="stylesheet" id="jetpack-carousel-css" href="https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/carousel/jetpack-carousel.css?ver=11.6" media="all">
<link rel="stylesheet" id="tiled-gallery-css" href="https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/tiled-gallery/tiled-gallery/tiled-gallery.css?ver=2012-09-21" media="all">
<link rel="preload" as="style" id="infomoney-bootstrap-preload-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/css/vendor/bootstrap.min.css?ver=6.4" media="all">
<link rel="stylesheet" id="infomoney-bootstrap-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/css/vendor/bootstrap.min.css?ver=6.4" media="all">
<link rel="preload" as="style" id="infomoney-style-preload-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/style.css?ver=6.4" media="all">
<link rel="stylesheet" id="infomoney-style-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/style.css?ver=6.4" media="all">
<link crossorigin="anonymous" rel="stylesheet" id="infomoney-fonts-material-icons-preload-css" href="https://fonts.googleapis.com/css2?family=Material+Icons&amp;display=swap&amp;ver=6.1.1" media="all">
<link crossorigin="anonymous" rel="stylesheet" id="infomoney-fonts-material-icons-css" href="https://fonts.googleapis.com/css2?family=Material+Icons&amp;display=swap&amp;ver=6.1.1" media="all">
<link rel="preload" as="script" id="infomoney-script-prescriptload-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/js/default-min.js?ver=6.4" media="all">
<link rel="preload" as="style" id="infomoney-widget-advertising-preload-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/css/templates/widget-advertising.css?ver=6.4" media="all">
<link rel="stylesheet" id="infomoney-widget-advertising-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/css/templates/widget-advertising.css?ver=6.4" media="all">












<link rel="https://api.w.org/" href="https://www.infomoney.com.br/wp-json/"><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.infomoney.com.br/xmlrpc.php?rsd">
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://www.infomoney.com.br/wp-includes/wlwmanifest.xml">
<meta name="generator" content="WordPress 6.1.1">
	
		        <link rel="preconnect" href="https://www.googletagmanager.com/">
        <link rel="preconnect" href="https://www.googletagservices.com/">
        <link rel="preconnect" href="https://connect.facebook.net/">
        <link rel="preconnect" href="https://apis.google.com/">
        <link rel="preconnect" href="https://securepubads.g.doubleclick.net/">
        <link rel="preconnect" href="https://tpc.googlesyndication.com/">
        <link rel="preconnect" href="https://pagead2.googlesyndication.com/">
        <link rel="preconnect" href="https://fonts.googleapis.com/" crossorigin="">
        <link rel="dns-prefetch" href="https://www.googletagmanager.com/">
        <link rel="dns-prefetch" href="https://www.googletagservices.com/">
        <link rel="dns-prefetch" href="https://fonts.googleapis.com/">
        <link rel="dns-prefetch" href="https://storage.googleapis.com/">
    <!-- There is no amphtml version available for this URL. -->			
			
		<link rel="icon" href="https://www.infomoney.com.br/wp-content/uploads/2019/10/IM-Favicon.png?fit=32%2C32&amp;quality=50&amp;strip=all" sizes="32x32">
<link rel="icon" href="https://www.infomoney.com.br/wp-content/uploads/2019/10/IM-Favicon.png?fit=128%2C128&amp;quality=50&amp;strip=all" sizes="192x192">
<link rel="apple-touch-icon" href="https://www.infomoney.com.br/wp-content/uploads/2019/10/IM-Favicon.png?fit=128%2C128&amp;quality=50&amp;strip=all">
<meta name="msapplication-TileImage" content="https://www.infomoney.com.br/wp-content/uploads/2019/10/IM-Favicon.png?fit=128%2C128&amp;quality=50&amp;strip=all">
		
		    <meta property="fb:admins" content="100001564845270,23205028,100001866890569,100001892083647,678214931">
    <meta property="fb:app_id" content="126135914251280">
    
            <!-- Analytics Tag & LGPD Component -->
        
        <!-- Analytics Tag - Optimize Anti-Flicker-->
        
        
        <!-- End Analytics Tag -->
        
    <meta http-equiv="origin-trial" content="Az6AfRvI8mo7yiW5fLfj04W21t0ig6aMsGYpIqMTaX60H+b0DkO1uDr+7BrzMcimWzv/X7SXR8jI+uvbV0IJlwYAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A+USTya+tNvDPaxUgJooz+LaVk5hPoAxpLvSxjogX4Mk8awCTQ9iop6zJ9d5ldgU7WmHqBlnQB41LHHRFxoaBwoAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7FovoGr67TUBYbnY+Z0IKoJbbmRmB8fCyirUGHavNDtD91CiGyHHSA2hDG9r9T3NjUKFi6egL3RbgTwhhcVDwUAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><link rel="preload" href="https://adservice.google.co.ao/adsid/integrator.js?domain=www.infomoney.com.br" as="script"><link rel="preload" href="https://adservice.google.com/adsid/integrator.js?domain=www.infomoney.com.br" as="script"></head>

<body class="blog infinite-scroll">
    <div id="fb-root"></div>

        
    
    <header class="container-header-small">
            <!-- /8003922/OutOfPage -->
    <div id="OutOfPage" data-google-query-id="CMWEwaLJtfwCFUTU3godBEIAkA"><div id="google_ads_iframe_/8003922/OutOfPage_0__container__" style="border: 0pt none; margin: auto; text-align: center;"></div></div>
<div class="site-header">
    

    <div class="header-full" style="">
        <div class="container-fluid">
            <div class="row">
                <div class="col d-flex align-items-center justify-content-between">
                    <div class="d-flex align-items-center">
                        <div class="header-action menu-open">
                            <i class="material-icons">menu</i>
                        </div>
                    </div>
                    <a href="https://www.infomoney.com.br/" class="logo-link">
                                            <img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.png" width="240" height="48" data-lazy-src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.png?is-pending-load=1" loading="lazy" class="logo jetpack-lazy-image" alt="logotipo_infomoney">
                                        </a>
                    <div class="userPanel">
                                                <div class="login-header user-logged" style="display: none;">
                            <i class="material-icons">account_circle</i>
                            <p></p>
                        </div>
                        <ul class="login-options">
                            <li><a href="https://minhaconta.infomoney.com.br/">Minha conta</a></li>
                            <li><a href="https://www.infomoney.com.br/ferramentas/carteira-de-acompanhamento">Minhas carteiras</a></li>
                            <li><a id="logout_user" href="https://auth.infomoney.com.br/api/auth/signout?redirect_to=https://www.infomoney.com.br%2Fwp-json%2Finfomoney%2Fv1%2Flogout-infomoney">Sair</a></li>
                        </ul>
                        <div class="login-header not-logged" style="display: flex;">
                            <a href="https://auth.infomoney.com.br/authentication/signin?response_type=code&amp;client_id=aaeb000318befb9a2fe0f400&amp;redirect_uri=http://ww3.infomoney.com.br/pages/authentication/callback&amp;origin=portal-header&amp;redirect_to=https://www.infomoney.com.br%2Fwp-json%2Finfomoney%2Fv1%2Flogin-infomoney">
                                <i class="material-icons">account_circle</i>
                                <p>Entrar</p>
                            </a>
                        </div>
                    </div>
                    <div class="d-flex align-items-center">
                        <div class="header-action open-search">
                            <i class="material-icons">search</i>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row container-nav-topics">
                <div class="col">
                    <div class="nav-topics d-flex align-items-center justify-content-center">
                        <i class="material-icons ml-n4 mr-2">trending_up</i>
                        <a data-wa="hot-topic;Governo Lula;https://www.infomoney.com.br/tudo-sobre/lula/" href="https://www.infomoney.com.br/tudo-sobre/lula/" class=" " title="Governo Lula">
                                Governo Lula                                </a><span>•</span><a data-wa="hot-topic;PETR4;https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/" href="https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/" class=" " title="PETR4">
                                PETR4                                </a><span>•</span><a data-wa="hot-topic;Infotrade;https://www.infomoney.com.br/tudo-sobre/trader/" href="https://www.infomoney.com.br/tudo-sobre/trader/" class=" " title="Infotrade">
                                Infotrade                                </a><span>•</span><a data-wa="hot-topic;Plataforma Investor Pass;https://lp.infomoney.com.br/investor-pass-ano-novo-vagas-abertas?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=202212_anip_info-ass_venda" href="https://lp.infomoney.com.br/investor-pass-ano-novo-vagas-abertas?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=202212_anip_info-ass_venda&amp;cid=29163866.1669118894" class=" " title="Plataforma Investor Pass">
                                Plataforma Investor Pass                                </a><span>•</span><a data-wa="hot-topic;Masterclass Renda Agro;https://lp.infomoney.com.br/masterclass-renda-agro-inscricao?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=_mrma_axp_lead" href="https://lp.infomoney.com.br/masterclass-renda-agro-inscricao?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=_mrma_axp_lead&amp;cid=29163866.1669118894" class=" " title="Masterclass Renda Agro">
                                Masterclass Renda Agro                                </a> 
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="header">
        <div class="container-fluid">
            <div class="row">
                <div class="col d-flex align-items-center justify-content-between">
                    <div class="d-flex align-items-center">
                        <div class="header-action menu-open">
                            <i class="material-icons">menu</i>
                        </div>
                        <a href="https://www.infomoney.com.br/" class="d-none d-lg-block logo-link">
                            <img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.svg" width="140" height="28" data-lazy-src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.svg?is-pending-load=1" loading="lazy" class="logo jetpack-lazy-image" alt="Infomoney">
                        </a>
                        <div class="nav-topics d-none d-lg-flex align-items-center">
                            <i class="material-icons ml-3 mr-2">trending_up</i>
                            <a href="https://www.infomoney.com.br/tudo-sobre/lula/" class=" " title="Governo Lula">
                                    Governo Lula                                    </a><span>•</span><a href="https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/" class=" " title="PETR4">
                                    PETR4                                    </a><span>•</span><a href="https://www.infomoney.com.br/tudo-sobre/trader/" class=" " title="Infotrade">
                                    Infotrade                                    </a><span>•</span><a href="https://lp.infomoney.com.br/investor-pass-ano-novo-vagas-abertas?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=202212_anip_info-ass_venda&amp;cid=29163866.1669118894" class=" " title="Plataforma Investor Pass">
                                    Plataforma Investor Pass                                    </a><span>•</span><a href="https://lp.infomoney.com.br/masterclass-renda-agro-inscricao?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=_mrma_axp_lead&amp;cid=29163866.1669118894" class=" " title="Masterclass Renda Agro">
                                    Masterclass Renda Agro                                    </a>                        </div>
                    </div>
                    <a href="https://www.infomoney.com.br/" class="d-lg-none ml-3 logo-link"><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.svg" width="140" height="28" loading="eager" class="logo jetpack-lazy-image jetpack-lazy-image--handled" alt="Infomoney" data-lazy-loaded="1"></a>
                    <div class="d-flex align-items-center">
                        <div class="userPanel">
                                                        <div class="login-header user-logged" style="display: none;">
                                <i class="material-icons">account_circle</i>
                                <p></p>
                            </div>
                            <ul class="login-options">
                                <li><a href="https://minhaconta.infomoney.com.br/">Minha conta</a></li>
                                <li><a href="https://www.infomoney.com.br/ferramentas/carteira-de-acompanhamento">Minhas carteiras</a></li>
                                <li>   
                                    <a id="logout_user" href="https://auth.infomoney.com.br/api/auth/signout?redirect_to=https://www.infomoney.com.br%2Fwp-json%2Finfomoney%2Fv1%2Flogout-infomoney">Sair</a>
                                </li>
                            </ul>
                            <div class="login-header not-logged" style="display: flex;">
                                <a href="https://auth.infomoney.com.br/authentication/signin?response_type=code&amp;client_id=aaeb000318befb9a2fe0f400&amp;redirect_uri=http://ww3.infomoney.com.br/pages/authentication/callback&amp;origin=portal-header&amp;redirect_to=https://www.infomoney.com.br%2Fwp-json%2Finfomoney%2Fv1%2Flogin-infomoney">
                                    <i class="material-icons">account_circle</i>
                                    <p>Entrar</p>
                                </a>
                            </div>
                        </div>
                        <div class="header-action open-search">
                            <i class="material-icons">search</i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container-search-header">
        <div class="header-search">
            <img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.png" width="140" height="28" data-lazy-src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.png?is-pending-load=1" loading="lazy" class="jetpack-lazy-image" alt="Infomoney">
            <button>
                <i class="material-icons">close</i>
            </button>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-12 col-lg-8 m-auto">
                    <form id="header-search" action="https://www.infomoney.com.br/busca" method="GET">
                        <input type="text" name="q" placeholder="Busque no InfoMoney">
                        <button type="submit">
                            <i class="material-icons">search</i>
                        </button>
                    </form>
                </div>
                <div class="col-12 col-lg-8 m-auto topics-search">
                                                <div>
                                <i class="material-icons">trending_up</i>
                                <a href="https://www.infomoney.com.br/tudo-sobre/lula/" title="Governo Lula">Governo Lula</a>
                            </div>
                                                        <div>
                                <i class="material-icons">trending_up</i>
                                <a href="https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/" title="PETR4">PETR4</a>
                            </div>
                                                        <div>
                                <i class="material-icons">trending_up</i>
                                <a href="https://www.infomoney.com.br/tudo-sobre/trader/" title="Infotrade">Infotrade</a>
                            </div>
                                                        <div>
                                <i class="material-icons">trending_up</i>
                                <a href="https://lp.infomoney.com.br/investor-pass-ano-novo-vagas-abertas?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=202212_anip_info-ass_venda&amp;cid=29163866.1669118894" title="Plataforma Investor Pass">Plataforma Investor Pass</a>
                            </div>
                                                        <div>
                                <i class="material-icons">trending_up</i>
                                <a href="https://lp.infomoney.com.br/masterclass-renda-agro-inscricao?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=_mrma_axp_lead&amp;cid=29163866.1669118894" title="Masterclass Renda Agro">Masterclass Renda Agro</a>
                            </div>
                                            </div>
            </div>
        </div>
    </div>

</div>    </header>

    <div id="menu-side">
    <div class="menu-header">
        <div id="menu-close">
            <i class="material-icons">close</i>
        </div>
    </div>
    <div class="userPanel">
                <div class="login-header user-logged" style="display: none;">
            <i class="material-icons">account_circle</i>
            <p></p>
        </div>
        <ul class="login-options">
            <li><a href="https://minhaconta.infomoney.com.br/">Minha conta</a></li>
            <li><a href="https://www.infomoney.com.br/ferramentas/carteira-de-acompanhamento">Minhas carteiras</a></li>
            <li><a id="logout_user" href="https://auth.infomoney.com.br/api/auth/signout?redirect_to=https://www.infomoney.com.br%2Fwp-json%2Finfomoney%2Fv1%2Flogout-infomoney">Sair</a></li>
        </ul>
        <div class="login-header not-logged" style="display: flex;">
            <a href="https://auth.infomoney.com.br/authentication/signin?response_type=code&amp;client_id=aaeb000318befb9a2fe0f400&amp;redirect_uri=http://ww3.infomoney.com.br/pages/authentication/callback&amp;origin=portal-header&amp;redirect_to=https://www.infomoney.com.br%2Fwp-json%2Finfomoney%2Fv1%2Flogin-infomoney">
                <i class="material-icons">account_circle</i>
                <p>Entrar</p>
            </a>
        </div>
    </div>
    <div class="topics-menu">
                        <a data-wa="hot-topic;Governo Lula;https://www.infomoney.com.br/tudo-sobre/lula/" href="https://www.infomoney.com.br/tudo-sobre/lula/" title="Governo Lula">
                    <i class="material-icons">trending_up</i>
                    <p>Governo Lula</p>
                </a>
                                <a data-wa="hot-topic;PETR4;https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/" href="https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/" title="PETR4">
                    <i class="material-icons">trending_up</i>
                    <p>PETR4</p>
                </a>
                                <a data-wa="hot-topic;Infotrade;https://www.infomoney.com.br/tudo-sobre/trader/" href="https://www.infomoney.com.br/tudo-sobre/trader/" title="Infotrade">
                    <i class="material-icons">trending_up</i>
                    <p>Infotrade</p>
                </a>
                                <a data-wa="hot-topic;Plataforma Investor Pass;https://lp.infomoney.com.br/investor-pass-ano-novo-vagas-abertas?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=202212_anip_info-ass_venda" href="https://lp.infomoney.com.br/investor-pass-ano-novo-vagas-abertas?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=202212_anip_info-ass_venda&amp;cid=29163866.1669118894" title="Plataforma Investor Pass">
                    <i class="material-icons">trending_up</i>
                    <p>Plataforma Investor Pass</p>
                </a>
                                <a data-wa="hot-topic;Masterclass Renda Agro;https://lp.infomoney.com.br/masterclass-renda-agro-inscricao?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=_mrma_axp_lead" href="https://lp.infomoney.com.br/masterclass-renda-agro-inscricao?utm_source=infomoney&amp;utm_medium=hot-topic&amp;utm_campaign=_mrma_axp_lead&amp;cid=29163866.1669118894" title="Masterclass Renda Agro">
                    <i class="material-icons">trending_up</i>
                    <p>Masterclass Renda Agro</p>
                </a>
                    </div>
    <ul id="menu-menu-principal" class="list-unstyled"><li id="menu-item-104" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-104"><a href="https://www.infomoney.com.br/ultimas-noticias/">Notícias</a>
<ul class="list-unstyled">
	<li id="menu-item-1318874" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1318874"><a href="https://www.infomoney.com.br/ultimas-noticias/">Últimas</a></li>
	<li id="menu-item-1716809" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1716809"><a href="https://www.infomoney.com.br/mercados/">Mercados</a></li>
	<li id="menu-item-1716810" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1716810"><a href="https://www.infomoney.com.br/onde-investir/">Onde Investir</a></li>
	<li id="menu-item-1716811" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1716811"><a href="https://www.infomoney.com.br/minhas-financas/">Minhas Finanças</a></li>
	<li id="menu-item-1716812" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1716812"><a href="https://www.infomoney.com.br/politica/">Política</a></li>
	<li id="menu-item-1645503" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1645503"><a href="https://www.infomoney.com.br/economia/">Economia</a></li>
	<li id="menu-item-1716813" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1716813"><a href="https://www.infomoney.com.br/negocios/">Negócios</a></li>
	<li id="menu-item-1716814" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1716814"><a href="https://www.infomoney.com.br/consumo/">Consumo</a></li>
	<li id="menu-item-1716815" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1716815"><a href="https://www.infomoney.com.br/carreira/">Carreira</a></li>
</ul>
</li>
<li id="menu-item-118" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home current-menu-ancestor current-menu-parent menu-item-has-children menu-item-118"><a href="https://www.infomoney.com.br/">Cotações</a>
<ul class="list-unstyled">
	<li id="menu-item-119" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-119"><a href="https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/">Ibovespa</a></li>
	<li id="menu-item-130" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-130"><a href="https://www.infomoney.com.br/ferramentas/altas-e-baixas/">Altas e Baixas</a></li>
	<li id="menu-item-121" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item menu-item-121"><a href="https://www.infomoney.com.br/ferramentas/cambio/" aria-current="page">Dólar e Moedas</a></li>
	<li id="menu-item-120" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-120"><a href="https://www.infomoney.com.br/cotacoes/cripto/">Criptos</a></li>
	<li id="menu-item-1953271" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1953271"><a href="https://www.infomoney.com.br/cotacoes/b3/bdr/">BDRs</a></li>
	<li id="menu-item-1756433" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1756433"><a href="https://www.infomoney.com.br/cotacoes/b3/etf/">ETFs</a></li>
	<li id="menu-item-1825611" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1825611"><a href="https://www.infomoney.com.br/cotacoes/b3/fii/">FIIs</a></li>
	<li id="menu-item-1953272" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1953272"><a href="https://www.infomoney.com.br/cotacoes/nasdaq/">Nasdaq</a></li>
	<li id="menu-item-1953273" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1953273"><a href="https://www.infomoney.com.br/cotacoes/nyse/">Nyse</a></li>
</ul>
</li>
<li id="menu-item-129" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-has-children menu-item-129"><a href="https://www.infomoney.com.br/">Ferramentas</a>
<ul class="list-unstyled">
	<li id="menu-item-1721007" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1721007"><a href="https://www.infomoney.com.br/ferramentas/simulador-xp/">Simulador de Investimentos</a></li>
	<li id="menu-item-1492849" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1492849"><a href="https://www.infomoney.com.br/ferramentas/comparador-de-fiis/">Comparador de FIIs</a></li>
	<li id="menu-item-4175" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4175"><a href="https://www.infomoney.com.br/ferramentas/comparador-renda-fixa/">Comparador de Renda Fixa</a></li>
	<li id="menu-item-1428103" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1428103"><a href="https://www.infomoney.com.br/ferramentas/comparador-de-fundos/">Comparador de Fundos</a></li>
	<li id="menu-item-1642351" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1642351"><a href="https://www.infomoney.com.br/ferramentas/comparador-de-investimentos/">Comparador de Investimentos</a></li>
	<li id="menu-item-1306407" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1306407"><a href="https://www.infomoney.com.br/ferramentas/carteira-de-acompanhamento/">Carteira de Acompanhamento</a></li>
	<li id="menu-item-127" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-127"><a href="https://www.infomoney.com.br/ferramentas/juros-futuros-di/">Juros Futuros</a></li>
	<li id="menu-item-128" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-128"><a href="https://www.infomoney.com.br/ferramentas/mini-contratos/">Mini Contratos</a></li>
	<li id="menu-item-1428105" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1428105"><a href="https://www.infomoney.com.br/ferramentas/inflacao/">Indicadores de Inflação</a></li>
	<li id="menu-item-123" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-123"><a href="https://www.infomoney.com.br/ferramentas/cotacoes-opcoes-de-acoes/">Opções de Ações</a></li>
	<li id="menu-item-132" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-132"><a href="https://www.infomoney.com.br/cotacoes/empresas-b3/">Empresas B3</a></li>
</ul>
</li>
<li id="menu-item-1756435" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1756435"><a>Aprenda</a>
<ul class="list-unstyled">
	<li id="menu-item-1632316" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1632316"><a href="https://www.infomoney.com.br/guias/">Guias</a></li>
	<li id="menu-item-1952543" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1952543"><a href="https://www.infomoney.com.br/cursos/">Cursos</a></li>
	<li id="menu-item-1632317" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1632317"><a href="https://www.infomoney.com.br/perfil/">Perfis</a></li>
	<li id="menu-item-1756436" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1756436"><a href="https://www.infomoney.com.br/ebooks/">Ebooks</a></li>
	<li id="menu-item-1756437" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1756437"><a href="https://www.infomoney.com.br/planilhas/">Planilhas</a></li>
</ul>
</li>
<li id="menu-item-1334706" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-has-children menu-item-1334706"><a href="https://www.infomoney.com.br/">Canais e Redes</a>
<ul class="list-unstyled">
	<li id="menu-item-1943552" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1943552"><a href="https://www.tiktok.com/@infomoney">TikTok</a></li>
	<li id="menu-item-1324161" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1324161"><a href="https://www.instagram.com/infomoney/">Instagram</a></li>
	<li id="menu-item-1364885" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1364885"><a href="https://www.infomoney.com.br/mercados/telegram-do-infomoney-tera-servico-gratuito-de-cobertura-em-tempo-real-a-partir-de-outubro/">Telegram</a></li>
	<li id="menu-item-1431169" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1431169"><a href="https://twitter.com/infomoney?lang=en">Twitter</a></li>
	<li id="menu-item-1324162" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1324162"><a href="https://www.linkedin.com/company/infomoney/">Linkedin</a></li>
	<li id="menu-item-1632328" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1632328"><a href="https://www.youtube.com/channel/UCxm0tptjIc76-i26EKQ9NpA">YouTube</a></li>
	<li id="menu-item-1409964" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1409964"><a href="https://www.facebook.com/InfoMoney/">Facebook</a></li>
	<li id="menu-item-1632326" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1632326"><a href="https://www.infomoney.com.br/newsletters/">Newsletter</a></li>
	<li id="menu-item-1632327" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1632327"><a href="https://www.infomoney.com.br/podcasts/">Podcasts</a></li>
</ul>
</li>
<li id="menu-item-1321907" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1321907"><a href="https://www.infomoney.com.br/colunistas/">Colunistas</a>
<ul class="list-unstyled">
	<li id="menu-item-1469565" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1469565"><a href="https://www.infomoney.com.br/colunistas/pedro-jobim/">Pedro Jobim</a></li>
	<li id="menu-item-1816097" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1816097"><a href="https://www.infomoney.com.br/colunistas/professor-baroni/">Prof. Baroni</a></li>
	<li id="menu-item-1874729" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1874729"><a href="https://www.infomoney.com.br/colunistas/paulo-gama/">Paulo Gama</a></li>
	<li id="menu-item-1323232" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1323232"><a href="https://www.infomoney.com.br/colunistas/cesar-grafietti/">Cesar Grafietti</a></li>
	<li id="menu-item-1441684" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1441684"><a href="https://www.infomoney.com.br/colunistas/felippe-hermes/">Felippe Hermes</a></li>
	<li id="menu-item-1874731" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1874731"><a href="https://www.infomoney.com.br/autor/roberto-dumas-damas/">Roberto Dumas Damas</a></li>
	<li id="menu-item-1373348" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1373348"><a href="https://www.infomoney.com.br/colunistas/blog-do-cunha/">Gustavo Cunha</a></li>
	<li id="menu-item-1634984" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1634984"><a href="https://www.infomoney.com.br/colunistas/tudo-clear/">Tudo Clear: A Vida dos Traders</a></li>
	<li id="menu-item-1323231" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1323231"><a href="https://www.infomoney.com.br/colunistas/o-mundo-sobre-muitas-rodas/">Raphael Galante</a></li>
	<li id="menu-item-1373345" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1373345"><a href="https://www.infomoney.com.br/colunistas/um-brasil/">Um Brasil</a></li>
	<li id="menu-item-1373343" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1373343"><a href="https://www.infomoney.com.br/colunistas/ifl-instituto-de-formacao-de-lideres/">IFL</a></li>
	<li id="menu-item-1643600" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1643600"><a href="https://www.infomoney.com.br/autor/dener-lippert/">Dener Lippert</a></li>
</ul>
</li>
<li id="menu-item-1334711" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1334711"><a href="https://www.infomoney.com.br/patrocinados/">Money Lab</a>
<ul class="list-unstyled">
	<li id="menu-item-1964659" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1964659"><a href="https://www.infomoney.com.br/tudo-sobre/inovacao/">Inovação</a></li>
	<li id="menu-item-1334712" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1334712"><a href="https://www.infomoney.com.br/patrocinados/blackrock/">Investindo no Exterior</a></li>
	<li id="menu-item-1334714" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1334714"><a href="https://www.infomoney.com.br/patrocinados/gestao-investimentos-alternativos/">Gestão de Investimentos alternativos</a></li>
	<li id="menu-item-1334716" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1334716"><a href="https://www.infomoney.com.br/patrocinados/ecommerce-b2b/">E-Commerce B2B</a></li>
</ul>
</li>
<li id="menu-item-1531207" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1531207"><a href="https://www.infomoney.com.br/quem-somos/">Quem Somos</a></li>
<li id="menu-item-1617161" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1617161"><a href="https://infomoney.onelink.me/Mmb2/705d28a2">App IM+</a></li>
</ul></div>
        <div class="after-header">
            <div class="ticker-container">
            <div class="ticker-carroussel">
                <div id="ticker-content">
                <a href="https://www.infomoney.com.br/ibovespa" class="positivo"><div class="title">Ibovespa</div><div class="points"><div class="value">108.964 pts</div><div class="spread">+1,23%</div></div></a><a href="https://www.infomoney.com.br/dolar" class="negativo"><div class="title">DÓLAR</div><div class="points"><div class="value">R$ 5,23</div><div class="spread">-2,19%</div></div></a><a href="https://www.infomoney.com.br/bitcoin" class="negativo"><div class="title">BITCOIN</div><div class="points"><div class="value">R$ 88.609</div><div class="spread">-1,73%</div></div></a><a href="https://www.infomoney.com.br/ifix" class="negativo"><div class="title">IFIX</div><div class="points"><div class="value">2.851 pts</div><div class="spread">-0,17%</div></div></a><a href="https://www.infomoney.com.br/mglu3" class="positivo"><div class="title">MGLU3</div><div class="points"><div class="value">R$ 2,76</div><div class="spread">+3,75%</div></div></a><a href="https://www.infomoney.com.br/petr4" class="negativo"><div class="title">PETR4</div><div class="points"><div class="value">R$ 23,74</div><div class="spread">-0,58%</div></div></a><a href="https://www.infomoney.com.br/vale3" class="positivo"><div class="title">VALE3</div><div class="points"><div class="value">R$ 92,34</div><div class="spread">+1,58%</div></div></a><a href="https://www.infomoney.com.br/itub4" class="positivo"><div class="title">ITUB4</div><div class="points"><div class="value">R$ 25,23</div><div class="spread">+1,73%</div></div></a><a href="https://www.infomoney.com.br/abev3" class="positivo"><div class="title">ABEV3</div><div class="points"><div class="value">R$ 14,32</div><div class="spread">+0,20%</div></div></a><a href="https://www.infomoney.com.br/ggbr4" class="positivo"><div class="title">GGBR4</div><div class="points"><div class="value">R$ 30,33</div><div class="spread">+0,76%</div></div></a><div class="aditional">
                <a href="https://www.infomoney.com.br/ibovespa" class="positivo"><div class="title">Ibovespa</div><div class="points"><div class="value">108.964 pts</div><div class="spread">+1,23%</div></div></a><a href="https://www.infomoney.com.br/dolar" class="negativo"><div class="title">DÓLAR</div><div class="points"><div class="value">R$ 5,23</div><div class="spread">-2,19%</div></div></a><a href="https://www.infomoney.com.br/bitcoin" class="negativo"><div class="title">BITCOIN</div><div class="points"><div class="value">R$ 88.609</div><div class="spread">-1,73%</div></div></a><a href="https://www.infomoney.com.br/ifix" class="negativo"><div class="title">IFIX</div><div class="points"><div class="value">2.851 pts</div><div class="spread">-0,17%</div></div></a><a href="https://www.infomoney.com.br/mglu3" class="positivo"><div class="title">MGLU3</div><div class="points"><div class="value">R$ 2,76</div><div class="spread">+3,75%</div></div></a><a href="https://www.infomoney.com.br/petr4" class="negativo"><div class="title">PETR4</div><div class="points"><div class="value">R$ 23,74</div><div class="spread">-0,58%</div></div></a><a href="https://www.infomoney.com.br/vale3" class="positivo"><div class="title">VALE3</div><div class="points"><div class="value">R$ 92,34</div><div class="spread">+1,58%</div></div></a><a href="https://www.infomoney.com.br/itub4" class="positivo"><div class="title">ITUB4</div><div class="points"><div class="value">R$ 25,23</div><div class="spread">+1,73%</div></div></a><a href="https://www.infomoney.com.br/abev3" class="positivo"><div class="title">ABEV3</div><div class="points"><div class="value">R$ 14,32</div><div class="spread">+0,20%</div></div></a><a href="https://www.infomoney.com.br/ggbr4" class="positivo"><div class="title">GGBR4</div><div class="points"><div class="value">R$ 30,33</div><div class="spread">+0,76%</div></div></a></div></div>
            </div>
            <div class="ticker-open-account">
                <!-- /8003922/Ticker -->
                <div id="Ticker" style="margin:0 auto" data-google-query-id="COj2uqLJtfwCFcwO0wodpqwDGg"><div id="google_ads_iframe_/8003922/Ticker_0__container__" style="border: 0pt none; margin: auto; text-align: center;"><iframe id="google_ads_iframe_/8003922/Ticker_0" name="google_ads_iframe_/8003922/Ticker_0" title="3rd party ad content" width="140" height="40" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" role="region" aria-label="Advertisement" tabindex="0" style="border: 0px; vertical-align: bottom;" data-load-complete="true" data-google-container-id="1"></iframe></div></div>
            </div>
        </div>
                    <div class="row mt-5 fill-lightwhite">
                <div class="container p-0">
                    <div class="col-12 col-lg-12 SUPER container-ads">
                        <div id="MobileLeaderboard" class="MobileLeaderboard" data-google-query-id="CN_1z6LJtfwCFQU90wod65QO0g" style="height: auto !important; max-height: none !important; padding-left: 0px !important; margin-left: 0px !important;">
                            
                        <div id="google_ads_iframe_/8003922/MobileLeaderboard_0__container__" style="border: 0pt none; margin: auto; text-align: center; max-height: none !important; max-width: 360px !important; padding: 0px !important; width: 360px !important; height: auto !important;"><iframe id="google_ads_iframe_/8003922/MobileLeaderboard_0" name="google_ads_iframe_/8003922/MobileLeaderboard_0" title="3rd party ad content" width="360" height="120" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" role="region" aria-label="Advertisement" tabindex="0" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" style="border: 0px; vertical-align: bottom;" data-load-complete="true" data-google-container-id="2"></iframe></div></div>
                    </div>
                </div>
            </div>    </div>
    <div class="container mt-4 mt-lg-5 tool-cambio">
            <div class="row">
                <div class="col-12 col-lg-8">
            
                    <div class="col post-header border-b px-0">
                        <div class="row">
                            <div class="col-12">
                                <h1 class="page-title-1">Câmbio</h1>
                                <p class="article-lead">As cotações do real em relação às principais moedas do mundo, o histórico de cotações do dólar e uma ferramenta de conversão de moedas. Quer investir em minicontratos de dólar com taxa ZERO? <a href="https://cadastro.xpi.com.br/?utm_source=infomoney&amp;utm_medium=cambio&amp;utm_campaign=link&amp;cid=29163866.1669118894" target="_blank">Abra uma conta gratuita na XP.</a> </p>
                                <div class="d-lg-flex m-0 pb-4 justify-content-end">
                                    <div class="post-share d-flex d-lg-initial align-items-center justify-content-end mt-3 mt-lg-0">
                                        		<i class="material-icons share-icon">reply</i>
				<a class="post-share-facebook" href="https://facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.infomoney.com.br%2Fferramentas%2Fcambio%2F%3Futm_source%3Dfacebook%26utm_medium%3Dsocial" target="_blank"><i class="fab fa-facebook"></i></a>
		<a class="post-share-twitter" href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.infomoney.com.br%2Fferramentas%2Fcambio%2F%3Futm_source%3Dtwitter%26utm_medium%3Dsocial&amp;text=Acompanhe%20as%20taxas%20de%20c%C3%A2mbio%20das%20principais%20moedas%3B%20D%C3%B3lar%2C%20Euro%2C%20Libra%2C%20Peso%20e%20mais.Aqui%20voc%C3%AA%20encontra%20a%20cota%C3%A7%C3%A3o%20de%20hoje%2C%20o%20hist%C3%B3rico%20e%20uma%20ferramenta%20de%20convers%C3%A3o%20para%20o%20real.&amp;via=InfoMoney" target="_blank"><i class="fab fa-twitter"></i></a>
		
		<a class="post-share-telegram" href="https://telegram.me/share/url?url=https%3A%2F%2Fwww.infomoney.com.br%2Fferramentas%2Fcambio%2F%3Futm_source%3Dtelegram%26utm_medium%3Dsocial&amp;text=Acompanhe%20as%20taxas%20de%20c%C3%A2mbio%20das%20principais%20moedas%3B%20D%C3%B3lar%2C%20Euro%2C%20Libra%2C%20Peso%20e%20mais.Aqui%20voc%C3%AA%20encontra%20a%20cota%C3%A7%C3%A3o%20de%20hoje%2C%20o%20hist%C3%B3rico%20e%20uma%20ferramenta%20de%20convers%C3%A3o%20para%20o%20real.&amp;via=InfoMoney" target="_blank"><i class="fab fa-telegram-plane"></i></a>
		
					<a class="post-share-whatsapp" href="whatsapp://send?text=Acompanhe%20as%20taxas%20de%20c%C3%A2mbio%20das%20principais%20moedas%3B%20D%C3%B3lar%2C%20Euro%2C%20Libra%2C%20Peso%20e%20mais.Aqui%20voc%C3%AA%20encontra%20a%20cota%C3%A7%C3%A3o%20de%20hoje%2C%20o%20hist%C3%B3rico%20e%20uma%20ferramenta%20de%20convers%C3%A3o%20para%20o%20real. https%3A%2F%2Fwww.infomoney.com.br%2Fferramentas%2Fcambio%2F%3Futm_source%3Dwhatsapp%26utm_medium%3Dsocial via InfoMoney" data-action="share/whatsapp/share" target="_blank"><i class="fab fa-whatsapp"></i></a>
					<a class="post-share-linkedin" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fwww.infomoney.com.br%2Fferramentas%2Fcambio%2F%3Futm_source%3Dlinkedin%26utm_medium%3Dsocial&amp;title=Acompanhe%20as%20taxas%20de%20c%C3%A2mbio%20das%20principais%20moedas%3B%20D%C3%B3lar%2C%20Euro%2C%20Libra%2C%20Peso%20e%20mais.Aqui%20voc%C3%AA%20encontra%20a%20cota%C3%A7%C3%A3o%20de%20hoje%2C%20o%20hist%C3%B3rico%20e%20uma%20ferramenta%20de%20convers%C3%A3o%20para%20o%20real.&amp;source=InfoMoney" target="_blank"><i class="fab fa-linkedin"></i></a>
		<a class="post-share-mail" href="mailto:?subject=Acompanhe%20as%20taxas%20de%20c%C3%A2mbio%20das%20principais%20moedas%3B%20D%C3%B3lar%2C%20Euro%2C%20Libra%2C%20Peso%20e%20mais.Aqui%20voc%C3%AA%20encontra%20a%20cota%C3%A7%C3%A3o%20de%20hoje%2C%20o%20hist%C3%B3rico%20e%20uma%20ferramenta%20de%20convers%C3%A3o%20para%20o%20real.&amp;body=Veja%20mais%20em%20https%3A%2F%2Fwww.infomoney.com.br%2Fferramentas%2Fcambio%2F%3Futm_source%3Demail%26utm_medium%3Dshare-content" target="_blank"><i class="fas fa-envelope"></i></a>
		
		                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="row mt-5">
                        <div class="col-12">
                            <h2>Real VS Moedas</h2>
                            <div id="container_table">
                                <table class="default-table">
                                    <thead>
                                        <tr>
                                            <th>Moeda</th>
                                            <th></th>
                                            <th>Compra</th>
                                            <th>Venda</th>
                                            <th>Var(%)</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                                                                    <tr>
                                                <td>Peso Argentino</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/ar.webp" alt="Peso Argentino"></td>
                                                <td>0,0287</td>
                                                <td>0,0292</td>
                                                <td class="negative">-2,34</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Dólar Australiano</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/au.webp" alt="Dólar Australiano"></td>
                                                <td>3,596</td>
                                                <td>3,601</td>
                                                <td class="negative">-0,5028</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Dólar Canadense</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/ca.webp" alt="Dólar Canadense"></td>
                                                <td>3,894</td>
                                                <td>3,897</td>
                                                <td class="negative">-1,2</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Franco Suíço</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/su.webp" alt="Franco Suíço"></td>
                                                <td>0,4217</td>
                                                <td>0,4218</td>
                                                <td class="negative">-87</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Dólar Comercial</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/us.webp" alt="Dólar Comercial"></td>
                                                <td>5,232</td>
                                                <td>5,234</td>
                                                <td class="negative">-2,18</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Dólar Turismo</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/us.webp" alt="Dólar Turismo"></td>
                                                <td>5,34</td>
                                                <td>5,442</td>
                                                <td class="negative">-2,45</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Euro</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/eu.webp" alt="Euro"></td>
                                                <td>5,574</td>
                                                <td>5,576</td>
                                                <td class="negative">-1,25</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Libra Esterlina</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/gb.webp" alt="Libra Esterlina"></td>
                                                <td>6,333</td>
                                                <td>6,333</td>
                                                <td class="negative">-0,8455</td>
                                            </tr>
                                                                                        <tr>
                                                <td>Iene</td>
                                                <td><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/jp.webp" alt="Iene"></td>
                                                <td>0,0478</td>
                                                <td>0,0478</td>
                                                <td class="positive">0,8439</td>
                                            </tr>
                                                                                </tbody>
                                </table>
                            
                            </div>
                        </div>
                    </div>
                    
                    <div class="row my-5">
                        <div class="col-12">
                            <div class="currencyConvert">
                                <div class="row mb-3">
                                    <div class="col-12 d-flex justify-content-between">
                                        <h2>Conversor de moedas</h2>
                                        <button class="button expanded currencyConvert__swap" id="swap">
                                            <i class="material-icons">swap_vert</i>
                                        </button>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-6">
                                        <input type="number" class="form-control" id="currencyValueA" step="1" min="0" value="100">
                                    </div>
                                    <div class="col-6 pl-0 pl-lg-3">
                                        <select id="currencyA" tabindex="-1" class="selectized" style="display: none;"><option value="0" selected="selected">Dólar</option></select><div class="selectize-control single"><div class="selectize-input items full has-options has-items"><div class="currencyConvert" data-value="0"><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/us.png"><span>Dólar (U$)</span></div><input type="select-one" autocomplete="off" tabindex="" id="currencyA-selectized" style="width: 4px;"></div><div class="selectize-dropdown single" style="display: none;"><div class="selectize-dropdown-content"></div></div></div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-6">
                                        <input type="number" class="form-control" id="currencyValueB" step="1" min="0">
                                    </div>
                                    <div class="col-6 pl-0 pl-lg-3">
                                        <select id="currencyB" tabindex="-1" class="selectized" style="display: none;"><option value="1" selected="selected">Real</option></select><div class="selectize-control single"><div class="selectize-input items full has-options has-items"><div class="currencyConvert" data-value="1"><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/br.png"><span>Real (R$)</span></div><input type="select-one" autocomplete="off" tabindex="" id="currencyB-selectized" style="width: 4px;"></div><div class="selectize-dropdown single" style="display: none;"><div class="selectize-dropdown-content"></div></div></div>
                                    </div>
                                </div>
                                <div class="row mt-3">
                                    <div class="col-12">
                                        <div class="currencyConvert__result hide"><b id="currencyPreConvert">U$ 100,00</b> → <b id="currencyConvert" class="currencyConvert__result-highlight">R$ 523,20</b></div>
                                        <div style="font-size:12px;" class="cm-pad-50-h">Conversão de <b id="displayCurrencyA">Dólar</b> para <b id="displayCurrencyB">Real</b> à taxa de câmbio <b id="displayCurrencyAValue">R$ 5,23</b> de <span id="dateTax">06/01/2023</span></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="row mt-5">
                        <div class="col-12">
                            <h2>Notícias de Câmbio</h2>
                            <div>
                                <div class="row py-3 item" id="post-2016796">
            <div class="col-12 col-lg-4 img-container">
            <a href="https://www.infomoney.com.br/minhas-financas/o-impacto-do-novo-marco-cambial-sobre-a-remessa-de-dinheiro-cambio-turismo-conta-em-dolares-e-mais/" title="O impacto do Novo Marco Cambial sobre a remessa de dinheiro, câmbio turismo, conta em dólares e mais">
                <figure>
                <img width="360" height="202" src="https://www.infomoney.com.br/wp-content/uploads/2022/12/Banner-Publi-Editorial-Infomoney2.png?resize=360%2C202&amp;quality=50&amp;strip=all" class="img-fluid wp-post-image" alt="Marco cambial" decoding="async" title="O impacto do Novo Marco Cambial sobre a remessa de dinheiro, câmbio turismo, conta em dólares e mais" data-attachment-id="2018334" data-permalink="https://www.infomoney.com.br/minhas-financas/o-impacto-do-novo-marco-cambial-sobre-a-remessa-de-dinheiro-cambio-turismo-conta-em-dolares-e-mais/attachment/banner-publi-editorial-infomoney2/" data-orig-file="https://www.infomoney.com.br/wp-content/uploads/2022/12/Banner-Publi-Editorial-Infomoney2.png?fit=701%2C430&amp;quality=50&amp;strip=all" data-orig-size="701,430" data-comments-opened="0" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Banner – Publi Editorial Infomoney2" data-image-description="" data-image-caption="" data-medium-file="https://www.infomoney.com.br/wp-content/uploads/2022/12/Banner-Publi-Editorial-Infomoney2.png?fit=300%2C184&amp;quality=50&amp;strip=all" data-large-file="https://www.infomoney.com.br/wp-content/uploads/2022/12/Banner-Publi-Editorial-Infomoney2.png?fit=701%2C430&amp;quality=50&amp;strip=all">                </figure>
            </a>
        </div>
            <div class="col-12 col-lg-8 pt-3 pt-lg-0 d-flex justify-content-center flex-column">
        <span class="hl-hat">Conteúdo Patrocinado</span>
        <span class="hl-title hl-title-2"><a href="https://www.infomoney.com.br/minhas-financas/o-impacto-do-novo-marco-cambial-sobre-a-remessa-de-dinheiro-cambio-turismo-conta-em-dolares-e-mais/" title="O impacto do Novo Marco Cambial sobre a remessa de dinheiro, câmbio turismo, conta em dólares e mais">O impacto do Novo Marco Cambial sobre a remessa de dinheiro, câmbio turismo, conta em dólares e mais</a></span>
        <span class="hl-date"><span class="posted-diff">3 dias atrás</span></span>
    </div>
</div><div class="row py-3 item" id="post-2020308">
            <div class="col-12 col-lg-4 img-container">
            <a href="https://www.infomoney.com.br/economia/boletim-focus-mercado-ve-inflacao-maior-em-2023-2024-e-2025-e-selic-mais-alta-neste-ano/" title="Boletim Focus: mercado vê inflação maior em 2023, 2024 e 2025 e Selic mais alta neste ano">
                <figure>
                <img width="360" height="202" src="https://www.infomoney.com.br/wp-content/uploads/2023/01/boletim-focus-02012023.jpg?resize=360%2C202&amp;quality=50&amp;strip=all" class="img-fluid wp-post-image" alt="Boletim Focus - 02/01/2023" decoding="async" title="Boletim Focus: mercado vê inflação maior em 2023, 2024 e 2025 e Selic mais alta neste ano" data-attachment-id="2020484" data-permalink="https://www.infomoney.com.br/economia/boletim-focus-mercado-ve-inflacao-maior-em-2023-2024-e-2025-e-selic-mais-alta-neste-ano/attachment/boletim-focus-02012023/" data-orig-file="https://www.infomoney.com.br/wp-content/uploads/2023/01/boletim-focus-02012023.jpg?fit=1920%2C1080&amp;quality=50&amp;strip=all" data-orig-size="1920,1080" data-comments-opened="0" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="boletim-focus-02012023" data-image-description="" data-image-caption="" data-medium-file="https://www.infomoney.com.br/wp-content/uploads/2023/01/boletim-focus-02012023.jpg?fit=300%2C169&amp;quality=50&amp;strip=all" data-large-file="https://www.infomoney.com.br/wp-content/uploads/2023/01/boletim-focus-02012023.jpg?fit=1280%2C720&amp;quality=50&amp;strip=all">                </figure>
            </a>
        </div>
            <div class="col-12 col-lg-8 pt-3 pt-lg-0 d-flex justify-content-center flex-column">
        <span class="hl-hat">Relatório do BC</span>
        <span class="hl-title hl-title-2"><a href="https://www.infomoney.com.br/economia/boletim-focus-mercado-ve-inflacao-maior-em-2023-2024-e-2025-e-selic-mais-alta-neste-ano/" title="Boletim Focus: mercado vê inflação maior em 2023, 2024 e 2025 e Selic mais alta neste ano">Boletim Focus: mercado vê inflação maior em 2023, 2024 e 2025 e Selic mais alta neste ano</a></span>
        <span class="hl-date"><span class="posted-diff">5 dias atrás</span></span>
    </div>
</div><div class="row py-3 item" id="post-2017840">
            <div class="col-12 col-lg-4 img-container">
            <a href="https://www.infomoney.com.br/economia/fluxo-cambial-total-no-ano-ate-23-de-dezembro-e-positivo-em-us-13789-bilhoes/" title="Fluxo cambial total no ano até 23 de dezembro é positivo em US$ 13,789 bilhões">
                <figure>
                <img width="360" height="202" src="https://www.infomoney.com.br/wp-content/uploads/2020/10/GettyImages-502911292-1.jpg?resize=360%2C202&amp;quality=50&amp;strip=all" class="img-fluid wp-post-image" alt="" decoding="async" title="Fluxo cambial total no ano até 23 de dezembro é positivo em US$ 13,789 bilhões" data-attachment-id="1540107" data-permalink="https://www.infomoney.com.br/economia/bilionarios-dos-eua-ficam-us-1-trilhao-mais-ricos-em-era-trump/attachment/gettyimages-502911292-1/" data-orig-file="https://www.infomoney.com.br/wp-content/uploads/2020/10/GettyImages-502911292-1.jpg?fit=2121%2C1414&amp;quality=50&amp;strip=all" data-orig-size="2121,1414" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Dólar dinheiro" data-image-description="<p>(Getty Images)</p>
" data-image-caption="<p>Notas de dólares (Getty Images)</p>
" data-medium-file="https://www.infomoney.com.br/wp-content/uploads/2020/10/GettyImages-502911292-1.jpg?fit=300%2C200&amp;quality=50&amp;strip=all" data-large-file="https://www.infomoney.com.br/wp-content/uploads/2020/10/GettyImages-502911292-1.jpg?fit=1280%2C853&amp;quality=50&amp;strip=all">                </figure>
            </a>
        </div>
            <div class="col-12 col-lg-8 pt-3 pt-lg-0 d-flex justify-content-center flex-column">
        <span class="hl-hat">Dólares</span>
        <span class="hl-title hl-title-2"><a href="https://www.infomoney.com.br/economia/fluxo-cambial-total-no-ano-ate-23-de-dezembro-e-positivo-em-us-13789-bilhoes/" title="Fluxo cambial total no ano até 23 de dezembro é positivo em US$ 13,789 bilhões">Fluxo cambial total no ano até 23 de dezembro é positivo em US$ 13,789 bilhões</a></span>
        <span class="hl-date"><span class="posted-diff">1 semana atrás</span></span>
    </div>
</div><div class="row py-3 item" id="post-2016448">
            <div class="col-12 col-lg-4 img-container">
            <a href="https://www.infomoney.com.br/mercados/real-sobe-em-2022-ante-o-dolar-e-fica-entre-as-melhores-moedas-emergentes-movimento-seguira-em-2023/" title="Real sobe em 2022 ante o dólar e fica entre as melhores moedas emergentes: movimento seguirá em 2023?">
                <figure>
                <img width="360" height="202" src="https://www.infomoney.com.br/wp-content/uploads/2022/07/GettyImages-1032338722.jpg?resize=360%2C202&amp;quality=50&amp;strip=all" class="img-fluid wp-post-image" alt="" decoding="async" title="Real sobe em 2022 ante o dólar e fica entre as melhores moedas emergentes: movimento seguirá em 2023?" data-attachment-id="1895673" data-permalink="https://www.infomoney.com.br/mercados/real-volta-a-sofrer-impacto-de-precos-de-commodities-e-pode-mudar-dinamica-de-margens-de-exportadoras/attachment/agricultural-concept-soybean-at-100-us-dollar-and-100-brazilian-real-banknote/" data-orig-file="https://www.infomoney.com.br/wp-content/uploads/2022/07/GettyImages-1032338722.jpg?fit=724%2C483&amp;quality=50&amp;strip=all" data-orig-size="724,483" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;29&quot;,&quot;credit&quot;:&quot;Getty Images\/iStockphoto&quot;,&quot;camera&quot;:&quot;Canon EOS Rebel T6i&quot;,&quot;caption&quot;:&quot;Agricultural concept, soybean at 100 US dollar and 100 Brazilian Real banknote&quot;,&quot;created_timestamp&quot;:&quot;1531668767&quot;,&quot;copyright&quot;:&quot;ALF Ribeiro&quot;,&quot;focal_length&quot;:&quot;105&quot;,&quot;iso&quot;:&quot;100&quot;,&quot;shutter_speed&quot;:&quot;1&quot;,&quot;title&quot;:&quot;Agricultural concept, soybean at 100 US dollar and 100 Brazilian Real banknote&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="notas de dólar e real soja" data-image-description="" data-image-caption="<p>Foto: Getty Images</p>
" data-medium-file="https://www.infomoney.com.br/wp-content/uploads/2022/07/GettyImages-1032338722.jpg?fit=300%2C200&amp;quality=50&amp;strip=all" data-large-file="https://www.infomoney.com.br/wp-content/uploads/2022/07/GettyImages-1032338722.jpg?fit=724%2C483&amp;quality=50&amp;strip=all">                </figure>
            </a>
        </div>
            <div class="col-12 col-lg-8 pt-3 pt-lg-0 d-flex justify-content-center flex-column">
        <span class="hl-hat">Câmbio</span>
        <span class="hl-title hl-title-2"><a href="https://www.infomoney.com.br/mercados/real-sobe-em-2022-ante-o-dolar-e-fica-entre-as-melhores-moedas-emergentes-movimento-seguira-em-2023/" title="Real sobe em 2022 ante o dólar e fica entre as melhores moedas emergentes: movimento seguirá em 2023?">Real sobe em 2022 ante o dólar e fica entre as melhores moedas emergentes: movimento seguirá em 2023?</a></span>
        <span class="hl-date"><span class="posted-diff">2 semanas atrás</span></span>
    </div>
</div><div class="row py-3 item" id="post-2006263">
            <div class="col-12 col-lg-4 img-container">
            <a href="https://www.infomoney.com.br/minhas-financas/marco-cambial-cria-caminho-para-consumidor-acessar-contas-em-dolar-no-brasil-veja-o-que-pode-mudar/" title="Marco cambial cria caminho para consumidor acessar contas em dólar no Brasil; veja o que pode mudar">
                <figure>
                <img width="360" height="202" src="https://www.infomoney.com.br/wp-content/uploads/2019/11/shutterstock_1144992485-1.jpg?resize=360%2C202&amp;quality=50&amp;strip=all" class="img-fluid wp-post-image" alt="Envelope com notas de dólar sobre uma mesa de madeira" decoding="async" title="Marco cambial cria caminho para consumidor acessar contas em dólar no Brasil; veja o que pode mudar" data-attachment-id="1355234" data-permalink="https://www.infomoney.com.br/carreira/retomada-da-economia-nao-reflete-em-aumentos-salariais-aponta-pesquisa-da-mercer/attachment/shutterstock_1144992485-1/" data-orig-file="https://www.infomoney.com.br/wp-content/uploads/2019/11/shutterstock_1144992485-1.jpg?fit=1000%2C667&amp;quality=50&amp;strip=all" data-orig-size="1000,667" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Notas de dólar" data-image-description="<p>Notas de dólar</p>
" data-image-caption="<p>(Shutterstock)</p>
" data-medium-file="https://www.infomoney.com.br/wp-content/uploads/2019/11/shutterstock_1144992485-1.jpg?fit=300%2C200&amp;quality=50&amp;strip=all" data-large-file="https://www.infomoney.com.br/wp-content/uploads/2019/11/shutterstock_1144992485-1.jpg?fit=1000%2C667&amp;quality=50&amp;strip=all">                </figure>
            </a>
        </div>
            <div class="col-12 col-lg-8 pt-3 pt-lg-0 d-flex justify-content-center flex-column">
        <span class="hl-hat">Nova realidade</span>
        <span class="hl-title hl-title-2"><a href="https://www.infomoney.com.br/minhas-financas/marco-cambial-cria-caminho-para-consumidor-acessar-contas-em-dolar-no-brasil-veja-o-que-pode-mudar/" title="Marco cambial cria caminho para consumidor acessar contas em dólar no Brasil; veja o que pode mudar">Marco cambial cria caminho para consumidor acessar contas em dólar no Brasil; veja o que pode mudar</a></span>
        <span class="hl-date"><span class="posted-diff">2 semanas atrás</span></span>
    </div>
</div>                            </div>
                            <a href="https://www.infomoney.com.br/tudo-sobre/cambio" class="load-more-news">Veja mais</a>
                        </div>
                    </div>

                    <div class="row mt-5">
                        <div class="col-12">
                            <h2>Histórico de cotações do Dólar</h2>
                            <div id="container_table">
                                <table class="default-table">
                                    <thead>
                                        <tr>
                                            <th>Data</th>
                                            <th>Valor</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                                                                    <tr>
                                                <td>06/01/23</td>
                                                <td>5.234</td>
                                            </tr>
                                                                                        <tr>
                                                <td>05/01/23</td>
                                                <td>5.351</td>
                                            </tr>
                                                                                        <tr>
                                                <td>04/01/23</td>
                                                <td>5.452</td>
                                            </tr>
                                                                                        <tr>
                                                <td>03/01/23</td>
                                                <td>5.45</td>
                                            </tr>
                                                                                        <tr>
                                                <td>02/01/23</td>
                                                <td>5.361</td>
                                            </tr>
                                                                                        <tr>
                                                <td>29/12/22</td>
                                                <td>5.281</td>
                                            </tr>
                                                                                        <tr>
                                                <td>28/12/22</td>
                                                <td>5.257</td>
                                            </tr>
                                                                                        <tr>
                                                <td>27/12/22</td>
                                                <td>5.285</td>
                                            </tr>
                                                                                        <tr>
                                                <td>26/12/22</td>
                                                <td>5.206</td>
                                            </tr>
                                                                                        <tr>
                                                <td>23/12/22</td>
                                                <td>5.162</td>
                                            </tr>
                                                                                        <tr>
                                                <td>22/12/22</td>
                                                <td>5.185</td>
                                            </tr>
                                                                                </tbody>
                                </table>
                            
                            </div>
                        </div>
                    </div>

                    
                    
                </div>
                                            <div class="
        col-12 col-lg-4 VERTICAL_AF_MOBILE container-ads">
            <div id="VERTICAL_AF_MOBILE" class="VERTICAL_AF_MOBILE">
                
            </div>
        </div>        <div class="
        col-12 col-lg-4 RETANGULO_BF_MOBILE container-ads">
            <div id="RETANGULO_BF_MOBILE" class="RETANGULO_BF_MOBILE">
                
            </div>
        </div>                            </div>
        </div>
        <footer class="footer mt-5" id="footer">
    <div class="container">
        <div class="row footer-top pb-5">
            <div class="col-md-12 col-lg-12 footer-map">
                <ul id="menu-rodape" class="list-unstyled"><li id="menu-item-601655" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-601655"><a href="https://www.infomoney.com.br/ultimas-noticias/">Notícias</a>
<ul class="list-unstyled">
	<li id="menu-item-601656" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601656"><a href="https://www.infomoney.com.br/mercados/">Mercados</a></li>
	<li id="menu-item-601657" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601657"><a href="https://www.infomoney.com.br/onde-investir/">Onde investir</a></li>
	<li id="menu-item-601658" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601658"><a href="https://www.infomoney.com.br/minhas-financas/">Minhas Finanças</a></li>
	<li id="menu-item-641973" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-641973"><a href="https://www.infomoney.com.br/negocios/">Negócios</a></li>
	<li id="menu-item-1325310" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1325310"><a href="https://www.infomoney.com.br/economia/">Economia</a></li>
	<li id="menu-item-601659" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601659"><a href="https://www.infomoney.com.br/politica/">Política</a></li>
	<li id="menu-item-601660" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601660"><a href="https://www.infomoney.com.br/carreira/">Carreira</a></li>
	<li id="menu-item-601661" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601661"><a href="https://www.infomoney.com.br/consumo/">Consumo</a></li>
	<li id="menu-item-1611581" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1611581"><a href="https://www.infomoney.com.br/web-stories/">WebStories</a></li>
</ul>
</li>
<li id="menu-item-1318891" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1318891"><a href="https://www.infomoney.com.br/cursos/">Aprenda</a>
<ul class="list-unstyled">
	<li id="menu-item-1331961" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1331961"><a href="https://www.infomoney.com.br/guias/">Guias</a></li>
	<li id="menu-item-601647" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601647"><a href="https://www.infomoney.com.br/cursos/">Cursos</a></li>
	<li id="menu-item-1952559" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1952559"><a href="https://www.infomoney.com.br/perfil/">Perfis</a></li>
	<li id="menu-item-1756441" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1756441"><a href="https://www.infomoney.com.br/ebooks/">Ebooks</a></li>
	<li id="menu-item-601654" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-601654"><a href="https://www.infomoney.com.br/planilhas/">Planilhas</a></li>
</ul>
</li>
<li id="menu-item-1318881" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-ancestor current-menu-parent menu-item-has-children menu-item-1318881"><a href="https://www.infomoney.com.br/cotacoes/b3/">Cotações</a>
<ul class="list-unstyled">
	<li id="menu-item-1318882" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1318882"><a href="https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/">Ibovespa</a></li>
	<li id="menu-item-641809" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-641809"><a href="https://www.infomoney.com.br/ferramentas/altas-e-baixas/">Altas e Baixas</a></li>
	<li id="menu-item-1318883" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item menu-item-1318883"><a href="https://www.infomoney.com.br/ferramentas/cambio/" aria-current="page">Dólar e câmbio</a></li>
	<li id="menu-item-1952565" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1952565"><a href="https://www.infomoney.com.br/cotacoes/b3/bdr/">BDRs</a></li>
	<li id="menu-item-1952566" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1952566"><a href="https://www.infomoney.com.br/cotacoes/b3/etf/">ETFs</a></li>
	<li id="menu-item-1952567" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1952567"><a href="https://www.infomoney.com.br/cotacoes/b3/fii/">FIIs</a></li>
	<li id="menu-item-1318885" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1318885"><a href="https://www.infomoney.com.br/cotacoes/cripto/">Criptoativos</a></li>
	<li id="menu-item-1952568" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1952568"><a href="https://www.infomoney.com.br/cotacoes/nasdaq/">Nasdaq</a></li>
	<li id="menu-item-1952571" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1952571"><a href="https://www.infomoney.com.br/cotacoes/nyse/">Nyse</a></li>
</ul>
</li>
<li id="menu-item-641805" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-has-children menu-item-641805"><a href="https://www.infomoney.com.br/">Ferramentas</a>
<ul class="list-unstyled">
	<li id="menu-item-1721009" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1721009"><a href="https://www.infomoney.com.br/ferramentas/simulador-xp/">Simulador de Investimentos</a></li>
	<li id="menu-item-1492847" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1492847"><a href="https://www.infomoney.com.br/ferramentas/comparador-de-fiis/">Comparador de FIIs</a></li>
	<li id="menu-item-641880" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-641880"><a href="https://www.infomoney.com.br/ferramentas/comparador-renda-fixa/">Comparador de Renda Fixa</a></li>
	<li id="menu-item-1428108" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1428108"><a href="https://www.infomoney.com.br/ferramentas/comparador-de-fundos/">Comparador de Fundos</a></li>
	<li id="menu-item-1642355" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1642355"><a href="https://www.infomoney.com.br/ferramentas/comparador-de-investimentos/">Comparador de Investimentos</a></li>
	<li id="menu-item-1318888" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1318888"><a href="https://www.infomoney.com.br/ferramentas/juros-futuros-di/">Juros Futuros</a></li>
	<li id="menu-item-1318887" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1318887"><a href="https://www.infomoney.com.br/ferramentas/cotacoes-opcoes-de-acoes/">Opções de Ações</a></li>
	<li id="menu-item-1318889" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1318889"><a href="https://www.infomoney.com.br/ferramentas/mini-contratos/">Minicontratos</a></li>
	<li id="menu-item-1428111" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1428111"><a href="https://www.infomoney.com.br/ferramentas/inflacao/">Índices de Inflação</a></li>
	<li id="menu-item-1318892" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1318892"><a href="https://www.infomoney.com.br/ferramentas/carteira-de-acompanhamento/">Carteira de Acompanhamento</a></li>
	<li id="menu-item-1428107" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1428107"><a href="https://www.infomoney.com.br/ferramentas/fatos-relevantes/">Fatos Relevantes</a></li>
	<li id="menu-item-641818" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-641818"><a href="https://www.infomoney.com.br/cotacoes/empresas-b3/">Empresas B3</a></li>
	<li id="menu-item-641868" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-641868"><a href="https://www.infomoney.com.br/ferramentas/calendario-economico/">Agendas</a></li>
</ul>
</li>
<li id="menu-item-1331960" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1331960"><a href="https://www.infomoney.com.br/newsletters/">Siga</a>
<ul class="list-unstyled">
	<li id="menu-item-1953268" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1953268"><a href="https://www.infomoney.com.br/newsletters/">Newsletter</a></li>
	<li id="menu-item-1953269" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1953269"><a href="https://www.infomoney.com.br/podcasts/">Podcasts</a></li>
	<li id="menu-item-1617165" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1617165"><a href="https://infomoney.onelink.me/Mmb2/7a80027f">App IM+</a></li>
</ul>
</li>
</ul>            </div>
        </div>
        
        <div class="row footer-menu-extra">
            <div class="col">
                <a href="https://www.infomoney.com.br/" class="logo-footer"><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.svg" data-lazy-src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/logo.svg?is-pending-load=1" loading="lazy" class="jetpack-lazy-image" alt="Infomoney"></a>
                <div class="menu-institucional-container"><ul id="menu-institucional" class="menu"><li id="menu-item-138" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-138"><a href="https://auth.infomoney.com.br/authentication/signin">Cadastre-se</a></li>
<li id="menu-item-1670619" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1670619"><a href="https://www.infomoney.com.br/quem-somos/">Quem Somos</a></li>
<li id="menu-item-139" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-139"><a href="https://lp.infomoney.com.br/moneylab-cases?cid=29163866.1669118894">Media Kit</a></li>
<li id="menu-item-1671809" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1671809"><a href="https://www.infomoney.com.br/wp-content/uploads/2021/07/MoneyLab-Tabela2021.pdf">Tabela de preços MoneyLab</a></li>
<li id="menu-item-1671810" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1671810"><a href="https://lp.infomoney.com.br/moneylab-cases?cid=29163866.1669118894">Cases de sucesso</a></li>
<li id="menu-item-1420106" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-privacy-policy menu-item-1420106"><a href="https://www.infomoney.com.br/politica-de-privacidade/">Política de Privacidade</a></li>
<li id="menu-item-1440450" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1440450"><a href="https://www.infomoney.com.br/politica-de-cookies/">Política de cookies</a></li>
<li id="menu-item-1718321" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1718321"><a>Preferências de cookies</a></li>
<li id="menu-item-157" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-157"><a href="https://www.infomoney.com.br/fale-conosco/">Fale conosco</a></li>
</ul></div>            </div>
        </div>
        <div class="row footer-menu-extra">
            <div class="col">
                <div class="footer-social mb-4"> 
                    
    <a href="https://www.facebook.com/InfoMoney" target="_blank"><i class="fab fa-facebook"></i></a>
    <a href="https://twitter.com/infomoney" target="_blank"><i class="fab fa-twitter"></i></a>
    <a href="https://www.youtube.com/user/tvinfomoney?sub_confirmation=1" target="_blank"><i class="fab fa-youtube"></i></a>
      
        <a href="https://t.me/infomoney_noticias" target="_blank"><i class="fab fa-telegram-plane"></i></a>
    <a href="https://www.linkedin.com/company/infomoney/" target="_blank"><i class="fab fa-linkedin"></i></a>
    <a href="https://www.instagram.com/infomoney/" target="_blank"><i class="fab fa-instagram"></i></a>
    <a href="https://www.tiktok.com/@infomoney" target="_blank"><svg style="height: 1em;" fill="#fff" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2859 3333" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd"><path d="M2081 0c55 473 319 755 778 785v532c-266 26-499-61-770-225v995c0 1264-1378 1659-1932 753-356-583-138-1606 1004-1647v561c-87 14-180 36-265 65-254 86-398 247-358 531 77 544 1075 705 992-358V1h551z"></path></svg></a>
                </div>

                <!-- APP -->
                <div class="down-app">
                    <a href="https://infomoney.onelink.me/Mmb2/5c8eab83"><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/google-play-badge.webp" data-lazy-src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/google-play-badge.webp?is-pending-load=1" loading="lazy" width="150" class="jetpack-lazy-image" alt="IM+ - Google Play"></a>
                    <a href="https://infomoney.onelink.me/Mmb2/5c8eab83"><img src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/app-store-badge.webp" data-lazy-src="https://www.infomoney.com.br/wp-content/themes/infomoney/assets/img/app-store-badge.webp?is-pending-load=1" loading="lazy" width="140" class="jetpack-lazy-image" alt="IM+ - Apple Store"></a>
                </div>
            </div>
        </div>
        <div class="footer-disclaimer">
            <div class="text-justify col-lg-8">
                <p>© 2000-2023 InfoMoney. Todos os direitos reservados.</p>

                <p>O InfoMoney preza a qualidade da informação e atesta a apuração de todo o conteúdo produzido por sua equipe, ressaltando, no entanto, que não faz qualquer tipo de recomendação de investimento, não se responsabilizando por perdas, danos (diretos, indiretos e incidentais), custos e lucros cessantes.</p>

                <p><b>IMPORTANTE:</b> O portal www.infomoney.com.br (o "Portal") é de propriedade da Infostocks Informações e Sistemas Ltda. (CNPJ/MF nº 03.082.929/0001-03) ("Infostocks"), sociedade controlada, indiretamente, pela XP Controle Participações S/A (CNPJ/MF nº 09.163.677/0001-15), sociedade holding que controla as empresas do XP Inc. O XP Inc tem em sua composição empresas que exercem atividades de: corretoras de valoresmobiliários, banco, seguradora, corretora de seguros, análise de investimentos de valores mobiliários, gestoras de recursos de terceiros. Apesar de as Sociedades XP estarem sob controle comum, os executivos responsáveis pela Infostocks são totalmente independentes e as notícias, matérias e opiniões veiculadas no Portal não são, sob qualquer aspecto, direcionadas e/ou influenciadas por relatórios de análise produzidos por áreas técnicas das empresas do XP Inc, nem por decisões comerciais e de negócio de tais sociedades, sendo produzidos de acordo com o juízo de valor e as convicções próprias da equipe interna da Infostocks.
                
                </p>

            </div>
        </div>
    </div>
</footer><!-- #page -->

		
				<div id="jp-carousel-loading-overlay">
			<div id="jp-carousel-loading-wrapper">
				<span id="jp-carousel-library-loading">&nbsp;</span>
			</div>
		</div>
		<div class="jp-carousel-overlay" style="display: none;">

		<div class="jp-carousel-container">
			<!-- The Carousel Swiper -->
			<div class="jp-carousel-wrap swiper-container jp-carousel-swiper-container jp-carousel-transitions" itemscope="" itemtype="https://schema.org/ImageGallery">
				<div class="jp-carousel swiper-wrapper"></div>
				<div class="jp-swiper-button-prev swiper-button-prev">
					<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
						<mask id="maskPrev" mask-type="alpha" maskUnits="userSpaceOnUse" x="8" y="6" width="9" height="12">
							<path d="M16.2072 16.59L11.6496 12L16.2072 7.41L14.8041 6L8.8335 12L14.8041 18L16.2072 16.59Z" fill="white"></path>
						</mask>
						<g mask="url(#maskPrev)">
							<rect x="0.579102" width="23.8823" height="24" fill="#FFFFFF"></rect>
						</g>
					</svg>
				</div>
				<div class="jp-swiper-button-next swiper-button-next">
					<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
						<mask id="maskNext" mask-type="alpha" maskUnits="userSpaceOnUse" x="8" y="6" width="8" height="12">
							<path d="M8.59814 16.59L13.1557 12L8.59814 7.41L10.0012 6L15.9718 12L10.0012 18L8.59814 16.59Z" fill="white"></path>
						</mask>
						<g mask="url(#maskNext)">
							<rect x="0.34375" width="23.8822" height="24" fill="#FFFFFF"></rect>
						</g>
					</svg>
				</div>
			</div>
			<!-- The main close buton -->
			<div class="jp-carousel-close-hint">
				<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
					<mask id="maskClose" mask-type="alpha" maskUnits="userSpaceOnUse" x="5" y="5" width="15" height="14">
						<path d="M19.3166 6.41L17.9135 5L12.3509 10.59L6.78834 5L5.38525 6.41L10.9478 12L5.38525 17.59L6.78834 19L12.3509 13.41L17.9135 19L19.3166 17.59L13.754 12L19.3166 6.41Z" fill="white"></path>
					</mask>
					<g mask="url(#maskClose)">
						<rect x="0.409668" width="23.8823" height="24" fill="#FFFFFF"></rect>
					</g>
				</svg>
			</div>
			<!-- Image info, comments and meta -->
			<div class="jp-carousel-info">
				<div class="jp-carousel-info-footer">
					<div class="jp-carousel-pagination-container">
						<div class="jp-swiper-pagination swiper-pagination"></div>
						<div class="jp-carousel-pagination"></div>
					</div>
					<div class="jp-carousel-photo-title-container">
						<h2 class="jp-carousel-photo-caption"></h2>
					</div>
					<div class="jp-carousel-photo-icons-container">
						<a href="https://www.infomoney.com.br/ferramentas/cambio/#" class="jp-carousel-icon-btn jp-carousel-icon-info" aria-label="Toggle photo metadata visibility">
							<span class="jp-carousel-icon">
								<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
									<mask id="maskInfo" mask-type="alpha" maskUnits="userSpaceOnUse" x="2" y="2" width="21" height="20">
										<path fill-rule="evenodd" clip-rule="evenodd" d="M12.7537 2C7.26076 2 2.80273 6.48 2.80273 12C2.80273 17.52 7.26076 22 12.7537 22C18.2466 22 22.7046 17.52 22.7046 12C22.7046 6.48 18.2466 2 12.7537 2ZM11.7586 7V9H13.7488V7H11.7586ZM11.7586 11V17H13.7488V11H11.7586ZM4.79292 12C4.79292 16.41 8.36531 20 12.7537 20C17.142 20 20.7144 16.41 20.7144 12C20.7144 7.59 17.142 4 12.7537 4C8.36531 4 4.79292 7.59 4.79292 12Z" fill="white"></path>
									</mask>
									<g mask="url(#maskInfo)">
										<rect x="0.8125" width="23.8823" height="24" fill="#FFFFFF"></rect>
									</g>
								</svg>
							</span>
						</a>
												<a href="https://www.infomoney.com.br/ferramentas/cambio/#" class="jp-carousel-icon-btn jp-carousel-icon-comments" aria-label="Toggle photo comments visibility">
							<span class="jp-carousel-icon">
								<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
									<mask id="maskComments" mask-type="alpha" maskUnits="userSpaceOnUse" x="2" y="2" width="21" height="20">
										<path fill-rule="evenodd" clip-rule="evenodd" d="M4.3271 2H20.2486C21.3432 2 22.2388 2.9 22.2388 4V16C22.2388 17.1 21.3432 18 20.2486 18H6.31729L2.33691 22V4C2.33691 2.9 3.2325 2 4.3271 2ZM6.31729 16H20.2486V4H4.3271V18L6.31729 16Z" fill="white"></path>
									</mask>
									<g mask="url(#maskComments)">
										<rect x="0.34668" width="23.8823" height="24" fill="#FFFFFF"></rect>
									</g>
								</svg>

								<span class="jp-carousel-has-comments-indicator" aria-label="This image has comments."></span>
							</span>
						</a>
											</div>
				</div>
				<div class="jp-carousel-info-extra">
					<div class="jp-carousel-info-content-wrapper">
						<div class="jp-carousel-photo-title-container">
							<h2 class="jp-carousel-photo-title"></h2>
						</div>
						<div class="jp-carousel-comments-wrapper">
															<div id="jp-carousel-comments-loading">
									<span>Loading Comments...</span>
								</div>
								<div class="jp-carousel-comments"></div>
								<div id="jp-carousel-comment-form-container">
									<span id="jp-carousel-comment-form-spinner">&nbsp;</span>
									<div id="jp-carousel-comment-post-results"></div>
																														<form id="jp-carousel-comment-form">
												<label for="jp-carousel-comment-form-comment-field" class="screen-reader-text">Write a Comment...</label>
												<textarea name="comment" class="jp-carousel-comment-form-field jp-carousel-comment-form-textarea" id="jp-carousel-comment-form-comment-field" placeholder="Write a Comment..."></textarea>
												<div id="jp-carousel-comment-form-submit-and-info-wrapper">
													<div id="jp-carousel-comment-form-commenting-as">
																													<fieldset>
																<label for="jp-carousel-comment-form-email-field">Email (Required)</label>
																<input type="text" name="email" class="jp-carousel-comment-form-field jp-carousel-comment-form-text-field" id="jp-carousel-comment-form-email-field">
															</fieldset>
															<fieldset>
																<label for="jp-carousel-comment-form-author-field">Name (Required)</label>
																<input type="text" name="author" class="jp-carousel-comment-form-field jp-carousel-comment-form-text-field" id="jp-carousel-comment-form-author-field">
															</fieldset>
															<fieldset>
																<label for="jp-carousel-comment-form-url-field">Website</label>
																<input type="text" name="url" class="jp-carousel-comment-form-field jp-carousel-comment-form-text-field" id="jp-carousel-comment-form-url-field">
															</fieldset>
																											</div>
													<input type="submit" name="submit" class="jp-carousel-comment-form-button" id="jp-carousel-comment-form-button-submit" value="Post Comment">
												</div>
											</form>
																											</div>
													</div>
						<div class="jp-carousel-image-meta">
							<div class="jp-carousel-title-and-caption">
								<div class="jp-carousel-photo-info">
									<h3 class="jp-carousel-caption" itemprop="caption description"></h3>
								</div>

								<div class="jp-carousel-photo-description"></div>
							</div>
							<ul class="jp-carousel-image-exif" style="display: none;"></ul>
							<a class="jp-carousel-image-download" target="_blank" style="display: none;">
								<svg width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
									<mask id="mask0" mask-type="alpha" maskUnits="userSpaceOnUse" x="3" y="3" width="19" height="18">
										<path fill-rule="evenodd" clip-rule="evenodd" d="M5.84615 5V19H19.7775V12H21.7677V19C21.7677 20.1 20.8721 21 19.7775 21H5.84615C4.74159 21 3.85596 20.1 3.85596 19V5C3.85596 3.9 4.74159 3 5.84615 3H12.8118V5H5.84615ZM14.802 5V3H21.7677V10H19.7775V6.41L9.99569 16.24L8.59261 14.83L18.3744 5H14.802Z" fill="white"></path>
									</mask>
									<g mask="url(#mask0)">
										<rect x="0.870605" width="23.8823" height="24" fill="#FFFFFF"></rect>
									</g>
								</svg>
								<span class="jp-carousel-download-text"></span>
							</a>
							<div class="jp-carousel-image-map" style="display: none;"></div>
						</div>
					</div>
				</div>
			</div>
		</div>

		</div>
		<link rel="stylesheet" id="infomoney-widget-ticker-css" href="https://www.infomoney.com.br/wp-content/themes/infomoney/css/templates/widget-ticker.css?ver=6.4" media="all">



 


























		
				<span id="infinite-aria" aria-live="assertive"></span>
			
	<iframe src="cid:frame-57999994083348FF37124287FC865906@mhtml.blink" style="visibility: hidden; display: none;"></iframe>



<img src="https://pixel.wp.com/g.gif?v=ext&amp;blog=161989173&amp;post=0&amp;tz=-3&amp;srv=www.infomoney.com.br&amp;hp=vip&amp;j=1%3A11.6&amp;host=www.infomoney.com.br&amp;ref=https%3A%2F%2Fwww.google.com%2F&amp;fcp=2812&amp;rand=0.9857212198997054" alt="" width="6" height="5" id="wpstats"><iframe name="google_ads_top_frame" id="google_ads_top_frame" style="display: none; position: fixed; left: -999px; top: -999px; width: 0px; height: 0px;"></iframe><iframe src="cid:frame-F3C6B2A5D4F800B0B2A063A08A4A5DBC@mhtml.blink" width="0" height="0" style="display: none;"></iframe><iframe src="cid:frame-1F4FB74B5671DFF51F1167D128EEC706@mhtml.blink" width="0" height="0" style="display: none;"></iframe></body></html>
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: cid:css-06067961-65bd-4c1d-beb2-6d7a245b4f70@mhtml.blink

@charset "utf-8";

:root { --sapphire:#0091FF; --apatite:#32C5FF; --ruby:#FF5252; --xpamber:#F7B500; --amazonite:#44D7B6; --lightgray:#F5F7F8; --darkgray:#212121; --gray:#6C757D; --gray24:rgba(108, 117, 125, 0.24); --blue:#0091FF; --lightblue:#32C5FF; --yellow:#ffc709; --red:#FF5252; --emerald:#1eb980; --white:#ffffff; }

* { letter-spacing: normal !important; }

html { scroll-behavior: smooth; }

body { font-family: "Helvetica Neue", "Helvetica Neue LT Pro", Helvetica, Arial, sans-serif; color: rgb(0, 0, 0); }

a { color: var(--sapphire); }

h1 { letter-spacing: -0.02em !important; }

p { font-weight: 400 !important; }

.hl-hat { display: block; font-size: 0.875rem; line-height: 16px; margin-bottom: 4px; color: rgb(102, 102, 102); width: 100%; font-weight: 400 !important; }

.hl-title { display: block; }

.hl-title a { color: rgb(0, 0, 0); }

.hl-title-2 { font-size: 24px; line-height: 28px; font-weight: 700; letter-spacing: -0.01em !important; }

.hl-title-2 a { color: rgb(0, 0, 0); letter-spacing: -0.01em !important; }

.hl-title-4 { font-size: 20px; line-height: 24px; letter-spacing: -0.5px; font-weight: 700; }

.hl-title-4 a { color: rgb(17, 17, 17); }

.hl-title-8 { font-size: 14px; line-height: 16px; font-weight: 600; letter-spacing: -0.1px; color: rgb(17, 17, 17); display: flex; }

.hl-title-8 i { font-size: 16px; color: rgb(0, 145, 255); margin: 0px 4px 0px 0px; }

.info-spotlight { position: absolute; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; padding: 0px 32px 32px; background: linear-gradient(to top, rgba(0, 0, 0, 0.7) 20%, rgba(0, 0, 0, 0) 60%); top: 0px; z-index: 1; }

.info-spotlight span, .info-spotlight span a { color: rgb(255, 255, 255); }

.cover-link { display: block; position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; background-color: transparent; z-index: 100; }

.border-t { border-top: 1px solid rgb(221, 221, 221); }

.fill-lightgray { background: var(--lightgray); }

.border-t-mobile { border-top: 0px; }

.img-container { width: 100%; align-self: flex-start; }

.img-container figure { position: relative; overflow: hidden; padding-top: 56.25%; margin: 0px; }

.img-container figure img { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); min-height: 100%; }

@supports (-ms-ime-align:auto) {
  .material-icons { font-feature-settings: "liga"; }
}

@media screen and (max-width: 991px) {
  body.is-padded-mobile { padding-top: 48px; }
  .hl-title-2 { font-size: 20px; line-height: 24px; letter-spacing: -0.6px; }
  .info-spotlight { position: relative; background: 0px 0px; padding: 0px 16px 16px; }
  .info-spotlight .hl-hat { color: rgb(108, 117, 125); }
  .info-spotlight .hl-title a { color: rgb(0, 0, 0); }
  .border-t-mobile { border-top: 1px solid rgba(0, 0, 0, 0.12); }
}

h1 { scroll-margin-top: 70px; }

.header { position: fixed; top: 0px; left: 0px; width: 100%; height: 48px; z-index: 1000; background: rgb(33, 33, 33); }

.header .logo-link { margin: 13px 0px 7px 16px; }

.header .logo-link .logo { max-height: 28px; }

.header .menu-open { color: rgba(255, 255, 255, 0.6); }

.header .nav-topics i { color: rgb(0, 145, 255); }

.header .nav-topics a { color: rgba(255, 255, 255, 0.9); }

.header .nav-topics span { color: rgb(255, 255, 255); }

.header .header-action { color: rgba(255, 255, 255, 0.6); }

.header-full { display: none; }

.header-full .logo-link { padding: 15px 0px 5px; }

.header-full .logo-link .logo { max-height: 48px; }

.header-full .nav-topics i { color: var(--blue); }

.header-full .nav-topics a { color: rgb(17, 17, 17); }

.header-full .header-action { color: var(--gray); }

.header-action { display: flex; align-items: center; justify-content: center; width: 24px; height: 24px; }

.container-nav-topics { background-color: rgb(249, 249, 249); }

.nav-topics { height: 40px; }

.nav-topics i { font-size: 18px; }

.nav-topics a { font-size: 14px; line-height: 16px; font-weight: 400; letter-spacing: -0.2px; }

.nav-topics span { margin: 0px 10px; }

.container-search-header { display: none; position: fixed; top: 0px; left: 0px; width: 100%; height: 1000%; background-color: rgb(255, 255, 255); z-index: 2000; animation: 0.5s ease 0s 1 normal none running fadein; }

.container-search-header .header-search { height: 48px; border-bottom: 1px solid rgb(221, 221, 221); display: flex; justify-content: space-between; }

.container-search-header .header-search img { height: 28px; margin: 13px 0px 7px 16px; }

.container-search-header .header-search button { background: 0px 0px; border: none; height: 24px; width: 24px; padding: 0px; margin: 12px 16px 12px 0px; }

.container-search-header .header-search button i { color: rgb(102, 102, 102); }

.container-search-header .container { height: 100vh; margin: -48px auto 0px; display: flex; align-items: center; }

.container-search-header .container .row { flex-basis: calc(100% + 32px); }

.container-search-header .container .row form#header-search { display: flex; }

.container-search-header .container .row form#header-search input[type="text"] { width: 100%; background: 0px 0px; border-width: 0px 0px 1px; border-color: rgb(221, 221, 221); font-size: 24px; font-weight: 700; line-height: 36px; height: 72px; padding: 18px 0px; }

.container-search-header .container .row form#header-search button { background: 0px 0px; height: 72px; border-width: 0px 0px 1px; border-color: rgb(221, 221, 221); border-style: solid; }

.container-search-header .container .row form#header-search button i { font-size: 26px; color: rgb(204, 204, 204); }

.container-search-header .container .row .topics-search { padding-top: 20px; }

.container-search-header .container .row .topics-search div { padding: 10px 16px; display: flex; }

.container-search-header .container .row .topics-search div i { color: rgb(0, 145, 255); font-size: 18px; }

.container-search-header .container .row .topics-search div a { font-size: 16px; font-weight: 600; line-height: 20px; letter-spacing: -0.3px; color: rgb(17, 17, 17); margin: 0px 0px 0px 16px; }

@media (min-width: 992px) {
  .header { transform: translateY(-100%); }
  .header-full { display: block; }
}

@media screen and (max-width: 991px) {
  .container-search-header .container { margin: 0px; align-items: start; }
  .container-search-header .container .row form#header-search { margin: 16px 0px 0px; }
  .container-search-header .container .row form#header-search input[type="text"] { font-size: 18px; }
  .container-search-header .container .row .topics-search div { padding: 10px 0px; }
}

@keyframes fadein { 
  0% { opacity: 0; }
  100% { opacity: 1; }
}

#menu-side { position: fixed; top: 0px; left: -320px; width: 320px; height: 100%; z-index: 2147483647; background-color: rgb(0, 0, 0); overflow-y: scroll; }

#menu-side .menu-header { height: 48px; }

#menu-side .menu-header #menu-close i { width: 24px; height: 24px; float: right; color: rgba(255, 255, 255, 0.6); font-size: 24px; margin: 12px 16px 0px 0px; }

#menu-side .topics-menu { padding: 8px 0px; border-bottom: 1px solid rgba(255, 255, 255, 0.12); }

#menu-side .topics-menu a { padding: 8px 16px; display: flex; }

#menu-side .topics-menu a i { color: rgb(0, 145, 255); font-size: 24px; }

#menu-side .topics-menu a p { font-size: 13px; font-weight: 600; line-height: 20px; color: rgba(255, 255, 255, 0.7); margin: 2px 0px 2px 16px; }

#menu-side ul { margin: 0px; }

#menu-side ul li { padding: 0px; }

#menu-side ul li a { font-size: 13px; line-height: 20px; font-weight: 600; color: rgba(255, 255, 255, 0.7); }

#menu-side ul li ul { background-color: rgba(255, 255, 255, 0.1); overflow: hidden; max-height: 0px; }

#menu-side ul li ul li a { padding: 10px 32px; display: block; }

#menu-side > ul > li.menu-item-has-children::before { content: "keyboard_arrow_down"; font-family: "Material Icons"; color: rgba(255, 255, 255, 0.7); position: absolute; right: 16px; z-index: -1; font-size: 24px; line-height: 40px; }

#menu-side > ul > li > a { padding: 10px 16px; display: block; }

#menu-side::-webkit-scrollbar { width: 0px !important; }

@media screen and (max-width: 320px) {
  #menu-side { width: 100%; }
}

.container, .container-fluid { padding-right: 16px; padding-left: 16px; }

.container { max-width: 1280px; }

.row { margin-right: -16px; margin-left: -16px; }

figure { margin: 0px; }

.img-fluid { width: 100%; }

.col, .col-12, .col-lg-12, .col-lg-6, .col-lg-8 { padding-right: 16px; padding-left: 16px; }

.mt-5 { margin-top: 40px !important; }

.userPanel { position: relative; }

.userPanel .login-header { display: none; padding: 15px 16px 17px; }

.userPanel .login-header i, .userPanel .login-header p { color: rgba(255, 255, 255, 0.9); }

.userPanel .login-header p { margin: 0px 24px 0px 16px; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; }

.userPanel .login-header a { display: flex; }

.userPanel .login-header::before { content: "keyboard_arrow_down"; font-family: "Material Icons"; color: rgba(255, 255, 255, 0.7); position: absolute; right: 16px; font-size: 24px; line-height: 24px; }

.userPanel .login-header.not-logged::before { content: ""; display: none; }

.userPanel .login-options { display: none; color: rgb(255, 255, 255); }

.header, .header-full { z-index: 1030; }

.header .userPanel, .header-full .userPanel { margin: 0px 24px 0px 0px; }

.header .userPanel .login-header, .header-full .userPanel .login-header { padding: 8px; }

.header .userPanel .login-header p, .header-full .userPanel .login-header p { font-size: 13px; letter-spacing: -0.2px; margin: 0px 24px 0px 4px; }

.header .userPanel .login-header::before, .header-full .userPanel .login-header::before { content: "arrow_drop_down"; right: 8px; }

.header .userPanel .login-header.not-logged p, .header-full .userPanel .login-header.not-logged p { margin: 0px 4px; }

.header .userPanel .login-options, .header-full .userPanel .login-options { position: absolute; background-color: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.5) 0px 2px 4px 0px; padding: 8px 0px; z-index: 9; min-width: 150px; }

.header .userPanel .login-options li, .header-full .userPanel .login-options li { padding: 12px 16px; list-style: none; }

.header .userPanel .login-options li a, .header-full .userPanel .login-options li a { font-size: 14px; line-height: 16px; letter-spacing: -0.2px; color: rgb(33, 33, 33); font-weight: 600; }

.header:not(.is-visible) .userPanel { display: none; }

.header-full .userPanel { position: absolute; right: 40px; }

.header-full .userPanel .login-header i, .header-full .userPanel .login-header p { color: rgb(102, 102, 102); }

.header-full .userPanel .login-header::before { color: rgb(33, 33, 33); }

#menu-side .userPanel .login-header { background-color: rgba(255, 255, 255, 0.15); }

#menu-side .userPanel .login-options { background-color: rgba(255, 255, 255, 0.1); padding: 0px; }

#menu-side .userPanel .login-options li { list-style: none; padding: 10px 16px; }

@media screen and (max-width: 991px) {
  .header .userPanel, .header-full .userPanel { display: none; }
}
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: cid:css-fb73eae7-6ccc-4e01-8217-fdfcc9621bc0@mhtml.blink

@charset "utf-8";

img.wp-smiley, img.emoji { display: inline !important; border: none !important; box-shadow: none !important; height: 1em !important; width: 1em !important; margin: 0px 0.07em !important; vertical-align: -0.1em !important; background: none !important; padding: 0px !important; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: cid:css-47acedb3-2edf-474c-9ba3-34a5dfb417a3@mhtml.blink

@charset "utf-8";

body { --wp--preset--color--black: #000000; --wp--preset--color--cyan-bluish-gray: #abb8c3; --wp--preset--color--white: #ffffff; --wp--preset--color--pale-pink: #f78da7; --wp--preset--color--vivid-red: #cf2e2e; --wp--preset--color--luminous-vivid-orange: #ff6900; --wp--preset--color--luminous-vivid-amber: #fcb900; --wp--preset--color--light-green-cyan: #7bdcb5; --wp--preset--color--vivid-green-cyan: #00d084; --wp--preset--color--pale-cyan-blue: #8ed1fc; --wp--preset--color--vivid-cyan-blue: #0693e3; --wp--preset--color--vivid-purple: #9b51e0; --wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%); --wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%); --wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%); --wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%); --wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%); --wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%); --wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%); --wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%); --wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%); --wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%); --wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%); --wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%); --wp--preset--duotone--dark-grayscale: url("#wp-duotone-dark-grayscale"); --wp--preset--duotone--grayscale: url("#wp-duotone-grayscale"); --wp--preset--duotone--purple-yellow: url("#wp-duotone-purple-yellow"); --wp--preset--duotone--blue-red: url("#wp-duotone-blue-red"); --wp--preset--duotone--midnight: url("#wp-duotone-midnight"); --wp--preset--duotone--magenta-yellow: url("#wp-duotone-magenta-yellow"); --wp--preset--duotone--purple-green: url("#wp-duotone-purple-green"); --wp--preset--duotone--blue-orange: url("#wp-duotone-blue-orange"); --wp--preset--font-size--small: 13px; --wp--preset--font-size--medium: 20px; --wp--preset--font-size--large: 36px; --wp--preset--font-size--x-large: 42px; --wp--preset--spacing--20: 0.44rem; --wp--preset--spacing--30: 0.67rem; --wp--preset--spacing--40: 1rem; --wp--preset--spacing--50: 1.5rem; --wp--preset--spacing--60: 2.25rem; --wp--preset--spacing--70: 3.38rem; --wp--preset--spacing--80: 5.06rem; }

body .is-layout-flow > .alignleft { float: left; margin-inline-start: 0px; margin-inline-end: 2em; }

body .is-layout-flow > .alignright { float: right; margin-inline-start: 2em; margin-inline-end: 0px; }

body .is-layout-flow > .aligncenter { margin-left: auto !important; margin-right: auto !important; }

body .is-layout-constrained > .alignleft { float: left; margin-inline-start: 0px; margin-inline-end: 2em; }

body .is-layout-constrained > .alignright { float: right; margin-inline-start: 2em; margin-inline-end: 0px; }

body .is-layout-constrained > .aligncenter { margin-left: auto !important; margin-right: auto !important; }

body .is-layout-constrained > .alignwide { max-width: var(--wp--style--global--wide-size); }

body .is-layout-flex { display: flex; }

body .is-layout-flex { flex-wrap: wrap; align-items: center; }

body .is-layout-flex > * { margin: 0px; }

.has-black-color { color: var(--wp--preset--color--black)  !important; }

.has-cyan-bluish-gray-color { color: var(--wp--preset--color--cyan-bluish-gray)  !important; }

.has-white-color { color: var(--wp--preset--color--white)  !important; }

.has-pale-pink-color { color: var(--wp--preset--color--pale-pink)  !important; }

.has-vivid-red-color { color: var(--wp--preset--color--vivid-red)  !important; }

.has-luminous-vivid-orange-color { color: var(--wp--preset--color--luminous-vivid-orange)  !important; }

.has-luminous-vivid-amber-color { color: var(--wp--preset--color--luminous-vivid-amber)  !important; }

.has-light-green-cyan-color { color: var(--wp--preset--color--light-green-cyan)  !important; }

.has-vivid-green-cyan-color { color: var(--wp--preset--color--vivid-green-cyan)  !important; }

.has-pale-cyan-blue-color { color: var(--wp--preset--color--pale-cyan-blue)  !important; }

.has-vivid-cyan-blue-color { color: var(--wp--preset--color--vivid-cyan-blue)  !important; }

.has-vivid-purple-color { color: var(--wp--preset--color--vivid-purple)  !important; }

.has-black-background-color { background-color: var(--wp--preset--color--black)  !important; }

.has-cyan-bluish-gray-background-color { background-color: var(--wp--preset--color--cyan-bluish-gray)  !important; }

.has-white-background-color { background-color: var(--wp--preset--color--white)  !important; }

.has-pale-pink-background-color { background-color: var(--wp--preset--color--pale-pink)  !important; }

.has-vivid-red-background-color { background-color: var(--wp--preset--color--vivid-red)  !important; }

.has-luminous-vivid-orange-background-color { background-color: var(--wp--preset--color--luminous-vivid-orange)  !important; }

.has-luminous-vivid-amber-background-color { background-color: var(--wp--preset--color--luminous-vivid-amber)  !important; }

.has-light-green-cyan-background-color { background-color: var(--wp--preset--color--light-green-cyan)  !important; }

.has-vivid-green-cyan-background-color { background-color: var(--wp--preset--color--vivid-green-cyan)  !important; }

.has-pale-cyan-blue-background-color { background-color: var(--wp--preset--color--pale-cyan-blue)  !important; }

.has-vivid-cyan-blue-background-color { background-color: var(--wp--preset--color--vivid-cyan-blue)  !important; }

.has-vivid-purple-background-color { background-color: var(--wp--preset--color--vivid-purple)  !important; }

.has-black-border-color { border-color: var(--wp--preset--color--black)  !important; }

.has-cyan-bluish-gray-border-color { border-color: var(--wp--preset--color--cyan-bluish-gray)  !important; }

.has-white-border-color { border-color: var(--wp--preset--color--white)  !important; }

.has-pale-pink-border-color { border-color: var(--wp--preset--color--pale-pink)  !important; }

.has-vivid-red-border-color { border-color: var(--wp--preset--color--vivid-red)  !important; }

.has-luminous-vivid-orange-border-color { border-color: var(--wp--preset--color--luminous-vivid-orange)  !important; }

.has-luminous-vivid-amber-border-color { border-color: var(--wp--preset--color--luminous-vivid-amber)  !important; }

.has-light-green-cyan-border-color { border-color: var(--wp--preset--color--light-green-cyan)  !important; }

.has-vivid-green-cyan-border-color { border-color: var(--wp--preset--color--vivid-green-cyan)  !important; }

.has-pale-cyan-blue-border-color { border-color: var(--wp--preset--color--pale-cyan-blue)  !important; }

.has-vivid-cyan-blue-border-color { border-color: var(--wp--preset--color--vivid-cyan-blue)  !important; }

.has-vivid-purple-border-color { border-color: var(--wp--preset--color--vivid-purple)  !important; }

.has-vivid-cyan-blue-to-vivid-purple-gradient-background { background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple)  !important; }

.has-light-green-cyan-to-vivid-green-cyan-gradient-background { background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan)  !important; }

.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background { background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange)  !important; }

.has-luminous-vivid-orange-to-vivid-red-gradient-background { background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red)  !important; }

.has-very-light-gray-to-cyan-bluish-gray-gradient-background { background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray)  !important; }

.has-cool-to-warm-spectrum-gradient-background { background: var(--wp--preset--gradient--cool-to-warm-spectrum)  !important; }

.has-blush-light-purple-gradient-background { background: var(--wp--preset--gradient--blush-light-purple)  !important; }

.has-blush-bordeaux-gradient-background { background: var(--wp--preset--gradient--blush-bordeaux)  !important; }

.has-luminous-dusk-gradient-background { background: var(--wp--preset--gradient--luminous-dusk)  !important; }

.has-pale-ocean-gradient-background { background: var(--wp--preset--gradient--pale-ocean)  !important; }

.has-electric-grass-gradient-background { background: var(--wp--preset--gradient--electric-grass)  !important; }

.has-midnight-gradient-background { background: var(--wp--preset--gradient--midnight)  !important; }

.has-small-font-size { font-size: var(--wp--preset--font-size--small)  !important; }

.has-medium-font-size { font-size: var(--wp--preset--font-size--medium)  !important; }

.has-large-font-size { font-size: var(--wp--preset--font-size--large)  !important; }

.has-x-large-font-size { font-size: var(--wp--preset--font-size--x-large)  !important; }

.wp-block-pullquote { font-size: 1.5em; line-height: 1.6; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: cid:css-cf9b1a48-580d-4b26-be19-cf570fb4c7bf@mhtml.blink

@charset "utf-8";

img#wpstats { display: none; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: cid:css-2c23ed12-3da7-4cae-b91d-b027048fcf86@mhtml.blink

@charset "utf-8";

html:not(.jetpack-lazy-images-js-enabled):not(.js) .jetpack-lazy-image { display: none; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: cid:css-31e41619-27cd-4853-b513-7a402782e2d5@mhtml.blink

@charset "utf-8";

body.postid-1561435 .advertising_super_home, body.postid-1627902 .advertising_super_home { display: none !important; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: cid:css-bc2216da-a751-4c2e-8841-7b1b5ecfbe61@mhtml.blink

@charset "utf-8";

.async-hide { opacity: 0 !important; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/infinite-scroll/infinity.css?ver=20140422

@charset "utf-8";

.infinite-loader { color: rgb(0, 0, 0); display: block; height: 28px; text-align: center; }

#infinite-handle span { background: rgb(51, 51, 51); border-radius: 1px; color: rgb(240, 240, 241); cursor: pointer; font-size: 13px; padding: 6px 16px; }

@keyframes spinner-inner { 
  0% { opacity: 1; }
  100% { opacity: 0; }
}

.infinite-loader .spinner-inner div { left: 47px; top: 24px; position: absolute; animation: 1s linear 0s infinite normal none running spinner-inner; background: rgb(0, 0, 0); outline: white solid 1px; width: 6px; height: 12px; border-radius: 3px / 6px; transform-origin: 3px 26px; }

.infinite-loader .spinner-inner div:nth-child(1) { transform: rotate(0deg); animation-delay: -0.916667s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(2) { transform: rotate(30deg); animation-delay: -0.833333s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(3) { transform: rotate(60deg); animation-delay: -0.75s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(4) { transform: rotate(90deg); animation-delay: -0.666667s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(5) { transform: rotate(120deg); animation-delay: -0.583333s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(6) { transform: rotate(150deg); animation-delay: -0.5s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(7) { transform: rotate(180deg); animation-delay: -0.416667s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(8) { transform: rotate(210deg); animation-delay: -0.333333s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(9) { transform: rotate(240deg); animation-delay: -0.25s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(10) { transform: rotate(270deg); animation-delay: -0.166667s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(11) { transform: rotate(300deg); animation-delay: -0.0833333s; background: rgb(0, 0, 0); }

.infinite-loader .spinner-inner div:nth-child(12) { transform: rotate(330deg); animation-delay: 0s; background: rgb(0, 0, 0); }

.infinite-loader .spinner { width: 28px; height: 28px; display: inline-block; overflow: hidden; background: none; }

.infinite-loader .spinner-inner { width: 100%; height: 100%; position: relative; transform: translateZ(0px) scale(0.28); backface-visibility: hidden; transform-origin: 0px 0px; }

.infinite-loader .spinner-inner div { box-sizing: content-box; }

#infinite-handle span button, #infinite-handle span button:hover, #infinite-handle span button:focus { display: inline; position: static; padding: 0px; margin: 0px; border: none; line-height: inherit; background: transparent; color: inherit; cursor: inherit; font-size: inherit; font-weight: inherit; font-family: inherit; }

@media (max-width: 800px) {
  #infinite-handle span::before { display: none; }
  #infinite-handle span { display: block; }
}

#infinite-footer { position: fixed; bottom: -50px; left: 0px; width: 100%; }

#infinite-footer a { text-decoration: none; }

#infinite-footer .blog-info a:hover, #infinite-footer .blog-credits a:hover { color: rgb(68, 68, 68); text-decoration: underline; }

#infinite-footer .container { background: rgba(255, 255, 255, 0.8); border-color: rgba(0, 0, 0, 0.1); border-style: solid; border-width: 1px 0px 0px; box-sizing: border-box; margin: 0px auto; overflow: hidden; padding: 1px 20px; width: 780px; }

#infinite-footer .blog-info, #infinite-footer .blog-credits { box-sizing: border-box; line-height: 25px; }

#infinite-footer .blog-info { float: left; overflow: hidden; text-align: left; text-overflow: ellipsis; white-space: nowrap; width: 40%; }

#infinite-footer .blog-credits { font-weight: normal; float: right; width: 60%; }

#infinite-footer .blog-info a { color: rgb(17, 17, 17); font-size: 14px; font-weight: bold; }

#infinite-footer .blog-credits { color: rgb(136, 136, 136); font-size: 12px; text-align: right; }

#infinite-footer .blog-credits a { color: rgb(100, 105, 112); }

.infinity-end.neverending #infinite-footer { display: none; }

@media (max-width: 640px) {
  #infinite-footer .container { box-sizing: border-box; width: 100%; }
  #infinite-footer .blog-info { width: 30%; }
  #infinite-footer .blog-credits { width: 70%; }
  #infinite-footer .blog-info a, #infinite-footer .blog-credits { font-size: 10px; }
}

@media (max-width: 640px) {
  #infinite-footer { position: static; }
}

#infinite-aria { position: absolute; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); height: 1px; width: 1px; margin: -1px; padding: 0px; border: 0px; }

.infinite-wrap:focus { outline: 0px !important; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/themes/infomoney/css/templates/tools.css?ver=6.4

@charset "utf-8";

.tool-logo { max-width: 155px; }

.tool-filters { background-color: var(--lightgray); padding: 40px 0px; margin: 0px; }

.tool-filters label.filter { font-size: 13px; line-height: 16px; color: rgb(33, 33, 33); font-weight: 600; margin: 0px 0px 12px; }

.tool-filters .row:not(:first-child), .tool-filters-inputs .row:not(:first-child) { margin-top: 64px; }

.tool-filters h6, .tool-filters-inputs h6 { font-weight: 700; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; color: rgb(33, 33, 33); margin: 0px; }

.tool-filters div.container-search, .tool-filters-inputs div.container-search { position: relative; width: 100%; }

.tool-filters div.container-search i, .tool-filters-inputs div.container-search i { position: absolute; z-index: 9; line-height: 52px; color: rgb(0, 0, 0); right: 16px; }

.tool-filters div.container-search select, .tool-filters-inputs div.container-search select { width: 100%; }

.tool-filters div.container-search .select2-container, .tool-filters-inputs div.container-search .select2-container { border: 1px solid var(--gray); width: 100% !important; }

.tool-filters div.container-search .select2-container .select2-selection, .tool-filters-inputs div.container-search .select2-container .select2-selection { height: 52px; }

.tool-filters div.container-search .select2-container .select2-selection .select2-selection__rendered, .tool-filters-inputs div.container-search .select2-container .select2-selection .select2-selection__rendered { height: 52px; padding: 16px 54px 16px 16px; display: block; font-size: 14px; line-height: 20px; letter-spacing: -0.3px; color: var(--gray); font-weight: 400; }

.tool-filters div.container-search .select2-container .select2-selection .select2-selection__rendered .select2-selection__placeholder, .tool-filters-inputs div.container-search .select2-container .select2-selection .select2-selection__rendered .select2-selection__placeholder { color: var(--darkgray); }

.tool-filters div.container-search .select2-container .select2-selection .select2-selection__arrow, .tool-filters-inputs div.container-search .select2-container .select2-selection .select2-selection__arrow { display: none; }

.tool-filters div.container-search .select2-container--default .select2-selection--single, .tool-filters-inputs div.container-search .select2-container--default .select2-selection--single { border: none; }

.tool-filters label.container-check, .tool-filters-inputs label.container-check { display: block; position: relative; padding-left: 35px; cursor: pointer; font-size: 22px; user-select: none; }

.tool-filters label.container-check input, .tool-filters-inputs label.container-check input { position: absolute; opacity: 0; cursor: pointer; height: 0px; width: 0px; }

.tool-filters label.container-check input[type="checkbox"] ~ .checkmark, .tool-filters-inputs label.container-check input[type="checkbox"] ~ .checkmark { position: absolute; top: 3px; left: 0px; height: 18px; width: 18px; background-color: rgb(238, 238, 238); border-radius: 3px; }

.tool-filters label.container-check input[type="checkbox"] ~ .checkmark::after, .tool-filters-inputs label.container-check input[type="checkbox"] ~ .checkmark::after { content: ""; position: absolute; display: none; left: 6px; top: 3px; width: 6px; height: 10px; border-style: solid; border-color: rgb(255, 255, 255); border-image: initial; border-width: 0px 3px 3px 0px; transform: rotate(45deg); }

.tool-filters label.container-check input[type="radio"] ~ .checkmark, .tool-filters-inputs label.container-check input[type="radio"] ~ .checkmark { position: absolute; top: 3px; left: 0px; height: 18px; width: 18px; background-color: rgb(238, 238, 238); border-radius: 50%; }

.tool-filters label.container-check input[type="radio"] ~ .checkmark::after, .tool-filters-inputs label.container-check input[type="radio"] ~ .checkmark::after { content: ""; position: absolute; display: none; left: 2px; top: 2px; width: 14px; height: 14px; border: 3px solid rgb(255, 255, 255); border-radius: 50%; }

.tool-filters label.container-check:hover input[type="checkbox"] ~ .checkmark, .tool-filters label.container-check:hover input[type="radio"] ~ .checkmark, .tool-filters-inputs label.container-check:hover input[type="checkbox"] ~ .checkmark, .tool-filters-inputs label.container-check:hover input[type="radio"] ~ .checkmark { background-color: rgb(204, 204, 204); }

.tool-filters label.container-check input[type="checkbox"]:checked ~ .checkmark, .tool-filters label.container-check input[type="radio"]:checked ~ .checkmark, .tool-filters-inputs label.container-check input[type="checkbox"]:checked ~ .checkmark, .tool-filters-inputs label.container-check input[type="radio"]:checked ~ .checkmark { background-color: rgb(33, 150, 243); }

.tool-filters label.container-check input[type="checkbox"]:checked ~ .checkmark::after, .tool-filters label.container-check input[type="radio"]:checked ~ .checkmark::after, .tool-filters-inputs label.container-check input[type="checkbox"]:checked ~ .checkmark::after, .tool-filters-inputs label.container-check input[type="radio"]:checked ~ .checkmark::after { display: block; }

.tool-filters label.container-check p, .tool-filters-inputs label.container-check p { margin: 0px; font-weight: 400; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; color: rgb(33, 33, 33); }

.tool-filters label.container-check:first-child, .tool-filters-inputs label.container-check:first-child { margin: 20px 0px 0px; }

.tool-filters label.container-check:not(:first-child), .tool-filters-inputs label.container-check:not(:first-child) { margin: 16px 0px 0px; }

.tool-filters div.container-range input[type="range"], .tool-filters-inputs div.container-range input[type="range"] { -webkit-appearance: none; width: 100%; background: 0px 0px; }

.tool-filters div.container-range input[type="range"]::-webkit-slider-thumb, .tool-filters-inputs div.container-range input[type="range"]::-webkit-slider-thumb { -webkit-appearance: none; height: 24px; width: 24px; margin-top: -10px; border: 3px solid rgb(0, 145, 255); background: rgb(255, 255, 255); border-radius: 50%; cursor: pointer; }

.tool-filters div.container-range input[type="range"]::-webkit-slider-runnable-track, .tool-filters-inputs div.container-range input[type="range"]::-webkit-slider-runnable-track { width: 100%; height: 4px; cursor: pointer; background: rgb(0, 145, 255); }

.tool-filters div.container-range h6, .tool-filters-inputs div.container-range h6 { display: inline-block; }

.tool-filters div.container-range div.label-value, .tool-filters-inputs div.container-range div.label-value { display: inline-block; float: right; }

.tool-filters button.applyFilter, .tool-filters-inputs button.applyFilter { font-weight: 600; font-size: 14px; line-height: 16px; background: rgb(0, 145, 255); color: rgb(255, 255, 255); border: none; cursor: pointer; padding: 7px 10px; }

button#open_tool_filter { position: fixed; top: 77px; left: 16px; z-index: 999999999; display: flex; background-color: rgb(0, 145, 255); height: 48px; border: none; color: rgb(255, 255, 255); padding: 0px 20px; border-radius: 24px; box-shadow: rgba(0, 0, 0, 0.24) 0px 6px 6px 0px, rgba(0, 0, 0, 0.12) 0px 0px 6px 0px; cursor: pointer; }

button#open_tool_filter i { line-height: 48px; }

button#open_tool_filter span { margin: 0px 0px 0px 12px; font-size: 12px; line-height: 48px; }

.tool-carteira-acompanhamento div#shadow_options, .tool-cotacoes-opcoes div#shadow_options { position: fixed; display: none; top: 0px; left: 0px; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); z-index: 9999; }

.tool-altas-e-baixas img#img_load_more_altas_e_baixas, .tool-altas-e-baixas img#img_load_more_cryptos_cotacoes, .tool-altas-e-baixas img#img_load_more_fatos_relevantes, .tool-altas-e-baixas img#img_load_more_opcoes_acoes, .tool-altas-e-baixas img#img_load_more_ranking_fiis, .tool-altas-e-baixas img#img_load_more_ranking_fundos, .tool-cotacoes-opcoes img#img_load_more_altas_e_baixas, .tool-cotacoes-opcoes img#img_load_more_cryptos_cotacoes, .tool-cotacoes-opcoes img#img_load_more_fatos_relevantes, .tool-cotacoes-opcoes img#img_load_more_opcoes_acoes, .tool-cotacoes-opcoes img#img_load_more_ranking_fiis, .tool-cotacoes-opcoes img#img_load_more_ranking_fundos, .tool-cryptos-cotacoes img#img_load_more_altas_e_baixas, .tool-cryptos-cotacoes img#img_load_more_cryptos_cotacoes, .tool-cryptos-cotacoes img#img_load_more_fatos_relevantes, .tool-cryptos-cotacoes img#img_load_more_opcoes_acoes, .tool-cryptos-cotacoes img#img_load_more_ranking_fiis, .tool-cryptos-cotacoes img#img_load_more_ranking_fundos, .tool-fatos-relevantes img#img_load_more_altas_e_baixas, .tool-fatos-relevantes img#img_load_more_cryptos_cotacoes, .tool-fatos-relevantes img#img_load_more_fatos_relevantes, .tool-fatos-relevantes img#img_load_more_opcoes_acoes, .tool-fatos-relevantes img#img_load_more_ranking_fiis, .tool-fatos-relevantes img#img_load_more_ranking_fundos, .tool-ranking-fundos img#img_load_more_altas_e_baixas, .tool-ranking-fundos img#img_load_more_cryptos_cotacoes, .tool-ranking-fundos img#img_load_more_fatos_relevantes, .tool-ranking-fundos img#img_load_more_opcoes_acoes, .tool-ranking-fundos img#img_load_more_ranking_fiis, .tool-ranking-fundos img#img_load_more_ranking_fundos { width: 30px; height: 30px; margin: 54px auto; display: block; }

.tool-compare-fixed-income #label_range_liquidity div, .tool-compare-fixed-income #label_range_maturity div, .tool-compare-fixed-income #label_range_minimum div, .tool-compare-fixed-income #label_range_rating div { display: none; }

.tool-compare-fixed-income #label_range_liquidity div:last-child, .tool-compare-fixed-income #label_range_maturity div:last-child, .tool-compare-fixed-income #label_range_minimum div:last-child, .tool-compare-fixed-income #label_range_rating div:last-child { display: block; }

.tool-carteira-acompanhamento h4 { font-size: 20px; line-height: 40px; letter-spacing: -0.4px; color: rgb(33, 33, 33); margin: 24px 0px; }

.tool-carteira-acompanhamento #wallets .wallet-header button { font-weight: 600; font-size: 14px; line-height: 16px; color: rgb(0, 145, 255); background: 0px 0px; border: none; cursor: pointer; }

.tool-carteira-acompanhamento #wallets #logged-with-wallet, .tool-carteira-acompanhamento #wallets #nowallet, .tool-carteira-acompanhamento #wallets #unlogged, .tool-carteira-acompanhamento #wallets button#new-wallet { display: none; }

.tool-carteira-acompanhamento #wallets #nowallet, .tool-carteira-acompanhamento #wallets #unlogged { margin: 0px 16px; padding: 40px 24px; width: calc(100% - 32px); background-color: var(--lightgray); }

.tool-carteira-acompanhamento #wallets #nowallet p, .tool-carteira-acompanhamento #wallets #unlogged p { font-weight: 600; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; color: rgb(33, 33, 33); margin: 0px; }

.tool-carteira-acompanhamento #wallets #nowallet button, .tool-carteira-acompanhamento #wallets #unlogged button { font-weight: 600; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; color: rgb(0, 145, 255); background: 0px 0px; border: none; cursor: pointer; }

.tool-carteira-acompanhamento #wallets #logged-with-wallet { margin: 0px 16px; padding: 24px; width: calc(100% - 32px); background-color: var(--lightgray); }

.tool-carteira-acompanhamento #wallets #logged-with-wallet .wallet-btns button { background: 0px 0px; border: none; color: var(--gray); cursor: pointer; }

.tool-carteira-acompanhamento #wallets #logged-with-wallet .wallet-btns button i { line-height: 54px; }

.tool-carteira-acompanhamento #wallets img#img_load_table_wallet, .tool-carteira-acompanhamento #wallets img#img_load_user_wallets { width: 30px; height: 30px; margin: 20px auto; display: none; }

.tool-carteira-acompanhamento #options-to-add { margin: 61px -16px 0px; }

.tool-carteira-acompanhamento #options-to-add #tabs-options { margin: 0px 16px; }

.tool-carteira-acompanhamento #options-to-add #tabs-options button { background: 0px 0px; border-top: none; border-right: none; border-left: none; border-image: initial; display: inline-flex; color: rgb(108, 117, 125); padding: 6px 24px 4px; border-bottom: 2px solid rgb(255, 255, 255); cursor: pointer; }

.tool-carteira-acompanhamento #options-to-add #tabs-options button i { line-height: 36px; }

.tool-carteira-acompanhamento #options-to-add #tabs-options button span { font-weight: 600; text-transform: uppercase; font-size: 12px; line-height: 36px; letter-spacing: 0.4px; margin: 0px 0px 0px 8px; }

.tool-carteira-acompanhamento #options-to-add #tabs-options button.active { color: rgb(0, 145, 255); border-bottom: 2px solid rgb(0, 145, 255); }

.tool-carteira-acompanhamento #options-to-add #container-options, .tool-carteira-acompanhamento #options-to-add #container-search { margin: 0px 16px; padding: 24px; width: calc(100% - 32px); background-color: var(--lightgray); }

.tool-carteira-acompanhamento #options-to-add #container-search { display: none; }

.tool-carteira-acompanhamento div#container_table_default i, .tool-carteira-acompanhamento div#container_table_search i, .tool-carteira-acompanhamento div#container_table_wallet i { cursor: pointer; font-size: 20px; }

.tool-carteira-acompanhamento div#container_table_wallet i { color: var(--gray); }

.tool-carteira-acompanhamento div#container_table_default i, .tool-carteira-acompanhamento div#container_table_search i { color: rgb(0, 145, 255); }

.tool-carteira-acompanhamento div#modal_options { position: fixed; display: none; top: 0px; left: 0px; width: 50%; max-height: calc(90vh); padding: 20px; margin: 5vh 25%; background-color: rgb(255, 255, 255); z-index: 99999; overflow-y: scroll; }

.tool-carteira-acompanhamento div#modal_options h5 { font-weight: 600; }

.tool-carteira-acompanhamento div#modal_options #config_cols { column-count: 2; }

.tool-carteira-acompanhamento div#modal_options #actions { margin: 30px 0px 0px; display: flex; justify-content: space-between; }

.tool-carteira-acompanhamento div.container-search { position: relative; width: 100%; }

.tool-carteira-acompanhamento div.container-search i { position: absolute; z-index: 9; line-height: 52px; color: rgb(0, 0, 0); right: 16px; }

.tool-carteira-acompanhamento div.container-search select { width: 100%; }

.tool-carteira-acompanhamento div.container-search .select2-container { border: 1px solid var(--gray); width: 100% !important; }

.tool-carteira-acompanhamento div.container-search .select2-container .select2-selection { height: 52px; }

.tool-carteira-acompanhamento div.container-search .select2-container .select2-selection .select2-selection__rendered { height: 52px; padding: 16px 54px 16px 16px; display: block; font-size: 14px; line-height: 20px; letter-spacing: -0.3px; color: var(--gray); font-weight: 400; }

.tool-carteira-acompanhamento div.container-search .select2-container .select2-selection .select2-selection__rendered .select2-selection__placeholder { color: var(--darkgray); }

.tool-carteira-acompanhamento div.container-search .select2-container .select2-selection .select2-selection__arrow { display: none; }

.tool-carteira-acompanhamento div.container-search .select2-container--default .select2-selection--single { border: none; }

.tool-carteira-acompanhamento div.container-search-input input { width: 100%; height: 52px; padding: 16px 54px 16px 16px; display: block; font-size: 14px; line-height: 20px; letter-spacing: -0.3px; color: var(--gray); font-weight: 400; }

.tool-carteira-acompanhamento #img_load_table_wallet_lock_screen { position: fixed; top: 50%; left: 50%; background-color: rgb(255, 255, 255); z-index: 9999; border-radius: 50%; width: 50px; height: 50px; padding: 5px; margin: -25px 0px 0px -25px; display: block !important; }

.tool-carteira-investimento-unlogged { margin: 0px 16px; padding: 40px 24px; width: calc(100% - 32px); background-color: var(--lightgray); }

.tool-carteira-investimento-unlogged p { font-weight: 600; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; color: rgb(33, 33, 33); margin: 0px; }

.tool-carteira-investimento-unlogged a { font-weight: 600; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; color: rgb(0, 145, 255); background: 0px 0px; border: none; cursor: pointer; }

.tool-cambio h2 { font-size: 20px; }

.tool-cambio .currencyConvert .currencyConvert__result { margin: 5px 0px; font-size: 25px; line-height: 32px; }

.tool-cambio .currencyConvert .currencyConvert__result-highlight { color: rgb(33, 153, 232); }

.tool-cambio button#swap { display: flex; background-color: rgb(0, 145, 255); border: none; color: rgb(255, 255, 255); padding: 5px; border-radius: 5px; cursor: pointer; }

.tool-cambio a.load-more-news { background-color: var(--blue); width: 100%; text-align: center; color: rgb(255, 255, 255); font-size: 14px; line-height: 1; font-weight: 600; border-radius: 2px; padding: 16px; margin: 24px auto 0px; display: block; }

.tool-agenda #dateMax, .tool-agenda button.applyFilter { margin: 0px 0px 0px 16px; }

.tool-agenda table#agendas_eventos td:nth-child(4), .tool-agenda table#agendas_eventos th:nth-child(4) { width: 50%; text-align: left; }

.tool-agenda table.default-table { min-width: 100% !important; }

.tool-inflation table.default-table { min-width: 100% !important; }

.tool-inflation table.default-table thead th { line-height: 12px; border-right: 1px solid rgba(108, 117, 125, 0.24); padding: 14px 16px; }

.tool-inflation table.default-table thead th:last-child { border-right: 0px; }

.tool-inflation table.default-table thead th.sorting { background-image: url("/wp-content/themes/infomoney/assets/img/arrow_both.webp"); background-position: right center; }

.tool-inflation table.default-table thead th.sorting_asc { background-image: url("/wp-content/themes/infomoney/assets/img/arrow_up.webp"); background-position: right center; }

.tool-inflation table.default-table thead th.sorting_desc { background-image: url("/wp-content/themes/infomoney/assets/img/arrow_down.webp"); background-position: right center; }

.tool-inflation table.default-table td, .tool-inflation table.default-table th { text-align: left; padding: 16px; }

.tool-inflation table.default-table tbody tr td:nth-child(1) { font-weight: 600; min-width: 110px; }

.tool-inflation table.default-table tbody td i { font-size: 14px; display: flex; justify-content: center; color: rgb(102, 102, 102); }

.tool-inflation table.default-table img { width: 70px; }

.tool-cryptos-cotacoes .tool-filters, .tool-ranking-fundos .tool-filters { padding: 32px; }

.tool-cryptos-cotacoes .update-export #last-update, .tool-ranking-fundos .update-export #last-update { font-size: 11px; line-height: 16px; }

.tool-cryptos-cotacoes div.container-search, .tool-ranking-fundos div.container-search { background-color: rgb(255, 255, 255); }

.tool-cryptos-cotacoes div.container-search i, .tool-ranking-fundos div.container-search i { line-height: 38px; right: 7px; color: rgb(102, 102, 102); z-index: 0; }

.tool-cryptos-cotacoes div.container-search .select2-container, .tool-ranking-fundos div.container-search .select2-container { border: 1px solid rgb(170, 170, 170); }

.tool-cryptos-cotacoes div.container-search .select2-container .select2-selection, .tool-ranking-fundos div.container-search .select2-container .select2-selection { height: 36px; background: 0px 0px; }

.tool-cryptos-cotacoes div.container-search .select2-container .select2-selection .select2-selection__rendered, .tool-ranking-fundos div.container-search .select2-container .select2-selection .select2-selection__rendered { height: 36px; padding: 9px 12px; font-size: 13px; line-height: 20px; letter-spacing: 0px; color: rgb(102, 102, 102); }

.tool-cryptos-cotacoes div.container-search .select2-container .select2-selection .select2-selection__rendered .select2-selection__placeholder, .tool-ranking-fundos div.container-search .select2-container .select2-selection .select2-selection__rendered .select2-selection__placeholder { color: rgb(102, 102, 102); }

.tool-cryptos-cotacoes .risk-legend, .tool-ranking-fundos .risk-legend { display: flex; font-size: 12px; line-height: 16px; }

.tool-cryptos-cotacoes .risk-legend p, .tool-ranking-fundos .risk-legend p { display: flex; }

.tool-cryptos-cotacoes .risk-legend .high-risk, .tool-cryptos-cotacoes .risk-legend .low-risk, .tool-cryptos-cotacoes .risk-legend .medium-risk, .tool-ranking-fundos .risk-legend .high-risk, .tool-ranking-fundos .risk-legend .low-risk, .tool-ranking-fundos .risk-legend .medium-risk { width: 16px; height: 16px; }

.tool-cryptos-cotacoes .risk-text, .tool-ranking-fundos .risk-text { font-size: 12px; line-height: 16px; }

.tool-cryptos-cotacoes .risk-text a, .tool-ranking-fundos .risk-text a { color: rgb(0, 0, 0); text-decoration: underline; }

.tool-cryptos-cotacoes .high-risk, .tool-cryptos-cotacoes .low-risk, .tool-cryptos-cotacoes .medium-risk, .tool-ranking-fundos .high-risk, .tool-ranking-fundos .low-risk, .tool-ranking-fundos .medium-risk { height: 24px; width: 32px; padding: 2px 0px; color: rgb(255, 255, 255); display: block; text-align: center; }

.tool-cryptos-cotacoes .low-risk, .tool-ranking-fundos .low-risk { background: rgb(224, 173, 0); }

.tool-cryptos-cotacoes .medium-risk, .tool-ranking-fundos .medium-risk { background: rgb(215, 123, 10); }

.tool-cryptos-cotacoes .high-risk, .tool-ranking-fundos .high-risk { background: rgb(204, 51, 51); }

.tool-cryptos-cotacoes div.container-search-input, .tool-ranking-fundos div.container-search-input { position: relative; }

.tool-cryptos-cotacoes div.container-search-input i, .tool-ranking-fundos div.container-search-input i { position: absolute; z-index: 7; line-height: 36px; color: rgb(102, 102, 102); right: 7px; }

.tool-cryptos-cotacoes div.container-search-input input, .tool-ranking-fundos div.container-search-input input { width: 100%; height: 36px; padding: 9px 12px; display: block; font-size: 13px; line-height: 20px; color: rgb(102, 102, 102); }

.tool-cryptos-cotacoes table#ranking_fiis th:nth-child(2), .tool-ranking-fundos table#ranking_fiis th:nth-child(2) { min-width: 50px; }

.tool-cryptos-cotacoes table.default-table, .tool-ranking-fundos table.default-table { min-width: 100% !important; }

.tool-cryptos-cotacoes table.default-table thead th, .tool-ranking-fundos table.default-table thead th { line-height: 12px; border-right: 1px solid rgba(108, 117, 125, 0.24); padding: 14px 16px; }

.tool-cryptos-cotacoes table.default-table thead th:nth-child(2), .tool-ranking-fundos table.default-table thead th:nth-child(2) { min-width: 250px; }

.tool-cryptos-cotacoes table.default-table thead th:last-child, .tool-ranking-fundos table.default-table thead th:last-child { border-right: 0px; }

.tool-cryptos-cotacoes table.default-table thead th.sorting, .tool-ranking-fundos table.default-table thead th.sorting { background-image: url("/wp-content/themes/infomoney/assets/img/arrow_both.webp"); background-position: right center; }

.tool-cryptos-cotacoes table.default-table thead th.sorting:first-child, .tool-cryptos-cotacoes table.default-table thead th.sorting:last-child, .tool-ranking-fundos table.default-table thead th.sorting:first-child, .tool-ranking-fundos table.default-table thead th.sorting:last-child { background-image: none; }

.tool-cryptos-cotacoes table.default-table thead th.sorting_asc, .tool-ranking-fundos table.default-table thead th.sorting_asc { background-image: url("/wp-content/themes/infomoney/assets/img/arrow_up.webp"); background-position: right center; }

.tool-cryptos-cotacoes table.default-table thead th.sorting_desc, .tool-ranking-fundos table.default-table thead th.sorting_desc { background-image: url("/wp-content/themes/infomoney/assets/img/arrow_down.webp"); background-position: right center; }

.tool-cryptos-cotacoes table.default-table td, .tool-cryptos-cotacoes table.default-table th, .tool-ranking-fundos table.default-table td, .tool-ranking-fundos table.default-table th { text-align: left; padding: 16px; }

.tool-cryptos-cotacoes table.default-table tbody tr td:nth-child(1), .tool-cryptos-cotacoes table.default-table tbody tr td:nth-child(2), .tool-ranking-fundos table.default-table tbody tr td:nth-child(1), .tool-ranking-fundos table.default-table tbody tr td:nth-child(2) { font-weight: 600; }

.tool-cryptos-cotacoes table.default-table tbody td i, .tool-ranking-fundos table.default-table tbody td i { font-size: 14px; display: flex; justify-content: center; color: rgb(102, 102, 102); }

.tool-cryptos-cotacoes table.default-table tbody td:nth-child(4), .tool-ranking-fundos table.default-table tbody td:nth-child(4) { min-width: 90px; }

.tool-cryptos-cotacoes table.default-table img, .tool-ranking-fundos table.default-table img { width: 70px; }

.tool-altas-e-baixas table.default-table { min-width: 100% !important; }

.tool-altas-e-baixas .tool-filters { padding: 0px; }

.tool-altas-e-baixas .tool-filters div.container-search .select2-container { border-top: none; border-right: none; border-left: none; border-image: initial; border-bottom: 1px solid rgb(108, 117, 125); }

.tool-altas-e-baixas .tool-filters div.container-search .select2-container .select2-selection__arrow { display: block; }

.tool-altas-e-baixas .tool-filters div.container-search .select2-container .select2-selection__arrow b { top: 100%; left: -30%; }

.tool-altas-e-baixas .tool-filters .select2-container--default .select2-selection--single { border-radius: 0px; }

.tool-altas-e-baixas .tool-filters-mobile { background-color: var(--lightgray); padding: 40px 0px; margin: 0px; }

.tool-altas-e-baixas .tool-filters-mobile .button-filter-mobile { background: rgb(0, 145, 255); width: 48px; height: 48px; cursor: pointer; }

.tool-altas-e-baixas .tool-filters-mobile .button-filter-mobile i { margin: 0px auto; color: rgb(255, 255, 255); }

.tool-altas-e-baixas button#apply-filters, .tool-altas-e-baixas button#apply-filters-mobile { padding: 0px; height: 54px; width: 130px; }

.tool-altas-e-baixas .export_data_table { cursor: pointer; }

.tool-altas-e-baixas .export_data_table i { font-size: 20px; color: rgb(0, 0, 0); font-weight: 100; cursor: pointer; }

button#apply-filters, button#apply-filters-mobile { font-weight: 600; font-size: 14px; line-height: 16px; background: rgb(0, 145, 255); color: rgb(255, 255, 255); border: none; cursor: pointer; padding: 14px 16px; height: 44px; }

@media screen and (min-width: 992px) {
  .tool-altas-e-baixas .tool-filters { display: flex !important; }
}

@media screen and (max-width: 991px) {
  .tool-cryptos-cotacoes table#cryptos_cotacoes th { min-width: 120px; }
  .tool-filters { padding: 0px 0px 32px; }
  .tool-filters .row:not(:first-child) { margin-top: 0px; }
  .tool-filters .col-12 { margin: 32px 0px 0px; }
  .tool-carteira-acompanhamento div#modal_options { width: 90%; height: 90%; margin: 5%; top: 0px; }
  .tool-agenda #dateMax, .tool-agenda button.applyFilter { margin: 16px 0px 0px; }
  .tool-ranking-fundos .tool-filters { padding: 32px 0px; }
  .tool-ranking-fundos .tool-filters .col-12 { margin: 0px; }
  .tool-ranking-fundos .tool-filters .filter-container.col-12:not(:first-child) { margin: 16px 0px 0px; }
  .tool-ranking-fundos .risk-legend { display: block; }
  .tool-altas-e-baixas .tool-filters { position: fixed; z-index: 100; height: 100vh; top: 0px; left: 0px; width: 100vw; animation: 0.5s ease 0s 1 normal none running fadein; padding-top: 100px !important; }
  .tool-altas-e-baixas .tool-filters .container-search { margin-bottom: 0.5rem !important; }
  .tool-altas-e-baixas .tool-filters .close { position: fixed; top: 0px; right: 0px; }
  .tool-altas-e-baixas .tool-filters .close i { color: rgb(0, 0, 0); }
}
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css?ver=6.1.1

@charset "utf-8";

table.dataTable { width: 100%; margin: 0px auto; clear: both; border-collapse: separate; border-spacing: 0px; }

table.dataTable thead th, table.dataTable tfoot th { font-weight: bold; }

table.dataTable thead th, table.dataTable thead td { padding: 10px 18px; border-bottom: 1px solid rgb(17, 17, 17); }

table.dataTable thead th:active, table.dataTable thead td:active { outline: none; }

table.dataTable tfoot th, table.dataTable tfoot td { padding: 10px 18px 6px; border-top: 1px solid rgb(17, 17, 17); }

table.dataTable thead .sorting, table.dataTable thead .sorting_asc, table.dataTable thead .sorting_desc, table.dataTable thead .sorting_asc_disabled, table.dataTable thead .sorting_desc_disabled { cursor: pointer; background-repeat: no-repeat; background-position: right center; }

table.dataTable thead .sorting { background-image: url("../images/sort_both.png"); }

table.dataTable thead .sorting_asc { background-image: url("../images/sort_asc.png"); }

table.dataTable thead .sorting_desc { background-image: url("../images/sort_desc.png"); }

table.dataTable thead .sorting_asc_disabled { background-image: url("../images/sort_asc_disabled.png"); }

table.dataTable thead .sorting_desc_disabled { background-image: url("../images/sort_desc_disabled.png"); }

table.dataTable tbody tr { background-color: rgb(255, 255, 255); }

table.dataTable tbody tr.selected { background-color: rgb(176, 190, 217); }

table.dataTable tbody th, table.dataTable tbody td { padding: 8px 10px; }

table.dataTable.row-border tbody th, table.dataTable.row-border tbody td, table.dataTable.display tbody th, table.dataTable.display tbody td { border-top: 1px solid rgb(221, 221, 221); }

table.dataTable.row-border tbody tr:first-child th, table.dataTable.row-border tbody tr:first-child td, table.dataTable.display tbody tr:first-child th, table.dataTable.display tbody tr:first-child td { border-top: none; }

table.dataTable.cell-border tbody th, table.dataTable.cell-border tbody td { border-top: 1px solid rgb(221, 221, 221); border-right: 1px solid rgb(221, 221, 221); }

table.dataTable.cell-border tbody tr th:first-child, table.dataTable.cell-border tbody tr td:first-child { border-left: 1px solid rgb(221, 221, 221); }

table.dataTable.cell-border tbody tr:first-child th, table.dataTable.cell-border tbody tr:first-child td { border-top: none; }

table.dataTable.stripe tbody tr.odd, table.dataTable.display tbody tr.odd { background-color: rgb(249, 249, 249); }

table.dataTable.stripe tbody tr.odd.selected, table.dataTable.display tbody tr.odd.selected { background-color: rgb(172, 186, 212); }

table.dataTable.hover tbody tr:hover, table.dataTable.display tbody tr:hover { background-color: rgb(246, 246, 246); }

table.dataTable.hover tbody tr:hover.selected, table.dataTable.display tbody tr:hover.selected { background-color: rgb(170, 183, 209); }

table.dataTable.order-column tbody tr > .sorting_1, table.dataTable.order-column tbody tr > .sorting_2, table.dataTable.order-column tbody tr > .sorting_3, table.dataTable.display tbody tr > .sorting_1, table.dataTable.display tbody tr > .sorting_2, table.dataTable.display tbody tr > .sorting_3 { background-color: rgb(250, 250, 250); }

table.dataTable.order-column tbody tr.selected > .sorting_1, table.dataTable.order-column tbody tr.selected > .sorting_2, table.dataTable.order-column tbody tr.selected > .sorting_3, table.dataTable.display tbody tr.selected > .sorting_1, table.dataTable.display tbody tr.selected > .sorting_2, table.dataTable.display tbody tr.selected > .sorting_3 { background-color: rgb(172, 186, 213); }

table.dataTable.display tbody tr.odd > .sorting_1, table.dataTable.order-column.stripe tbody tr.odd > .sorting_1 { background-color: rgb(241, 241, 241); }

table.dataTable.display tbody tr.odd > .sorting_2, table.dataTable.order-column.stripe tbody tr.odd > .sorting_2 { background-color: rgb(243, 243, 243); }

table.dataTable.display tbody tr.odd > .sorting_3, table.dataTable.order-column.stripe tbody tr.odd > .sorting_3 { background-color: whitesmoke; }

table.dataTable.display tbody tr.odd.selected > .sorting_1, table.dataTable.order-column.stripe tbody tr.odd.selected > .sorting_1 { background-color: rgb(166, 180, 205); }

table.dataTable.display tbody tr.odd.selected > .sorting_2, table.dataTable.order-column.stripe tbody tr.odd.selected > .sorting_2 { background-color: rgb(168, 181, 207); }

table.dataTable.display tbody tr.odd.selected > .sorting_3, table.dataTable.order-column.stripe tbody tr.odd.selected > .sorting_3 { background-color: rgb(169, 183, 209); }

table.dataTable.display tbody tr.even > .sorting_1, table.dataTable.order-column.stripe tbody tr.even > .sorting_1 { background-color: rgb(250, 250, 250); }

table.dataTable.display tbody tr.even > .sorting_2, table.dataTable.order-column.stripe tbody tr.even > .sorting_2 { background-color: rgb(252, 252, 252); }

table.dataTable.display tbody tr.even > .sorting_3, table.dataTable.order-column.stripe tbody tr.even > .sorting_3 { background-color: rgb(254, 254, 254); }

table.dataTable.display tbody tr.even.selected > .sorting_1, table.dataTable.order-column.stripe tbody tr.even.selected > .sorting_1 { background-color: rgb(172, 186, 213); }

table.dataTable.display tbody tr.even.selected > .sorting_2, table.dataTable.order-column.stripe tbody tr.even.selected > .sorting_2 { background-color: rgb(174, 188, 214); }

table.dataTable.display tbody tr.even.selected > .sorting_3, table.dataTable.order-column.stripe tbody tr.even.selected > .sorting_3 { background-color: rgb(175, 189, 216); }

table.dataTable.display tbody tr:hover > .sorting_1, table.dataTable.order-column.hover tbody tr:hover > .sorting_1 { background-color: rgb(234, 234, 234); }

table.dataTable.display tbody tr:hover > .sorting_2, table.dataTable.order-column.hover tbody tr:hover > .sorting_2 { background-color: rgb(236, 236, 236); }

table.dataTable.display tbody tr:hover > .sorting_3, table.dataTable.order-column.hover tbody tr:hover > .sorting_3 { background-color: rgb(239, 239, 239); }

table.dataTable.display tbody tr:hover.selected > .sorting_1, table.dataTable.order-column.hover tbody tr:hover.selected > .sorting_1 { background-color: rgb(162, 174, 199); }

table.dataTable.display tbody tr:hover.selected > .sorting_2, table.dataTable.order-column.hover tbody tr:hover.selected > .sorting_2 { background-color: rgb(163, 176, 201); }

table.dataTable.display tbody tr:hover.selected > .sorting_3, table.dataTable.order-column.hover tbody tr:hover.selected > .sorting_3 { background-color: rgb(165, 178, 203); }

table.dataTable.no-footer { border-bottom: 1px solid rgb(17, 17, 17); }

table.dataTable.nowrap th, table.dataTable.nowrap td { white-space: nowrap; }

table.dataTable.compact thead th, table.dataTable.compact thead td { padding: 4px 17px 4px 4px; }

table.dataTable.compact tfoot th, table.dataTable.compact tfoot td { padding: 4px; }

table.dataTable.compact tbody th, table.dataTable.compact tbody td { padding: 4px; }

table.dataTable th.dt-left, table.dataTable td.dt-left { text-align: left; }

table.dataTable th.dt-center, table.dataTable td.dt-center, table.dataTable td.dataTables_empty { text-align: center; }

table.dataTable th.dt-right, table.dataTable td.dt-right { text-align: right; }

table.dataTable th.dt-justify, table.dataTable td.dt-justify { text-align: justify; }

table.dataTable th.dt-nowrap, table.dataTable td.dt-nowrap { white-space: nowrap; }

table.dataTable thead th.dt-head-left, table.dataTable thead td.dt-head-left, table.dataTable tfoot th.dt-head-left, table.dataTable tfoot td.dt-head-left { text-align: left; }

table.dataTable thead th.dt-head-center, table.dataTable thead td.dt-head-center, table.dataTable tfoot th.dt-head-center, table.dataTable tfoot td.dt-head-center { text-align: center; }

table.dataTable thead th.dt-head-right, table.dataTable thead td.dt-head-right, table.dataTable tfoot th.dt-head-right, table.dataTable tfoot td.dt-head-right { text-align: right; }

table.dataTable thead th.dt-head-justify, table.dataTable thead td.dt-head-justify, table.dataTable tfoot th.dt-head-justify, table.dataTable tfoot td.dt-head-justify { text-align: justify; }

table.dataTable thead th.dt-head-nowrap, table.dataTable thead td.dt-head-nowrap, table.dataTable tfoot th.dt-head-nowrap, table.dataTable tfoot td.dt-head-nowrap { white-space: nowrap; }

table.dataTable tbody th.dt-body-left, table.dataTable tbody td.dt-body-left { text-align: left; }

table.dataTable tbody th.dt-body-center, table.dataTable tbody td.dt-body-center { text-align: center; }

table.dataTable tbody th.dt-body-right, table.dataTable tbody td.dt-body-right { text-align: right; }

table.dataTable tbody th.dt-body-justify, table.dataTable tbody td.dt-body-justify { text-align: justify; }

table.dataTable tbody th.dt-body-nowrap, table.dataTable tbody td.dt-body-nowrap { white-space: nowrap; }

table.dataTable, table.dataTable th, table.dataTable td { box-sizing: content-box; }

.dataTables_wrapper { position: relative; clear: both; zoom: 1; }

.dataTables_wrapper .dataTables_length { float: left; }

.dataTables_wrapper .dataTables_filter { float: right; text-align: right; }

.dataTables_wrapper .dataTables_filter input { margin-left: 0.5em; }

.dataTables_wrapper .dataTables_info { clear: both; float: left; padding-top: 0.755em; }

.dataTables_wrapper .dataTables_paginate { float: right; text-align: right; padding-top: 0.25em; }

.dataTables_wrapper .dataTables_paginate .paginate_button { box-sizing: border-box; display: inline-block; min-width: 1.5em; padding: 0.5em 1em; margin-left: 2px; text-align: center; cursor: pointer; border: 1px solid transparent; border-radius: 2px; text-decoration: none !important; color: rgb(51, 51, 51) !important; }

.dataTables_wrapper .dataTables_paginate .paginate_button.current, .dataTables_wrapper .dataTables_paginate .paginate_button.current:hover { border: 1px solid rgb(151, 151, 151); background: linear-gradient(rgb(255, 255, 255) 0%, rgb(220, 220, 220) 100%); color: rgb(51, 51, 51) !important; }

.dataTables_wrapper .dataTables_paginate .paginate_button.disabled, .dataTables_wrapper .dataTables_paginate .paginate_button.disabled:hover, .dataTables_wrapper .dataTables_paginate .paginate_button.disabled:active { cursor: default; border: 1px solid transparent; background: transparent; box-shadow: none; color: rgb(102, 102, 102) !important; }

.dataTables_wrapper .dataTables_paginate .paginate_button:hover { border: 1px solid rgb(17, 17, 17); background: linear-gradient(rgb(88, 88, 88) 0%, rgb(17, 17, 17) 100%); color: white !important; }

.dataTables_wrapper .dataTables_paginate .paginate_button:active { outline: none; background: linear-gradient(rgb(43, 43, 43) 0%, rgb(12, 12, 12) 100%); box-shadow: rgb(17, 17, 17) 0px 0px 3px inset; }

.dataTables_wrapper .dataTables_paginate .ellipsis { padding: 0px 1em; }

.dataTables_wrapper .dataTables_processing { position: absolute; top: 50%; left: 50%; width: 100%; height: 40px; margin-left: -50%; margin-top: -25px; padding-top: 20px; text-align: center; font-size: 1.2em; background: linear-gradient(to right, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.9) 25%, rgba(255, 255, 255, 0.9) 75%, rgba(255, 255, 255, 0) 100%); }

.dataTables_wrapper .dataTables_length, .dataTables_wrapper .dataTables_filter, .dataTables_wrapper .dataTables_info, .dataTables_wrapper .dataTables_processing, .dataTables_wrapper .dataTables_paginate { color: rgb(51, 51, 51); }

.dataTables_wrapper .dataTables_scroll { clear: both; }

.dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody { }

.dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > thead > tr > th, .dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > thead > tr > td, .dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > tbody > tr > th, .dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > tbody > tr > td { vertical-align: middle; }

.dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > thead > tr > th > div.dataTables_sizing, .dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > thead > tr > td > div.dataTables_sizing, .dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > tbody > tr > th > div.dataTables_sizing, .dataTables_wrapper .dataTables_scroll div.dataTables_scrollBody > table > tbody > tr > td > div.dataTables_sizing { height: 0px; overflow: hidden; margin: 0px !important; padding: 0px !important; }

.dataTables_wrapper.no-footer .dataTables_scrollBody { border-bottom: 1px solid rgb(17, 17, 17); }

.dataTables_wrapper.no-footer div.dataTables_scrollHead table.dataTable, .dataTables_wrapper.no-footer div.dataTables_scrollBody > table { border-bottom: none; }

.dataTables_wrapper::after { visibility: hidden; display: block; content: ""; clear: both; height: 0px; }

@media screen and (max-width: 767px) {
  .dataTables_wrapper .dataTables_info, .dataTables_wrapper .dataTables_paginate { float: none; text-align: center; }
  .dataTables_wrapper .dataTables_paginate { margin-top: 0.5em; }
}

@media screen and (max-width: 640px) {
  .dataTables_wrapper .dataTables_length, .dataTables_wrapper .dataTables_filter { float: none; text-align: center; }
  .dataTables_wrapper .dataTables_filter { margin-top: 0.5em; }
}
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.7/css/select2.min.css?ver=6.1.1

@charset "utf-8";

.select2-container { box-sizing: border-box; display: inline-block; margin: 0px; position: relative; vertical-align: middle; }

.select2-container .select2-selection--single { box-sizing: border-box; cursor: pointer; display: block; height: 28px; user-select: none; }

.select2-container .select2-selection--single .select2-selection__rendered { display: block; padding-left: 8px; padding-right: 20px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.select2-container .select2-selection--single .select2-selection__clear { position: relative; }

.select2-container[dir="rtl"] .select2-selection--single .select2-selection__rendered { padding-right: 8px; padding-left: 20px; }

.select2-container .select2-selection--multiple { box-sizing: border-box; cursor: pointer; display: block; min-height: 32px; user-select: none; }

.select2-container .select2-selection--multiple .select2-selection__rendered { display: inline-block; overflow: hidden; padding-left: 8px; text-overflow: ellipsis; white-space: nowrap; }

.select2-container .select2-search--inline { float: left; }

.select2-container .select2-search--inline .select2-search__field { box-sizing: border-box; border: none; font-size: 100%; margin-top: 5px; padding: 0px; }

.select2-container .select2-search--inline .select2-search__field::-webkit-search-cancel-button { -webkit-appearance: none; }

.select2-dropdown { background-color: white; border: 1px solid rgb(170, 170, 170); border-radius: 4px; box-sizing: border-box; display: block; position: absolute; left: -100000px; width: 100%; z-index: 1051; }

.select2-results { display: block; }

.select2-results__options { list-style: none; margin: 0px; padding: 0px; }

.select2-results__option { padding: 6px; user-select: none; }

.select2-results__option[aria-selected] { cursor: pointer; }

.select2-container--open .select2-dropdown { left: 0px; }

.select2-container--open .select2-dropdown--above { border-bottom: none; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; }

.select2-container--open .select2-dropdown--below { border-top: none; border-top-left-radius: 0px; border-top-right-radius: 0px; }

.select2-search--dropdown { display: block; padding: 4px; }

.select2-search--dropdown .select2-search__field { padding: 4px; width: 100%; box-sizing: border-box; }

.select2-search--dropdown .select2-search__field::-webkit-search-cancel-button { -webkit-appearance: none; }

.select2-search--dropdown.select2-search--hide { display: none; }

.select2-close-mask { border: 0px; margin: 0px; padding: 0px; display: block; position: fixed; left: 0px; top: 0px; min-height: 100%; min-width: 100%; height: auto; width: auto; opacity: 0; z-index: 99; background-color: rgb(255, 255, 255); }

.select2-hidden-accessible { border: 0px !important; clip: rect(0px, 0px, 0px, 0px) !important; clip-path: inset(50%) !important; height: 1px !important; overflow: hidden !important; padding: 0px !important; position: absolute !important; width: 1px !important; white-space: nowrap !important; }

.select2-container--default .select2-selection--single { background-color: rgb(255, 255, 255); border: 1px solid rgb(170, 170, 170); border-radius: 4px; }

.select2-container--default .select2-selection--single .select2-selection__rendered { color: rgb(68, 68, 68); line-height: 28px; }

.select2-container--default .select2-selection--single .select2-selection__clear { cursor: pointer; float: right; font-weight: bold; }

.select2-container--default .select2-selection--single .select2-selection__placeholder { color: rgb(153, 153, 153); }

.select2-container--default .select2-selection--single .select2-selection__arrow { height: 26px; position: absolute; top: 1px; right: 1px; width: 20px; }

.select2-container--default .select2-selection--single .select2-selection__arrow b { border-color: rgb(136, 136, 136) transparent transparent; border-style: solid; border-width: 5px 4px 0px; height: 0px; left: 50%; margin-left: -4px; margin-top: -2px; position: absolute; top: 50%; width: 0px; }

.select2-container--default[dir="rtl"] .select2-selection--single .select2-selection__clear { float: left; }

.select2-container--default[dir="rtl"] .select2-selection--single .select2-selection__arrow { left: 1px; right: auto; }

.select2-container--default.select2-container--disabled .select2-selection--single { background-color: rgb(238, 238, 238); cursor: default; }

.select2-container--default.select2-container--disabled .select2-selection--single .select2-selection__clear { display: none; }

.select2-container--default.select2-container--open .select2-selection--single .select2-selection__arrow b { border-color: transparent transparent rgb(136, 136, 136); border-width: 0px 4px 5px; }

.select2-container--default .select2-selection--multiple { background-color: white; border: 1px solid rgb(170, 170, 170); border-radius: 4px; cursor: text; }

.select2-container--default .select2-selection--multiple .select2-selection__rendered { box-sizing: border-box; list-style: none; margin: 0px; padding: 0px 5px; width: 100%; }

.select2-container--default .select2-selection--multiple .select2-selection__rendered li { list-style: none; }

.select2-container--default .select2-selection--multiple .select2-selection__placeholder { color: rgb(153, 153, 153); margin-top: 5px; float: left; }

.select2-container--default .select2-selection--multiple .select2-selection__clear { cursor: pointer; float: right; font-weight: bold; margin-top: 5px; margin-right: 10px; }

.select2-container--default .select2-selection--multiple .select2-selection__choice { background-color: rgb(228, 228, 228); border: 1px solid rgb(170, 170, 170); border-radius: 4px; cursor: default; float: left; margin-right: 5px; margin-top: 5px; padding: 0px 5px; }

.select2-container--default .select2-selection--multiple .select2-selection__choice__remove { color: rgb(153, 153, 153); cursor: pointer; display: inline-block; font-weight: bold; margin-right: 2px; }

.select2-container--default .select2-selection--multiple .select2-selection__choice__remove:hover { color: rgb(51, 51, 51); }

.select2-container--default[dir="rtl"] .select2-selection--multiple .select2-selection__choice, .select2-container--default[dir="rtl"] .select2-selection--multiple .select2-selection__placeholder, .select2-container--default[dir="rtl"] .select2-selection--multiple .select2-search--inline { float: right; }

.select2-container--default[dir="rtl"] .select2-selection--multiple .select2-selection__choice { margin-left: 5px; margin-right: auto; }

.select2-container--default[dir="rtl"] .select2-selection--multiple .select2-selection__choice__remove { margin-left: 2px; margin-right: auto; }

.select2-container--default.select2-container--focus .select2-selection--multiple { border: 1px solid black; outline: 0px; }

.select2-container--default.select2-container--disabled .select2-selection--multiple { background-color: rgb(238, 238, 238); cursor: default; }

.select2-container--default.select2-container--disabled .select2-selection__choice__remove { display: none; }

.select2-container--default.select2-container--open.select2-container--above .select2-selection--single, .select2-container--default.select2-container--open.select2-container--above .select2-selection--multiple { border-top-left-radius: 0px; border-top-right-radius: 0px; }

.select2-container--default.select2-container--open.select2-container--below .select2-selection--single, .select2-container--default.select2-container--open.select2-container--below .select2-selection--multiple { border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; }

.select2-container--default .select2-search--dropdown .select2-search__field { border: 1px solid rgb(170, 170, 170); }

.select2-container--default .select2-search--inline .select2-search__field { background: transparent; border: none; outline: 0px; box-shadow: none; -webkit-appearance: textfield; }

.select2-container--default .select2-results > .select2-results__options { max-height: 200px; overflow-y: auto; }

.select2-container--default .select2-results__option[role="group"] { padding: 0px; }

.select2-container--default .select2-results__option[aria-disabled="true"] { color: rgb(153, 153, 153); }

.select2-container--default .select2-results__option[aria-selected="true"] { background-color: rgb(221, 221, 221); }

.select2-container--default .select2-results__option .select2-results__option { padding-left: 1em; }

.select2-container--default .select2-results__option .select2-results__option .select2-results__group { padding-left: 0px; }

.select2-container--default .select2-results__option .select2-results__option .select2-results__option { margin-left: -1em; padding-left: 2em; }

.select2-container--default .select2-results__option .select2-results__option .select2-results__option .select2-results__option { margin-left: -2em; padding-left: 3em; }

.select2-container--default .select2-results__option .select2-results__option .select2-results__option .select2-results__option .select2-results__option { margin-left: -3em; padding-left: 4em; }

.select2-container--default .select2-results__option .select2-results__option .select2-results__option .select2-results__option .select2-results__option .select2-results__option { margin-left: -4em; padding-left: 5em; }

.select2-container--default .select2-results__option .select2-results__option .select2-results__option .select2-results__option .select2-results__option .select2-results__option .select2-results__option { margin-left: -5em; padding-left: 6em; }

.select2-container--default .select2-results__option--highlighted[aria-selected] { background-color: rgb(88, 151, 251); color: white; }

.select2-container--default .select2-results__group { cursor: default; display: block; padding: 6px; }

.select2-container--classic .select2-selection--single { background-color: rgb(247, 247, 247); border: 1px solid rgb(170, 170, 170); border-radius: 4px; outline: 0px; background-image: linear-gradient(rgb(255, 255, 255) 50%, rgb(238, 238, 238) 100%); background-repeat: repeat-x; }

.select2-container--classic .select2-selection--single:focus { border: 1px solid rgb(88, 151, 251); }

.select2-container--classic .select2-selection--single .select2-selection__rendered { color: rgb(68, 68, 68); line-height: 28px; }

.select2-container--classic .select2-selection--single .select2-selection__clear { cursor: pointer; float: right; font-weight: bold; margin-right: 10px; }

.select2-container--classic .select2-selection--single .select2-selection__placeholder { color: rgb(153, 153, 153); }

.select2-container--classic .select2-selection--single .select2-selection__arrow { background-color: rgb(221, 221, 221); border-top: none; border-right: none; border-bottom: none; border-image: initial; border-left: 1px solid rgb(170, 170, 170); border-top-right-radius: 4px; border-bottom-right-radius: 4px; height: 26px; position: absolute; top: 1px; right: 1px; width: 20px; background-image: linear-gradient(rgb(238, 238, 238) 50%, rgb(204, 204, 204) 100%); background-repeat: repeat-x; }

.select2-container--classic .select2-selection--single .select2-selection__arrow b { border-color: rgb(136, 136, 136) transparent transparent; border-style: solid; border-width: 5px 4px 0px; height: 0px; left: 50%; margin-left: -4px; margin-top: -2px; position: absolute; top: 50%; width: 0px; }

.select2-container--classic[dir="rtl"] .select2-selection--single .select2-selection__clear { float: left; }

.select2-container--classic[dir="rtl"] .select2-selection--single .select2-selection__arrow { border-top: none; border-bottom: none; border-left: none; border-image: initial; border-right: 1px solid rgb(170, 170, 170); border-radius: 4px 0px 0px 4px; left: 1px; right: auto; }

.select2-container--classic.select2-container--open .select2-selection--single { border: 1px solid rgb(88, 151, 251); }

.select2-container--classic.select2-container--open .select2-selection--single .select2-selection__arrow { background: transparent; border: none; }

.select2-container--classic.select2-container--open .select2-selection--single .select2-selection__arrow b { border-color: transparent transparent rgb(136, 136, 136); border-width: 0px 4px 5px; }

.select2-container--classic.select2-container--open.select2-container--above .select2-selection--single { border-top: none; border-top-left-radius: 0px; border-top-right-radius: 0px; background-image: linear-gradient(rgb(255, 255, 255) 0%, rgb(238, 238, 238) 50%); background-repeat: repeat-x; }

.select2-container--classic.select2-container--open.select2-container--below .select2-selection--single { border-bottom: none; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; background-image: linear-gradient(rgb(238, 238, 238) 50%, rgb(255, 255, 255) 100%); background-repeat: repeat-x; }

.select2-container--classic .select2-selection--multiple { background-color: white; border: 1px solid rgb(170, 170, 170); border-radius: 4px; cursor: text; outline: 0px; }

.select2-container--classic .select2-selection--multiple:focus { border: 1px solid rgb(88, 151, 251); }

.select2-container--classic .select2-selection--multiple .select2-selection__rendered { list-style: none; margin: 0px; padding: 0px 5px; }

.select2-container--classic .select2-selection--multiple .select2-selection__clear { display: none; }

.select2-container--classic .select2-selection--multiple .select2-selection__choice { background-color: rgb(228, 228, 228); border: 1px solid rgb(170, 170, 170); border-radius: 4px; cursor: default; float: left; margin-right: 5px; margin-top: 5px; padding: 0px 5px; }

.select2-container--classic .select2-selection--multiple .select2-selection__choice__remove { color: rgb(136, 136, 136); cursor: pointer; display: inline-block; font-weight: bold; margin-right: 2px; }

.select2-container--classic .select2-selection--multiple .select2-selection__choice__remove:hover { color: rgb(85, 85, 85); }

.select2-container--classic[dir="rtl"] .select2-selection--multiple .select2-selection__choice { float: right; margin-left: 5px; margin-right: auto; }

.select2-container--classic[dir="rtl"] .select2-selection--multiple .select2-selection__choice__remove { margin-left: 2px; margin-right: auto; }

.select2-container--classic.select2-container--open .select2-selection--multiple { border: 1px solid rgb(88, 151, 251); }

.select2-container--classic.select2-container--open.select2-container--above .select2-selection--multiple { border-top: none; border-top-left-radius: 0px; border-top-right-radius: 0px; }

.select2-container--classic.select2-container--open.select2-container--below .select2-selection--multiple { border-bottom: none; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; }

.select2-container--classic .select2-search--dropdown .select2-search__field { border: 1px solid rgb(170, 170, 170); outline: 0px; }

.select2-container--classic .select2-search--inline .select2-search__field { outline: 0px; box-shadow: none; }

.select2-container--classic .select2-dropdown { background-color: rgb(255, 255, 255); border: 1px solid transparent; }

.select2-container--classic .select2-dropdown--above { border-bottom: none; }

.select2-container--classic .select2-dropdown--below { border-top: none; }

.select2-container--classic .select2-results > .select2-results__options { max-height: 200px; overflow-y: auto; }

.select2-container--classic .select2-results__option[role="group"] { padding: 0px; }

.select2-container--classic .select2-results__option[aria-disabled="true"] { color: grey; }

.select2-container--classic .select2-results__option--highlighted[aria-selected] { background-color: rgb(56, 117, 215); color: rgb(255, 255, 255); }

.select2-container--classic .select2-results__group { cursor: default; display: block; padding: 6px; }

.select2-container--classic.select2-container--open .select2-dropdown { border-color: rgb(88, 151, 251); }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.6/css/selectize.bootstrap3.min.css?ver=6.1.1

@charset "utf-8";

.selectize-control.plugin-drag_drop.multi > .selectize-input > div.ui-sortable-placeholder { box-shadow: rgb(255, 255, 255) 0px 0px 12px 4px inset; visibility: visible !important; background: rgba(0, 0, 0, 0.06) !important; border: 0px none !important; }

.selectize-control.plugin-drag_drop .ui-sortable-placeholder::after { content: "!"; visibility: hidden; }

.selectize-control.plugin-drag_drop .ui-sortable-helper { box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 5px; }

.selectize-dropdown-header { position: relative; padding: 3px 12px; border-bottom: 1px solid rgb(208, 208, 208); background: rgb(248, 248, 248); border-radius: 4px 4px 0px 0px; }

.selectize-dropdown-header-close { position: absolute; right: 12px; top: 50%; color: rgb(51, 51, 51); opacity: 0.4; margin-top: -12px; line-height: 20px; font-size: 20px !important; }

.selectize-dropdown-header-close:hover { color: rgb(0, 0, 0); }

.selectize-dropdown.plugin-optgroup_columns .optgroup { border-right: 1px solid rgb(242, 242, 242); border-top: 0px none; float: left; box-sizing: border-box; }

.selectize-dropdown.plugin-optgroup_columns .optgroup:last-child { border-right: 0px none; }

.selectize-dropdown.plugin-optgroup_columns .optgroup::before { display: none; }

.selectize-dropdown.plugin-optgroup_columns .optgroup-header { border-top: 0px none; }

.selectize-control.plugin-remove_button [data-value] { position: relative; padding-right: 24px !important; }

.selectize-control.plugin-remove_button [data-value] .remove { z-index: 1; position: absolute; top: 0px; right: 0px; bottom: 0px; width: 17px; text-align: center; font-weight: 700; font-size: 12px; color: inherit; text-decoration: none; vertical-align: middle; display: inline-block; padding: 1px 0px 0px; border-left: 1px solid transparent; border-radius: 0px 2px 2px 0px; box-sizing: border-box; }

.selectize-control.plugin-remove_button [data-value] .remove:hover { background: rgba(0, 0, 0, 0.05); }

.selectize-control.plugin-remove_button [data-value].active .remove { border-left-color: transparent; }

.selectize-control.plugin-remove_button .disabled [data-value] .remove:hover { background: 0px 0px; }

.selectize-control.plugin-remove_button .disabled [data-value] .remove { border-left-color: rgba(77, 77, 77, 0); }

.selectize-control.plugin-remove_button .remove-single { position: absolute; right: 0px; top: 0px; font-size: 23px; }

.selectize-control { position: relative; }

.selectize-dropdown, .selectize-input, .selectize-input input { color: rgb(51, 51, 51); font-family: inherit; font-size: inherit; line-height: 20px; -webkit-font-smoothing: inherit; }

.selectize-control.single .selectize-input.input-active, .selectize-input { background: rgb(255, 255, 255); cursor: text; display: inline-block; }

.selectize-input { border: 1px solid rgb(204, 204, 204); padding: 6px 12px; display: inline-block; width: 100%; overflow: hidden; position: relative; z-index: 1; box-sizing: border-box; box-shadow: none; border-radius: 4px; }

.selectize-control.multi .selectize-input.has-items { padding: 5px 12px 2px; }

.selectize-input.full { background-color: rgb(255, 255, 255); }

.selectize-input.disabled, .selectize-input.disabled * { cursor: default !important; }

.selectize-input.focus { box-shadow: rgba(0, 0, 0, 0.15) 0px 1px 2px inset; }

.selectize-input.dropdown-active { border-radius: 4px 4px 0px 0px; }

.selectize-input > * { vertical-align: baseline; display: inline-block; zoom: 1; }

.selectize-control.multi .selectize-input > div { cursor: pointer; margin: 0px 3px 3px 0px; padding: 1px 3px; background: rgb(239, 239, 239); color: rgb(51, 51, 51); border: 0px solid transparent; }

.selectize-control.multi .selectize-input > div.active { background: rgb(66, 139, 202); color: rgb(255, 255, 255); border: 0px solid transparent; }

.selectize-control.multi .selectize-input.disabled > div, .selectize-control.multi .selectize-input.disabled > div.active { color: grey; background: rgb(255, 255, 255); border: 0px solid rgba(77, 77, 77, 0); }

.selectize-input > input { display: inline-block !important; padding: 0px !important; min-height: 0px !important; max-height: none !important; max-width: 100% !important; margin: 0px !important; text-indent: 0px !important; border: 0px none !important; background: 0px 0px !important; line-height: inherit !important; user-select: auto !important; box-shadow: none !important; }

.selectize-input > input:focus { outline: 0px !important; }

.selectize-input::after { content: " "; display: block; clear: left; }

.selectize-input.dropdown-active::before { content: " "; display: block; position: absolute; background: rgb(255, 255, 255); height: 1px; bottom: 0px; left: 0px; right: 0px; }

.selectize-dropdown { position: absolute; z-index: 10; border-width: 0px 1px 1px; border-style: none solid solid; border-right-color: rgb(208, 208, 208); border-bottom-color: rgb(208, 208, 208); border-left-color: rgb(208, 208, 208); border-image: initial; background: rgb(255, 255, 255); margin: -1px 0px 0px; border-top-color: initial; box-sizing: border-box; box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px; border-radius: 0px 0px 4px 4px; }

.selectize-dropdown [data-selectable] { cursor: pointer; overflow: hidden; }

.selectize-dropdown [data-selectable] .highlight { background: rgba(255, 237, 40, 0.4); border-radius: 1px; }

.selectize-dropdown .optgroup-header, .selectize-dropdown .option { padding: 3px 12px; }

.selectize-dropdown .option, .selectize-dropdown [data-disabled], .selectize-dropdown [data-disabled] [data-selectable].option { cursor: inherit; opacity: 0.5; }

.selectize-dropdown [data-selectable].option { opacity: 1; }

.selectize-dropdown .optgroup:first-child .optgroup-header { border-top: 0px none; }

.selectize-dropdown .optgroup-header { color: rgb(119, 119, 119); background: rgb(255, 255, 255); cursor: default; }

.selectize-dropdown .active { background-color: rgb(245, 245, 245); color: rgb(38, 38, 38); }

.selectize-dropdown .active.create { color: rgb(38, 38, 38); }

.selectize-dropdown .create { color: rgba(51, 51, 51, 0.5); }

.selectize-dropdown-content { overflow: hidden auto; max-height: 200px; }

.selectize-control.single .selectize-input, .selectize-control.single .selectize-input input { cursor: pointer; }

.selectize-control.single .selectize-input.input-active, .selectize-control.single .selectize-input.input-active input { cursor: text; }

.selectize-control.single .selectize-input::after { content: " "; display: block; position: absolute; top: 50%; right: 17px; margin-top: -3px; width: 0px; height: 0px; border-style: solid; border-width: 5px 5px 0px; border-color: rgb(51, 51, 51) transparent transparent; }

.selectize-control.single .selectize-input.dropdown-active::after { margin-top: -4px; border-width: 0px 5px 5px; border-color: transparent transparent rgb(51, 51, 51); }

.selectize-control.rtl.single .selectize-input::after { left: 17px; right: auto; }

.selectize-control.rtl .selectize-input > input { margin: 0px 4px 0px -2px !important; }

.selectize-control .selectize-input.disabled { opacity: 0.5; background-color: rgb(255, 255, 255); }

.selectize-dropdown, .selectize-dropdown.form-control { height: auto; padding: 0px; margin: 2px 0px 0px; z-index: 1000; background: rgb(255, 255, 255); border: 1px solid rgba(0, 0, 0, 0.15); border-radius: 4px; box-shadow: rgba(0, 0, 0, 0.176) 0px 6px 12px; }

.selectize-dropdown .optgroup-header { font-size: 12px; line-height: 1.42857; }

.selectize-dropdown .optgroup:first-child::before { display: none; }

.selectize-dropdown .optgroup::before { content: " "; display: block; height: 1px; margin: 9px -12px; overflow: hidden; background-color: rgb(229, 229, 229); }

.selectize-dropdown-content { padding: 5px 0px; }

.selectize-dropdown-header { padding: 6px 12px; }

.selectize-input { min-height: 34px; }

.selectize-input.dropdown-active { border-radius: 4px; }

.selectize-input.dropdown-active::before { display: none; }

.selectize-input.focus { border-color: rgb(102, 175, 233); outline: 0px; box-shadow: rgba(0, 0, 0, 0.075) 0px 1px 1px inset, rgba(102, 175, 233, 0.6) 0px 0px 8px; }

.has-error .selectize-input { border-color: rgb(169, 68, 66); box-shadow: rgba(0, 0, 0, 0.075) 0px 1px 1px inset; }

.has-error .selectize-input:focus { border-color: rgb(132, 53, 52); box-shadow: rgba(0, 0, 0, 0.075) 0px 1px 1px inset, rgb(206, 132, 131) 0px 0px 6px; }

.selectize-control.multi .selectize-input.has-items { padding-left: 9px; padding-right: 9px; }

.selectize-control.multi .selectize-input > div { border-radius: 3px; }

.form-control.selectize-control { padding: 0px; height: auto; border: none; background: 0px 0px; box-shadow: none; border-radius: 0px; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.17

@charset "utf-8";

.mejs-offscreen { border: 0px; clip: rect(1px, 1px, 1px, 1px); clip-path: inset(50%); height: 1px; margin: -1px; overflow: hidden; padding: 0px; position: absolute; width: 1px; overflow-wrap: normal; }

.mejs-container { background: rgb(0, 0, 0); font-family: Helvetica, Arial, serif; position: relative; text-align: left; text-indent: 0px; vertical-align: top; }

.mejs-container, .mejs-container * { box-sizing: border-box; }

.mejs-container video::-webkit-media-controls, .mejs-container video::-webkit-media-controls-panel, .mejs-container video::-webkit-media-controls-panel-container, .mejs-container video::-webkit-media-controls-start-playback-button { -webkit-appearance: none; display: none !important; }

.mejs-fill-container, .mejs-fill-container .mejs-container { height: 100%; width: 100%; }

.mejs-fill-container { background: transparent; margin: 0px auto; overflow: hidden; position: relative; }

.mejs-container:focus { outline: none; }

.mejs-iframe-overlay { height: 100%; position: absolute; width: 100%; }

.mejs-embed, .mejs-embed body { background: rgb(0, 0, 0); height: 100%; margin: 0px; overflow: hidden; padding: 0px; width: 100%; }

.mejs-fullscreen { overflow: hidden !important; }

.mejs-container-fullscreen { bottom: 0px; left: 0px; overflow: hidden; position: fixed; right: 0px; top: 0px; z-index: 1000; }

.mejs-container-fullscreen .mejs-mediaelement, .mejs-container-fullscreen video { height: 100% !important; width: 100% !important; }

.mejs-background, .mejs-mediaelement { left: 0px; position: absolute; top: 0px; }

.mejs-mediaelement { height: 100%; width: 100%; z-index: 0; }

.mejs-poster { background-position: 50% 50%; background-repeat: no-repeat; background-size: cover; left: 0px; position: absolute; top: 0px; z-index: 1; }

:root .mejs-poster-img { display: none; }

.mejs-poster-img { border: 0px; padding: 0px; }

.mejs-overlay { -webkit-box-align: center; align-items: center; display: flex; -webkit-box-pack: center; justify-content: center; left: 0px; position: absolute; top: 0px; }

.mejs-layer { z-index: 1; }

.mejs-overlay-play { cursor: pointer; }

.mejs-overlay-button { background: url("mejs-controls.svg") 0px -39px no-repeat; height: 80px; width: 80px; }

.mejs-overlay:hover > .mejs-overlay-button { background-position: -80px -39px; }

.mejs-overlay-loading { height: 80px; width: 80px; }

.mejs-overlay-loading-bg-img { animation: 1s linear 0s infinite normal none running a; background: url("mejs-controls.svg") -160px -40px no-repeat transparent; display: block; height: 80px; width: 80px; z-index: 1; }

@-webkit-keyframes a { 
  100% { transform: rotate(1turn); }
}

@keyframes a { 
  100% { transform: rotate(1turn); }
}

.mejs-controls { bottom: 0px; display: flex; height: 40px; left: 0px; list-style-type: none; margin: 0px; padding: 0px 10px; position: absolute; width: 100%; z-index: 3; }

.mejs-controls:not([style*="display: none"]) { background: linear-gradient(transparent, rgba(0, 0, 0, 0.35)); }

.mejs-button, .mejs-time, .mejs-time-rail { font-size: 10px; height: 40px; line-height: 10px; margin: 0px; width: 32px; }

.mejs-button > button { background: url("mejs-controls.svg") transparent; border: 0px; cursor: pointer; display: block; font-size: 0px; height: 20px; line-height: 0; margin: 10px 6px; overflow: hidden; padding: 0px; position: absolute; text-decoration: none; width: 20px; }

.mejs-button > button:focus { outline: rgb(153, 153, 153) dotted 1px; }

.mejs-container-keyboard-inactive [role="slider"], .mejs-container-keyboard-inactive [role="slider"]:focus, .mejs-container-keyboard-inactive a, .mejs-container-keyboard-inactive a:focus, .mejs-container-keyboard-inactive button, .mejs-container-keyboard-inactive button:focus { outline: 0px; }

.mejs-time { box-sizing: content-box; color: rgb(255, 255, 255); font-size: 11px; font-weight: 700; height: 24px; overflow: hidden; padding: 16px 6px 0px; text-align: center; width: auto; }

.mejs-play > button { background-position: 0px 0px; }

.mejs-pause > button { background-position: -20px 0px; }

.mejs-replay > button { background-position: -160px 0px; }

.mejs-time-rail { direction: ltr; -webkit-box-flex: 1; flex-grow: 1; height: 40px; margin: 0px 10px; padding-top: 10px; position: relative; }

.mejs-time-buffering, .mejs-time-current, .mejs-time-float, .mejs-time-float-corner, .mejs-time-float-current, .mejs-time-hovered, .mejs-time-loaded, .mejs-time-marker, .mejs-time-total { border-radius: 2px; cursor: pointer; display: block; height: 10px; position: absolute; }

.mejs-time-total { background: rgba(255, 255, 255, 0.3); margin: 5px 0px 0px; width: 100%; }

.mejs-time-buffering { animation: 2s linear 0s infinite normal none running b; background: linear-gradient(-45deg, rgba(255, 255, 255, 0.4) 25%, transparent 0px, transparent 50%, rgba(255, 255, 255, 0.4) 0px, rgba(255, 255, 255, 0.4) 75%, transparent 0px, transparent) 0% 0% / 15px 15px; width: 100%; }

@-webkit-keyframes b { 
  0% { background-position: 0px 0px; }
  100% { background-position: 30px 0px; }
}

@keyframes b { 
  0% { background-position: 0px 0px; }
  100% { background-position: 30px 0px; }
}

.mejs-time-loaded { background: rgba(255, 255, 255, 0.3); }

.mejs-time-current, .mejs-time-handle-content { background: rgba(255, 255, 255, 0.9); }

.mejs-time-hovered { background: rgba(255, 255, 255, 0.5); z-index: 10; }

.mejs-time-hovered.negative { background: rgba(0, 0, 0, 0.2); }

.mejs-time-buffering, .mejs-time-current, .mejs-time-hovered, .mejs-time-loaded { left: 0px; transform: scaleX(0); transform-origin: 0px 0px; transition: all 0.15s ease-in 0s; width: 100%; }

.mejs-time-buffering { transform: scaleX(1); }

.mejs-time-hovered { transition: height 0.1s cubic-bezier(0.44, 0, 1, 1) 0s; }

.mejs-time-hovered.no-hover { transform: scaleX(0) !important; }

.mejs-time-handle, .mejs-time-handle-content { border: 4px solid transparent; cursor: pointer; left: 0px; position: absolute; transform: translateX(0px); z-index: 11; }

.mejs-time-handle-content { border: 4px solid rgba(255, 255, 255, 0.9); border-radius: 50%; height: 10px; left: -7px; top: -4px; transform: scale(0); width: 10px; }

.mejs-time-rail .mejs-time-handle-content:active, .mejs-time-rail .mejs-time-handle-content:focus, .mejs-time-rail:hover .mejs-time-handle-content { transform: scale(1); }

.mejs-time-float { background: rgb(238, 238, 238); border: 1px solid rgb(51, 51, 51); bottom: 100%; color: rgb(17, 17, 17); display: none; height: 17px; margin-bottom: 9px; position: absolute; text-align: center; transform: translateX(-50%); width: 36px; }

.mejs-time-float-current { display: block; left: 0px; margin: 2px; text-align: center; width: 30px; }

.mejs-time-float-corner { border-width: 5px; border-style: solid; border-image: initial; border-color: rgb(238, 238, 238) transparent transparent; border-radius: 0px; display: block; height: 0px; left: 50%; line-height: 0; position: absolute; top: 100%; transform: translateX(-50%); width: 0px; }

.mejs-long-video .mejs-time-float { margin-left: -23px; width: 64px; }

.mejs-long-video .mejs-time-float-current { width: 60px; }

.mejs-broadcast { color: rgb(255, 255, 255); height: 10px; position: absolute; top: 15px; width: 100%; }

.mejs-fullscreen-button > button { background-position: -80px 0px; }

.mejs-unfullscreen > button { background-position: -100px 0px; }

.mejs-mute > button { background-position: -60px 0px; }

.mejs-unmute > button { background-position: -40px 0px; }

.mejs-volume-button { position: relative; }

.mejs-volume-button > .mejs-volume-slider { backface-visibility: hidden; background: rgba(50, 50, 50, 0.7); border-radius: 0px; bottom: 100%; display: none; height: 115px; left: 50%; margin: 0px; position: absolute; transform: translateX(-50%); width: 25px; z-index: 1; }

.mejs-volume-button:hover { border-radius: 0px 0px 4px 4px; }

.mejs-volume-total { background: rgba(255, 255, 255, 0.5); height: 100px; left: 50%; margin: 0px; position: absolute; top: 8px; transform: translateX(-50%); width: 2px; }

.mejs-volume-current { left: 0px; margin: 0px; width: 100%; }

.mejs-volume-current, .mejs-volume-handle { background: rgba(255, 255, 255, 0.9); position: absolute; }

.mejs-volume-handle { border-radius: 1px; cursor: ns-resize; height: 6px; left: 50%; transform: translateX(-50%); width: 16px; }

.mejs-horizontal-volume-slider { display: block; height: 36px; position: relative; vertical-align: middle; width: 56px; }

.mejs-horizontal-volume-total { background: rgba(50, 50, 50, 0.8); height: 8px; top: 16px; width: 50px; }

.mejs-horizontal-volume-current, .mejs-horizontal-volume-total { border-radius: 2px; font-size: 1px; left: 0px; margin: 0px; padding: 0px; position: absolute; }

.mejs-horizontal-volume-current { background: rgba(255, 255, 255, 0.8); height: 100%; top: 0px; width: 100%; }

.mejs-horizontal-volume-handle { display: none; }

.mejs-captions-button, .mejs-chapters-button { position: relative; }

.mejs-captions-button > button { background-position: -140px 0px; }

.mejs-chapters-button > button { background-position: -180px 0px; }

.mejs-captions-button > .mejs-captions-selector, .mejs-chapters-button > .mejs-chapters-selector { background: rgba(50, 50, 50, 0.7); border: 1px solid transparent; border-radius: 0px; bottom: 100%; margin-right: -43px; overflow: hidden; padding: 0px; position: absolute; right: 50%; visibility: visible; width: 86px; }

.mejs-chapters-button > .mejs-chapters-selector { margin-right: -55px; width: 110px; }

.mejs-captions-selector-list, .mejs-chapters-selector-list { margin: 0px; overflow: hidden; padding: 0px; list-style-type: none !important; }

.mejs-captions-selector-list-item, .mejs-chapters-selector-list-item { color: rgb(255, 255, 255); cursor: pointer; display: block; margin: 0px 0px 6px; overflow: hidden; padding: 0px; list-style-type: none !important; }

.mejs-captions-selector-list-item:hover, .mejs-chapters-selector-list-item:hover { background-color: rgba(255, 255, 255, 0.4) !important; }

.mejs-captions-selector-input, .mejs-chapters-selector-input { clear: both; float: left; left: -1000px; margin: 3px 3px 0px 5px; position: absolute; }

.mejs-captions-selector-label, .mejs-chapters-selector-label { cursor: pointer; float: left; font-size: 10px; line-height: 15px; padding: 4px 10px 0px; width: 100%; }

.mejs-captions-selected, .mejs-chapters-selected { color: rgb(33, 248, 248); }

.mejs-captions-translations { font-size: 10px; margin: 0px 0px 5px; }

.mejs-captions-layer { bottom: 0px; color: rgb(255, 255, 255); font-size: 16px; left: 0px; line-height: 20px; position: absolute; text-align: center; }

.mejs-captions-layer a { color: rgb(255, 255, 255); text-decoration: underline; }

.mejs-captions-layer[lang="ar"] { font-size: 20px; font-weight: 400; }

.mejs-captions-position { bottom: 15px; left: 0px; position: absolute; width: 100%; }

.mejs-captions-position-hover { bottom: 35px; }

.mejs-captions-text, .mejs-captions-text * { background: rgba(20, 20, 20, 0.5); box-shadow: rgba(20, 20, 20, 0.5) 5px 0px 0px, rgba(20, 20, 20, 0.5) -5px 0px 0px; padding: 0px; white-space: pre-wrap; }

.mejs-container.mejs-hide-cues video::-webkit-media-text-track-container { display: none; }

.mejs-overlay-error { position: relative; }

.mejs-overlay-error > img { left: 0px; max-width: 100%; position: absolute; top: 0px; z-index: -1; }

.mejs-cannotplay, .mejs-cannotplay a { color: rgb(255, 255, 255); font-size: 0.8em; }

.mejs-cannotplay { position: relative; }

.mejs-cannotplay a, .mejs-cannotplay p { display: inline-block; padding: 0px 15px; width: 100%; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=6.1.1

@charset "utf-8";

.mejs-container { clear: both; max-width: 100%; }

.mejs-container * { font-family: Helvetica, Arial; }

.mejs-container, .mejs-container .mejs-controls, .mejs-embed, .mejs-embed body { background: rgb(34, 34, 34); }

.mejs-time { font-weight: 400; overflow-wrap: normal; }

.mejs-controls a.mejs-horizontal-volume-slider { display: table; }

.mejs-controls .mejs-horizontal-volume-slider .mejs-horizontal-volume-current, .mejs-controls .mejs-time-rail .mejs-time-loaded { background: rgb(255, 255, 255); }

.mejs-controls .mejs-time-rail .mejs-time-current { background: rgb(0, 115, 170); }

.mejs-controls .mejs-horizontal-volume-slider .mejs-horizontal-volume-total, .mejs-controls .mejs-time-rail .mejs-time-total { background: rgba(255, 255, 255, 0.33); }

.mejs-controls .mejs-horizontal-volume-slider .mejs-horizontal-volume-current, .mejs-controls .mejs-horizontal-volume-slider .mejs-horizontal-volume-total, .mejs-controls .mejs-time-rail span { border-radius: 0px; }

.mejs-overlay-loading { background: 0px 0px; }

.mejs-controls button:hover { border: none; box-shadow: none; }

.me-cannotplay { width: auto !important; }

.media-embed-details .wp-audio-shortcode { display: inline-block; max-width: 400px; }

.audio-details .embed-media-settings { overflow: visible; }

.media-embed-details .embed-media-settings .setting span:not(.button-group) { max-width: 400px; width: auto; }

.media-embed-details .embed-media-settings .checkbox-setting span { display: inline-block; }

.media-embed-details .embed-media-settings { padding-top: 0px; top: 28px; }

.media-embed-details .instructions { padding: 16px 0px; max-width: 600px; }

.media-embed-details .setting .remove-setting, .media-embed-details .setting p { color: rgb(170, 0, 0); font-size: 10px; text-transform: uppercase; }

.media-embed-details .setting .remove-setting { padding: 5px 0px; }

.media-embed-details .setting a:hover { color: rgb(220, 50, 50); }

.media-embed-details .embed-media-settings .checkbox-setting { float: none; margin: 0px 0px 10px; }

.wp-video { max-width: 100%; height: auto; }

.wp_attachment_holder .wp-audio-shortcode, .wp_attachment_holder .wp-video { margin-top: 18px; }

.wp-video-shortcode video, video.wp-video-shortcode { max-width: 100%; display: inline-block; }

.video-details .wp-video-holder { width: 100%; max-width: 640px; }

.wp-playlist { border: 1px solid rgb(204, 204, 204); padding: 10px; margin: 12px 0px 18px; font-size: 14px; line-height: 1.5; }

.wp-admin .wp-playlist { margin: 0px 0px 18px; }

.wp-playlist video { display: inline-block; max-width: 100%; }

.wp-playlist audio { display: none; max-width: 100%; width: 400px; }

.wp-playlist .mejs-container { margin: 0px; max-width: 100%; }

.wp-playlist .mejs-controls .mejs-button button { outline: 0px; }

.wp-playlist-light { background: rgb(255, 255, 255); color: rgb(0, 0, 0); }

.wp-playlist-dark { color: rgb(255, 255, 255); background: rgb(0, 0, 0); }

.wp-playlist-caption { display: block; max-width: 88%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-size: 14px; line-height: 1.5; }

.wp-playlist-item .wp-playlist-caption { text-decoration: none; color: rgb(0, 0, 0); max-width: calc(100% - 40px); }

.wp-playlist-item-meta { display: block; font-size: 14px; line-height: 1.5; }

.wp-playlist-item-title { font-size: 14px; line-height: 1.5; }

.wp-playlist-item-album { font-style: italic; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.wp-playlist-item-artist { font-size: 12px; text-transform: uppercase; }

.wp-playlist-item-length { position: absolute; right: 3px; top: 0px; font-size: 14px; line-height: 1.5; }

.rtl .wp-playlist-item-length { left: 3px; right: auto; }

.wp-playlist-tracks { margin-top: 10px; }

.wp-playlist-item { position: relative; cursor: pointer; padding: 0px 3px; border-bottom: 1px solid rgb(204, 204, 204); }

.wp-playlist-item:last-child { border-bottom: 0px; }

.wp-playlist-light .wp-playlist-caption { color: rgb(51, 51, 51); }

.wp-playlist-dark .wp-playlist-caption { color: rgb(221, 221, 221); }

.wp-playlist-playing { font-weight: 700; background: rgb(247, 247, 247); }

.wp-playlist-light .wp-playlist-playing { background: rgb(255, 255, 255); color: rgb(0, 0, 0); }

.wp-playlist-dark .wp-playlist-playing { background: rgb(0, 0, 0); color: rgb(255, 255, 255); }

.wp-playlist-current-item { overflow: hidden; margin-bottom: 10px; height: 60px; }

.wp-playlist .wp-playlist-current-item img { float: left; max-width: 60px; height: auto; margin-right: 10px; padding: 0px; border: 0px; }

.rtl .wp-playlist .wp-playlist-current-item img { float: right; margin-left: 10px; margin-right: 0px; }

.wp-playlist-current-item .wp-playlist-item-artist, .wp-playlist-current-item .wp-playlist-item-title { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.wp-audio-playlist .me-cannotplay span { padding: 5px 15px; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/mu-plugins/search/elasticpress/dist/css/related-posts-block-styles.min.css?ver=3.6.5

@charset "utf-8";

.editor-styles-wrapper .wp-block-elasticpress-related-posts ul, .wp-block-elasticpress-related-posts ul { list-style-type: none; padding: 0px; }

.editor-styles-wrapper .wp-block-elasticpress-related-posts ul li a > div { display: inline; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-includes/css/classic-themes.min.css?ver=1

@charset "utf-8";

.wp-block-button__link { color: rgb(255, 255, 255); background-color: rgb(50, 55, 60); border-radius: 9999px; box-shadow: none; text-decoration: none; padding: calc(0.667em + 2px) calc(1.333em + 2px); font-size: 1.125em; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/plugins/livenews/front/assets/css/component.css?ver=1.1.0

@charset "utf-8";

.live-container { display: flex; flex-direction: column; padding-top: 2rem; border-top: 1px solid rgb(224, 224, 224); }

[data-type="livenews"] .live-container:first-of-type { border-top: none; }

.live-container .live-published { background: rgb(247, 247, 247); border-left: 4px solid rgb(5, 0, 245); border-radius: 0.25rem; width: fit-content; margin-bottom: 1rem; font-size: 1rem; display: flex; flex-direction: row; gap: 0.5rem; height: 2.5rem; align-items: center; padding: 0px 1rem 0px 0.75rem; }

.live-container .live-published .live-published-icon { color: rgb(5, 0, 245); }

.live-container .live-title { font-size: 1.25rem; line-height: 1.2; font-weight: 700; margin: 0px 0px 1rem; }

@media (min-width: 64rem) {
  .live-container .live-title { font-size: 1.5rem; }
}

.live-container .live-content { font-size: 1.125rem; line-height: 1.4; font-weight: 400; color: rgb(0, 0, 0); margin-bottom: 2rem; }

@media (min-width: 64rem) {
  .live-container .live-content { font-size: 1.25rem; }
}

.live-container .live-content p, .live-container .live-content ul, .live-container .live-content ol, .live-container .live-content span { font-size: inherit; line-height: inherit; font-weight: inherit; color: inherit; margin-bottom: 2rem; }

.live-container .live-content :last-child { margin-bottom: 0px; }

.live-container .live-content a { color: rgb(5, 0, 245); }

.live-container .live-content .instagram-media { margin: 1px auto !important; }

.live-container .live-content iframe, .live-container .live-content blockquote { width: 100%; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/carousel/swiper-bundle.css?ver=11.6

@charset "utf-8";

@font-face { font-family: swiper-icons; src: url("data:application/font-woff;charset=utf-8;base64, d09GRgABAAAAAAZgABAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABGRlRNAAAGRAAAABoAAAAci6qHkUdERUYAAAWgAAAAIwAAACQAYABXR1BPUwAABhQAAAAuAAAANuAY7+xHU1VCAAAFxAAAAFAAAABm2fPczU9TLzIAAAHcAAAASgAAAGBP9V5RY21hcAAAAkQAAACIAAABYt6F0cBjdnQgAAACzAAAAAQAAAAEABEBRGdhc3AAAAWYAAAACAAAAAj//wADZ2x5ZgAAAywAAADMAAAD2MHtryVoZWFkAAABbAAAADAAAAA2E2+eoWhoZWEAAAGcAAAAHwAAACQC9gDzaG10eAAAAigAAAAZAAAArgJkABFsb2NhAAAC0AAAAFoAAABaFQAUGG1heHAAAAG8AAAAHwAAACAAcABAbmFtZQAAA/gAAAE5AAACXvFdBwlwb3N0AAAFNAAAAGIAAACE5s74hXjaY2BkYGAAYpf5Hu/j+W2+MnAzMYDAzaX6QjD6/4//Bxj5GA8AuRwMYGkAPywL13jaY2BkYGA88P8Agx4j+/8fQDYfA1AEBWgDAIB2BOoAeNpjYGRgYNBh4GdgYgABEMnIABJzYNADCQAACWgAsQB42mNgYfzCOIGBlYGB0YcxjYGBwR1Kf2WQZGhhYGBiYGVmgAFGBiQQkOaawtDAoMBQxXjg/wEGPcYDDA4wNUA2CCgwsAAAO4EL6gAAeNpj2M0gyAACqxgGNWBkZ2D4/wMA+xkDdgAAAHjaY2BgYGaAYBkGRgYQiAHyGMF8FgYHIM3DwMHABGQrMOgyWDLEM1T9/w8UBfEMgLzE////P/5//f/V/xv+r4eaAAeMbAxwIUYmIMHEgKYAYjUcsDAwsLKxc3BycfPw8jEQA/gZBASFhEVExcQlJKWkZWTl5BUUlZRVVNXUNTQZBgMAAMR+E+gAEQFEAAAAKgAqACoANAA+AEgAUgBcAGYAcAB6AIQAjgCYAKIArAC2AMAAygDUAN4A6ADyAPwBBgEQARoBJAEuATgBQgFMAVYBYAFqAXQBfgGIAZIBnAGmAbIBzgHsAAB42u2NMQ6CUAyGW568x9AneYYgm4MJbhKFaExIOAVX8ApewSt4Bic4AfeAid3VOBixDxfPYEza5O+Xfi04YADggiUIULCuEJK8VhO4bSvpdnktHI5QCYtdi2sl8ZnXaHlqUrNKzdKcT8cjlq+rwZSvIVczNiezsfnP/uznmfPFBNODM2K7MTQ45YEAZqGP81AmGGcF3iPqOop0r1SPTaTbVkfUe4HXj97wYE+yNwWYxwWu4v1ugWHgo3S1XdZEVqWM7ET0cfnLGxWfkgR42o2PvWrDMBSFj/IHLaF0zKjRgdiVMwScNRAoWUoH78Y2icB/yIY09An6AH2Bdu/UB+yxopYshQiEvnvu0dURgDt8QeC8PDw7Fpji3fEA4z/PEJ6YOB5hKh4dj3EvXhxPqH/SKUY3rJ7srZ4FZnh1PMAtPhwP6fl2PMJMPDgeQ4rY8YT6Gzao0eAEA409DuggmTnFnOcSCiEiLMgxCiTI6Cq5DZUd3Qmp10vO0LaLTd2cjN4fOumlc7lUYbSQcZFkutRG7g6JKZKy0RmdLY680CDnEJ+UMkpFFe1RN7nxdVpXrC4aTtnaurOnYercZg2YVmLN/d/gczfEimrE/fs/bOuq29Zmn8tloORaXgZgGa78yO9/cnXm2BpaGvq25Dv9S4E9+5SIc9PqupJKhYFSSl47+Qcr1mYNAAAAeNptw0cKwkAAAMDZJA8Q7OUJvkLsPfZ6zFVERPy8qHh2YER+3i/BP83vIBLLySsoKimrqKqpa2hp6+jq6RsYGhmbmJqZSy0sraxtbO3sHRydnEMU4uR6yx7JJXveP7WrDycAAAAAAAH//wACeNpjYGRgYOABYhkgZgJCZgZNBkYGLQZtIJsFLMYAAAw3ALgAeNolizEKgDAQBCchRbC2sFER0YD6qVQiBCv/H9ezGI6Z5XBAw8CBK/m5iQQVauVbXLnOrMZv2oLdKFa8Pjuru2hJzGabmOSLzNMzvutpB3N42mNgZGBg4GKQYzBhYMxJLMlj4GBgAYow/P/PAJJhLM6sSoWKfWCAAwDAjgbRAAB42mNgYGBkAIIbCZo5IPrmUn0hGA0AO8EFTQAA") format("woff"); font-weight: 400; font-style: normal; }

:root { --swiper-theme-color: #007aff; }

.jp-carousel-overlay .swiper-container { margin-left: auto; margin-right: auto; position: relative; overflow: hidden; list-style: none; padding: 0px; z-index: 1; }

.jp-carousel-overlay .swiper-container-vertical > .swiper-wrapper { flex-direction: column; }

.jp-carousel-overlay .swiper-wrapper { position: relative; width: 100%; height: 100%; z-index: 1; display: flex; transition-property: transform; box-sizing: content-box; }

.jp-carousel-overlay .swiper-container-android .swiper-slide, .jp-carousel-overlay .swiper-wrapper { transform: translate3d(0px, 0px, 0px); }

.jp-carousel-overlay .swiper-container-multirow > .swiper-wrapper { flex-wrap: wrap; }

.jp-carousel-overlay .swiper-container-multirow-column > .swiper-wrapper { flex-flow: column wrap; }

.jp-carousel-overlay .swiper-container-free-mode > .swiper-wrapper { transition-timing-function: ease-out; margin: 0px auto; }

.jp-carousel-overlay .swiper-container-pointer-events { touch-action: pan-y; }

.jp-carousel-overlay .swiper-container-pointer-events.swiper-container-vertical { touch-action: pan-x; }

.jp-carousel-overlay .swiper-slide { flex-shrink: 0; width: 100%; height: 100%; position: relative; transition-property: transform; }

.jp-carousel-overlay .swiper-slide-invisible-blank { visibility: hidden; }

.jp-carousel-overlay .swiper-container-autoheight, .jp-carousel-overlay .swiper-container-autoheight .swiper-slide { height: auto; }

.jp-carousel-overlay .swiper-container-autoheight .swiper-wrapper { align-items: flex-start; transition-property: transform, height; }

.jp-carousel-overlay .swiper-container-3d { perspective: 1200px; }

.jp-carousel-overlay .swiper-container-3d .swiper-wrapper, .jp-carousel-overlay .swiper-container-3d .swiper-slide, .jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-left, .jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-right, .jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-top, .jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-bottom, .jp-carousel-overlay .swiper-container-3d .swiper-cube-shadow { transform-style: preserve-3d; }

.jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-left, .jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-right, .jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-top, .jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-bottom { position: absolute; left: 0px; top: 0px; width: 100%; height: 100%; pointer-events: none; z-index: 10; }

.jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-left { background-image: linear-gradient(to left, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0)); }

.jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-right { background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0)); }

.jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-top { background-image: linear-gradient(to top, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0)); }

.jp-carousel-overlay .swiper-container-3d .swiper-slide-shadow-bottom { background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0)); }

.jp-carousel-overlay .swiper-container-css-mode > .swiper-wrapper { overflow: auto; }

.jp-carousel-overlay .swiper-container-css-mode > .swiper-wrapper::-webkit-scrollbar { display: none; }

.jp-carousel-overlay .swiper-container-css-mode > .swiper-wrapper > .swiper-slide { scroll-snap-align: start; }

.jp-carousel-overlay .swiper-container-horizontal.swiper-container-css-mode > .swiper-wrapper { scroll-snap-type: x mandatory; }

.jp-carousel-overlay .swiper-container-vertical.swiper-container-css-mode > .swiper-wrapper { scroll-snap-type: y mandatory; }

:root { --swiper-navigation-size: 44px; }

.jp-carousel-overlay .swiper-button-prev, .jp-carousel-overlay .swiper-button-next { position: absolute; top: 50%; width: calc( var( --swiper-navigation-size ) / 44 * 27 ); height: var( --swiper-navigation-size ); margin-top: calc( 0px - ( var( --swiper-navigation-size ) / 2 ) ); z-index: 10; cursor: pointer; display: flex; align-items: center; justify-content: center; color: var( --swiper-navigation-color, var( --swiper-theme-color ) ); }

.jp-carousel-overlay .swiper-button-prev.swiper-button-disabled, .jp-carousel-overlay .swiper-button-next.swiper-button-disabled { opacity: 0.35; cursor: auto; pointer-events: none; }

.jp-carousel-overlay .swiper-button-prev::after, .jp-carousel-overlay .swiper-button-next::after { font-family: swiper-icons; font-size: var( --swiper-navigation-size ); letter-spacing: 0px; font-variant: initial; line-height: 1; text-transform: none !important; }

.jp-carousel-overlay .swiper-button-prev, .jp-carousel-overlay .swiper-container-rtl .swiper-button-next { left: 10px; right: auto; }

.jp-carousel-overlay .swiper-button-prev::after, .jp-carousel-overlay .swiper-container-rtl .swiper-button-next::after { content: "prev"; }

.jp-carousel-overlay .swiper-button-next, .jp-carousel-overlay .swiper-container-rtl .swiper-button-prev { right: 10px; left: auto; }

.jp-carousel-overlay .swiper-button-next::after, .jp-carousel-overlay .swiper-container-rtl .swiper-button-prev::after { content: "next"; }

.jp-carousel-overlay .swiper-button-prev.swiper-button-white, .jp-carousel-overlay .swiper-button-next.swiper-button-white { --swiper-navigation-color: #ffffff; }

.jp-carousel-overlay .swiper-button-prev.swiper-button-black, .jp-carousel-overlay .swiper-button-next.swiper-button-black { --swiper-navigation-color: #000000; }

.jp-carousel-overlay .swiper-button-lock { display: none; }

:root { }

.jp-carousel-overlay .swiper-pagination { position: absolute; text-align: center; transition: opacity 300ms ease 0s; transform: translate3d(0px, 0px, 0px); z-index: 10; }

.jp-carousel-overlay .swiper-pagination.swiper-pagination-hidden { opacity: 0; }

.jp-carousel-overlay .swiper-pagination-fraction, .jp-carousel-overlay .swiper-pagination-custom, .jp-carousel-overlay .swiper-container-horizontal > .swiper-pagination-bullets { bottom: 10px; left: 0px; width: 100%; }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic { overflow: hidden; font-size: 0px; }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic .swiper-pagination-bullet { transform: scale(0.33); position: relative; }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic .swiper-pagination-bullet-active { transform: scale(1); }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic .swiper-pagination-bullet-active-main { transform: scale(1); }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic .swiper-pagination-bullet-active-prev { transform: scale(0.66); }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic .swiper-pagination-bullet-active-prev-prev { transform: scale(0.33); }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic .swiper-pagination-bullet-active-next { transform: scale(0.66); }

.jp-carousel-overlay .swiper-pagination-bullets-dynamic .swiper-pagination-bullet-active-next-next { transform: scale(0.33); }

.jp-carousel-overlay .swiper-pagination-bullet { width: 8px; height: 8px; display: inline-block; border-radius: 50%; background: rgb(0, 0, 0); opacity: 0.2; }

.jp-carousel-overlay button.swiper-pagination-bullet { border: none; margin: 0px; padding: 0px; box-shadow: none; -webkit-appearance: none; }

.jp-carousel-overlay .swiper-pagination-clickable .swiper-pagination-bullet { cursor: pointer; }

.jp-carousel-overlay .swiper-pagination-bullet-active { opacity: 1; background: var( --swiper-pagination-color, var( --swiper-theme-color ) ); }

.jp-carousel-overlay .swiper-container-vertical > .swiper-pagination-bullets { right: 10px; top: 50%; transform: translate3d(0px, -50%, 0px); }

.jp-carousel-overlay .swiper-container-vertical > .swiper-pagination-bullets .swiper-pagination-bullet { margin: 6px 0px; display: block; }

.jp-carousel-overlay .swiper-container-vertical > .swiper-pagination-bullets.swiper-pagination-bullets-dynamic { top: 50%; transform: translateY(-50%); width: 8px; }

.jp-carousel-overlay .swiper-container-vertical > .swiper-pagination-bullets.swiper-pagination-bullets-dynamic .swiper-pagination-bullet { display: inline-block; transition: transform 200ms ease 0s, top 200ms ease 0s; }

.jp-carousel-overlay .swiper-container-horizontal > .swiper-pagination-bullets .swiper-pagination-bullet { margin: 0px 4px; }

.jp-carousel-overlay .swiper-container-horizontal > .swiper-pagination-bullets.swiper-pagination-bullets-dynamic { left: 50%; transform: translateX(-50%); white-space: nowrap; }

.jp-carousel-overlay .swiper-container-horizontal > .swiper-pagination-bullets.swiper-pagination-bullets-dynamic .swiper-pagination-bullet { transition: transform 200ms ease 0s, left 200ms ease 0s; }

.jp-carousel-overlay .swiper-container-horizontal.swiper-container-rtl > .swiper-pagination-bullets-dynamic .swiper-pagination-bullet { transition: transform 200ms ease 0s, right 200ms ease 0s; }

.jp-carousel-overlay .swiper-pagination-progressbar { background: rgba(0, 0, 0, 0.25); position: absolute; }

.jp-carousel-overlay .swiper-pagination-progressbar .swiper-pagination-progressbar-fill { background: var( --swiper-pagination-color, var( --swiper-theme-color ) ); position: absolute; left: 0px; top: 0px; width: 100%; height: 100%; transform: scale(0); transform-origin: left top; }

.jp-carousel-overlay .swiper-container-rtl .swiper-pagination-progressbar .swiper-pagination-progressbar-fill { transform-origin: right top; }

.jp-carousel-overlay .swiper-container-horizontal > .swiper-pagination-progressbar, .jp-carousel-overlay .swiper-container-vertical > .swiper-pagination-progressbar.swiper-pagination-progressbar-opposite { width: 100%; height: 4px; left: 0px; top: 0px; }

.jp-carousel-overlay .swiper-container-vertical > .swiper-pagination-progressbar, .jp-carousel-overlay .swiper-container-horizontal > .swiper-pagination-progressbar.swiper-pagination-progressbar-opposite { width: 4px; height: 100%; left: 0px; top: 0px; }

.jp-carousel-overlay .swiper-pagination-white { --swiper-pagination-color: #ffffff; }

.jp-carousel-overlay .swiper-pagination-black { --swiper-pagination-color: #000000; }

.jp-carousel-overlay .swiper-pagination-lock { display: none; }

.jp-carousel-overlay .swiper-zoom-container { width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; text-align: center; }

.jp-carousel-overlay .swiper-zoom-container > img, .jp-carousel-overlay .swiper-zoom-container > svg, .jp-carousel-overlay .swiper-zoom-container > canvas { max-width: 100%; max-height: 100%; object-fit: contain; }

.jp-carousel-overlay .swiper-slide-zoomed { cursor: move; }

.jp-carousel-overlay .swiper-container .swiper-notification { position: absolute; left: 0px; top: 0px; pointer-events: none; opacity: 0; z-index: -1000; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/carousel/jetpack-carousel.css?ver=11.6

@charset "utf-8";

:root { --jp-carousel-primary-color: #fff; --jp-carousel-primary-subtle-color: #999; --jp-carousel-bg-color: #000; --jp-carousel-bg-faded-color: #222; --jp-carousel-border-color: #3a3a3a; }

:root .jp-carousel-light { --jp-carousel-primary-color: #000; --jp-carousel-primary-subtle-color: #646970; --jp-carousel-bg-color: #fff; --jp-carousel-bg-faded-color: #fbfbfb; --jp-carousel-border-color: #dcdcde; }

.jp-carousel-overlay .swiper-button-prev, .jp-carousel-overlay .swiper-container-rtl .swiper-button-next, .jp-carousel-overlay .swiper-button-next, .jp-carousel-overlay .swiper-container-rtl .swiper-button-prev { background-image: none; }

[data-carousel-extra]:not(.jp-carousel-wrap) img, [data-carousel-extra]:not(.jp-carousel-wrap) img + figcaption { cursor: pointer; }

.jp-carousel-wrap * { line-height: inherit; }

.jp-carousel-wrap.swiper-container { height: auto; width: 100vw; }

.jp-carousel-overlay .swiper-zoom-container { background-size: 200%; background-repeat: no-repeat; background-position: center center; }

.jp-carousel-overlay .swiper-slide.swiper-slide-prev .swiper-zoom-container img, .jp-carousel-overlay .swiper-slide.swiper-slide-next .swiper-zoom-container img { transition: none 0s ease 0s !important; }

.jp-carousel-overlay .swiper-button-prev, .jp-carousel-overlay .swiper-button-next { opacity: 0.5; transition: opacity 0.5s ease-out 0s; height: initial; width: initial; padding: 20px 40px; background-image: none; }

.jp-carousel-overlay .swiper-button-prev:hover, .jp-carousel-overlay .swiper-button-next:hover { opacity: 1; }

.jp-carousel-overlay .swiper-button-next::after, .jp-carousel-overlay .swiper-container-rtl .swiper-button-next::after, .jp-carousel-overlay .swiper-button-prev::after, .jp-carousel-overlay .swiper-container-rtl .swiper-button-prev::after { content: none; }

.jp-carousel-overlay .swiper-button-prev svg, .jp-carousel-overlay .swiper-button-next svg { height: 30px; width: 28px; background: var(--jp-carousel-bg-color); border-radius: 4px; }

.jp-carousel-overlay { z-index: 2147483647; overflow: hidden auto; direction: ltr; position: fixed; top: 0px; right: 0px; bottom: 0px; left: 0px; background: var(--jp-carousel-bg-color); font-family: "Helvetica Neue", sans-serif !important; }

.jp-carousel-overlay * { box-sizing: border-box; }

.jp-carousel-overlay h1::before, .jp-carousel-overlay h2::before, .jp-carousel-overlay h3::before { content: none; display: none; }

.jp-carousel-overlay .swiper-container .swiper-button-prev { left: 0px; right: auto; }

.jp-carousel-overlay .swiper-container .swiper-button-next { right: 0px; left: auto; }

.jp-carousel-overlay .swiper-container.swiper-container-rtl .swiper-button-prev, .jp-carousel-overlay .swiper-container.swiper-container-rtl .swiper-button-next { transform: scaleX(-1); }

.jp-carousel-container { display: grid; grid-template-rows: 1fr 64px; height: 100%; }

.jp-carousel-hide-controls .jp-carousel-container { grid-template-rows: 1fr; }

.jp-carousel-hide-controls .swiper-wrapper { margin-top: -32px; }

.jp-carousel-hide-controls .jp-swiper-button-next, .jp-carousel-hide-controls .jp-swiper-button-prev { margin-top: -54px; }

.jp-carousel-msg { font-family: "Open Sans", sans-serif; font-style: normal; display: inline-block; line-height: 19px; padding: 11px 15px; font-size: 14px; text-align: center; margin: 25px 20px 0px 2px; background-color: var(--jp-carousel-primary-color); border-left: 4px solid rgb(255, 186, 0); box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 1px 0px; }

.jp-carousel-info { display: flex; flex-direction: column; z-index: 100; background-color: var(--jp-carousel-bg-color); transition: opacity 200ms ease-out 0s; opacity: 1; text-align: left !important; -webkit-font-smoothing: subpixel-antialiased !important; }

.jp-carousel-hide-controls .jp-carousel-info { visibility: hidden; height: 0px; overflow: hidden; }

.jp-carousel-info-footer { position: relative; background-color: var(--jp-carousel-bg-color); height: 64px; display: flex; align-items: center; justify-content: space-between; width: 100vw; }

.jp-carousel-info-extra { display: none; background-color: var(--jp-carousel-bg-color); padding: 35px; width: 100vw; border-top: 1px solid var(--jp-carousel-bg-faded-color); }

.jp-carousel-title-and-caption { margin-bottom: 15px; }

.jp-carousel-info-extra.jp-carousel-show { display: block; }

.jp-carousel-info ::selection { background: var(--jp-carousel-primary-color); color: var(--jp-carousel-primary-color); }

.jp-carousel-photo-info { left: 0px !important; width: 100% !important; }

.jp-carousel-comments-wrapper { padding: 0px; display: none; width: 100% !important; }

.jp-carousel-comments-wrapper.jp-carousel-show { display: block; }

.jp-carousel-comments-wrapper > .jp-carousel-photo-info { display: none; }

.jp-carousel-transitions .jp-carousel-photo-info { transition: all 400ms ease-out 0s; }

.jp-carousel-buttons { margin: -18px -20px 15px; padding: 8px 10px; border-bottom: 1px solid rgb(34, 34, 34); background: rgb(34, 34, 34); text-align: center; }

div.jp-carousel-buttons a { color: var(--jp-carousel-primary-subtle-color); padding: 5px 2px 5px 0px; vertical-align: middle; -webkit-font-smoothing: subpixel-antialiased; border: none !important; font: 11px / 1.2em "Helvetica Neue", sans-serif !important; letter-spacing: 0px !important; text-decoration: none !important; text-shadow: none !important; }

div.jp-carousel-buttons a:hover { color: var(--jp-carousel-primary-color); border: none !important; }

.jp-carousel-transitions div.jp-carousel-buttons a:hover { transition: none 0s ease 0s !important; }

.jp-carousel-slide, .jp-carousel-slide img { transform: translate3d(0px, 0px, 0px); }

.jp-carousel-close-hint { position: fixed; top: 20px; right: 30px; padding: 10px; text-align: right; width: 45px; height: 45px; z-index: 15; color: var(--jp-carousel-primary-color); cursor: pointer; transition: opacity 200ms ease-out 0s; letter-spacing: 0px !important; }

.jp-carousel-transitions .jp-carousel-close-hint { transition: color 200ms linear 0s; }

.jp-carousel-close-hint svg { padding: 3px 2px; background: var(--jp-carousel-bg-color); border-radius: 4px; }

.jp-carousel-close-hint:hover { color: var(--jp-carousel-primary-color); }

.jp-carousel-close-hint:hover span { border-color: var(--jp-carousel-primary-color); }

.jp-carousel-pagination-container { flex: 1 1 0%; margin: 0px 15px 0px 35px; }

.jp-swiper-pagination, .jp-carousel-pagination { color: var(--jp-carousel-primary-color); font-size: 15px; font-weight: normal; white-space: nowrap; display: none; position: static !important; }

.jp-carousel-pagination-container .swiper-pagination { text-align: left; line-height: 8px; }

.jp-carousel-pagination { padding-left: 5px; }

.jp-swiper-pagination .swiper-pagination-bullet { background: var(--jp-carousel-primary-subtle-color); margin: 0px 9px; }

.jp-swiper-pagination .swiper-pagination-bullet.swiper-pagination-bullet-active { background: var(--jp-carousel-primary-color); }

.jp-swiper-pagination .swiper-pagination-bullet:not(.swiper-pagination-bullet-active) { background: var(--jp-carousel-primary-color); opacity: 0.5; }

.jp-carousel-info-footer .jp-carousel-photo-title-container { flex: 4 1 0%; justify-content: center; overflow: hidden; margin: 0px; }

.jp-carousel-photo-title, .jp-carousel-photo-caption { display: inline-block; font: 20px "Helvetica Neue", sans-serif; margin: 0px 0px 10px; padding: 0px; overflow: hidden; color: var(--jp-carousel-primary-color); background: none !important; border: none !important; letter-spacing: 0px !important; text-shadow: none !important; text-transform: none !important; }

.jp-carousel-info-footer .jp-carousel-photo-caption { text-align: center; font-size: 15px; white-space: nowrap; color: var(--jp-carousel-primary-subtle-color); cursor: pointer; margin: 0px; text-overflow: ellipsis; }

.jp-carousel-info-footer .jp-carousel-photo-caption p { margin: 0px; }

.jp-carousel-photo-title { font-size: 32px; margin-bottom: 2px; }

.jp-carousel-photo-description { color: var(--jp-carousel-primary-subtle-color); font-size: 16px; margin: 25px 0px; width: 100%; }

.jp-carousel-photo-description { overflow: hidden; overflow-wrap: break-word; }

.jp-carousel-photo-description p { color: var(--jp-carousel-primary-subtle-color); line-height: 1.4; margin-bottom: 0px; }

.jp-carousel-photo-description p a, .jp-carousel-comments p a, .jp-carousel-info h2 a { color: var(--jp-carousel-primary-color)  !important; border: none !important; text-decoration: underline !important; font-weight: normal !important; font-style: normal !important; }

.jp-carousel-photo-description p strong, .jp-carousel-photo-description p b { font-weight: bold; color: var(--jp-carousel-primary-subtle-color); }

.jp-carousel-photo-description p em, .jp-carousel-photo-description p i { font-style: italic; color: var(--jp-carousel-primary-subtle-color); }

.jp-carousel-photo-description p a:hover, .jp-carousel-comments p a:hover, .jp-carousel-info h2 a:hover { color: var(--jp-carousel-primary-subtle-color)  !important; }

.jp-carousel-photo-description p:empty { display: none; }

.jp-carousel-photo-info h1::before, .jp-carousel-photo-info h1::after, .jp-carousel-comments-wrapper h1::before, .jp-carousel-comments-wrapper h1::after { content: none !important; }

.jp-carousel-caption { font-size: 14px; font-weight: normal; margin: 0px; }

.jp-carousel-image-meta { color: var(--jp-carousel-primary-color); width: 100%; display: none; font: 12px / 1.4 "Helvetica Neue", sans-serif !important; }

.jp-carousel-image-meta.jp-carousel-show { display: block; }

.jp-carousel-image-meta li, .jp-carousel-image-meta h5 { font-family: "Helvetica Neue", sans-serif !important; position: inherit !important; top: auto !important; right: auto !important; left: auto !important; bottom: auto !important; background: none !important; border: none !important; font-weight: 400 !important; line-height: 1.3em !important; }

.jp-carousel-image-meta ul { margin: 0px !important; padding: 0px !important; list-style: none !important; }

.jp-carousel-image-meta li { width: 48% !important; display: inline-block !important; vertical-align: top !important; margin: 0px 2% 15px 0px !important; color: var(--jp-carousel-primary-color)  !important; font-size: 13px !important; }

.jp-carousel-image-meta h5 { color: var(--jp-carousel-primary-subtle-color)  !important; text-transform: uppercase !important; font-size: 10px !important; margin: 0px 0px 2px !important; letter-spacing: 0.1em !important; }

a.jp-carousel-image-download { display: inline-block; clear: both; color: var(--jp-carousel-primary-subtle-color); line-height: 1; font-weight: 400; font-size: 14px; text-decoration: none; }

a.jp-carousel-image-download svg { display: inline-block; vertical-align: middle; margin: 0px 3px; padding-bottom: 2px; }

a.jp-carousel-image-download span.photo-size { font-size: 11px; border-radius: 1em; margin-left: 2px; display: inline-block; }

a.jp-carousel-image-download span.photo-size-times { padding: 0px 1px 0px 2px; }

.jp-carousel-comments { background: none transparent; width: 100%; bottom: 10px; margin-top: 20px; font: 15px / 1.7 "Helvetica Neue", sans-serif !important; }

.jp-carousel-comments p a:hover, .jp-carousel-comments p a:focus, .jp-carousel-comments p a:active { color: var(--jp-carousel-primary-color)  !important; }

.jp-carousel-comment { background: none transparent; color: var(--jp-carousel-primary-subtle-color); overflow: auto; width: 100%; display: flex; }

.jp-carousel-comment + .jp-carousel-comment { margin-top: 20px; }

.jp-carousel-comment:last-of-type { margin-bottom: 20px; }

.jp-carousel-comment p { color: var(--jp-carousel-primary-subtle-color)  !important; }

.jp-carousel-comment .comment-author { font-size: 15px; font-weight: 500; padding: 0px; width: auto; display: inline; float: none; border: none; margin: 0px; }

.jp-carousel-comment .comment-author a { color: var(--jp-carousel-primary-color); }

.jp-carousel-comment .comment-gravatar { float: none; margin-right: 10px; }

.jp-carousel-comment .comment-content { border: none; padding: 0px; }

.jp-carousel-comment .avatar { margin: 0px; border-radius: 4px; min-width: 64px; min-height: 64px; width: 64px; height: 64px; border: none !important; padding: 0px !important; background-color: transparent !important; }

.jp-carousel-comment .comment-date { color: var(--jp-carousel-primary-subtle-color); font-size: 11px; border-bottom: 1px solid var(--jp-carousel-bg-faded-color); margin-bottom: 6px; }

#jp-carousel-comment-form { width: 100%; margin: 0px 0px 10px !important; }

#jp-carousel-comment-form.jp-carousel-is-disabled { opacity: 0.5; pointer-events: none; }

textarea#jp-carousel-comment-form-comment-field { background: var(--jp-carousel-bg-faded-color); border: 1px solid var(--jp-carousel-border-color); color: var(--jp-carousel-primary-subtle-color); width: 100%; padding: 10px 10px 5px; margin: 0px; float: none; height: 147px; box-shadow: rgba(0, 0, 0, 0.1) 2px 2px 2px inset; border-radius: 3px; overflow: hidden; box-sizing: border-box; font: 16px / 1.4 "Helvetica Neue", sans-serif !important; }

textarea#jp-carousel-comment-form-comment-field::-webkit-input-placeholder { color: rgb(85, 85, 85); }

textarea#jp-carousel-comment-form-comment-field:focus { background: var(--jp-carousel-bg-faded-color); color: var(--jp-carousel-primary-subtle-color); }

textarea#jp-carousel-comment-form-comment-field:focus::-webkit-input-placeholder { color: var(--jp-carousel-primary-subtle-color); }

#jp-carousel-loading-overlay { display: none; position: fixed; top: 0px; bottom: 0px; left: 0px; right: 0px; }

#jp-carousel-loading-wrapper { display: flex; align-items: center; justify-content: center; height: 100vh; width: 100vw; }

#jp-carousel-library-loading, #jp-carousel-library-loading::after { border-radius: 50%; width: 40px; height: 40px; }

#jp-carousel-library-loading { float: left; margin: 22px 0px 0px 10px; font-size: 10px; position: relative; text-indent: -9999em; border-top: 8px solid rgba(255, 255, 255, 0.2); border-right: 8px solid rgba(255, 255, 255, 0.2); border-bottom: 8px solid rgba(255, 255, 255, 0.2); border-left: 8px solid var(--jp-carousel-primary-color); transform: translateZ(0px); animation: 1.1s linear 0s infinite normal none running load8; }

#jp-carousel-comment-form-spinner, #jp-carousel-comment-form-spinner::after { border-radius: 50%; width: 20px; height: 20px; }

#jp-carousel-comment-form-spinner { display: none; float: left; font-size: 10px; position: absolute; text-indent: -9999em; border-top: 4px solid rgba(255, 255, 255, 0.2); border-right: 4px solid rgba(255, 255, 255, 0.2); border-bottom: 4px solid rgba(255, 255, 255, 0.2); border-left: 4px solid var(--jp-carousel-primary-color); transform: translateZ(0px); animation: 1.1s linear 0s infinite normal none running load8; margin: 0px auto; top: calc(50% - 15px); left: 0px; bottom: 0px; right: 0px; }

@-webkit-keyframes load8 { 
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes load8 { 
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.jp-carousel-info-content-wrapper { max-width: 800px; margin: auto; }

#jp-carousel-comment-form-submit-and-info-wrapper { display: none; overflow: hidden; width: 100%; }

#jp-carousel-comment-form-commenting-as input { background: var(--jp-carousel-bg-color); border: 1px solid var(--jp-carousel-border-color); color: var(--jp-carousel-primary-subtle-color); padding: 10px; float: left; box-shadow: rgba(0, 0, 0, 0.2) 2px 2px 2px inset; border-radius: 2px; width: 285px; font: 16px / 1.4 "Helvetica Neue", sans-serif !important; }

#jp-carousel-comment-form-commenting-as input:focus { background: var(--jp-carousel-bg-faded-color); color: var(--jp-carousel-primary-subtle-color); }

#jp-carousel-comment-form-commenting-as p { margin: 22px 0px 0px; float: left; font: 400 13px / 1.7 "Helvetica Neue", sans-serif !important; }

#jp-carousel-comment-form-commenting-as fieldset { float: left; border: none; margin: 20px 0px 0px; padding: 0px; clear: both; }

#jp-carousel-comment-form-commenting-as label { margin: 0px 20px 3px 0px; float: left; width: 100px; font: 400 13px / 1.7 "Helvetica Neue", sans-serif !important; }

#jp-carousel-comment-form-button-submit { margin-top: 20px; margin-left: auto; display: block; border: solid 1px var(--jp-carousel-primary-color); background: var(--jp-carousel-bg-color); border-radius: 3px; padding: 8px 16px; font-size: 14px; color: var(--jp-carousel-primary-color); }

#jp-carousel-comment-form-button-submit:active, #jp-carousel-comment-form-button-submit:focus { background: var(--jp-carousel-primary-color); color: var(--jp-carousel-bg-color); }

#jp-carousel-comment-form-container { margin-bottom: 15px; width: 100%; margin-top: 20px; color: var(--jp-carousel-primary-subtle-color); position: relative; overflow: hidden; }

#jp-carousel-comment-post-results { display: none; overflow: auto; width: 100%; }

#jp-carousel-comment-post-results span { display: block; text-align: center; margin-top: 20px; width: 100%; overflow: auto; padding: 1em 0px; box-sizing: border-box; border-radius: 2px; border: 1px solid var(--jp-carousel-border-color); box-shadow: rgba(0, 0, 0, 0.2) 0px 0px 5px 0px inset; font: 13px / 1.4 "Helvetica Neue", sans-serif !important; }

.jp-carousel-comment-post-error { color: rgb(223, 73, 38); }

#jp-carousel-comments-closed { display: none; color: var(--jp-carousel-primary-subtle-color); }

#jp-carousel-comments-loading { display: none; color: var(--jp-carousel-primary-subtle-color); text-align: left; margin-bottom: 20px; width: 100%; bottom: 10px; margin-top: 20px; font: 400 15px / 1.7 "Helvetica Neue", sans-serif !important; }

.jp-carousel-photo-icons-container { flex: 1 1 0%; display: block; text-align: right; margin: 0px 20px 0px 30px; white-space: nowrap; }

.jp-carousel-icon-btn { padding: 16px; text-decoration: none; border: none; background: none; display: inline-block; height: 64px; }

.jp-carousel-icon { border: none; pointer-events: none; display: inline-block; line-height: 0; font-weight: 400; font-style: normal; border-radius: 4px; width: 31px; padding: 4px 3px 3px; }

.jp-carousel-icon svg { display: inline-block; }

.jp-carousel-overlay rect { fill: var(--jp-carousel-primary-color); }

.jp-carousel-selected .jp-carousel-icon { background: var(--jp-carousel-primary-color); }

.jp-carousel-selected rect { fill: var(--jp-carousel-bg-color); }

.jp-carousel-icon-comments.jp-carousel-show { display: inline-block; }

.jp-carousel-icon .jp-carousel-has-comments-indicator { display: none; font-size: 12px; vertical-align: top; margin-left: -16px; line-height: 1; padding: 2px 4px; border-radius: 4px; background: var(--jp-carousel-primary-color); color: var(--jp-carousel-bg-color); font-weight: normal; position: relative; font-family: "Helvetica Neue", sans-serif !important; }

.jp-carousel-selected .jp-carousel-icon .jp-carousel-has-comments-indicator { background: var(--jp-carousel-bg-color); color: var(--jp-carousel-primary-color); }

.jp-carousel-has-comments-indicator.jp-carousel-show { display: inline-block; }

@media only screen and (max-width: 760px) {
  .jp-carousel-overlay .swiper-container .swiper-button-next, .jp-carousel-overlay .swiper-container .swiper-button-prev { display: none !important; }
  .jp-carousel-buttons { display: none !important; }
  .jp-carousel-image-meta { box-sizing: border-box; margin-left: 0px; float: none !important; width: 100% !important; }
  .jp-carousel-close-hint { top: 10px; right: 10px; font-size: 26px !important; position: fixed !important; }
  .admin-bar .jp-carousel-close-hint { top: 40px; }
  .jp-carousel-slide img { opacity: 1; }
  .jp-carousel-wrap { background-color: var(--jp-carousel-bg-color); }
  .jp-carousel-fadeaway { display: none; }
  .jp-carousel-info > .jp-carousel-photo-info { display: none; }
  .jp-carousel-comments-wrapper > .jp-carousel-photo-info { display: block; }
  .jp-carousel-caption { overflow: visible !important; }
  .jp-carousel-info-footer .jp-carousel-photo-title-container { display: none; }
  .jp-carousel-photo-icons-container { margin: 0px 10px 0px 0px; white-space: nowrap; }
  .jp-carousel-icon-btn { padding-left: 20px; }
  .jp-carousel-pagination { padding-left: 5px; }
  .jp-carousel-pagination-container { margin-left: 25px; }
  .jp-carousel-comment .avatar { min-width: 48px; }
  #jp-carousel-comment-form-commenting-as fieldset, #jp-carousel-comment-form-commenting-as input { width: 100%; float: none; }
}
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/mu-plugins/jetpack-11.6/modules/tiled-gallery/tiled-gallery/tiled-gallery.css?ver=2012-09-21

@charset "utf-8";

.tiled-gallery { clear: both; margin: 0px 0px 20px; overflow: hidden; }

.tiled-gallery img { margin: 2px !important; }

.tiled-gallery .gallery-group { float: left; position: relative; }

.tiled-gallery .tiled-gallery-item { float: left; margin: 0px; position: relative; width: inherit; }

.tiled-gallery .gallery-row { overflow: hidden; }

.tiled-gallery .tiled-gallery-item a { background: transparent; border: none; color: inherit; margin: 0px; padding: 0px; text-decoration: none; width: auto; }

.tiled-gallery .tiled-gallery-item img, .tiled-gallery .tiled-gallery-item img:hover { background: none; border: none; box-shadow: none; max-width: 100%; padding: 0px; vertical-align: middle; }

.tiled-gallery-caption { background: rgba(255, 255, 255, 0.8); color: rgb(51, 51, 51); font-size: 13px; font-weight: 400; overflow: hidden; padding: 10px 0px; position: absolute; bottom: 0px; text-indent: 10px; text-overflow: ellipsis; width: 100%; white-space: nowrap; }

.tiled-gallery .tiled-gallery-item-small .tiled-gallery-caption { font-size: 11px; }

.widget-gallery .tiled-gallery-unresized { visibility: hidden; height: 0px; overflow: hidden; }

.tiled-gallery .tiled-gallery-item img.grayscale { position: absolute; left: 0px; top: 0px; }

.tiled-gallery .tiled-gallery-item img.grayscale:hover { opacity: 0; }

.tiled-gallery.type-circle .tiled-gallery-item img { object-fit: cover; border-radius: 50% !important; }

.tiled-gallery.type-circle .tiled-gallery-caption { display: none; }

.tiled-gallery.type-square .tiled-gallery-item img { object-fit: cover; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/themes/infomoney/css/vendor/bootstrap.min.css?ver=6.4

@charset "utf-8";

:root { --blue:#007bff; --indigo:#6610f2; --purple:#6f42c1; --pink:#e83e8c; --red:#dc3545; --orange:#fd7e14; --yellow:#ffc107; --green:#28a745; --teal:#20c997; --cyan:#17a2b8; --white:#fff; --gray:#6c757d; --gray-dark:#343a40; --primary:#007bff; --secondary:#6c757d; --success:#28a745; --info:#17a2b8; --warning:#ffc107; --danger:#dc3545; --light:#f8f9fa; --dark:#343a40; --breakpoint-xs:0; --breakpoint-sm:576px; --breakpoint-md:768px; --breakpoint-lg:992px; --breakpoint-xl:1200px; --font-family-sans-serif:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"; --font-family-monospace:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace; }

*, ::after, ::before { box-sizing: border-box; }

html { font-family: sans-serif; line-height: 1.15; text-size-adjust: 100%; -webkit-tap-highlight-color: transparent; }

article, aside, figcaption, figure, footer, header, hgroup, main, nav, section { display: block; }

body { margin: 0px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; font-size: 1rem; font-weight: 400; line-height: 1.5; color: rgb(33, 37, 41); text-align: left; background-color: rgb(255, 255, 255); }

[tabindex="-1"]:focus { outline: 0px !important; }

hr { box-sizing: content-box; height: 0px; overflow: visible; }

h1, h2, h3, h4, h5, h6 { margin-top: 0px; margin-bottom: 0.5rem; }

p { margin-top: 0px; margin-bottom: 1rem; }

abbr[data-original-title], abbr[title] { text-decoration: underline dotted; cursor: help; border-bottom: 0px; text-decoration-skip-ink: none; }

address { margin-bottom: 1rem; font-style: normal; line-height: inherit; }

dl, ol, ul { margin-top: 0px; margin-bottom: 1rem; }

ol ol, ol ul, ul ol, ul ul { margin-bottom: 0px; }

dt { font-weight: 700; }

dd { margin-bottom: 0.5rem; margin-left: 0px; }

blockquote { margin: 0px 0px 1rem; }

b, strong { font-weight: bolder; }

small { font-size: 80%; }

sub, sup { position: relative; font-size: 75%; line-height: 0; vertical-align: baseline; }

sub { bottom: -0.25em; }

sup { top: -0.5em; }

a { color: rgb(0, 123, 255); text-decoration: none; background-color: transparent; }

a:hover { color: rgb(0, 86, 179); text-decoration: underline; }

a:not([href]):not([tabindex]) { color: inherit; text-decoration: none; }

a:not([href]):not([tabindex]):focus, a:not([href]):not([tabindex]):hover { color: inherit; text-decoration: none; }

a:not([href]):not([tabindex]):focus { outline: 0px; }

code, kbd, pre, samp { font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 1em; }

pre { margin-top: 0px; margin-bottom: 1rem; overflow: auto; }

figure { margin: 0px 0px 1rem; }

img { vertical-align: middle; border-style: none; }

svg { overflow: hidden; vertical-align: middle; }

table { border-collapse: collapse; }

caption { padding-top: 0.75rem; padding-bottom: 0.75rem; color: rgb(108, 117, 125); text-align: left; caption-side: bottom; }

th { text-align: inherit; }

label { display: inline-block; margin-bottom: 0.5rem; }

button { border-radius: 0px; }

button:focus { outline: -webkit-focus-ring-color auto 5px; }

button, input, optgroup, select, textarea { margin: 0px; font-family: inherit; font-size: inherit; line-height: inherit; }

button, input { overflow: visible; }

button, select { text-transform: none; }

[type="button"], [type="reset"], [type="submit"], button { -webkit-appearance: button; }

input[type="checkbox"], input[type="radio"] { box-sizing: border-box; padding: 0px; }

input[type="date"], input[type="datetime-local"], input[type="month"], input[type="time"] { -webkit-appearance: listbox; }

textarea { overflow: auto; resize: vertical; }

fieldset { min-width: 0px; padding: 0px; margin: 0px; border: 0px; }

legend { display: block; width: 100%; max-width: 100%; padding: 0px; margin-bottom: 0.5rem; font-size: 1.5rem; line-height: inherit; color: inherit; white-space: normal; }

progress { vertical-align: baseline; }

[type="number"]::-webkit-inner-spin-button, [type="number"]::-webkit-outer-spin-button { height: auto; }

[type="search"] { outline-offset: -2px; -webkit-appearance: none; }

[type="search"]::-webkit-search-decoration { -webkit-appearance: none; }

::-webkit-file-upload-button { font: inherit; -webkit-appearance: button; }

output { display: inline-block; }

summary { display: list-item; cursor: pointer; }

template { display: none; }

[hidden] { display: none !important; }

.h1, .h2, .h3, .h4, .h5, .h6, h1, h2, h3, h4, h5, h6 { margin-bottom: 0.5rem; font-family: inherit; font-weight: 400; line-height: 1.2; color: inherit; }

.h1, h1 { font-size: 2.5rem; }

.h2, h2 { font-size: 2rem; }

.h3, h3 { font-size: 1.75rem; }

.h4, h4 { font-size: 1.5rem; }

.h5, h5 { font-size: 1.25rem; }

.h6, h6 { font-size: 1rem; }

.lead { font-size: 1.25rem; font-weight: 300; }

.display-1 { font-size: 6rem; font-weight: 300; line-height: 1.2; }

.display-2 { font-size: 5.5rem; font-weight: 300; line-height: 1.2; }

.display-3 { font-size: 4.5rem; font-weight: 300; line-height: 1.2; }

.display-4 { font-size: 3.5rem; font-weight: 300; line-height: 1.2; }

hr { margin-top: 1rem; margin-bottom: 1rem; border-width: 1px 0px 0px; border-right-style: initial; border-bottom-style: initial; border-left-style: initial; border-right-color: initial; border-bottom-color: initial; border-left-color: initial; border-image: initial; border-top-style: solid; border-top-color: rgba(0, 0, 0, 0.1); }

.small, small { font-size: 80%; font-weight: 400; }

.mark, mark { padding: 0.2em; background-color: rgb(252, 248, 227); }

.list-unstyled { padding-left: 0px; list-style: none; }

.list-inline { padding-left: 0px; list-style: none; }

.list-inline-item { display: inline-block; }

.list-inline-item:not(:last-child) { margin-right: 0.5rem; }

.initialism { font-size: 90%; text-transform: uppercase; }

.blockquote { margin-bottom: 1rem; font-size: 1.25rem; }

.blockquote-footer { display: block; font-size: 80%; color: rgb(108, 117, 125); }

.blockquote-footer::before { content: "— "; }

.img-fluid { max-width: 100%; height: auto; }

.img-thumbnail { padding: 0.25rem; background-color: rgb(255, 255, 255); border: 1px solid rgb(222, 226, 230); border-radius: 0.25rem; max-width: 100%; height: auto; }

.figure { display: inline-block; }

.figure-img { margin-bottom: 0.5rem; line-height: 1; }

.figure-caption { font-size: 90%; color: rgb(108, 117, 125); }

code { font-size: 87.5%; color: rgb(232, 62, 140); word-break: break-word; }

a > code { color: inherit; }

kbd { padding: 0.2rem 0.4rem; font-size: 87.5%; color: rgb(255, 255, 255); background-color: rgb(33, 37, 41); border-radius: 0.2rem; }

kbd kbd { padding: 0px; font-size: 100%; font-weight: 700; }

pre { display: block; font-size: 87.5%; color: rgb(33, 37, 41); }

pre code { font-size: inherit; color: inherit; word-break: normal; }

.pre-scrollable { max-height: 340px; overflow-y: scroll; }

.container { width: 100%; padding-right: 15px; padding-left: 15px; margin-right: auto; margin-left: auto; }

@media (min-width: 576px) {
  .container { max-width: 540px; }
}

@media (min-width: 768px) {
  .container { max-width: 720px; }
}

@media (min-width: 992px) {
  .container { max-width: 960px; }
}

@media (min-width: 1200px) {
  .container { max-width: 1140px; }
}

.container-fluid { width: 100%; padding-right: 15px; padding-left: 15px; margin-right: auto; margin-left: auto; }

.row { display: flex; flex-wrap: wrap; margin-right: -15px; margin-left: -15px; }

.no-gutters { margin-right: 0px; margin-left: 0px; }

.no-gutters > .col, .no-gutters > [class*="col-"] { padding-right: 0px; padding-left: 0px; }

.col, .col-1, .col-10, .col-11, .col-12, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-auto, .col-lg, .col-lg-1, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-auto, .col-md, .col-md-1, .col-md-10, .col-md-11, .col-md-12, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-auto, .col-sm, .col-sm-1, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-auto, .col-xl, .col-xl-1, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-auto { position: relative; width: 100%; padding-right: 15px; padding-left: 15px; }

.col { flex-basis: 0px; flex-grow: 1; max-width: 100%; }

.col-auto { flex: 0 0 auto; width: auto; max-width: 100%; }

.col-1 { flex: 0 0 8.33333%; max-width: 8.33333%; }

.col-2 { flex: 0 0 16.6667%; max-width: 16.6667%; }

.col-3 { flex: 0 0 25%; max-width: 25%; }

.col-4 { flex: 0 0 33.3333%; max-width: 33.3333%; }

.col-5 { flex: 0 0 41.6667%; max-width: 41.6667%; }

.col-6 { flex: 0 0 50%; max-width: 50%; }

.col-7 { flex: 0 0 58.3333%; max-width: 58.3333%; }

.col-8 { flex: 0 0 66.6667%; max-width: 66.6667%; }

.col-9 { flex: 0 0 75%; max-width: 75%; }

.col-10 { flex: 0 0 83.3333%; max-width: 83.3333%; }

.col-11 { flex: 0 0 91.6667%; max-width: 91.6667%; }

.col-12 { flex: 0 0 100%; max-width: 100%; }

.order-first { order: -1; }

.order-last { order: 13; }

.order-0 { order: 0; }

.order-1 { order: 1; }

.order-2 { order: 2; }

.order-3 { order: 3; }

.order-4 { order: 4; }

.order-5 { order: 5; }

.order-6 { order: 6; }

.order-7 { order: 7; }

.order-8 { order: 8; }

.order-9 { order: 9; }

.order-10 { order: 10; }

.order-11 { order: 11; }

.order-12 { order: 12; }

.offset-1 { margin-left: 8.33333%; }

.offset-2 { margin-left: 16.6667%; }

.offset-3 { margin-left: 25%; }

.offset-4 { margin-left: 33.3333%; }

.offset-5 { margin-left: 41.6667%; }

.offset-6 { margin-left: 50%; }

.offset-7 { margin-left: 58.3333%; }

.offset-8 { margin-left: 66.6667%; }

.offset-9 { margin-left: 75%; }

.offset-10 { margin-left: 83.3333%; }

.offset-11 { margin-left: 91.6667%; }

@media (min-width: 576px) {
  .col-sm { flex-basis: 0px; flex-grow: 1; max-width: 100%; }
  .col-sm-auto { flex: 0 0 auto; width: auto; max-width: 100%; }
  .col-sm-1 { flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-sm-2 { flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-sm-3 { flex: 0 0 25%; max-width: 25%; }
  .col-sm-4 { flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-sm-5 { flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-sm-6 { flex: 0 0 50%; max-width: 50%; }
  .col-sm-7 { flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-sm-8 { flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-sm-9 { flex: 0 0 75%; max-width: 75%; }
  .col-sm-10 { flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-sm-11 { flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-sm-12 { flex: 0 0 100%; max-width: 100%; }
  .order-sm-first { order: -1; }
  .order-sm-last { order: 13; }
  .order-sm-0 { order: 0; }
  .order-sm-1 { order: 1; }
  .order-sm-2 { order: 2; }
  .order-sm-3 { order: 3; }
  .order-sm-4 { order: 4; }
  .order-sm-5 { order: 5; }
  .order-sm-6 { order: 6; }
  .order-sm-7 { order: 7; }
  .order-sm-8 { order: 8; }
  .order-sm-9 { order: 9; }
  .order-sm-10 { order: 10; }
  .order-sm-11 { order: 11; }
  .order-sm-12 { order: 12; }
  .offset-sm-0 { margin-left: 0px; }
  .offset-sm-1 { margin-left: 8.33333%; }
  .offset-sm-2 { margin-left: 16.6667%; }
  .offset-sm-3 { margin-left: 25%; }
  .offset-sm-4 { margin-left: 33.3333%; }
  .offset-sm-5 { margin-left: 41.6667%; }
  .offset-sm-6 { margin-left: 50%; }
  .offset-sm-7 { margin-left: 58.3333%; }
  .offset-sm-8 { margin-left: 66.6667%; }
  .offset-sm-9 { margin-left: 75%; }
  .offset-sm-10 { margin-left: 83.3333%; }
  .offset-sm-11 { margin-left: 91.6667%; }
}

@media (min-width: 768px) {
  .col-md { flex-basis: 0px; flex-grow: 1; max-width: 100%; }
  .col-md-auto { flex: 0 0 auto; width: auto; max-width: 100%; }
  .col-md-1 { flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-md-2 { flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-md-3 { flex: 0 0 25%; max-width: 25%; }
  .col-md-4 { flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-md-5 { flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-md-6 { flex: 0 0 50%; max-width: 50%; }
  .col-md-7 { flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-md-8 { flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-md-9 { flex: 0 0 75%; max-width: 75%; }
  .col-md-10 { flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-md-11 { flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-md-12 { flex: 0 0 100%; max-width: 100%; }
  .order-md-first { order: -1; }
  .order-md-last { order: 13; }
  .order-md-0 { order: 0; }
  .order-md-1 { order: 1; }
  .order-md-2 { order: 2; }
  .order-md-3 { order: 3; }
  .order-md-4 { order: 4; }
  .order-md-5 { order: 5; }
  .order-md-6 { order: 6; }
  .order-md-7 { order: 7; }
  .order-md-8 { order: 8; }
  .order-md-9 { order: 9; }
  .order-md-10 { order: 10; }
  .order-md-11 { order: 11; }
  .order-md-12 { order: 12; }
  .offset-md-0 { margin-left: 0px; }
  .offset-md-1 { margin-left: 8.33333%; }
  .offset-md-2 { margin-left: 16.6667%; }
  .offset-md-3 { margin-left: 25%; }
  .offset-md-4 { margin-left: 33.3333%; }
  .offset-md-5 { margin-left: 41.6667%; }
  .offset-md-6 { margin-left: 50%; }
  .offset-md-7 { margin-left: 58.3333%; }
  .offset-md-8 { margin-left: 66.6667%; }
  .offset-md-9 { margin-left: 75%; }
  .offset-md-10 { margin-left: 83.3333%; }
  .offset-md-11 { margin-left: 91.6667%; }
}

@media (min-width: 992px) {
  .col-lg { flex-basis: 0px; flex-grow: 1; max-width: 100%; }
  .col-lg-auto { flex: 0 0 auto; width: auto; max-width: 100%; }
  .col-lg-1 { flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-lg-2 { flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-lg-3 { flex: 0 0 25%; max-width: 25%; }
  .col-lg-4 { flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-lg-5 { flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-lg-6 { flex: 0 0 50%; max-width: 50%; }
  .col-lg-7 { flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-lg-8 { flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-lg-9 { flex: 0 0 75%; max-width: 75%; }
  .col-lg-10 { flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-lg-11 { flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-lg-12 { flex: 0 0 100%; max-width: 100%; }
  .order-lg-first { order: -1; }
  .order-lg-last { order: 13; }
  .order-lg-0 { order: 0; }
  .order-lg-1 { order: 1; }
  .order-lg-2 { order: 2; }
  .order-lg-3 { order: 3; }
  .order-lg-4 { order: 4; }
  .order-lg-5 { order: 5; }
  .order-lg-6 { order: 6; }
  .order-lg-7 { order: 7; }
  .order-lg-8 { order: 8; }
  .order-lg-9 { order: 9; }
  .order-lg-10 { order: 10; }
  .order-lg-11 { order: 11; }
  .order-lg-12 { order: 12; }
  .offset-lg-0 { margin-left: 0px; }
  .offset-lg-1 { margin-left: 8.33333%; }
  .offset-lg-2 { margin-left: 16.6667%; }
  .offset-lg-3 { margin-left: 25%; }
  .offset-lg-4 { margin-left: 33.3333%; }
  .offset-lg-5 { margin-left: 41.6667%; }
  .offset-lg-6 { margin-left: 50%; }
  .offset-lg-7 { margin-left: 58.3333%; }
  .offset-lg-8 { margin-left: 66.6667%; }
  .offset-lg-9 { margin-left: 75%; }
  .offset-lg-10 { margin-left: 83.3333%; }
  .offset-lg-11 { margin-left: 91.6667%; }
}

@media (min-width: 1200px) {
  .col-xl { flex-basis: 0px; flex-grow: 1; max-width: 100%; }
  .col-xl-auto { flex: 0 0 auto; width: auto; max-width: 100%; }
  .col-xl-1 { flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-xl-2 { flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-xl-3 { flex: 0 0 25%; max-width: 25%; }
  .col-xl-4 { flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-xl-5 { flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-xl-6 { flex: 0 0 50%; max-width: 50%; }
  .col-xl-7 { flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-xl-8 { flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-xl-9 { flex: 0 0 75%; max-width: 75%; }
  .col-xl-10 { flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-xl-11 { flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-xl-12 { flex: 0 0 100%; max-width: 100%; }
  .order-xl-first { order: -1; }
  .order-xl-last { order: 13; }
  .order-xl-0 { order: 0; }
  .order-xl-1 { order: 1; }
  .order-xl-2 { order: 2; }
  .order-xl-3 { order: 3; }
  .order-xl-4 { order: 4; }
  .order-xl-5 { order: 5; }
  .order-xl-6 { order: 6; }
  .order-xl-7 { order: 7; }
  .order-xl-8 { order: 8; }
  .order-xl-9 { order: 9; }
  .order-xl-10 { order: 10; }
  .order-xl-11 { order: 11; }
  .order-xl-12 { order: 12; }
  .offset-xl-0 { margin-left: 0px; }
  .offset-xl-1 { margin-left: 8.33333%; }
  .offset-xl-2 { margin-left: 16.6667%; }
  .offset-xl-3 { margin-left: 25%; }
  .offset-xl-4 { margin-left: 33.3333%; }
  .offset-xl-5 { margin-left: 41.6667%; }
  .offset-xl-6 { margin-left: 50%; }
  .offset-xl-7 { margin-left: 58.3333%; }
  .offset-xl-8 { margin-left: 66.6667%; }
  .offset-xl-9 { margin-left: 75%; }
  .offset-xl-10 { margin-left: 83.3333%; }
  .offset-xl-11 { margin-left: 91.6667%; }
}

.table { width: 100%; margin-bottom: 1rem; background-color: transparent; }

.table td, .table th { padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230); }

.table thead th { vertical-align: bottom; border-bottom: 2px solid rgb(222, 226, 230); }

.table tbody + tbody { border-top: 2px solid rgb(222, 226, 230); }

.table .table { background-color: rgb(255, 255, 255); }

.table-sm td, .table-sm th { padding: 0.3rem; }

.table-bordered { border: 1px solid rgb(222, 226, 230); }

.table-bordered td, .table-bordered th { border: 1px solid rgb(222, 226, 230); }

.table-bordered thead td, .table-bordered thead th { border-bottom-width: 2px; }

.table-borderless tbody + tbody, .table-borderless td, .table-borderless th, .table-borderless thead th { border: 0px; }

.table-striped tbody tr:nth-of-type(2n+1) { background-color: rgba(0, 0, 0, 0.05); }

.table-hover tbody tr:hover { background-color: rgba(0, 0, 0, 0.075); }

.table-primary, .table-primary > td, .table-primary > th { background-color: rgb(184, 218, 255); }

.table-primary tbody + tbody, .table-primary td, .table-primary th, .table-primary thead th { border-color: rgb(122, 186, 255); }

.table-hover .table-primary:hover { background-color: rgb(159, 205, 255); }

.table-hover .table-primary:hover > td, .table-hover .table-primary:hover > th { background-color: rgb(159, 205, 255); }

.table-secondary, .table-secondary > td, .table-secondary > th { background-color: rgb(214, 216, 219); }

.table-secondary tbody + tbody, .table-secondary td, .table-secondary th, .table-secondary thead th { border-color: rgb(179, 183, 187); }

.table-hover .table-secondary:hover { background-color: rgb(200, 203, 207); }

.table-hover .table-secondary:hover > td, .table-hover .table-secondary:hover > th { background-color: rgb(200, 203, 207); }

.table-success, .table-success > td, .table-success > th { background-color: rgb(195, 230, 203); }

.table-success tbody + tbody, .table-success td, .table-success th, .table-success thead th { border-color: rgb(143, 209, 158); }

.table-hover .table-success:hover { background-color: rgb(177, 223, 187); }

.table-hover .table-success:hover > td, .table-hover .table-success:hover > th { background-color: rgb(177, 223, 187); }

.table-info, .table-info > td, .table-info > th { background-color: rgb(190, 229, 235); }

.table-info tbody + tbody, .table-info td, .table-info th, .table-info thead th { border-color: rgb(134, 207, 218); }

.table-hover .table-info:hover { background-color: rgb(171, 221, 229); }

.table-hover .table-info:hover > td, .table-hover .table-info:hover > th { background-color: rgb(171, 221, 229); }

.table-warning, .table-warning > td, .table-warning > th { background-color: rgb(255, 238, 186); }

.table-warning tbody + tbody, .table-warning td, .table-warning th, .table-warning thead th { border-color: rgb(255, 223, 126); }

.table-hover .table-warning:hover { background-color: rgb(255, 232, 161); }

.table-hover .table-warning:hover > td, .table-hover .table-warning:hover > th { background-color: rgb(255, 232, 161); }

.table-danger, .table-danger > td, .table-danger > th { background-color: rgb(245, 198, 203); }

.table-danger tbody + tbody, .table-danger td, .table-danger th, .table-danger thead th { border-color: rgb(237, 150, 158); }

.table-hover .table-danger:hover { background-color: rgb(241, 176, 183); }

.table-hover .table-danger:hover > td, .table-hover .table-danger:hover > th { background-color: rgb(241, 176, 183); }

.table-light, .table-light > td, .table-light > th { background-color: rgb(253, 253, 254); }

.table-light tbody + tbody, .table-light td, .table-light th, .table-light thead th { border-color: rgb(251, 252, 252); }

.table-hover .table-light:hover { background-color: rgb(236, 236, 246); }

.table-hover .table-light:hover > td, .table-hover .table-light:hover > th { background-color: rgb(236, 236, 246); }

.table-dark, .table-dark > td, .table-dark > th { background-color: rgb(198, 200, 202); }

.table-dark tbody + tbody, .table-dark td, .table-dark th, .table-dark thead th { border-color: rgb(149, 153, 156); }

.table-hover .table-dark:hover { background-color: rgb(185, 187, 190); }

.table-hover .table-dark:hover > td, .table-hover .table-dark:hover > th { background-color: rgb(185, 187, 190); }

.table-active, .table-active > td, .table-active > th { background-color: rgba(0, 0, 0, 0.075); }

.table-hover .table-active:hover { background-color: rgba(0, 0, 0, 0.075); }

.table-hover .table-active:hover > td, .table-hover .table-active:hover > th { background-color: rgba(0, 0, 0, 0.075); }

.table .thead-dark th { color: rgb(255, 255, 255); background-color: rgb(33, 37, 41); border-color: rgb(50, 56, 62); }

.table .thead-light th { color: rgb(73, 80, 87); background-color: rgb(233, 236, 239); border-color: rgb(222, 226, 230); }

.table-dark { color: rgb(255, 255, 255); background-color: rgb(33, 37, 41); }

.table-dark td, .table-dark th, .table-dark thead th { border-color: rgb(50, 56, 62); }

.table-dark.table-bordered { border: 0px; }

.table-dark.table-striped tbody tr:nth-of-type(2n+1) { background-color: rgba(255, 255, 255, 0.05); }

.table-dark.table-hover tbody tr:hover { background-color: rgba(255, 255, 255, 0.075); }

@media (max-width: 575.98px) {
  .table-responsive-sm { display: block; width: 100%; overflow-x: auto; }
  .table-responsive-sm > .table-bordered { border: 0px; }
}

@media (max-width: 767.98px) {
  .table-responsive-md { display: block; width: 100%; overflow-x: auto; }
  .table-responsive-md > .table-bordered { border: 0px; }
}

@media (max-width: 991.98px) {
  .table-responsive-lg { display: block; width: 100%; overflow-x: auto; }
  .table-responsive-lg > .table-bordered { border: 0px; }
}

@media (max-width: 1199.98px) {
  .table-responsive-xl { display: block; width: 100%; overflow-x: auto; }
  .table-responsive-xl > .table-bordered { border: 0px; }
}

.table-responsive { display: block; width: 100%; overflow-x: auto; }

.table-responsive > .table-bordered { border: 0px; }

.form-control { display: block; width: 100%; height: calc(2.25rem + 2px); padding: 0.375rem 0.75rem; font-size: 1rem; font-weight: 400; line-height: 1.5; color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .form-control { transition: none 0s ease 0s; }
}

.form-control:focus { color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); border-color: rgb(128, 189, 255); outline: 0px; box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.form-control::-webkit-input-placeholder { color: rgb(108, 117, 125); opacity: 1; }

.form-control::placeholder { color: rgb(108, 117, 125); opacity: 1; }

.form-control:disabled, .form-control[readonly] { background-color: rgb(233, 236, 239); opacity: 1; }

.form-control-file, .form-control-range { display: block; width: 100%; }

.col-form-label { padding-top: calc(0.375rem + 1px); padding-bottom: calc(0.375rem + 1px); margin-bottom: 0px; font-size: inherit; line-height: 1.5; }

.col-form-label-lg { padding-top: calc(0.5rem + 1px); padding-bottom: calc(0.5rem + 1px); font-size: 1.25rem; line-height: 1.5; }

.col-form-label-sm { padding-top: calc(0.25rem + 1px); padding-bottom: calc(0.25rem + 1px); font-size: 0.875rem; line-height: 1.5; }

.form-control-plaintext { display: block; width: 100%; padding-top: 0.375rem; padding-bottom: 0.375rem; margin-bottom: 0px; line-height: 1.5; color: rgb(33, 37, 41); background-color: transparent; border-style: solid; border-color: transparent; border-image: initial; border-width: 1px 0px; }

.form-control-plaintext.form-control-lg, .form-control-plaintext.form-control-sm { padding-right: 0px; padding-left: 0px; }

.form-control-sm { height: calc(1.8125rem + 2px); padding: 0.25rem 0.5rem; font-size: 0.875rem; line-height: 1.5; border-radius: 0.2rem; }

.form-control-lg { height: calc(2.875rem + 2px); padding: 0.5rem 1rem; font-size: 1.25rem; line-height: 1.5; border-radius: 0.3rem; }

select.form-control[multiple], select.form-control[size] { height: auto; }

textarea.form-control { height: auto; }

.form-group { margin-bottom: 1rem; }

.form-text { display: block; margin-top: 0.25rem; }

.form-row { display: flex; flex-wrap: wrap; margin-right: -5px; margin-left: -5px; }

.form-row > .col, .form-row > [class*="col-"] { padding-right: 5px; padding-left: 5px; }

.form-check { position: relative; display: block; padding-left: 1.25rem; }

.form-check-input { position: absolute; margin-top: 0.3rem; margin-left: -1.25rem; }

.form-check-input:disabled ~ .form-check-label { color: rgb(108, 117, 125); }

.form-check-label { margin-bottom: 0px; }

.form-check-inline { display: inline-flex; align-items: center; padding-left: 0px; margin-right: 0.75rem; }

.form-check-inline .form-check-input { position: static; margin-top: 0px; margin-right: 0.3125rem; margin-left: 0px; }

.valid-feedback { display: none; width: 100%; margin-top: 0.25rem; font-size: 80%; color: rgb(40, 167, 69); }

.valid-tooltip { position: absolute; top: 100%; z-index: 5; display: none; max-width: 100%; padding: 0.25rem 0.5rem; margin-top: 0.1rem; font-size: 0.875rem; line-height: 1.5; color: rgb(255, 255, 255); background-color: rgba(40, 167, 69, 0.9); border-radius: 0.25rem; }

.form-control.is-valid, .was-validated .form-control:valid { border-color: rgb(40, 167, 69); padding-right: 2.25rem; background-repeat: no-repeat; background-position: right calc(0.5625rem) center; background-size: calc(1.125rem) calc(1.125rem); background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2328a745' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e"); }

.form-control.is-valid:focus, .was-validated .form-control:valid:focus { border-color: rgb(40, 167, 69); box-shadow: rgba(40, 167, 69, 0.25) 0px 0px 0px 0.2rem; }

.form-control.is-valid ~ .valid-feedback, .form-control.is-valid ~ .valid-tooltip, .was-validated .form-control:valid ~ .valid-feedback, .was-validated .form-control:valid ~ .valid-tooltip { display: block; }

.was-validated textarea.form-control:valid, textarea.form-control.is-valid { padding-right: 2.25rem; background-position: right calc(0.5625rem) top calc(0.5625rem); }

.custom-select.is-valid, .was-validated .custom-select:valid { border-color: rgb(40, 167, 69); padding-right: 3.4375rem; background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") right 0.75rem center / 8px 10px no-repeat, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2328a745' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e") right 1.75rem center / 1.125rem 1.125rem no-repeat; }

.custom-select.is-valid:focus, .was-validated .custom-select:valid:focus { border-color: rgb(40, 167, 69); box-shadow: rgba(40, 167, 69, 0.25) 0px 0px 0px 0.2rem; }

.custom-select.is-valid ~ .valid-feedback, .custom-select.is-valid ~ .valid-tooltip, .was-validated .custom-select:valid ~ .valid-feedback, .was-validated .custom-select:valid ~ .valid-tooltip { display: block; }

.form-control-file.is-valid ~ .valid-feedback, .form-control-file.is-valid ~ .valid-tooltip, .was-validated .form-control-file:valid ~ .valid-feedback, .was-validated .form-control-file:valid ~ .valid-tooltip { display: block; }

.form-check-input.is-valid ~ .form-check-label, .was-validated .form-check-input:valid ~ .form-check-label { color: rgb(40, 167, 69); }

.form-check-input.is-valid ~ .valid-feedback, .form-check-input.is-valid ~ .valid-tooltip, .was-validated .form-check-input:valid ~ .valid-feedback, .was-validated .form-check-input:valid ~ .valid-tooltip { display: block; }

.custom-control-input.is-valid ~ .custom-control-label, .was-validated .custom-control-input:valid ~ .custom-control-label { color: rgb(40, 167, 69); }

.custom-control-input.is-valid ~ .custom-control-label::before, .was-validated .custom-control-input:valid ~ .custom-control-label::before { border-color: rgb(40, 167, 69); }

.custom-control-input.is-valid ~ .valid-feedback, .custom-control-input.is-valid ~ .valid-tooltip, .was-validated .custom-control-input:valid ~ .valid-feedback, .was-validated .custom-control-input:valid ~ .valid-tooltip { display: block; }

.custom-control-input.is-valid:checked ~ .custom-control-label::before, .was-validated .custom-control-input:valid:checked ~ .custom-control-label::before { border-color: rgb(52, 206, 87); background-color: rgb(52, 206, 87); }

.custom-control-input.is-valid:focus ~ .custom-control-label::before, .was-validated .custom-control-input:valid:focus ~ .custom-control-label::before { box-shadow: rgba(40, 167, 69, 0.25) 0px 0px 0px 0.2rem; }

.custom-control-input.is-valid:focus:not(:checked) ~ .custom-control-label::before, .was-validated .custom-control-input:valid:focus:not(:checked) ~ .custom-control-label::before { border-color: rgb(40, 167, 69); }

.custom-file-input.is-valid ~ .custom-file-label, .was-validated .custom-file-input:valid ~ .custom-file-label { border-color: rgb(40, 167, 69); }

.custom-file-input.is-valid ~ .valid-feedback, .custom-file-input.is-valid ~ .valid-tooltip, .was-validated .custom-file-input:valid ~ .valid-feedback, .was-validated .custom-file-input:valid ~ .valid-tooltip { display: block; }

.custom-file-input.is-valid:focus ~ .custom-file-label, .was-validated .custom-file-input:valid:focus ~ .custom-file-label { border-color: rgb(40, 167, 69); box-shadow: rgba(40, 167, 69, 0.25) 0px 0px 0px 0.2rem; }

.invalid-feedback { display: none; width: 100%; margin-top: 0.25rem; font-size: 80%; color: rgb(220, 53, 69); }

.invalid-tooltip { position: absolute; top: 100%; z-index: 5; display: none; max-width: 100%; padding: 0.25rem 0.5rem; margin-top: 0.1rem; font-size: 0.875rem; line-height: 1.5; color: rgb(255, 255, 255); background-color: rgba(220, 53, 69, 0.9); border-radius: 0.25rem; }

.form-control.is-invalid, .was-validated .form-control:invalid { border-color: rgb(220, 53, 69); padding-right: 2.25rem; background-repeat: no-repeat; background-position: right calc(0.5625rem) center; background-size: calc(1.125rem) calc(1.125rem); background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23dc3545' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23d9534f' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E"); }

.form-control.is-invalid:focus, .was-validated .form-control:invalid:focus { border-color: rgb(220, 53, 69); box-shadow: rgba(220, 53, 69, 0.25) 0px 0px 0px 0.2rem; }

.form-control.is-invalid ~ .invalid-feedback, .form-control.is-invalid ~ .invalid-tooltip, .was-validated .form-control:invalid ~ .invalid-feedback, .was-validated .form-control:invalid ~ .invalid-tooltip { display: block; }

.was-validated textarea.form-control:invalid, textarea.form-control.is-invalid { padding-right: 2.25rem; background-position: right calc(0.5625rem) top calc(0.5625rem); }

.custom-select.is-invalid, .was-validated .custom-select:invalid { border-color: rgb(220, 53, 69); padding-right: 3.4375rem; background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") right 0.75rem center / 8px 10px no-repeat, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23dc3545' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23d9534f' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E") right 1.75rem center / 1.125rem 1.125rem no-repeat; }

.custom-select.is-invalid:focus, .was-validated .custom-select:invalid:focus { border-color: rgb(220, 53, 69); box-shadow: rgba(220, 53, 69, 0.25) 0px 0px 0px 0.2rem; }

.custom-select.is-invalid ~ .invalid-feedback, .custom-select.is-invalid ~ .invalid-tooltip, .was-validated .custom-select:invalid ~ .invalid-feedback, .was-validated .custom-select:invalid ~ .invalid-tooltip { display: block; }

.form-control-file.is-invalid ~ .invalid-feedback, .form-control-file.is-invalid ~ .invalid-tooltip, .was-validated .form-control-file:invalid ~ .invalid-feedback, .was-validated .form-control-file:invalid ~ .invalid-tooltip { display: block; }

.form-check-input.is-invalid ~ .form-check-label, .was-validated .form-check-input:invalid ~ .form-check-label { color: rgb(220, 53, 69); }

.form-check-input.is-invalid ~ .invalid-feedback, .form-check-input.is-invalid ~ .invalid-tooltip, .was-validated .form-check-input:invalid ~ .invalid-feedback, .was-validated .form-check-input:invalid ~ .invalid-tooltip { display: block; }

.custom-control-input.is-invalid ~ .custom-control-label, .was-validated .custom-control-input:invalid ~ .custom-control-label { color: rgb(220, 53, 69); }

.custom-control-input.is-invalid ~ .custom-control-label::before, .was-validated .custom-control-input:invalid ~ .custom-control-label::before { border-color: rgb(220, 53, 69); }

.custom-control-input.is-invalid ~ .invalid-feedback, .custom-control-input.is-invalid ~ .invalid-tooltip, .was-validated .custom-control-input:invalid ~ .invalid-feedback, .was-validated .custom-control-input:invalid ~ .invalid-tooltip { display: block; }

.custom-control-input.is-invalid:checked ~ .custom-control-label::before, .was-validated .custom-control-input:invalid:checked ~ .custom-control-label::before { border-color: rgb(228, 96, 109); background-color: rgb(228, 96, 109); }

.custom-control-input.is-invalid:focus ~ .custom-control-label::before, .was-validated .custom-control-input:invalid:focus ~ .custom-control-label::before { box-shadow: rgba(220, 53, 69, 0.25) 0px 0px 0px 0.2rem; }

.custom-control-input.is-invalid:focus:not(:checked) ~ .custom-control-label::before, .was-validated .custom-control-input:invalid:focus:not(:checked) ~ .custom-control-label::before { border-color: rgb(220, 53, 69); }

.custom-file-input.is-invalid ~ .custom-file-label, .was-validated .custom-file-input:invalid ~ .custom-file-label { border-color: rgb(220, 53, 69); }

.custom-file-input.is-invalid ~ .invalid-feedback, .custom-file-input.is-invalid ~ .invalid-tooltip, .was-validated .custom-file-input:invalid ~ .invalid-feedback, .was-validated .custom-file-input:invalid ~ .invalid-tooltip { display: block; }

.custom-file-input.is-invalid:focus ~ .custom-file-label, .was-validated .custom-file-input:invalid:focus ~ .custom-file-label { border-color: rgb(220, 53, 69); box-shadow: rgba(220, 53, 69, 0.25) 0px 0px 0px 0.2rem; }

.form-inline { display: flex; flex-flow: row wrap; align-items: center; }

.form-inline .form-check { width: 100%; }

@media (min-width: 576px) {
  .form-inline label { display: flex; align-items: center; justify-content: center; margin-bottom: 0px; }
  .form-inline .form-group { display: flex; flex: 0 0 auto; flex-flow: row wrap; align-items: center; margin-bottom: 0px; }
  .form-inline .form-control { display: inline-block; width: auto; vertical-align: middle; }
  .form-inline .form-control-plaintext { display: inline-block; }
  .form-inline .custom-select, .form-inline .input-group { width: auto; }
  .form-inline .form-check { display: flex; align-items: center; justify-content: center; width: auto; padding-left: 0px; }
  .form-inline .form-check-input { position: relative; margin-top: 0px; margin-right: 0.25rem; margin-left: 0px; }
  .form-inline .custom-control { align-items: center; justify-content: center; }
  .form-inline .custom-control-label { margin-bottom: 0px; }
}

.btn { display: inline-block; font-weight: 400; color: rgb(33, 37, 41); text-align: center; vertical-align: middle; user-select: none; background-color: transparent; border: 1px solid transparent; padding: 0.375rem 0.75rem; font-size: 1rem; line-height: 1.5; border-radius: 0.25rem; transition: color 0.15s ease-in-out 0s, background-color 0.15s ease-in-out 0s, border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .btn { transition: none 0s ease 0s; }
}

.btn:hover { color: rgb(33, 37, 41); text-decoration: none; }

.btn.focus, .btn:focus { outline: 0px; box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.btn.disabled, .btn:disabled { opacity: 0.65; }

.btn:not(:disabled):not(.disabled) { cursor: pointer; }

a.btn.disabled, fieldset:disabled a.btn { pointer-events: none; }

.btn-primary { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-primary:hover { color: rgb(255, 255, 255); background-color: rgb(0, 105, 217); border-color: rgb(0, 98, 204); }

.btn-primary.focus, .btn-primary:focus { box-shadow: rgba(38, 143, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-primary.disabled, .btn-primary:disabled { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-primary:not(:disabled):not(.disabled).active, .btn-primary:not(:disabled):not(.disabled):active, .show > .btn-primary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(0, 98, 204); border-color: rgb(0, 92, 191); }

.btn-primary:not(:disabled):not(.disabled).active:focus, .btn-primary:not(:disabled):not(.disabled):active:focus, .show > .btn-primary.dropdown-toggle:focus { box-shadow: rgba(38, 143, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-secondary { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-secondary:hover { color: rgb(255, 255, 255); background-color: rgb(90, 98, 104); border-color: rgb(84, 91, 98); }

.btn-secondary.focus, .btn-secondary:focus { box-shadow: rgba(130, 138, 145, 0.5) 0px 0px 0px 0.2rem; }

.btn-secondary.disabled, .btn-secondary:disabled { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-secondary:not(:disabled):not(.disabled).active, .btn-secondary:not(:disabled):not(.disabled):active, .show > .btn-secondary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(84, 91, 98); border-color: rgb(78, 85, 91); }

.btn-secondary:not(:disabled):not(.disabled).active:focus, .btn-secondary:not(:disabled):not(.disabled):active:focus, .show > .btn-secondary.dropdown-toggle:focus { box-shadow: rgba(130, 138, 145, 0.5) 0px 0px 0px 0.2rem; }

.btn-success { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-success:hover { color: rgb(255, 255, 255); background-color: rgb(33, 136, 56); border-color: rgb(30, 126, 52); }

.btn-success.focus, .btn-success:focus { box-shadow: rgba(72, 180, 97, 0.5) 0px 0px 0px 0.2rem; }

.btn-success.disabled, .btn-success:disabled { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-success:not(:disabled):not(.disabled).active, .btn-success:not(:disabled):not(.disabled):active, .show > .btn-success.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(30, 126, 52); border-color: rgb(28, 116, 48); }

.btn-success:not(:disabled):not(.disabled).active:focus, .btn-success:not(:disabled):not(.disabled):active:focus, .show > .btn-success.dropdown-toggle:focus { box-shadow: rgba(72, 180, 97, 0.5) 0px 0px 0px 0.2rem; }

.btn-info { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-info:hover { color: rgb(255, 255, 255); background-color: rgb(19, 132, 150); border-color: rgb(17, 122, 139); }

.btn-info.focus, .btn-info:focus { box-shadow: rgba(58, 176, 195, 0.5) 0px 0px 0px 0.2rem; }

.btn-info.disabled, .btn-info:disabled { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-info:not(:disabled):not(.disabled).active, .btn-info:not(:disabled):not(.disabled):active, .show > .btn-info.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(17, 122, 139); border-color: rgb(16, 112, 127); }

.btn-info:not(:disabled):not(.disabled).active:focus, .btn-info:not(:disabled):not(.disabled):active:focus, .show > .btn-info.dropdown-toggle:focus { box-shadow: rgba(58, 176, 195, 0.5) 0px 0px 0px 0.2rem; }

.btn-warning { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-warning:hover { color: rgb(33, 37, 41); background-color: rgb(224, 168, 0); border-color: rgb(211, 158, 0); }

.btn-warning.focus, .btn-warning:focus { box-shadow: rgba(222, 170, 12, 0.5) 0px 0px 0px 0.2rem; }

.btn-warning.disabled, .btn-warning:disabled { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-warning:not(:disabled):not(.disabled).active, .btn-warning:not(:disabled):not(.disabled):active, .show > .btn-warning.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(211, 158, 0); border-color: rgb(198, 149, 0); }

.btn-warning:not(:disabled):not(.disabled).active:focus, .btn-warning:not(:disabled):not(.disabled):active:focus, .show > .btn-warning.dropdown-toggle:focus { box-shadow: rgba(222, 170, 12, 0.5) 0px 0px 0px 0.2rem; }

.btn-danger { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-danger:hover { color: rgb(255, 255, 255); background-color: rgb(200, 35, 51); border-color: rgb(189, 33, 48); }

.btn-danger.focus, .btn-danger:focus { box-shadow: rgba(225, 83, 97, 0.5) 0px 0px 0px 0.2rem; }

.btn-danger.disabled, .btn-danger:disabled { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-danger:not(:disabled):not(.disabled).active, .btn-danger:not(:disabled):not(.disabled):active, .show > .btn-danger.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(189, 33, 48); border-color: rgb(178, 31, 45); }

.btn-danger:not(:disabled):not(.disabled).active:focus, .btn-danger:not(:disabled):not(.disabled):active:focus, .show > .btn-danger.dropdown-toggle:focus { box-shadow: rgba(225, 83, 97, 0.5) 0px 0px 0px 0.2rem; }

.btn-light { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-light:hover { color: rgb(33, 37, 41); background-color: rgb(226, 230, 234); border-color: rgb(218, 224, 229); }

.btn-light.focus, .btn-light:focus { box-shadow: rgba(216, 217, 219, 0.5) 0px 0px 0px 0.2rem; }

.btn-light.disabled, .btn-light:disabled { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-light:not(:disabled):not(.disabled).active, .btn-light:not(:disabled):not(.disabled):active, .show > .btn-light.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(218, 224, 229); border-color: rgb(211, 217, 223); }

.btn-light:not(:disabled):not(.disabled).active:focus, .btn-light:not(:disabled):not(.disabled):active:focus, .show > .btn-light.dropdown-toggle:focus { box-shadow: rgba(216, 217, 219, 0.5) 0px 0px 0px 0.2rem; }

.btn-dark { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-dark:hover { color: rgb(255, 255, 255); background-color: rgb(35, 39, 43); border-color: rgb(29, 33, 36); }

.btn-dark.focus, .btn-dark:focus { box-shadow: rgba(82, 88, 93, 0.5) 0px 0px 0px 0.2rem; }

.btn-dark.disabled, .btn-dark:disabled { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-dark:not(:disabled):not(.disabled).active, .btn-dark:not(:disabled):not(.disabled):active, .show > .btn-dark.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(29, 33, 36); border-color: rgb(23, 26, 29); }

.btn-dark:not(:disabled):not(.disabled).active:focus, .btn-dark:not(:disabled):not(.disabled):active:focus, .show > .btn-dark.dropdown-toggle:focus { box-shadow: rgba(82, 88, 93, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-primary { color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-outline-primary:hover { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-outline-primary.focus, .btn-outline-primary:focus { box-shadow: rgba(0, 123, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-primary.disabled, .btn-outline-primary:disabled { color: rgb(0, 123, 255); background-color: transparent; }

.btn-outline-primary:not(:disabled):not(.disabled).active, .btn-outline-primary:not(:disabled):not(.disabled):active, .show > .btn-outline-primary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-outline-primary:not(:disabled):not(.disabled).active:focus, .btn-outline-primary:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-primary.dropdown-toggle:focus { box-shadow: rgba(0, 123, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-secondary { color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-outline-secondary:hover { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-outline-secondary.focus, .btn-outline-secondary:focus { box-shadow: rgba(108, 117, 125, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-secondary.disabled, .btn-outline-secondary:disabled { color: rgb(108, 117, 125); background-color: transparent; }

.btn-outline-secondary:not(:disabled):not(.disabled).active, .btn-outline-secondary:not(:disabled):not(.disabled):active, .show > .btn-outline-secondary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-outline-secondary:not(:disabled):not(.disabled).active:focus, .btn-outline-secondary:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-secondary.dropdown-toggle:focus { box-shadow: rgba(108, 117, 125, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-success { color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-outline-success:hover { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-outline-success.focus, .btn-outline-success:focus { box-shadow: rgba(40, 167, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-success.disabled, .btn-outline-success:disabled { color: rgb(40, 167, 69); background-color: transparent; }

.btn-outline-success:not(:disabled):not(.disabled).active, .btn-outline-success:not(:disabled):not(.disabled):active, .show > .btn-outline-success.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-outline-success:not(:disabled):not(.disabled).active:focus, .btn-outline-success:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-success.dropdown-toggle:focus { box-shadow: rgba(40, 167, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-info { color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-outline-info:hover { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-outline-info.focus, .btn-outline-info:focus { box-shadow: rgba(23, 162, 184, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-info.disabled, .btn-outline-info:disabled { color: rgb(23, 162, 184); background-color: transparent; }

.btn-outline-info:not(:disabled):not(.disabled).active, .btn-outline-info:not(:disabled):not(.disabled):active, .show > .btn-outline-info.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-outline-info:not(:disabled):not(.disabled).active:focus, .btn-outline-info:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-info.dropdown-toggle:focus { box-shadow: rgba(23, 162, 184, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-warning { color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-outline-warning:hover { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-outline-warning.focus, .btn-outline-warning:focus { box-shadow: rgba(255, 193, 7, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-warning.disabled, .btn-outline-warning:disabled { color: rgb(255, 193, 7); background-color: transparent; }

.btn-outline-warning:not(:disabled):not(.disabled).active, .btn-outline-warning:not(:disabled):not(.disabled):active, .show > .btn-outline-warning.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-outline-warning:not(:disabled):not(.disabled).active:focus, .btn-outline-warning:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-warning.dropdown-toggle:focus { box-shadow: rgba(255, 193, 7, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-danger { color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-outline-danger:hover { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-outline-danger.focus, .btn-outline-danger:focus { box-shadow: rgba(220, 53, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-danger.disabled, .btn-outline-danger:disabled { color: rgb(220, 53, 69); background-color: transparent; }

.btn-outline-danger:not(:disabled):not(.disabled).active, .btn-outline-danger:not(:disabled):not(.disabled):active, .show > .btn-outline-danger.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-outline-danger:not(:disabled):not(.disabled).active:focus, .btn-outline-danger:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-danger.dropdown-toggle:focus { box-shadow: rgba(220, 53, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-light { color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-outline-light:hover { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-outline-light.focus, .btn-outline-light:focus { box-shadow: rgba(248, 249, 250, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-light.disabled, .btn-outline-light:disabled { color: rgb(248, 249, 250); background-color: transparent; }

.btn-outline-light:not(:disabled):not(.disabled).active, .btn-outline-light:not(:disabled):not(.disabled):active, .show > .btn-outline-light.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-outline-light:not(:disabled):not(.disabled).active:focus, .btn-outline-light:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-light.dropdown-toggle:focus { box-shadow: rgba(248, 249, 250, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-dark { color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-outline-dark:hover { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-outline-dark.focus, .btn-outline-dark:focus { box-shadow: rgba(52, 58, 64, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-dark.disabled, .btn-outline-dark:disabled { color: rgb(52, 58, 64); background-color: transparent; }

.btn-outline-dark:not(:disabled):not(.disabled).active, .btn-outline-dark:not(:disabled):not(.disabled):active, .show > .btn-outline-dark.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-outline-dark:not(:disabled):not(.disabled).active:focus, .btn-outline-dark:not(:disabled):not(.disabled):active:focus, .show > .btn-outline-dark.dropdown-toggle:focus { box-shadow: rgba(52, 58, 64, 0.5) 0px 0px 0px 0.2rem; }

.btn-link { font-weight: 400; color: rgb(0, 123, 255); }

.btn-link:hover { color: rgb(0, 86, 179); text-decoration: underline; }

.btn-link.focus, .btn-link:focus { text-decoration: underline; box-shadow: none; }

.btn-link.disabled, .btn-link:disabled { color: rgb(108, 117, 125); pointer-events: none; }

.btn-group-lg > .btn, .btn-lg { padding: 0.5rem 1rem; font-size: 1.25rem; line-height: 1.5; border-radius: 0.3rem; }

.btn-group-sm > .btn, .btn-sm { padding: 0.25rem 0.5rem; font-size: 0.875rem; line-height: 1.5; border-radius: 0.2rem; }

.btn-block { display: block; width: 100%; }

.btn-block + .btn-block { margin-top: 0.5rem; }

input[type="button"].btn-block, input[type="reset"].btn-block, input[type="submit"].btn-block { width: 100%; }

.fade { transition: opacity 0.15s linear 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .fade { transition: none 0s ease 0s; }
}

.fade:not(.show) { opacity: 0; }

.collapse:not(.show) { display: none; }

.collapsing { position: relative; height: 0px; overflow: hidden; transition: height 0.35s ease 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .collapsing { transition: none 0s ease 0s; }
}

.dropdown, .dropleft, .dropright, .dropup { position: relative; }

.dropdown-toggle::after { display: inline-block; margin-left: 0.255em; vertical-align: 0.255em; content: ""; border-width: 0.3em 0.3em 0px; border-top-style: solid; border-top-color: initial; border-right-style: solid; border-right-color: transparent; border-bottom-style: initial; border-bottom-color: initial; border-left-style: solid; border-left-color: transparent; }

.dropdown-toggle:empty::after { margin-left: 0px; }

.dropdown-menu { position: absolute; top: 100%; left: 0px; z-index: 1000; display: none; float: left; min-width: 10rem; padding: 0.5rem 0px; margin: 0.125rem 0px 0px; font-size: 1rem; color: rgb(33, 37, 41); text-align: left; list-style: none; background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgba(0, 0, 0, 0.15); border-radius: 0.25rem; }

.dropdown-menu-right { right: 0px; left: auto; }

@media (min-width: 576px) {
  .dropdown-menu-sm-right { right: 0px; left: auto; }
}

@media (min-width: 768px) {
  .dropdown-menu-md-right { right: 0px; left: auto; }
}

@media (min-width: 992px) {
  .dropdown-menu-lg-right { right: 0px; left: auto; }
}

@media (min-width: 1200px) {
  .dropdown-menu-xl-right { right: 0px; left: auto; }
}

.dropdown-menu-left { right: auto; left: 0px; }

@media (min-width: 576px) {
  .dropdown-menu-sm-left { right: auto; left: 0px; }
}

@media (min-width: 768px) {
  .dropdown-menu-md-left { right: auto; left: 0px; }
}

@media (min-width: 992px) {
  .dropdown-menu-lg-left { right: auto; left: 0px; }
}

@media (min-width: 1200px) {
  .dropdown-menu-xl-left { right: auto; left: 0px; }
}

.dropup .dropdown-menu { top: auto; bottom: 100%; margin-top: 0px; margin-bottom: 0.125rem; }

.dropup .dropdown-toggle::after { display: inline-block; margin-left: 0.255em; vertical-align: 0.255em; content: ""; border-width: 0px 0.3em 0.3em; border-top-style: initial; border-top-color: initial; border-right-style: solid; border-right-color: transparent; border-bottom-style: solid; border-bottom-color: initial; border-left-style: solid; border-left-color: transparent; }

.dropup .dropdown-toggle:empty::after { margin-left: 0px; }

.dropright .dropdown-menu { top: 0px; right: auto; left: 100%; margin-top: 0px; margin-left: 0.125rem; }

.dropright .dropdown-toggle::after { display: inline-block; margin-left: 0.255em; vertical-align: 0.255em; content: ""; border-width: 0.3em 0px 0.3em 0.3em; border-top-style: solid; border-top-color: transparent; border-right-style: initial; border-right-color: initial; border-bottom-style: solid; border-bottom-color: transparent; border-left-style: solid; border-left-color: initial; }

.dropright .dropdown-toggle:empty::after { margin-left: 0px; }

.dropright .dropdown-toggle::after { vertical-align: 0px; }

.dropleft .dropdown-menu { top: 0px; right: 100%; left: auto; margin-top: 0px; margin-right: 0.125rem; }

.dropleft .dropdown-toggle::after { display: inline-block; margin-left: 0.255em; vertical-align: 0.255em; content: ""; }

.dropleft .dropdown-toggle::after { display: none; }

.dropleft .dropdown-toggle::before { display: inline-block; margin-right: 0.255em; vertical-align: 0.255em; content: ""; border-top: 0.3em solid transparent; border-right: 0.3em solid; border-bottom: 0.3em solid transparent; }

.dropleft .dropdown-toggle:empty::after { margin-left: 0px; }

.dropleft .dropdown-toggle::before { vertical-align: 0px; }

.dropdown-menu[x-placement^="bottom"], .dropdown-menu[x-placement^="left"], .dropdown-menu[x-placement^="right"], .dropdown-menu[x-placement^="top"] { right: auto; bottom: auto; }

.dropdown-divider { height: 0px; margin: 0.5rem 0px; overflow: hidden; border-top: 1px solid rgb(233, 236, 239); }

.dropdown-item { display: block; width: 100%; padding: 0.25rem 1.5rem; clear: both; font-weight: 400; color: rgb(33, 37, 41); text-align: inherit; white-space: nowrap; background-color: transparent; border: 0px; }

.dropdown-item:first-child { border-top-left-radius: calc(0.25rem - 1px); border-top-right-radius: calc(0.25rem - 1px); }

.dropdown-item:last-child { border-bottom-right-radius: calc(0.25rem - 1px); border-bottom-left-radius: calc(0.25rem - 1px); }

.dropdown-item:focus, .dropdown-item:hover { color: rgb(22, 24, 27); text-decoration: none; background-color: rgb(248, 249, 250); }

.dropdown-item.active, .dropdown-item:active { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(0, 123, 255); }

.dropdown-item.disabled, .dropdown-item:disabled { color: rgb(108, 117, 125); pointer-events: none; background-color: transparent; }

.dropdown-menu.show { display: block; }

.dropdown-header { display: block; padding: 0.5rem 1.5rem; margin-bottom: 0px; font-size: 0.875rem; color: rgb(108, 117, 125); white-space: nowrap; }

.dropdown-item-text { display: block; padding: 0.25rem 1.5rem; color: rgb(33, 37, 41); }

.btn-group, .btn-group-vertical { position: relative; display: inline-flex; vertical-align: middle; }

.btn-group-vertical > .btn, .btn-group > .btn { position: relative; flex: 1 1 auto; }

.btn-group-vertical > .btn:hover, .btn-group > .btn:hover { z-index: 1; }

.btn-group-vertical > .btn.active, .btn-group-vertical > .btn:active, .btn-group-vertical > .btn:focus, .btn-group > .btn.active, .btn-group > .btn:active, .btn-group > .btn:focus { z-index: 1; }

.btn-toolbar { display: flex; flex-wrap: wrap; justify-content: flex-start; }

.btn-toolbar .input-group { width: auto; }

.btn-group > .btn-group:not(:first-child), .btn-group > .btn:not(:first-child) { margin-left: -1px; }

.btn-group > .btn-group:not(:last-child) > .btn, .btn-group > .btn:not(:last-child):not(.dropdown-toggle) { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.btn-group > .btn-group:not(:first-child) > .btn, .btn-group > .btn:not(:first-child) { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.dropdown-toggle-split { padding-right: 0.5625rem; padding-left: 0.5625rem; }

.dropdown-toggle-split::after, .dropright .dropdown-toggle-split::after, .dropup .dropdown-toggle-split::after { margin-left: 0px; }

.dropleft .dropdown-toggle-split::before { margin-right: 0px; }

.btn-group-sm > .btn + .dropdown-toggle-split, .btn-sm + .dropdown-toggle-split { padding-right: 0.375rem; padding-left: 0.375rem; }

.btn-group-lg > .btn + .dropdown-toggle-split, .btn-lg + .dropdown-toggle-split { padding-right: 0.75rem; padding-left: 0.75rem; }

.btn-group-vertical { flex-direction: column; align-items: flex-start; justify-content: center; }

.btn-group-vertical > .btn, .btn-group-vertical > .btn-group { width: 100%; }

.btn-group-vertical > .btn-group:not(:first-child), .btn-group-vertical > .btn:not(:first-child) { margin-top: -1px; }

.btn-group-vertical > .btn-group:not(:last-child) > .btn, .btn-group-vertical > .btn:not(:last-child):not(.dropdown-toggle) { border-bottom-right-radius: 0px; border-bottom-left-radius: 0px; }

.btn-group-vertical > .btn-group:not(:first-child) > .btn, .btn-group-vertical > .btn:not(:first-child) { border-top-left-radius: 0px; border-top-right-radius: 0px; }

.btn-group-toggle > .btn, .btn-group-toggle > .btn-group > .btn { margin-bottom: 0px; }

.btn-group-toggle > .btn input[type="checkbox"], .btn-group-toggle > .btn input[type="radio"], .btn-group-toggle > .btn-group > .btn input[type="checkbox"], .btn-group-toggle > .btn-group > .btn input[type="radio"] { position: absolute; clip: rect(0px, 0px, 0px, 0px); pointer-events: none; }

.input-group { position: relative; display: flex; flex-wrap: wrap; align-items: stretch; width: 100%; }

.input-group > .custom-file, .input-group > .custom-select, .input-group > .form-control, .input-group > .form-control-plaintext { position: relative; flex: 1 1 auto; width: 1%; margin-bottom: 0px; }

.input-group > .custom-file + .custom-file, .input-group > .custom-file + .custom-select, .input-group > .custom-file + .form-control, .input-group > .custom-select + .custom-file, .input-group > .custom-select + .custom-select, .input-group > .custom-select + .form-control, .input-group > .form-control + .custom-file, .input-group > .form-control + .custom-select, .input-group > .form-control + .form-control, .input-group > .form-control-plaintext + .custom-file, .input-group > .form-control-plaintext + .custom-select, .input-group > .form-control-plaintext + .form-control { margin-left: -1px; }

.input-group > .custom-file .custom-file-input:focus ~ .custom-file-label, .input-group > .custom-select:focus, .input-group > .form-control:focus { z-index: 3; }

.input-group > .custom-file .custom-file-input:focus { z-index: 4; }

.input-group > .custom-select:not(:last-child), .input-group > .form-control:not(:last-child) { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.input-group > .custom-select:not(:first-child), .input-group > .form-control:not(:first-child) { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.input-group > .custom-file { display: flex; align-items: center; }

.input-group > .custom-file:not(:last-child) .custom-file-label, .input-group > .custom-file:not(:last-child) .custom-file-label::after { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.input-group > .custom-file:not(:first-child) .custom-file-label { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.input-group-append, .input-group-prepend { display: flex; }

.input-group-append .btn, .input-group-prepend .btn { position: relative; z-index: 2; }

.input-group-append .btn:focus, .input-group-prepend .btn:focus { z-index: 3; }

.input-group-append .btn + .btn, .input-group-append .btn + .input-group-text, .input-group-append .input-group-text + .btn, .input-group-append .input-group-text + .input-group-text, .input-group-prepend .btn + .btn, .input-group-prepend .btn + .input-group-text, .input-group-prepend .input-group-text + .btn, .input-group-prepend .input-group-text + .input-group-text { margin-left: -1px; }

.input-group-prepend { margin-right: -1px; }

.input-group-append { margin-left: -1px; }

.input-group-text { display: flex; align-items: center; padding: 0.375rem 0.75rem; margin-bottom: 0px; font-size: 1rem; font-weight: 400; line-height: 1.5; color: rgb(73, 80, 87); text-align: center; white-space: nowrap; background-color: rgb(233, 236, 239); border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; }

.input-group-text input[type="checkbox"], .input-group-text input[type="radio"] { margin-top: 0px; }

.input-group-lg > .custom-select, .input-group-lg > .form-control:not(textarea) { height: calc(2.875rem + 2px); }

.input-group-lg > .custom-select, .input-group-lg > .form-control, .input-group-lg > .input-group-append > .btn, .input-group-lg > .input-group-append > .input-group-text, .input-group-lg > .input-group-prepend > .btn, .input-group-lg > .input-group-prepend > .input-group-text { padding: 0.5rem 1rem; font-size: 1.25rem; line-height: 1.5; border-radius: 0.3rem; }

.input-group-sm > .custom-select, .input-group-sm > .form-control:not(textarea) { height: calc(1.8125rem + 2px); }

.input-group-sm > .custom-select, .input-group-sm > .form-control, .input-group-sm > .input-group-append > .btn, .input-group-sm > .input-group-append > .input-group-text, .input-group-sm > .input-group-prepend > .btn, .input-group-sm > .input-group-prepend > .input-group-text { padding: 0.25rem 0.5rem; font-size: 0.875rem; line-height: 1.5; border-radius: 0.2rem; }

.input-group-lg > .custom-select, .input-group-sm > .custom-select { padding-right: 1.75rem; }

.input-group > .input-group-append:last-child > .btn:not(:last-child):not(.dropdown-toggle), .input-group > .input-group-append:last-child > .input-group-text:not(:last-child), .input-group > .input-group-append:not(:last-child) > .btn, .input-group > .input-group-append:not(:last-child) > .input-group-text, .input-group > .input-group-prepend > .btn, .input-group > .input-group-prepend > .input-group-text { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.input-group > .input-group-append > .btn, .input-group > .input-group-append > .input-group-text, .input-group > .input-group-prepend:first-child > .btn:not(:first-child), .input-group > .input-group-prepend:first-child > .input-group-text:not(:first-child), .input-group > .input-group-prepend:not(:first-child) > .btn, .input-group > .input-group-prepend:not(:first-child) > .input-group-text { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.custom-control { position: relative; display: block; min-height: 1.5rem; padding-left: 1.5rem; }

.custom-control-inline { display: inline-flex; margin-right: 1rem; }

.custom-control-input { position: absolute; z-index: -1; opacity: 0; }

.custom-control-input:checked ~ .custom-control-label::before { color: rgb(255, 255, 255); border-color: rgb(0, 123, 255); background-color: rgb(0, 123, 255); }

.custom-control-input:focus ~ .custom-control-label::before { box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.custom-control-input:focus:not(:checked) ~ .custom-control-label::before { border-color: rgb(128, 189, 255); }

.custom-control-input:not(:disabled):active ~ .custom-control-label::before { color: rgb(255, 255, 255); background-color: rgb(179, 215, 255); border-color: rgb(179, 215, 255); }

.custom-control-input:disabled ~ .custom-control-label { color: rgb(108, 117, 125); }

.custom-control-input:disabled ~ .custom-control-label::before { background-color: rgb(233, 236, 239); }

.custom-control-label { position: relative; margin-bottom: 0px; vertical-align: top; }

.custom-control-label::before { position: absolute; top: 0.25rem; left: -1.5rem; display: block; width: 1rem; height: 1rem; pointer-events: none; content: ""; background-color: rgb(255, 255, 255); border: 1px solid rgb(173, 181, 189); }

.custom-control-label::after { position: absolute; top: 0.25rem; left: -1.5rem; display: block; width: 1rem; height: 1rem; content: ""; background-repeat: no-repeat; background-position: center center; background-size: 50% 50%; }

.custom-checkbox .custom-control-label::before { border-radius: 0.25rem; }

.custom-checkbox .custom-control-input:checked ~ .custom-control-label::after { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3e%3c/svg%3e"); }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::before { border-color: rgb(0, 123, 255); background-color: rgb(0, 123, 255); }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::after { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3e%3cpath stroke='%23fff' d='M0 2h4'/%3e%3c/svg%3e"); }

.custom-checkbox .custom-control-input:disabled:checked ~ .custom-control-label::before { background-color: rgba(0, 123, 255, 0.5); }

.custom-checkbox .custom-control-input:disabled:indeterminate ~ .custom-control-label::before { background-color: rgba(0, 123, 255, 0.5); }

.custom-radio .custom-control-label::before { border-radius: 50%; }

.custom-radio .custom-control-input:checked ~ .custom-control-label::after { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e"); }

.custom-radio .custom-control-input:disabled:checked ~ .custom-control-label::before { background-color: rgba(0, 123, 255, 0.5); }

.custom-switch { padding-left: 2.25rem; }

.custom-switch .custom-control-label::before { left: -2.25rem; width: 1.75rem; pointer-events: all; border-radius: 0.5rem; }

.custom-switch .custom-control-label::after { top: calc(0.25rem + 2px); left: calc(-2.25rem + 2px); width: calc(1rem - 4px); height: calc(1rem - 4px); background-color: rgb(173, 181, 189); border-radius: 0.5rem; transition: transform 0.15s ease-in-out 0s, background-color 0.15s ease-in-out 0s, border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s, -webkit-transform 0.15s ease-in-out 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .custom-switch .custom-control-label::after { transition: none 0s ease 0s; }
}

.custom-switch .custom-control-input:checked ~ .custom-control-label::after { background-color: rgb(255, 255, 255); transform: translateX(0.75rem); }

.custom-switch .custom-control-input:disabled:checked ~ .custom-control-label::before { background-color: rgba(0, 123, 255, 0.5); }

.custom-select { display: inline-block; width: 100%; height: calc(2.25rem + 2px); padding: 0.375rem 1.75rem 0.375rem 0.75rem; font-weight: 400; line-height: 1.5; color: rgb(73, 80, 87); vertical-align: middle; background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") right 0.75rem center / 8px 10px no-repeat rgb(255, 255, 255); border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; -webkit-appearance: none; }

.custom-select:focus { border-color: rgb(128, 189, 255); outline: 0px; box-shadow: rgba(128, 189, 255, 0.5) 0px 0px 0px 0.2rem; }

.custom-select[multiple], .custom-select[size]:not([size="1"]) { height: auto; padding-right: 0.75rem; background-image: none; }

.custom-select:disabled { color: rgb(108, 117, 125); background-color: rgb(233, 236, 239); }

.custom-select-sm { height: calc(1.8125rem + 2px); padding-top: 0.25rem; padding-bottom: 0.25rem; padding-left: 0.5rem; font-size: 0.875rem; }

.custom-select-lg { height: calc(2.875rem + 2px); padding-top: 0.5rem; padding-bottom: 0.5rem; padding-left: 1rem; font-size: 1.25rem; }

.custom-file { position: relative; display: inline-block; width: 100%; height: calc(2.25rem + 2px); margin-bottom: 0px; }

.custom-file-input { position: relative; z-index: 2; width: 100%; height: calc(2.25rem + 2px); margin: 0px; opacity: 0; }

.custom-file-input:focus ~ .custom-file-label { border-color: rgb(128, 189, 255); box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.custom-file-input:disabled ~ .custom-file-label { background-color: rgb(233, 236, 239); }

.custom-file-input:lang(en) ~ .custom-file-label::after { content: "Browse"; }

.custom-file-input ~ .custom-file-label[data-browse]::after { content: attr(data-browse); }

.custom-file-label { position: absolute; top: 0px; right: 0px; left: 0px; z-index: 1; height: calc(2.25rem + 2px); padding: 0.375rem 0.75rem; font-weight: 400; line-height: 1.5; color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; }

.custom-file-label::after { position: absolute; top: 0px; right: 0px; bottom: 0px; z-index: 3; display: block; height: 2.25rem; padding: 0.375rem 0.75rem; line-height: 1.5; color: rgb(73, 80, 87); content: "Browse"; background-color: rgb(233, 236, 239); border-left: inherit; border-radius: 0px 0.25rem 0.25rem 0px; }

.custom-range { width: 100%; height: calc(1.4rem); padding: 0px; background-color: transparent; -webkit-appearance: none; }

.custom-range:focus { outline: 0px; }

.custom-range:focus::-webkit-slider-thumb { box-shadow: rgb(255, 255, 255) 0px 0px 0px 1px, rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.custom-range::-webkit-slider-thumb { width: 1rem; height: 1rem; margin-top: -0.25rem; background-color: rgb(0, 123, 255); border: 0px; border-radius: 1rem; transition: background-color 0.15s ease-in-out 0s, border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s; -webkit-appearance: none; }

@media screen and (prefers-reduced-motion: reduce) {
  .custom-range::-webkit-slider-thumb { transition: none 0s ease 0s; }
}

.custom-range::-webkit-slider-thumb:active { background-color: rgb(179, 215, 255); }

.custom-range::-webkit-slider-runnable-track { width: 100%; height: 0.5rem; color: transparent; cursor: pointer; background-color: rgb(222, 226, 230); border-color: transparent; border-radius: 1rem; }

@media screen and (prefers-reduced-motion: reduce) {
}

@media screen and (prefers-reduced-motion: reduce) {
}

.custom-range:disabled::-webkit-slider-thumb { background-color: rgb(173, 181, 189); }

.custom-range:disabled::-webkit-slider-runnable-track { cursor: default; }

.custom-control-label::before, .custom-file-label, .custom-select { transition: background-color 0.15s ease-in-out 0s, border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .custom-control-label::before, .custom-file-label, .custom-select { transition: none 0s ease 0s; }
}

.nav { display: flex; flex-wrap: wrap; padding-left: 0px; margin-bottom: 0px; list-style: none; }

.nav-link { display: block; padding: 0.5rem 1rem; }

.nav-link:focus, .nav-link:hover { text-decoration: none; }

.nav-link.disabled { color: rgb(108, 117, 125); pointer-events: none; cursor: default; }

.nav-tabs { border-bottom: 1px solid rgb(222, 226, 230); }

.nav-tabs .nav-item { margin-bottom: -1px; }

.nav-tabs .nav-link { border: 1px solid transparent; border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }

.nav-tabs .nav-link:focus, .nav-tabs .nav-link:hover { border-color: rgb(233, 236, 239) rgb(233, 236, 239) rgb(222, 226, 230); }

.nav-tabs .nav-link.disabled { color: rgb(108, 117, 125); background-color: transparent; border-color: transparent; }

.nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active { color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); border-color: rgb(222, 226, 230) rgb(222, 226, 230) rgb(255, 255, 255); }

.nav-tabs .dropdown-menu { margin-top: -1px; border-top-left-radius: 0px; border-top-right-radius: 0px; }

.nav-pills .nav-link { border-radius: 0.25rem; }

.nav-pills .nav-link.active, .nav-pills .show > .nav-link { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); }

.nav-fill .nav-item { flex: 1 1 auto; text-align: center; }

.nav-justified .nav-item { flex-basis: 0px; flex-grow: 1; text-align: center; }

.tab-content > .tab-pane { display: none; }

.tab-content > .active { display: block; }

.navbar { position: relative; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; padding: 0.5rem 1rem; }

.navbar > .container, .navbar > .container-fluid { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; }

.navbar-brand { display: inline-block; padding-top: 0.3125rem; padding-bottom: 0.3125rem; margin-right: 1rem; font-size: 1.25rem; line-height: inherit; white-space: nowrap; }

.navbar-brand:focus, .navbar-brand:hover { text-decoration: none; }

.navbar-nav { display: flex; flex-direction: column; padding-left: 0px; margin-bottom: 0px; list-style: none; }

.navbar-nav .nav-link { padding-right: 0px; padding-left: 0px; }

.navbar-nav .dropdown-menu { position: static; float: none; }

.navbar-text { display: inline-block; padding-top: 0.5rem; padding-bottom: 0.5rem; }

.navbar-collapse { flex-basis: 100%; flex-grow: 1; align-items: center; }

.navbar-toggler { padding: 0.25rem 0.75rem; font-size: 1.25rem; line-height: 1; background-color: transparent; border: 1px solid transparent; border-radius: 0.25rem; }

.navbar-toggler:focus, .navbar-toggler:hover { text-decoration: none; }

.navbar-toggler:not(:disabled):not(.disabled) { cursor: pointer; }

.navbar-toggler-icon { display: inline-block; width: 1.5em; height: 1.5em; vertical-align: middle; content: ""; background: center center / 100% 100% no-repeat; }

@media (max-width: 575.98px) {
  .navbar-expand-sm > .container, .navbar-expand-sm > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 576px) {
  .navbar-expand-sm { flex-flow: row nowrap; justify-content: flex-start; }
  .navbar-expand-sm .navbar-nav { flex-direction: row; }
  .navbar-expand-sm .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-sm .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-sm > .container, .navbar-expand-sm > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-sm .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-sm .navbar-toggler { display: none; }
}

@media (max-width: 767.98px) {
  .navbar-expand-md > .container, .navbar-expand-md > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 768px) {
  .navbar-expand-md { flex-flow: row nowrap; justify-content: flex-start; }
  .navbar-expand-md .navbar-nav { flex-direction: row; }
  .navbar-expand-md .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-md .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-md > .container, .navbar-expand-md > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-md .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-md .navbar-toggler { display: none; }
}

@media (max-width: 991.98px) {
  .navbar-expand-lg > .container, .navbar-expand-lg > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 992px) {
  .navbar-expand-lg { flex-flow: row nowrap; justify-content: flex-start; }
  .navbar-expand-lg .navbar-nav { flex-direction: row; }
  .navbar-expand-lg .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-lg .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-lg > .container, .navbar-expand-lg > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-lg .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-lg .navbar-toggler { display: none; }
}

@media (max-width: 1199.98px) {
  .navbar-expand-xl > .container, .navbar-expand-xl > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 1200px) {
  .navbar-expand-xl { flex-flow: row nowrap; justify-content: flex-start; }
  .navbar-expand-xl .navbar-nav { flex-direction: row; }
  .navbar-expand-xl .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-xl .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-xl > .container, .navbar-expand-xl > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-xl .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-xl .navbar-toggler { display: none; }
}

.navbar-expand { flex-flow: row nowrap; justify-content: flex-start; }

.navbar-expand > .container, .navbar-expand > .container-fluid { padding-right: 0px; padding-left: 0px; }

.navbar-expand .navbar-nav { flex-direction: row; }

.navbar-expand .navbar-nav .dropdown-menu { position: absolute; }

.navbar-expand .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }

.navbar-expand > .container, .navbar-expand > .container-fluid { flex-wrap: nowrap; }

.navbar-expand .navbar-collapse { flex-basis: auto; display: flex !important; }

.navbar-expand .navbar-toggler { display: none; }

.navbar-light .navbar-brand { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-brand:focus, .navbar-light .navbar-brand:hover { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-nav .nav-link { color: rgba(0, 0, 0, 0.5); }

.navbar-light .navbar-nav .nav-link:focus, .navbar-light .navbar-nav .nav-link:hover { color: rgba(0, 0, 0, 0.7); }

.navbar-light .navbar-nav .nav-link.disabled { color: rgba(0, 0, 0, 0.3); }

.navbar-light .navbar-nav .active > .nav-link, .navbar-light .navbar-nav .nav-link.active, .navbar-light .navbar-nav .nav-link.show, .navbar-light .navbar-nav .show > .nav-link { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-toggler { color: rgba(0, 0, 0, 0.5); border-color: rgba(0, 0, 0, 0.1); }

.navbar-light .navbar-toggler-icon { background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e"); }

.navbar-light .navbar-text { color: rgba(0, 0, 0, 0.5); }

.navbar-light .navbar-text a { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-text a:focus, .navbar-light .navbar-text a:hover { color: rgba(0, 0, 0, 0.9); }

.navbar-dark .navbar-brand { color: rgb(255, 255, 255); }

.navbar-dark .navbar-brand:focus, .navbar-dark .navbar-brand:hover { color: rgb(255, 255, 255); }

.navbar-dark .navbar-nav .nav-link { color: rgba(255, 255, 255, 0.5); }

.navbar-dark .navbar-nav .nav-link:focus, .navbar-dark .navbar-nav .nav-link:hover { color: rgba(255, 255, 255, 0.75); }

.navbar-dark .navbar-nav .nav-link.disabled { color: rgba(255, 255, 255, 0.25); }

.navbar-dark .navbar-nav .active > .nav-link, .navbar-dark .navbar-nav .nav-link.active, .navbar-dark .navbar-nav .nav-link.show, .navbar-dark .navbar-nav .show > .nav-link { color: rgb(255, 255, 255); }

.navbar-dark .navbar-toggler { color: rgba(255, 255, 255, 0.5); border-color: rgba(255, 255, 255, 0.1); }

.navbar-dark .navbar-toggler-icon { background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='rgba(255, 255, 255, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e"); }

.navbar-dark .navbar-text { color: rgba(255, 255, 255, 0.5); }

.navbar-dark .navbar-text a { color: rgb(255, 255, 255); }

.navbar-dark .navbar-text a:focus, .navbar-dark .navbar-text a:hover { color: rgb(255, 255, 255); }

.card { position: relative; display: flex; flex-direction: column; min-width: 0px; overflow-wrap: break-word; background-color: rgb(255, 255, 255); background-clip: border-box; border: 1px solid rgba(0, 0, 0, 0.125); border-radius: 0.25rem; }

.card > hr { margin-right: 0px; margin-left: 0px; }

.card > .list-group:first-child .list-group-item:first-child { border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }

.card > .list-group:last-child .list-group-item:last-child { border-bottom-right-radius: 0.25rem; border-bottom-left-radius: 0.25rem; }

.card-body { flex: 1 1 auto; padding: 1.25rem; }

.card-title { margin-bottom: 0.75rem; }

.card-subtitle { margin-top: -0.375rem; margin-bottom: 0px; }

.card-text:last-child { margin-bottom: 0px; }

.card-link:hover { text-decoration: none; }

.card-link + .card-link { margin-left: 1.25rem; }

.card-header { padding: 0.75rem 1.25rem; margin-bottom: 0px; color: inherit; background-color: rgba(0, 0, 0, 0.03); border-bottom: 1px solid rgba(0, 0, 0, 0.125); }

.card-header:first-child { border-radius: calc(0.25rem - 1px) calc(0.25rem - 1px) 0px 0px; }

.card-header + .list-group .list-group-item:first-child { border-top: 0px; }

.card-footer { padding: 0.75rem 1.25rem; background-color: rgba(0, 0, 0, 0.03); border-top: 1px solid rgba(0, 0, 0, 0.125); }

.card-footer:last-child { border-radius: 0px 0px calc(0.25rem - 1px) calc(0.25rem - 1px); }

.card-header-tabs { margin-right: -0.625rem; margin-bottom: -0.75rem; margin-left: -0.625rem; border-bottom: 0px; }

.card-header-pills { margin-right: -0.625rem; margin-left: -0.625rem; }

.card-img-overlay { position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; padding: 1.25rem; }

.card-img { width: 100%; border-radius: calc(0.25rem - 1px); }

.card-img-top { width: 100%; border-top-left-radius: calc(0.25rem - 1px); border-top-right-radius: calc(0.25rem - 1px); }

.card-img-bottom { width: 100%; border-bottom-right-radius: calc(0.25rem - 1px); border-bottom-left-radius: calc(0.25rem - 1px); }

.card-deck { display: flex; flex-direction: column; }

.card-deck .card { margin-bottom: 15px; }

@media (min-width: 576px) {
  .card-deck { flex-flow: row wrap; margin-right: -15px; margin-left: -15px; }
  .card-deck .card { display: flex; flex: 1 0 0%; flex-direction: column; margin-right: 15px; margin-bottom: 0px; margin-left: 15px; }
}

.card-group { display: flex; flex-direction: column; }

.card-group > .card { margin-bottom: 15px; }

@media (min-width: 576px) {
  .card-group { flex-flow: row wrap; }
  .card-group > .card { flex: 1 0 0%; margin-bottom: 0px; }
  .card-group > .card + .card { margin-left: 0px; border-left: 0px; }
  .card-group > .card:first-child { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }
  .card-group > .card:first-child .card-header, .card-group > .card:first-child .card-img-top { border-top-right-radius: 0px; }
  .card-group > .card:first-child .card-footer, .card-group > .card:first-child .card-img-bottom { border-bottom-right-radius: 0px; }
  .card-group > .card:last-child { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }
  .card-group > .card:last-child .card-header, .card-group > .card:last-child .card-img-top { border-top-left-radius: 0px; }
  .card-group > .card:last-child .card-footer, .card-group > .card:last-child .card-img-bottom { border-bottom-left-radius: 0px; }
  .card-group > .card:only-child { border-radius: 0.25rem; }
  .card-group > .card:only-child .card-header, .card-group > .card:only-child .card-img-top { border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }
  .card-group > .card:only-child .card-footer, .card-group > .card:only-child .card-img-bottom { border-bottom-right-radius: 0.25rem; border-bottom-left-radius: 0.25rem; }
  .card-group > .card:not(:first-child):not(:last-child):not(:only-child) { border-radius: 0px; }
  .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-footer, .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-header, .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-img-bottom, .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-img-top { border-radius: 0px; }
}

.card-columns .card { margin-bottom: 0.75rem; }

@media (min-width: 576px) {
  .card-columns { column-count: 3; column-gap: 1.25rem; orphans: 1; widows: 1; }
  .card-columns .card { display: inline-block; width: 100%; }
}

.accordion .card { overflow: hidden; }

.accordion .card:not(:first-of-type) .card-header:first-child { border-radius: 0px; }

.accordion .card:not(:first-of-type):not(:last-of-type) { border-bottom: 0px; border-radius: 0px; }

.accordion .card:first-of-type { border-bottom: 0px; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px; }

.accordion .card:last-of-type { border-top-left-radius: 0px; border-top-right-radius: 0px; }

.accordion .card .card-header { margin-bottom: -1px; }

.breadcrumb { display: flex; flex-wrap: wrap; padding: 0.75rem 1rem; margin-bottom: 1rem; list-style: none; background-color: rgb(233, 236, 239); border-radius: 0.25rem; }

.breadcrumb-item + .breadcrumb-item { padding-left: 0.5rem; }

.breadcrumb-item + .breadcrumb-item::before { display: inline-block; padding-right: 0.5rem; color: rgb(108, 117, 125); content: "/"; }

.breadcrumb-item + .breadcrumb-item:hover::before { text-decoration: underline; }

.breadcrumb-item + .breadcrumb-item:hover::before { text-decoration: none; }

.breadcrumb-item.active { color: rgb(108, 117, 125); }

.pagination { display: flex; padding-left: 0px; list-style: none; border-radius: 0.25rem; }

.page-link { position: relative; display: block; padding: 0.5rem 0.75rem; margin-left: -1px; line-height: 1.25; color: rgb(0, 123, 255); background-color: rgb(255, 255, 255); border: 1px solid rgb(222, 226, 230); }

.page-link:hover { z-index: 2; color: rgb(0, 86, 179); text-decoration: none; background-color: rgb(233, 236, 239); border-color: rgb(222, 226, 230); }

.page-link:focus { z-index: 2; outline: 0px; box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.page-link:not(:disabled):not(.disabled) { cursor: pointer; }

.page-item:first-child .page-link { margin-left: 0px; border-top-left-radius: 0.25rem; border-bottom-left-radius: 0.25rem; }

.page-item:last-child .page-link { border-top-right-radius: 0.25rem; border-bottom-right-radius: 0.25rem; }

.page-item.active .page-link { z-index: 1; color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.page-item.disabled .page-link { color: rgb(108, 117, 125); pointer-events: none; cursor: auto; background-color: rgb(255, 255, 255); border-color: rgb(222, 226, 230); }

.pagination-lg .page-link { padding: 0.75rem 1.5rem; font-size: 1.25rem; line-height: 1.5; }

.pagination-lg .page-item:first-child .page-link { border-top-left-radius: 0.3rem; border-bottom-left-radius: 0.3rem; }

.pagination-lg .page-item:last-child .page-link { border-top-right-radius: 0.3rem; border-bottom-right-radius: 0.3rem; }

.pagination-sm .page-link { padding: 0.25rem 0.5rem; font-size: 0.875rem; line-height: 1.5; }

.pagination-sm .page-item:first-child .page-link { border-top-left-radius: 0.2rem; border-bottom-left-radius: 0.2rem; }

.pagination-sm .page-item:last-child .page-link { border-top-right-radius: 0.2rem; border-bottom-right-radius: 0.2rem; }

.badge { display: inline-block; padding: 0.25em 0.4em; font-size: 75%; font-weight: 700; line-height: 1; text-align: center; white-space: nowrap; vertical-align: baseline; border-radius: 0.25rem; }

a.badge:focus, a.badge:hover { text-decoration: none; }

.badge:empty { display: none; }

.btn .badge { position: relative; top: -1px; }

.badge-pill { padding-right: 0.6em; padding-left: 0.6em; border-radius: 10rem; }

.badge-primary { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); }

a.badge-primary:focus, a.badge-primary:hover { color: rgb(255, 255, 255); background-color: rgb(0, 98, 204); }

.badge-secondary { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); }

a.badge-secondary:focus, a.badge-secondary:hover { color: rgb(255, 255, 255); background-color: rgb(84, 91, 98); }

.badge-success { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); }

a.badge-success:focus, a.badge-success:hover { color: rgb(255, 255, 255); background-color: rgb(30, 126, 52); }

.badge-info { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); }

a.badge-info:focus, a.badge-info:hover { color: rgb(255, 255, 255); background-color: rgb(17, 122, 139); }

.badge-warning { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); }

a.badge-warning:focus, a.badge-warning:hover { color: rgb(33, 37, 41); background-color: rgb(211, 158, 0); }

.badge-danger { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); }

a.badge-danger:focus, a.badge-danger:hover { color: rgb(255, 255, 255); background-color: rgb(189, 33, 48); }

.badge-light { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); }

a.badge-light:focus, a.badge-light:hover { color: rgb(33, 37, 41); background-color: rgb(218, 224, 229); }

.badge-dark { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); }

a.badge-dark:focus, a.badge-dark:hover { color: rgb(255, 255, 255); background-color: rgb(29, 33, 36); }

.jumbotron { padding: 2rem 1rem; margin-bottom: 2rem; background-color: rgb(233, 236, 239); border-radius: 0.3rem; }

@media (min-width: 576px) {
  .jumbotron { padding: 4rem 2rem; }
}

.jumbotron-fluid { padding-right: 0px; padding-left: 0px; border-radius: 0px; }

.alert { position: relative; padding: 0.75rem 1.25rem; margin-bottom: 1rem; border: 1px solid transparent; border-radius: 0.25rem; }

.alert-heading { color: inherit; }

.alert-link { font-weight: 700; }

.alert-dismissible { padding-right: 4rem; }

.alert-dismissible .close { position: absolute; top: 0px; right: 0px; padding: 0.75rem 1.25rem; color: inherit; }

.alert-primary { color: rgb(0, 64, 133); background-color: rgb(204, 229, 255); border-color: rgb(184, 218, 255); }

.alert-primary hr { border-top-color: rgb(159, 205, 255); }

.alert-primary .alert-link { color: rgb(0, 39, 82); }

.alert-secondary { color: rgb(56, 61, 65); background-color: rgb(226, 227, 229); border-color: rgb(214, 216, 219); }

.alert-secondary hr { border-top-color: rgb(200, 203, 207); }

.alert-secondary .alert-link { color: rgb(32, 35, 38); }

.alert-success { color: rgb(21, 87, 36); background-color: rgb(212, 237, 218); border-color: rgb(195, 230, 203); }

.alert-success hr { border-top-color: rgb(177, 223, 187); }

.alert-success .alert-link { color: rgb(11, 46, 19); }

.alert-info { color: rgb(12, 84, 96); background-color: rgb(209, 236, 241); border-color: rgb(190, 229, 235); }

.alert-info hr { border-top-color: rgb(171, 221, 229); }

.alert-info .alert-link { color: rgb(6, 44, 51); }

.alert-warning { color: rgb(133, 100, 4); background-color: rgb(255, 243, 205); border-color: rgb(255, 238, 186); }

.alert-warning hr { border-top-color: rgb(255, 232, 161); }

.alert-warning .alert-link { color: rgb(83, 63, 3); }

.alert-danger { color: rgb(114, 28, 36); background-color: rgb(248, 215, 218); border-color: rgb(245, 198, 203); }

.alert-danger hr { border-top-color: rgb(241, 176, 183); }

.alert-danger .alert-link { color: rgb(73, 18, 23); }

.alert-light { color: rgb(129, 129, 130); background-color: rgb(254, 254, 254); border-color: rgb(253, 253, 254); }

.alert-light hr { border-top-color: rgb(236, 236, 246); }

.alert-light .alert-link { color: rgb(104, 104, 104); }

.alert-dark { color: rgb(27, 30, 33); background-color: rgb(214, 216, 217); border-color: rgb(198, 200, 202); }

.alert-dark hr { border-top-color: rgb(185, 187, 190); }

.alert-dark .alert-link { color: rgb(4, 5, 5); }

@-webkit-keyframes progress-bar-stripes { 
  0% { background-position: 1rem 0px; }
  100% { background-position: 0px 0px; }
}

@keyframes progress-bar-stripes { 
  0% { background-position: 1rem 0px; }
  100% { background-position: 0px 0px; }
}

.progress { display: flex; height: 1rem; overflow: hidden; font-size: 0.75rem; background-color: rgb(233, 236, 239); border-radius: 0.25rem; }

.progress-bar { display: flex; flex-direction: column; justify-content: center; color: rgb(255, 255, 255); text-align: center; white-space: nowrap; background-color: rgb(0, 123, 255); transition: width 0.6s ease 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .progress-bar { transition: none 0s ease 0s; }
}

.progress-bar-striped { background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent); background-size: 1rem 1rem; }

.progress-bar-animated { animation: 1s linear 0s infinite normal none running progress-bar-stripes; }

.media { display: flex; align-items: flex-start; }

.media-body { flex: 1 1 0%; }

.list-group { display: flex; flex-direction: column; padding-left: 0px; margin-bottom: 0px; }

.list-group-item-action { width: 100%; color: rgb(73, 80, 87); text-align: inherit; }

.list-group-item-action:focus, .list-group-item-action:hover { color: rgb(73, 80, 87); text-decoration: none; background-color: rgb(248, 249, 250); }

.list-group-item-action:active { color: rgb(33, 37, 41); background-color: rgb(233, 236, 239); }

.list-group-item { position: relative; display: block; padding: 0.75rem 1.25rem; margin-bottom: -1px; background-color: rgb(255, 255, 255); border: 1px solid rgba(0, 0, 0, 0.125); }

.list-group-item:first-child { border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }

.list-group-item:last-child { margin-bottom: 0px; border-bottom-right-radius: 0.25rem; border-bottom-left-radius: 0.25rem; }

.list-group-item:focus, .list-group-item:hover { z-index: 1; text-decoration: none; }

.list-group-item.disabled, .list-group-item:disabled { color: rgb(108, 117, 125); pointer-events: none; background-color: rgb(255, 255, 255); }

.list-group-item.active { z-index: 2; color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.list-group-flush .list-group-item { border-right: 0px; border-left: 0px; border-radius: 0px; }

.list-group-flush .list-group-item:last-child { margin-bottom: -1px; }

.list-group-flush:first-child .list-group-item:first-child { border-top: 0px; }

.list-group-flush:last-child .list-group-item:last-child { margin-bottom: 0px; border-bottom: 0px; }

.list-group-item-primary { color: rgb(0, 64, 133); background-color: rgb(184, 218, 255); }

.list-group-item-primary.list-group-item-action:focus, .list-group-item-primary.list-group-item-action:hover { color: rgb(0, 64, 133); background-color: rgb(159, 205, 255); }

.list-group-item-primary.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(0, 64, 133); border-color: rgb(0, 64, 133); }

.list-group-item-secondary { color: rgb(56, 61, 65); background-color: rgb(214, 216, 219); }

.list-group-item-secondary.list-group-item-action:focus, .list-group-item-secondary.list-group-item-action:hover { color: rgb(56, 61, 65); background-color: rgb(200, 203, 207); }

.list-group-item-secondary.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(56, 61, 65); border-color: rgb(56, 61, 65); }

.list-group-item-success { color: rgb(21, 87, 36); background-color: rgb(195, 230, 203); }

.list-group-item-success.list-group-item-action:focus, .list-group-item-success.list-group-item-action:hover { color: rgb(21, 87, 36); background-color: rgb(177, 223, 187); }

.list-group-item-success.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(21, 87, 36); border-color: rgb(21, 87, 36); }

.list-group-item-info { color: rgb(12, 84, 96); background-color: rgb(190, 229, 235); }

.list-group-item-info.list-group-item-action:focus, .list-group-item-info.list-group-item-action:hover { color: rgb(12, 84, 96); background-color: rgb(171, 221, 229); }

.list-group-item-info.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(12, 84, 96); border-color: rgb(12, 84, 96); }

.list-group-item-warning { color: rgb(133, 100, 4); background-color: rgb(255, 238, 186); }

.list-group-item-warning.list-group-item-action:focus, .list-group-item-warning.list-group-item-action:hover { color: rgb(133, 100, 4); background-color: rgb(255, 232, 161); }

.list-group-item-warning.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(133, 100, 4); border-color: rgb(133, 100, 4); }

.list-group-item-danger { color: rgb(114, 28, 36); background-color: rgb(245, 198, 203); }

.list-group-item-danger.list-group-item-action:focus, .list-group-item-danger.list-group-item-action:hover { color: rgb(114, 28, 36); background-color: rgb(241, 176, 183); }

.list-group-item-danger.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(114, 28, 36); border-color: rgb(114, 28, 36); }

.list-group-item-light { color: rgb(129, 129, 130); background-color: rgb(253, 253, 254); }

.list-group-item-light.list-group-item-action:focus, .list-group-item-light.list-group-item-action:hover { color: rgb(129, 129, 130); background-color: rgb(236, 236, 246); }

.list-group-item-light.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(129, 129, 130); border-color: rgb(129, 129, 130); }

.list-group-item-dark { color: rgb(27, 30, 33); background-color: rgb(198, 200, 202); }

.list-group-item-dark.list-group-item-action:focus, .list-group-item-dark.list-group-item-action:hover { color: rgb(27, 30, 33); background-color: rgb(185, 187, 190); }

.list-group-item-dark.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(27, 30, 33); border-color: rgb(27, 30, 33); }

.close { float: right; font-size: 1.5rem; font-weight: 700; line-height: 1; color: rgb(0, 0, 0); text-shadow: rgb(255, 255, 255) 0px 1px 0px; opacity: 0.5; }

.close:hover { color: rgb(0, 0, 0); text-decoration: none; }

.close:not(:disabled):not(.disabled) { cursor: pointer; }

.close:not(:disabled):not(.disabled):focus, .close:not(:disabled):not(.disabled):hover { opacity: 0.75; }

button.close { padding: 0px; background-color: transparent; border: 0px; -webkit-appearance: none; }

a.close.disabled { pointer-events: none; }

.toast { max-width: 350px; overflow: hidden; font-size: 0.875rem; background-color: rgba(255, 255, 255, 0.85); background-clip: padding-box; border: 1px solid rgba(0, 0, 0, 0.1); border-radius: 0.25rem; box-shadow: rgba(0, 0, 0, 0.1) 0px 0.25rem 0.75rem; backdrop-filter: blur(10px); opacity: 0; }

.toast:not(:last-child) { margin-bottom: 0.75rem; }

.toast.showing { opacity: 1; }

.toast.show { display: block; opacity: 1; }

.toast.hide { display: none; }

.toast-header { display: flex; align-items: center; padding: 0.25rem 0.75rem; color: rgb(108, 117, 125); background-color: rgba(255, 255, 255, 0.85); background-clip: padding-box; border-bottom: 1px solid rgba(0, 0, 0, 0.05); }

.toast-body { padding: 0.75rem; }

.modal-open { overflow: hidden; }

.modal-open .modal { overflow: hidden auto; }

.modal { position: fixed; top: 0px; left: 0px; z-index: 1050; display: none; width: 100%; height: 100%; overflow: hidden; outline: 0px; }

.modal-dialog { position: relative; width: auto; margin: 0.5rem; pointer-events: none; }

.modal.fade .modal-dialog { transition: transform 0.3s ease-out 0s, -webkit-transform 0.3s ease-out 0s; transform: translate(0px, -50px); }

@media screen and (prefers-reduced-motion: reduce) {
  .modal.fade .modal-dialog { transition: none 0s ease 0s; }
}

.modal.show .modal-dialog { transform: none; }

.modal-dialog-centered { display: flex; align-items: center; min-height: calc(100% - 1rem); }

.modal-dialog-centered::before { display: block; height: calc(100vh - 1rem); content: ""; }

.modal-content { position: relative; display: flex; flex-direction: column; width: 100%; pointer-events: auto; background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 0.3rem; outline: 0px; }

.modal-backdrop { position: fixed; top: 0px; left: 0px; z-index: 1040; width: 100vw; height: 100vh; background-color: rgb(0, 0, 0); }

.modal-backdrop.fade { opacity: 0; }

.modal-backdrop.show { opacity: 0.5; }

.modal-header { display: flex; align-items: flex-start; justify-content: space-between; padding: 1rem; border-bottom: 1px solid rgb(233, 236, 239); border-top-left-radius: 0.3rem; border-top-right-radius: 0.3rem; }

.modal-header .close { padding: 1rem; margin: -1rem -1rem -1rem auto; }

.modal-title { margin-bottom: 0px; line-height: 1.5; }

.modal-body { position: relative; flex: 1 1 auto; padding: 1rem; }

.modal-footer { display: flex; align-items: center; justify-content: flex-end; padding: 1rem; border-top: 1px solid rgb(233, 236, 239); border-bottom-right-radius: 0.3rem; border-bottom-left-radius: 0.3rem; }

.modal-footer > :not(:first-child) { margin-left: 0.25rem; }

.modal-footer > :not(:last-child) { margin-right: 0.25rem; }

.modal-scrollbar-measure { position: absolute; top: -9999px; width: 50px; height: 50px; overflow: scroll; }

@media (min-width: 576px) {
  .modal-dialog { max-width: 500px; margin: 1.75rem auto; }
  .modal-dialog-centered { min-height: calc(100% - 3.5rem); }
  .modal-dialog-centered::before { height: calc(100vh - 3.5rem); }
  .modal-sm { max-width: 300px; }
}

@media (min-width: 992px) {
  .modal-lg, .modal-xl { max-width: 800px; }
}

@media (min-width: 1200px) {
  .modal-xl { max-width: 1140px; }
}

.tooltip { position: absolute; z-index: 1070; display: block; margin: 0px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; font-style: normal; font-weight: 400; line-height: 1.5; text-align: start; text-decoration: none; text-shadow: none; text-transform: none; letter-spacing: normal; word-break: normal; word-spacing: normal; white-space: normal; line-break: auto; font-size: 0.875rem; overflow-wrap: break-word; opacity: 0; }

.tooltip.show { opacity: 0.9; }

.tooltip .arrow { position: absolute; display: block; width: 0.8rem; height: 0.4rem; }

.tooltip .arrow::before { position: absolute; content: ""; border-color: transparent; border-style: solid; }

.bs-tooltip-auto[x-placement^="top"], .bs-tooltip-top { padding: 0.4rem 0px; }

.bs-tooltip-auto[x-placement^="top"] .arrow, .bs-tooltip-top .arrow { bottom: 0px; }

.bs-tooltip-auto[x-placement^="top"] .arrow::before, .bs-tooltip-top .arrow::before { top: 0px; border-width: 0.4rem 0.4rem 0px; border-top-color: rgb(0, 0, 0); }

.bs-tooltip-auto[x-placement^="right"], .bs-tooltip-right { padding: 0px 0.4rem; }

.bs-tooltip-auto[x-placement^="right"] .arrow, .bs-tooltip-right .arrow { left: 0px; width: 0.4rem; height: 0.8rem; }

.bs-tooltip-auto[x-placement^="right"] .arrow::before, .bs-tooltip-right .arrow::before { right: 0px; border-width: 0.4rem 0.4rem 0.4rem 0px; border-right-color: rgb(0, 0, 0); }

.bs-tooltip-auto[x-placement^="bottom"], .bs-tooltip-bottom { padding: 0.4rem 0px; }

.bs-tooltip-auto[x-placement^="bottom"] .arrow, .bs-tooltip-bottom .arrow { top: 0px; }

.bs-tooltip-auto[x-placement^="bottom"] .arrow::before, .bs-tooltip-bottom .arrow::before { bottom: 0px; border-width: 0px 0.4rem 0.4rem; border-bottom-color: rgb(0, 0, 0); }

.bs-tooltip-auto[x-placement^="left"], .bs-tooltip-left { padding: 0px 0.4rem; }

.bs-tooltip-auto[x-placement^="left"] .arrow, .bs-tooltip-left .arrow { right: 0px; width: 0.4rem; height: 0.8rem; }

.bs-tooltip-auto[x-placement^="left"] .arrow::before, .bs-tooltip-left .arrow::before { left: 0px; border-width: 0.4rem 0px 0.4rem 0.4rem; border-left-color: rgb(0, 0, 0); }

.tooltip-inner { max-width: 200px; padding: 0.25rem 0.5rem; color: rgb(255, 255, 255); text-align: center; background-color: rgb(0, 0, 0); border-radius: 0.25rem; }

.popover { position: absolute; top: 0px; left: 0px; z-index: 1060; display: block; max-width: 276px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"; font-style: normal; font-weight: 400; line-height: 1.5; text-align: start; text-decoration: none; text-shadow: none; text-transform: none; letter-spacing: normal; word-break: normal; word-spacing: normal; white-space: normal; line-break: auto; font-size: 0.875rem; overflow-wrap: break-word; background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 0.3rem; }

.popover .arrow { position: absolute; display: block; width: 1rem; height: 0.5rem; margin: 0px 0.3rem; }

.popover .arrow::after, .popover .arrow::before { position: absolute; display: block; content: ""; border-color: transparent; border-style: solid; }

.bs-popover-auto[x-placement^="top"], .bs-popover-top { margin-bottom: 0.5rem; }

.bs-popover-auto[x-placement^="top"] .arrow, .bs-popover-top .arrow { bottom: calc((0.5rem + 1px) * -1); }

.bs-popover-auto[x-placement^="top"] .arrow::after, .bs-popover-auto[x-placement^="top"] .arrow::before, .bs-popover-top .arrow::after, .bs-popover-top .arrow::before { border-width: 0.5rem 0.5rem 0px; }

.bs-popover-auto[x-placement^="top"] .arrow::before, .bs-popover-top .arrow::before { bottom: 0px; border-top-color: rgba(0, 0, 0, 0.25); }

.bs-popover-auto[x-placement^="top"] .arrow::after, .bs-popover-top .arrow::after { bottom: 1px; border-top-color: rgb(255, 255, 255); }

.bs-popover-auto[x-placement^="right"], .bs-popover-right { margin-left: 0.5rem; }

.bs-popover-auto[x-placement^="right"] .arrow, .bs-popover-right .arrow { left: calc((0.5rem + 1px) * -1); width: 0.5rem; height: 1rem; margin: 0.3rem 0px; }

.bs-popover-auto[x-placement^="right"] .arrow::after, .bs-popover-auto[x-placement^="right"] .arrow::before, .bs-popover-right .arrow::after, .bs-popover-right .arrow::before { border-width: 0.5rem 0.5rem 0.5rem 0px; }

.bs-popover-auto[x-placement^="right"] .arrow::before, .bs-popover-right .arrow::before { left: 0px; border-right-color: rgba(0, 0, 0, 0.25); }

.bs-popover-auto[x-placement^="right"] .arrow::after, .bs-popover-right .arrow::after { left: 1px; border-right-color: rgb(255, 255, 255); }

.bs-popover-auto[x-placement^="bottom"], .bs-popover-bottom { margin-top: 0.5rem; }

.bs-popover-auto[x-placement^="bottom"] .arrow, .bs-popover-bottom .arrow { top: calc((0.5rem + 1px) * -1); }

.bs-popover-auto[x-placement^="bottom"] .arrow::after, .bs-popover-auto[x-placement^="bottom"] .arrow::before, .bs-popover-bottom .arrow::after, .bs-popover-bottom .arrow::before { border-width: 0px 0.5rem 0.5rem; }

.bs-popover-auto[x-placement^="bottom"] .arrow::before, .bs-popover-bottom .arrow::before { top: 0px; border-bottom-color: rgba(0, 0, 0, 0.25); }

.bs-popover-auto[x-placement^="bottom"] .arrow::after, .bs-popover-bottom .arrow::after { top: 1px; border-bottom-color: rgb(255, 255, 255); }

.bs-popover-auto[x-placement^="bottom"] .popover-header::before, .bs-popover-bottom .popover-header::before { position: absolute; top: 0px; left: 50%; display: block; width: 1rem; margin-left: -0.5rem; content: ""; border-bottom: 1px solid rgb(247, 247, 247); }

.bs-popover-auto[x-placement^="left"], .bs-popover-left { margin-right: 0.5rem; }

.bs-popover-auto[x-placement^="left"] .arrow, .bs-popover-left .arrow { right: calc((0.5rem + 1px) * -1); width: 0.5rem; height: 1rem; margin: 0.3rem 0px; }

.bs-popover-auto[x-placement^="left"] .arrow::after, .bs-popover-auto[x-placement^="left"] .arrow::before, .bs-popover-left .arrow::after, .bs-popover-left .arrow::before { border-width: 0.5rem 0px 0.5rem 0.5rem; }

.bs-popover-auto[x-placement^="left"] .arrow::before, .bs-popover-left .arrow::before { right: 0px; border-left-color: rgba(0, 0, 0, 0.25); }

.bs-popover-auto[x-placement^="left"] .arrow::after, .bs-popover-left .arrow::after { right: 1px; border-left-color: rgb(255, 255, 255); }

.popover-header { padding: 0.5rem 0.75rem; margin-bottom: 0px; font-size: 1rem; color: inherit; background-color: rgb(247, 247, 247); border-bottom: 1px solid rgb(235, 235, 235); border-top-left-radius: calc(0.3rem - 1px); border-top-right-radius: calc(0.3rem - 1px); }

.popover-header:empty { display: none; }

.popover-body { padding: 0.5rem 0.75rem; color: rgb(33, 37, 41); }

.carousel { position: relative; }

.carousel.pointer-event { touch-action: pan-y; }

.carousel-inner { position: relative; width: 100%; overflow: hidden; }

.carousel-inner::after { display: block; clear: both; content: ""; }

.carousel-item { position: relative; display: none; float: left; width: 100%; margin-right: -100%; backface-visibility: hidden; transition: transform 0.6s ease-in-out 0s, -webkit-transform 0.6s ease-in-out 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .carousel-item { transition: none 0s ease 0s; }
}

.carousel-item-next, .carousel-item-prev, .carousel-item.active { display: block; }

.active.carousel-item-right, .carousel-item-next:not(.carousel-item-left) { transform: translateX(100%); }

.active.carousel-item-left, .carousel-item-prev:not(.carousel-item-right) { transform: translateX(-100%); }

.carousel-fade .carousel-item { opacity: 0; transition-property: opacity; transform: none; }

.carousel-fade .carousel-item-next.carousel-item-left, .carousel-fade .carousel-item-prev.carousel-item-right, .carousel-fade .carousel-item.active { z-index: 1; opacity: 1; }

.carousel-fade .active.carousel-item-left, .carousel-fade .active.carousel-item-right { z-index: 0; opacity: 0; transition: opacity 0s ease 0.6s; }

@media screen and (prefers-reduced-motion: reduce) {
  .carousel-fade .active.carousel-item-left, .carousel-fade .active.carousel-item-right { transition: none 0s ease 0s; }
}

.carousel-control-next, .carousel-control-prev { position: absolute; top: 0px; bottom: 0px; z-index: 1; display: flex; align-items: center; justify-content: center; width: 15%; color: rgb(255, 255, 255); text-align: center; opacity: 0.5; transition: opacity 0.15s ease 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .carousel-control-next, .carousel-control-prev { transition: none 0s ease 0s; }
}

.carousel-control-next:focus, .carousel-control-next:hover, .carousel-control-prev:focus, .carousel-control-prev:hover { color: rgb(255, 255, 255); text-decoration: none; outline: 0px; opacity: 0.9; }

.carousel-control-prev { left: 0px; }

.carousel-control-next { right: 0px; }

.carousel-control-next-icon, .carousel-control-prev-icon { display: inline-block; width: 20px; height: 20px; background: center center / 100% 100% no-repeat transparent; }

.carousel-control-prev-icon { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3e%3cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3e%3c/svg%3e"); }

.carousel-control-next-icon { background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3e%3cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3e%3c/svg%3e"); }

.carousel-indicators { position: absolute; right: 0px; bottom: 0px; left: 0px; z-index: 15; display: flex; justify-content: center; padding-left: 0px; margin-right: 15%; margin-left: 15%; list-style: none; }

.carousel-indicators li { box-sizing: content-box; flex: 0 1 auto; width: 30px; height: 3px; margin-right: 3px; margin-left: 3px; text-indent: -999px; cursor: pointer; background-color: rgb(255, 255, 255); background-clip: padding-box; border-top: 10px solid transparent; border-bottom: 10px solid transparent; opacity: 0.5; transition: opacity 0.6s ease 0s; }

@media screen and (prefers-reduced-motion: reduce) {
  .carousel-indicators li { transition: none 0s ease 0s; }
}

.carousel-indicators .active { opacity: 1; }

.carousel-caption { position: absolute; right: 15%; bottom: 20px; left: 15%; z-index: 10; padding-top: 20px; padding-bottom: 20px; color: rgb(255, 255, 255); text-align: center; }

@-webkit-keyframes spinner-border { 
  100% { transform: rotate(360deg); }
}

@keyframes spinner-border { 
  100% { transform: rotate(360deg); }
}

.spinner-border { display: inline-block; width: 2rem; height: 2rem; vertical-align: text-bottom; border-width: 0.25em; border-style: solid; border-color: currentcolor transparent currentcolor currentcolor; border-image: initial; border-radius: 50%; animation: 0.75s linear 0s infinite normal none running spinner-border; }

.spinner-border-sm { width: 1rem; height: 1rem; border-width: 0.2em; }

@-webkit-keyframes spinner-grow { 
  0% { transform: scale(0); }
  50% { opacity: 1; }
}

@keyframes spinner-grow { 
  0% { transform: scale(0); }
  50% { opacity: 1; }
}

.spinner-grow { display: inline-block; width: 2rem; height: 2rem; vertical-align: text-bottom; background-color: currentcolor; border-radius: 50%; opacity: 0; animation: 0.75s linear 0s infinite normal none running spinner-grow; }

.spinner-grow-sm { width: 1rem; height: 1rem; }

.align-baseline { vertical-align: baseline !important; }

.align-top { vertical-align: top !important; }

.align-middle { vertical-align: middle !important; }

.align-bottom { vertical-align: bottom !important; }

.align-text-bottom { vertical-align: text-bottom !important; }

.align-text-top { vertical-align: text-top !important; }

.bg-primary { background-color: rgb(0, 123, 255) !important; }

a.bg-primary:focus, a.bg-primary:hover, button.bg-primary:focus, button.bg-primary:hover { background-color: rgb(0, 98, 204) !important; }

.bg-secondary { background-color: rgb(108, 117, 125) !important; }

a.bg-secondary:focus, a.bg-secondary:hover, button.bg-secondary:focus, button.bg-secondary:hover { background-color: rgb(84, 91, 98) !important; }

.bg-success { background-color: rgb(40, 167, 69) !important; }

a.bg-success:focus, a.bg-success:hover, button.bg-success:focus, button.bg-success:hover { background-color: rgb(30, 126, 52) !important; }

.bg-info { background-color: rgb(23, 162, 184) !important; }

a.bg-info:focus, a.bg-info:hover, button.bg-info:focus, button.bg-info:hover { background-color: rgb(17, 122, 139) !important; }

.bg-warning { background-color: rgb(255, 193, 7) !important; }

a.bg-warning:focus, a.bg-warning:hover, button.bg-warning:focus, button.bg-warning:hover { background-color: rgb(211, 158, 0) !important; }

.bg-danger { background-color: rgb(220, 53, 69) !important; }

a.bg-danger:focus, a.bg-danger:hover, button.bg-danger:focus, button.bg-danger:hover { background-color: rgb(189, 33, 48) !important; }

.bg-light { background-color: rgb(248, 249, 250) !important; }

a.bg-light:focus, a.bg-light:hover, button.bg-light:focus, button.bg-light:hover { background-color: rgb(218, 224, 229) !important; }

.bg-dark { background-color: rgb(52, 58, 64) !important; }

a.bg-dark:focus, a.bg-dark:hover, button.bg-dark:focus, button.bg-dark:hover { background-color: rgb(29, 33, 36) !important; }

.bg-white { background-color: rgb(255, 255, 255) !important; }

.bg-transparent { background-color: transparent !important; }

.border { border: 1px solid rgb(222, 226, 230) !important; }

.border-top { border-top: 1px solid rgb(222, 226, 230) !important; }

.border-right { border-right: 1px solid rgb(222, 226, 230) !important; }

.border-bottom { border-bottom: 1px solid rgb(222, 226, 230) !important; }

.border-left { border-left: 1px solid rgb(222, 226, 230) !important; }

.border-0 { border: 0px !important; }

.border-top-0 { border-top: 0px !important; }

.border-right-0 { border-right: 0px !important; }

.border-bottom-0 { border-bottom: 0px !important; }

.border-left-0 { border-left: 0px !important; }

.border-primary { border-color: rgb(0, 123, 255) !important; }

.border-secondary { border-color: rgb(108, 117, 125) !important; }

.border-success { border-color: rgb(40, 167, 69) !important; }

.border-info { border-color: rgb(23, 162, 184) !important; }

.border-warning { border-color: rgb(255, 193, 7) !important; }

.border-danger { border-color: rgb(220, 53, 69) !important; }

.border-light { border-color: rgb(248, 249, 250) !important; }

.border-dark { border-color: rgb(52, 58, 64) !important; }

.border-white { border-color: rgb(255, 255, 255) !important; }

.rounded { border-radius: 0.25rem !important; }

.rounded-top { border-top-left-radius: 0.25rem !important; border-top-right-radius: 0.25rem !important; }

.rounded-right { border-top-right-radius: 0.25rem !important; border-bottom-right-radius: 0.25rem !important; }

.rounded-bottom { border-bottom-right-radius: 0.25rem !important; border-bottom-left-radius: 0.25rem !important; }

.rounded-left { border-top-left-radius: 0.25rem !important; border-bottom-left-radius: 0.25rem !important; }

.rounded-circle { border-radius: 50% !important; }

.rounded-pill { border-radius: 50rem !important; }

.rounded-0 { border-radius: 0px !important; }

.clearfix::after { display: block; clear: both; content: ""; }

.d-none { display: none !important; }

.d-inline { display: inline !important; }

.d-inline-block { display: inline-block !important; }

.d-block { display: block !important; }

.d-table { display: table !important; }

.d-table-row { display: table-row !important; }

.d-table-cell { display: table-cell !important; }

.d-flex { display: flex !important; }

.d-inline-flex { display: inline-flex !important; }

@media (min-width: 576px) {
  .d-sm-none { display: none !important; }
  .d-sm-inline { display: inline !important; }
  .d-sm-inline-block { display: inline-block !important; }
  .d-sm-block { display: block !important; }
  .d-sm-table { display: table !important; }
  .d-sm-table-row { display: table-row !important; }
  .d-sm-table-cell { display: table-cell !important; }
  .d-sm-flex { display: flex !important; }
  .d-sm-inline-flex { display: inline-flex !important; }
}

@media (min-width: 768px) {
  .d-md-none { display: none !important; }
  .d-md-inline { display: inline !important; }
  .d-md-inline-block { display: inline-block !important; }
  .d-md-block { display: block !important; }
  .d-md-table { display: table !important; }
  .d-md-table-row { display: table-row !important; }
  .d-md-table-cell { display: table-cell !important; }
  .d-md-flex { display: flex !important; }
  .d-md-inline-flex { display: inline-flex !important; }
}

@media (min-width: 992px) {
  .d-lg-none { display: none !important; }
  .d-lg-inline { display: inline !important; }
  .d-lg-inline-block { display: inline-block !important; }
  .d-lg-block { display: block !important; }
  .d-lg-table { display: table !important; }
  .d-lg-table-row { display: table-row !important; }
  .d-lg-table-cell { display: table-cell !important; }
  .d-lg-flex { display: flex !important; }
  .d-lg-inline-flex { display: inline-flex !important; }
}

@media (min-width: 1200px) {
  .d-xl-none { display: none !important; }
  .d-xl-inline { display: inline !important; }
  .d-xl-inline-block { display: inline-block !important; }
  .d-xl-block { display: block !important; }
  .d-xl-table { display: table !important; }
  .d-xl-table-row { display: table-row !important; }
  .d-xl-table-cell { display: table-cell !important; }
  .d-xl-flex { display: flex !important; }
  .d-xl-inline-flex { display: inline-flex !important; }
}

@media print {
  .d-print-none { display: none !important; }
  .d-print-inline { display: inline !important; }
  .d-print-inline-block { display: inline-block !important; }
  .d-print-block { display: block !important; }
  .d-print-table { display: table !important; }
  .d-print-table-row { display: table-row !important; }
  .d-print-table-cell { display: table-cell !important; }
  .d-print-flex { display: flex !important; }
  .d-print-inline-flex { display: inline-flex !important; }
}

.embed-responsive { position: relative; display: block; width: 100%; padding: 0px; overflow: hidden; }

.embed-responsive::before { display: block; content: ""; }

.embed-responsive .embed-responsive-item, .embed-responsive embed, .embed-responsive iframe, .embed-responsive object, .embed-responsive video { position: absolute; top: 0px; bottom: 0px; left: 0px; width: 100%; height: 100%; border: 0px; }

.embed-responsive-21by9::before { padding-top: 42.8571%; }

.embed-responsive-16by9::before { padding-top: 56.25%; }

.embed-responsive-3by4::before { padding-top: 133.333%; }

.embed-responsive-1by1::before { padding-top: 100%; }

.flex-row { flex-direction: row !important; }

.flex-column { flex-direction: column !important; }

.flex-row-reverse { flex-direction: row-reverse !important; }

.flex-column-reverse { flex-direction: column-reverse !important; }

.flex-wrap { flex-wrap: wrap !important; }

.flex-nowrap { flex-wrap: nowrap !important; }

.flex-wrap-reverse { flex-wrap: wrap-reverse !important; }

.flex-fill { flex: 1 1 auto !important; }

.flex-grow-0 { flex-grow: 0 !important; }

.flex-grow-1 { flex-grow: 1 !important; }

.flex-shrink-0 { flex-shrink: 0 !important; }

.flex-shrink-1 { flex-shrink: 1 !important; }

.justify-content-start { justify-content: flex-start !important; }

.justify-content-end { justify-content: flex-end !important; }

.justify-content-center { justify-content: center !important; }

.justify-content-between { justify-content: space-between !important; }

.justify-content-around { justify-content: space-around !important; }

.align-items-start { align-items: flex-start !important; }

.align-items-end { align-items: flex-end !important; }

.align-items-center { align-items: center !important; }

.align-items-baseline { align-items: baseline !important; }

.align-items-stretch { align-items: stretch !important; }

.align-content-start { align-content: flex-start !important; }

.align-content-end { align-content: flex-end !important; }

.align-content-center { align-content: center !important; }

.align-content-between { align-content: space-between !important; }

.align-content-around { align-content: space-around !important; }

.align-content-stretch { align-content: stretch !important; }

.align-self-auto { align-self: auto !important; }

.align-self-start { align-self: flex-start !important; }

.align-self-end { align-self: flex-end !important; }

.align-self-center { align-self: center !important; }

.align-self-baseline { align-self: baseline !important; }

.align-self-stretch { align-self: stretch !important; }

@media (min-width: 576px) {
  .flex-sm-row { flex-direction: row !important; }
  .flex-sm-column { flex-direction: column !important; }
  .flex-sm-row-reverse { flex-direction: row-reverse !important; }
  .flex-sm-column-reverse { flex-direction: column-reverse !important; }
  .flex-sm-wrap { flex-wrap: wrap !important; }
  .flex-sm-nowrap { flex-wrap: nowrap !important; }
  .flex-sm-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .flex-sm-fill { flex: 1 1 auto !important; }
  .flex-sm-grow-0 { flex-grow: 0 !important; }
  .flex-sm-grow-1 { flex-grow: 1 !important; }
  .flex-sm-shrink-0 { flex-shrink: 0 !important; }
  .flex-sm-shrink-1 { flex-shrink: 1 !important; }
  .justify-content-sm-start { justify-content: flex-start !important; }
  .justify-content-sm-end { justify-content: flex-end !important; }
  .justify-content-sm-center { justify-content: center !important; }
  .justify-content-sm-between { justify-content: space-between !important; }
  .justify-content-sm-around { justify-content: space-around !important; }
  .align-items-sm-start { align-items: flex-start !important; }
  .align-items-sm-end { align-items: flex-end !important; }
  .align-items-sm-center { align-items: center !important; }
  .align-items-sm-baseline { align-items: baseline !important; }
  .align-items-sm-stretch { align-items: stretch !important; }
  .align-content-sm-start { align-content: flex-start !important; }
  .align-content-sm-end { align-content: flex-end !important; }
  .align-content-sm-center { align-content: center !important; }
  .align-content-sm-between { align-content: space-between !important; }
  .align-content-sm-around { align-content: space-around !important; }
  .align-content-sm-stretch { align-content: stretch !important; }
  .align-self-sm-auto { align-self: auto !important; }
  .align-self-sm-start { align-self: flex-start !important; }
  .align-self-sm-end { align-self: flex-end !important; }
  .align-self-sm-center { align-self: center !important; }
  .align-self-sm-baseline { align-self: baseline !important; }
  .align-self-sm-stretch { align-self: stretch !important; }
}

@media (min-width: 768px) {
  .flex-md-row { flex-direction: row !important; }
  .flex-md-column { flex-direction: column !important; }
  .flex-md-row-reverse { flex-direction: row-reverse !important; }
  .flex-md-column-reverse { flex-direction: column-reverse !important; }
  .flex-md-wrap { flex-wrap: wrap !important; }
  .flex-md-nowrap { flex-wrap: nowrap !important; }
  .flex-md-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .flex-md-fill { flex: 1 1 auto !important; }
  .flex-md-grow-0 { flex-grow: 0 !important; }
  .flex-md-grow-1 { flex-grow: 1 !important; }
  .flex-md-shrink-0 { flex-shrink: 0 !important; }
  .flex-md-shrink-1 { flex-shrink: 1 !important; }
  .justify-content-md-start { justify-content: flex-start !important; }
  .justify-content-md-end { justify-content: flex-end !important; }
  .justify-content-md-center { justify-content: center !important; }
  .justify-content-md-between { justify-content: space-between !important; }
  .justify-content-md-around { justify-content: space-around !important; }
  .align-items-md-start { align-items: flex-start !important; }
  .align-items-md-end { align-items: flex-end !important; }
  .align-items-md-center { align-items: center !important; }
  .align-items-md-baseline { align-items: baseline !important; }
  .align-items-md-stretch { align-items: stretch !important; }
  .align-content-md-start { align-content: flex-start !important; }
  .align-content-md-end { align-content: flex-end !important; }
  .align-content-md-center { align-content: center !important; }
  .align-content-md-between { align-content: space-between !important; }
  .align-content-md-around { align-content: space-around !important; }
  .align-content-md-stretch { align-content: stretch !important; }
  .align-self-md-auto { align-self: auto !important; }
  .align-self-md-start { align-self: flex-start !important; }
  .align-self-md-end { align-self: flex-end !important; }
  .align-self-md-center { align-self: center !important; }
  .align-self-md-baseline { align-self: baseline !important; }
  .align-self-md-stretch { align-self: stretch !important; }
}

@media (min-width: 992px) {
  .flex-lg-row { flex-direction: row !important; }
  .flex-lg-column { flex-direction: column !important; }
  .flex-lg-row-reverse { flex-direction: row-reverse !important; }
  .flex-lg-column-reverse { flex-direction: column-reverse !important; }
  .flex-lg-wrap { flex-wrap: wrap !important; }
  .flex-lg-nowrap { flex-wrap: nowrap !important; }
  .flex-lg-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .flex-lg-fill { flex: 1 1 auto !important; }
  .flex-lg-grow-0 { flex-grow: 0 !important; }
  .flex-lg-grow-1 { flex-grow: 1 !important; }
  .flex-lg-shrink-0 { flex-shrink: 0 !important; }
  .flex-lg-shrink-1 { flex-shrink: 1 !important; }
  .justify-content-lg-start { justify-content: flex-start !important; }
  .justify-content-lg-end { justify-content: flex-end !important; }
  .justify-content-lg-center { justify-content: center !important; }
  .justify-content-lg-between { justify-content: space-between !important; }
  .justify-content-lg-around { justify-content: space-around !important; }
  .align-items-lg-start { align-items: flex-start !important; }
  .align-items-lg-end { align-items: flex-end !important; }
  .align-items-lg-center { align-items: center !important; }
  .align-items-lg-baseline { align-items: baseline !important; }
  .align-items-lg-stretch { align-items: stretch !important; }
  .align-content-lg-start { align-content: flex-start !important; }
  .align-content-lg-end { align-content: flex-end !important; }
  .align-content-lg-center { align-content: center !important; }
  .align-content-lg-between { align-content: space-between !important; }
  .align-content-lg-around { align-content: space-around !important; }
  .align-content-lg-stretch { align-content: stretch !important; }
  .align-self-lg-auto { align-self: auto !important; }
  .align-self-lg-start { align-self: flex-start !important; }
  .align-self-lg-end { align-self: flex-end !important; }
  .align-self-lg-center { align-self: center !important; }
  .align-self-lg-baseline { align-self: baseline !important; }
  .align-self-lg-stretch { align-self: stretch !important; }
}

@media (min-width: 1200px) {
  .flex-xl-row { flex-direction: row !important; }
  .flex-xl-column { flex-direction: column !important; }
  .flex-xl-row-reverse { flex-direction: row-reverse !important; }
  .flex-xl-column-reverse { flex-direction: column-reverse !important; }
  .flex-xl-wrap { flex-wrap: wrap !important; }
  .flex-xl-nowrap { flex-wrap: nowrap !important; }
  .flex-xl-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .flex-xl-fill { flex: 1 1 auto !important; }
  .flex-xl-grow-0 { flex-grow: 0 !important; }
  .flex-xl-grow-1 { flex-grow: 1 !important; }
  .flex-xl-shrink-0 { flex-shrink: 0 !important; }
  .flex-xl-shrink-1 { flex-shrink: 1 !important; }
  .justify-content-xl-start { justify-content: flex-start !important; }
  .justify-content-xl-end { justify-content: flex-end !important; }
  .justify-content-xl-center { justify-content: center !important; }
  .justify-content-xl-between { justify-content: space-between !important; }
  .justify-content-xl-around { justify-content: space-around !important; }
  .align-items-xl-start { align-items: flex-start !important; }
  .align-items-xl-end { align-items: flex-end !important; }
  .align-items-xl-center { align-items: center !important; }
  .align-items-xl-baseline { align-items: baseline !important; }
  .align-items-xl-stretch { align-items: stretch !important; }
  .align-content-xl-start { align-content: flex-start !important; }
  .align-content-xl-end { align-content: flex-end !important; }
  .align-content-xl-center { align-content: center !important; }
  .align-content-xl-between { align-content: space-between !important; }
  .align-content-xl-around { align-content: space-around !important; }
  .align-content-xl-stretch { align-content: stretch !important; }
  .align-self-xl-auto { align-self: auto !important; }
  .align-self-xl-start { align-self: flex-start !important; }
  .align-self-xl-end { align-self: flex-end !important; }
  .align-self-xl-center { align-self: center !important; }
  .align-self-xl-baseline { align-self: baseline !important; }
  .align-self-xl-stretch { align-self: stretch !important; }
}

.float-left { float: left !important; }

.float-right { float: right !important; }

.float-none { float: none !important; }

@media (min-width: 576px) {
  .float-sm-left { float: left !important; }
  .float-sm-right { float: right !important; }
  .float-sm-none { float: none !important; }
}

@media (min-width: 768px) {
  .float-md-left { float: left !important; }
  .float-md-right { float: right !important; }
  .float-md-none { float: none !important; }
}

@media (min-width: 992px) {
  .float-lg-left { float: left !important; }
  .float-lg-right { float: right !important; }
  .float-lg-none { float: none !important; }
}

@media (min-width: 1200px) {
  .float-xl-left { float: left !important; }
  .float-xl-right { float: right !important; }
  .float-xl-none { float: none !important; }
}

.overflow-auto { overflow: auto !important; }

.overflow-hidden { overflow: hidden !important; }

.position-static { position: static !important; }

.position-relative { position: relative !important; }

.position-absolute { position: absolute !important; }

.position-fixed { position: fixed !important; }

.position-sticky { position: sticky !important; }

.fixed-top { position: fixed; top: 0px; right: 0px; left: 0px; z-index: 1030; }

.fixed-bottom { position: fixed; right: 0px; bottom: 0px; left: 0px; z-index: 1030; }

@supports ((position:-webkit-sticky) or (position:sticky)) {
  .sticky-top { position: sticky; top: 0px; z-index: 1020; }
}

.sr-only { position: absolute; width: 1px; height: 1px; padding: 0px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; border: 0px; }

.sr-only-focusable:active, .sr-only-focusable:focus { position: static; width: auto; height: auto; overflow: visible; clip: auto; white-space: normal; }

.shadow-sm { box-shadow: rgba(0, 0, 0, 0.075) 0px 0.125rem 0.25rem !important; }

.shadow { box-shadow: rgba(0, 0, 0, 0.15) 0px 0.5rem 1rem !important; }

.shadow-lg { box-shadow: rgba(0, 0, 0, 0.176) 0px 1rem 3rem !important; }

.shadow-none { box-shadow: none !important; }

.w-25 { width: 25% !important; }

.w-50 { width: 50% !important; }

.w-75 { width: 75% !important; }

.w-100 { width: 100% !important; }

.w-auto { width: auto !important; }

.h-25 { height: 25% !important; }

.h-50 { height: 50% !important; }

.h-75 { height: 75% !important; }

.h-100 { height: 100% !important; }

.h-auto { height: auto !important; }

.mw-100 { max-width: 100% !important; }

.mh-100 { max-height: 100% !important; }

.min-vw-100 { min-width: 100vw !important; }

.min-vh-100 { min-height: 100vh !important; }

.vw-100 { width: 100vw !important; }

.vh-100 { height: 100vh !important; }

.m-0 { margin: 0px !important; }

.mt-0, .my-0 { margin-top: 0px !important; }

.mr-0, .mx-0 { margin-right: 0px !important; }

.mb-0, .my-0 { margin-bottom: 0px !important; }

.ml-0, .mx-0 { margin-left: 0px !important; }

.m-1 { margin: 0.25rem !important; }

.mt-1, .my-1 { margin-top: 0.25rem !important; }

.mr-1, .mx-1 { margin-right: 0.25rem !important; }

.mb-1, .my-1 { margin-bottom: 0.25rem !important; }

.ml-1, .mx-1 { margin-left: 0.25rem !important; }

.m-2 { margin: 0.5rem !important; }

.mt-2, .my-2 { margin-top: 0.5rem !important; }

.mr-2, .mx-2 { margin-right: 0.5rem !important; }

.mb-2, .my-2 { margin-bottom: 0.5rem !important; }

.ml-2, .mx-2 { margin-left: 0.5rem !important; }

.m-3 { margin: 1rem !important; }

.mt-3, .my-3 { margin-top: 1rem !important; }

.mr-3, .mx-3 { margin-right: 1rem !important; }

.mb-3, .my-3 { margin-bottom: 1rem !important; }

.ml-3, .mx-3 { margin-left: 1rem !important; }

.m-4 { margin: 1.5rem !important; }

.mt-4, .my-4 { margin-top: 1.5rem !important; }

.mr-4, .mx-4 { margin-right: 1.5rem !important; }

.mb-4, .my-4 { margin-bottom: 1.5rem !important; }

.ml-4, .mx-4 { margin-left: 1.5rem !important; }

.m-5 { margin: 3rem !important; }

.mt-5, .my-5 { margin-top: 3rem !important; }

.mr-5, .mx-5 { margin-right: 3rem !important; }

.mb-5, .my-5 { margin-bottom: 3rem !important; }

.ml-5, .mx-5 { margin-left: 3rem !important; }

.p-0 { padding: 0px !important; }

.pt-0, .py-0 { padding-top: 0px !important; }

.pr-0, .px-0 { padding-right: 0px !important; }

.pb-0, .py-0 { padding-bottom: 0px !important; }

.pl-0, .px-0 { padding-left: 0px !important; }

.p-1 { padding: 0.25rem !important; }

.pt-1, .py-1 { padding-top: 0.25rem !important; }

.pr-1, .px-1 { padding-right: 0.25rem !important; }

.pb-1, .py-1 { padding-bottom: 0.25rem !important; }

.pl-1, .px-1 { padding-left: 0.25rem !important; }

.p-2 { padding: 0.5rem !important; }

.pt-2, .py-2 { padding-top: 0.5rem !important; }

.pr-2, .px-2 { padding-right: 0.5rem !important; }

.pb-2, .py-2 { padding-bottom: 0.5rem !important; }

.pl-2, .px-2 { padding-left: 0.5rem !important; }

.p-3 { padding: 1rem !important; }

.pt-3, .py-3 { padding-top: 1rem !important; }

.pr-3, .px-3 { padding-right: 1rem !important; }

.pb-3, .py-3 { padding-bottom: 1rem !important; }

.pl-3, .px-3 { padding-left: 1rem !important; }

.p-4 { padding: 1.5rem !important; }

.pt-4, .py-4 { padding-top: 1.5rem !important; }

.pr-4, .px-4 { padding-right: 1.5rem !important; }

.pb-4, .py-4 { padding-bottom: 1.5rem !important; }

.pl-4, .px-4 { padding-left: 1.5rem !important; }

.p-5 { padding: 3rem !important; }

.pt-5, .py-5 { padding-top: 3rem !important; }

.pr-5, .px-5 { padding-right: 3rem !important; }

.pb-5, .py-5 { padding-bottom: 3rem !important; }

.pl-5, .px-5 { padding-left: 3rem !important; }

.m-n1 { margin: -0.25rem !important; }

.mt-n1, .my-n1 { margin-top: -0.25rem !important; }

.mr-n1, .mx-n1 { margin-right: -0.25rem !important; }

.mb-n1, .my-n1 { margin-bottom: -0.25rem !important; }

.ml-n1, .mx-n1 { margin-left: -0.25rem !important; }

.m-n2 { margin: -0.5rem !important; }

.mt-n2, .my-n2 { margin-top: -0.5rem !important; }

.mr-n2, .mx-n2 { margin-right: -0.5rem !important; }

.mb-n2, .my-n2 { margin-bottom: -0.5rem !important; }

.ml-n2, .mx-n2 { margin-left: -0.5rem !important; }

.m-n3 { margin: -1rem !important; }

.mt-n3, .my-n3 { margin-top: -1rem !important; }

.mr-n3, .mx-n3 { margin-right: -1rem !important; }

.mb-n3, .my-n3 { margin-bottom: -1rem !important; }

.ml-n3, .mx-n3 { margin-left: -1rem !important; }

.m-n4 { margin: -1.5rem !important; }

.mt-n4, .my-n4 { margin-top: -1.5rem !important; }

.mr-n4, .mx-n4 { margin-right: -1.5rem !important; }

.mb-n4, .my-n4 { margin-bottom: -1.5rem !important; }

.ml-n4, .mx-n4 { margin-left: -1.5rem !important; }

.m-n5 { margin: -3rem !important; }

.mt-n5, .my-n5 { margin-top: -3rem !important; }

.mr-n5, .mx-n5 { margin-right: -3rem !important; }

.mb-n5, .my-n5 { margin-bottom: -3rem !important; }

.ml-n5, .mx-n5 { margin-left: -3rem !important; }

.m-auto { margin: auto !important; }

.mt-auto, .my-auto { margin-top: auto !important; }

.mr-auto, .mx-auto { margin-right: auto !important; }

.mb-auto, .my-auto { margin-bottom: auto !important; }

.ml-auto, .mx-auto { margin-left: auto !important; }

@media (min-width: 576px) {
  .m-sm-0 { margin: 0px !important; }
  .mt-sm-0, .my-sm-0 { margin-top: 0px !important; }
  .mr-sm-0, .mx-sm-0 { margin-right: 0px !important; }
  .mb-sm-0, .my-sm-0 { margin-bottom: 0px !important; }
  .ml-sm-0, .mx-sm-0 { margin-left: 0px !important; }
  .m-sm-1 { margin: 0.25rem !important; }
  .mt-sm-1, .my-sm-1 { margin-top: 0.25rem !important; }
  .mr-sm-1, .mx-sm-1 { margin-right: 0.25rem !important; }
  .mb-sm-1, .my-sm-1 { margin-bottom: 0.25rem !important; }
  .ml-sm-1, .mx-sm-1 { margin-left: 0.25rem !important; }
  .m-sm-2 { margin: 0.5rem !important; }
  .mt-sm-2, .my-sm-2 { margin-top: 0.5rem !important; }
  .mr-sm-2, .mx-sm-2 { margin-right: 0.5rem !important; }
  .mb-sm-2, .my-sm-2 { margin-bottom: 0.5rem !important; }
  .ml-sm-2, .mx-sm-2 { margin-left: 0.5rem !important; }
  .m-sm-3 { margin: 1rem !important; }
  .mt-sm-3, .my-sm-3 { margin-top: 1rem !important; }
  .mr-sm-3, .mx-sm-3 { margin-right: 1rem !important; }
  .mb-sm-3, .my-sm-3 { margin-bottom: 1rem !important; }
  .ml-sm-3, .mx-sm-3 { margin-left: 1rem !important; }
  .m-sm-4 { margin: 1.5rem !important; }
  .mt-sm-4, .my-sm-4 { margin-top: 1.5rem !important; }
  .mr-sm-4, .mx-sm-4 { margin-right: 1.5rem !important; }
  .mb-sm-4, .my-sm-4 { margin-bottom: 1.5rem !important; }
  .ml-sm-4, .mx-sm-4 { margin-left: 1.5rem !important; }
  .m-sm-5 { margin: 3rem !important; }
  .mt-sm-5, .my-sm-5 { margin-top: 3rem !important; }
  .mr-sm-5, .mx-sm-5 { margin-right: 3rem !important; }
  .mb-sm-5, .my-sm-5 { margin-bottom: 3rem !important; }
  .ml-sm-5, .mx-sm-5 { margin-left: 3rem !important; }
  .p-sm-0 { padding: 0px !important; }
  .pt-sm-0, .py-sm-0 { padding-top: 0px !important; }
  .pr-sm-0, .px-sm-0 { padding-right: 0px !important; }
  .pb-sm-0, .py-sm-0 { padding-bottom: 0px !important; }
  .pl-sm-0, .px-sm-0 { padding-left: 0px !important; }
  .p-sm-1 { padding: 0.25rem !important; }
  .pt-sm-1, .py-sm-1 { padding-top: 0.25rem !important; }
  .pr-sm-1, .px-sm-1 { padding-right: 0.25rem !important; }
  .pb-sm-1, .py-sm-1 { padding-bottom: 0.25rem !important; }
  .pl-sm-1, .px-sm-1 { padding-left: 0.25rem !important; }
  .p-sm-2 { padding: 0.5rem !important; }
  .pt-sm-2, .py-sm-2 { padding-top: 0.5rem !important; }
  .pr-sm-2, .px-sm-2 { padding-right: 0.5rem !important; }
  .pb-sm-2, .py-sm-2 { padding-bottom: 0.5rem !important; }
  .pl-sm-2, .px-sm-2 { padding-left: 0.5rem !important; }
  .p-sm-3 { padding: 1rem !important; }
  .pt-sm-3, .py-sm-3 { padding-top: 1rem !important; }
  .pr-sm-3, .px-sm-3 { padding-right: 1rem !important; }
  .pb-sm-3, .py-sm-3 { padding-bottom: 1rem !important; }
  .pl-sm-3, .px-sm-3 { padding-left: 1rem !important; }
  .p-sm-4 { padding: 1.5rem !important; }
  .pt-sm-4, .py-sm-4 { padding-top: 1.5rem !important; }
  .pr-sm-4, .px-sm-4 { padding-right: 1.5rem !important; }
  .pb-sm-4, .py-sm-4 { padding-bottom: 1.5rem !important; }
  .pl-sm-4, .px-sm-4 { padding-left: 1.5rem !important; }
  .p-sm-5 { padding: 3rem !important; }
  .pt-sm-5, .py-sm-5 { padding-top: 3rem !important; }
  .pr-sm-5, .px-sm-5 { padding-right: 3rem !important; }
  .pb-sm-5, .py-sm-5 { padding-bottom: 3rem !important; }
  .pl-sm-5, .px-sm-5 { padding-left: 3rem !important; }
  .m-sm-n1 { margin: -0.25rem !important; }
  .mt-sm-n1, .my-sm-n1 { margin-top: -0.25rem !important; }
  .mr-sm-n1, .mx-sm-n1 { margin-right: -0.25rem !important; }
  .mb-sm-n1, .my-sm-n1 { margin-bottom: -0.25rem !important; }
  .ml-sm-n1, .mx-sm-n1 { margin-left: -0.25rem !important; }
  .m-sm-n2 { margin: -0.5rem !important; }
  .mt-sm-n2, .my-sm-n2 { margin-top: -0.5rem !important; }
  .mr-sm-n2, .mx-sm-n2 { margin-right: -0.5rem !important; }
  .mb-sm-n2, .my-sm-n2 { margin-bottom: -0.5rem !important; }
  .ml-sm-n2, .mx-sm-n2 { margin-left: -0.5rem !important; }
  .m-sm-n3 { margin: -1rem !important; }
  .mt-sm-n3, .my-sm-n3 { margin-top: -1rem !important; }
  .mr-sm-n3, .mx-sm-n3 { margin-right: -1rem !important; }
  .mb-sm-n3, .my-sm-n3 { margin-bottom: -1rem !important; }
  .ml-sm-n3, .mx-sm-n3 { margin-left: -1rem !important; }
  .m-sm-n4 { margin: -1.5rem !important; }
  .mt-sm-n4, .my-sm-n4 { margin-top: -1.5rem !important; }
  .mr-sm-n4, .mx-sm-n4 { margin-right: -1.5rem !important; }
  .mb-sm-n4, .my-sm-n4 { margin-bottom: -1.5rem !important; }
  .ml-sm-n4, .mx-sm-n4 { margin-left: -1.5rem !important; }
  .m-sm-n5 { margin: -3rem !important; }
  .mt-sm-n5, .my-sm-n5 { margin-top: -3rem !important; }
  .mr-sm-n5, .mx-sm-n5 { margin-right: -3rem !important; }
  .mb-sm-n5, .my-sm-n5 { margin-bottom: -3rem !important; }
  .ml-sm-n5, .mx-sm-n5 { margin-left: -3rem !important; }
  .m-sm-auto { margin: auto !important; }
  .mt-sm-auto, .my-sm-auto { margin-top: auto !important; }
  .mr-sm-auto, .mx-sm-auto { margin-right: auto !important; }
  .mb-sm-auto, .my-sm-auto { margin-bottom: auto !important; }
  .ml-sm-auto, .mx-sm-auto { margin-left: auto !important; }
}

@media (min-width: 768px) {
  .m-md-0 { margin: 0px !important; }
  .mt-md-0, .my-md-0 { margin-top: 0px !important; }
  .mr-md-0, .mx-md-0 { margin-right: 0px !important; }
  .mb-md-0, .my-md-0 { margin-bottom: 0px !important; }
  .ml-md-0, .mx-md-0 { margin-left: 0px !important; }
  .m-md-1 { margin: 0.25rem !important; }
  .mt-md-1, .my-md-1 { margin-top: 0.25rem !important; }
  .mr-md-1, .mx-md-1 { margin-right: 0.25rem !important; }
  .mb-md-1, .my-md-1 { margin-bottom: 0.25rem !important; }
  .ml-md-1, .mx-md-1 { margin-left: 0.25rem !important; }
  .m-md-2 { margin: 0.5rem !important; }
  .mt-md-2, .my-md-2 { margin-top: 0.5rem !important; }
  .mr-md-2, .mx-md-2 { margin-right: 0.5rem !important; }
  .mb-md-2, .my-md-2 { margin-bottom: 0.5rem !important; }
  .ml-md-2, .mx-md-2 { margin-left: 0.5rem !important; }
  .m-md-3 { margin: 1rem !important; }
  .mt-md-3, .my-md-3 { margin-top: 1rem !important; }
  .mr-md-3, .mx-md-3 { margin-right: 1rem !important; }
  .mb-md-3, .my-md-3 { margin-bottom: 1rem !important; }
  .ml-md-3, .mx-md-3 { margin-left: 1rem !important; }
  .m-md-4 { margin: 1.5rem !important; }
  .mt-md-4, .my-md-4 { margin-top: 1.5rem !important; }
  .mr-md-4, .mx-md-4 { margin-right: 1.5rem !important; }
  .mb-md-4, .my-md-4 { margin-bottom: 1.5rem !important; }
  .ml-md-4, .mx-md-4 { margin-left: 1.5rem !important; }
  .m-md-5 { margin: 3rem !important; }
  .mt-md-5, .my-md-5 { margin-top: 3rem !important; }
  .mr-md-5, .mx-md-5 { margin-right: 3rem !important; }
  .mb-md-5, .my-md-5 { margin-bottom: 3rem !important; }
  .ml-md-5, .mx-md-5 { margin-left: 3rem !important; }
  .p-md-0 { padding: 0px !important; }
  .pt-md-0, .py-md-0 { padding-top: 0px !important; }
  .pr-md-0, .px-md-0 { padding-right: 0px !important; }
  .pb-md-0, .py-md-0 { padding-bottom: 0px !important; }
  .pl-md-0, .px-md-0 { padding-left: 0px !important; }
  .p-md-1 { padding: 0.25rem !important; }
  .pt-md-1, .py-md-1 { padding-top: 0.25rem !important; }
  .pr-md-1, .px-md-1 { padding-right: 0.25rem !important; }
  .pb-md-1, .py-md-1 { padding-bottom: 0.25rem !important; }
  .pl-md-1, .px-md-1 { padding-left: 0.25rem !important; }
  .p-md-2 { padding: 0.5rem !important; }
  .pt-md-2, .py-md-2 { padding-top: 0.5rem !important; }
  .pr-md-2, .px-md-2 { padding-right: 0.5rem !important; }
  .pb-md-2, .py-md-2 { padding-bottom: 0.5rem !important; }
  .pl-md-2, .px-md-2 { padding-left: 0.5rem !important; }
  .p-md-3 { padding: 1rem !important; }
  .pt-md-3, .py-md-3 { padding-top: 1rem !important; }
  .pr-md-3, .px-md-3 { padding-right: 1rem !important; }
  .pb-md-3, .py-md-3 { padding-bottom: 1rem !important; }
  .pl-md-3, .px-md-3 { padding-left: 1rem !important; }
  .p-md-4 { padding: 1.5rem !important; }
  .pt-md-4, .py-md-4 { padding-top: 1.5rem !important; }
  .pr-md-4, .px-md-4 { padding-right: 1.5rem !important; }
  .pb-md-4, .py-md-4 { padding-bottom: 1.5rem !important; }
  .pl-md-4, .px-md-4 { padding-left: 1.5rem !important; }
  .p-md-5 { padding: 3rem !important; }
  .pt-md-5, .py-md-5 { padding-top: 3rem !important; }
  .pr-md-5, .px-md-5 { padding-right: 3rem !important; }
  .pb-md-5, .py-md-5 { padding-bottom: 3rem !important; }
  .pl-md-5, .px-md-5 { padding-left: 3rem !important; }
  .m-md-n1 { margin: -0.25rem !important; }
  .mt-md-n1, .my-md-n1 { margin-top: -0.25rem !important; }
  .mr-md-n1, .mx-md-n1 { margin-right: -0.25rem !important; }
  .mb-md-n1, .my-md-n1 { margin-bottom: -0.25rem !important; }
  .ml-md-n1, .mx-md-n1 { margin-left: -0.25rem !important; }
  .m-md-n2 { margin: -0.5rem !important; }
  .mt-md-n2, .my-md-n2 { margin-top: -0.5rem !important; }
  .mr-md-n2, .mx-md-n2 { margin-right: -0.5rem !important; }
  .mb-md-n2, .my-md-n2 { margin-bottom: -0.5rem !important; }
  .ml-md-n2, .mx-md-n2 { margin-left: -0.5rem !important; }
  .m-md-n3 { margin: -1rem !important; }
  .mt-md-n3, .my-md-n3 { margin-top: -1rem !important; }
  .mr-md-n3, .mx-md-n3 { margin-right: -1rem !important; }
  .mb-md-n3, .my-md-n3 { margin-bottom: -1rem !important; }
  .ml-md-n3, .mx-md-n3 { margin-left: -1rem !important; }
  .m-md-n4 { margin: -1.5rem !important; }
  .mt-md-n4, .my-md-n4 { margin-top: -1.5rem !important; }
  .mr-md-n4, .mx-md-n4 { margin-right: -1.5rem !important; }
  .mb-md-n4, .my-md-n4 { margin-bottom: -1.5rem !important; }
  .ml-md-n4, .mx-md-n4 { margin-left: -1.5rem !important; }
  .m-md-n5 { margin: -3rem !important; }
  .mt-md-n5, .my-md-n5 { margin-top: -3rem !important; }
  .mr-md-n5, .mx-md-n5 { margin-right: -3rem !important; }
  .mb-md-n5, .my-md-n5 { margin-bottom: -3rem !important; }
  .ml-md-n5, .mx-md-n5 { margin-left: -3rem !important; }
  .m-md-auto { margin: auto !important; }
  .mt-md-auto, .my-md-auto { margin-top: auto !important; }
  .mr-md-auto, .mx-md-auto { margin-right: auto !important; }
  .mb-md-auto, .my-md-auto { margin-bottom: auto !important; }
  .ml-md-auto, .mx-md-auto { margin-left: auto !important; }
}

@media (min-width: 992px) {
  .m-lg-0 { margin: 0px !important; }
  .mt-lg-0, .my-lg-0 { margin-top: 0px !important; }
  .mr-lg-0, .mx-lg-0 { margin-right: 0px !important; }
  .mb-lg-0, .my-lg-0 { margin-bottom: 0px !important; }
  .ml-lg-0, .mx-lg-0 { margin-left: 0px !important; }
  .m-lg-1 { margin: 0.25rem !important; }
  .mt-lg-1, .my-lg-1 { margin-top: 0.25rem !important; }
  .mr-lg-1, .mx-lg-1 { margin-right: 0.25rem !important; }
  .mb-lg-1, .my-lg-1 { margin-bottom: 0.25rem !important; }
  .ml-lg-1, .mx-lg-1 { margin-left: 0.25rem !important; }
  .m-lg-2 { margin: 0.5rem !important; }
  .mt-lg-2, .my-lg-2 { margin-top: 0.5rem !important; }
  .mr-lg-2, .mx-lg-2 { margin-right: 0.5rem !important; }
  .mb-lg-2, .my-lg-2 { margin-bottom: 0.5rem !important; }
  .ml-lg-2, .mx-lg-2 { margin-left: 0.5rem !important; }
  .m-lg-3 { margin: 1rem !important; }
  .mt-lg-3, .my-lg-3 { margin-top: 1rem !important; }
  .mr-lg-3, .mx-lg-3 { margin-right: 1rem !important; }
  .mb-lg-3, .my-lg-3 { margin-bottom: 1rem !important; }
  .ml-lg-3, .mx-lg-3 { margin-left: 1rem !important; }
  .m-lg-4 { margin: 1.5rem !important; }
  .mt-lg-4, .my-lg-4 { margin-top: 1.5rem !important; }
  .mr-lg-4, .mx-lg-4 { margin-right: 1.5rem !important; }
  .mb-lg-4, .my-lg-4 { margin-bottom: 1.5rem !important; }
  .ml-lg-4, .mx-lg-4 { margin-left: 1.5rem !important; }
  .m-lg-5 { margin: 3rem !important; }
  .mt-lg-5, .my-lg-5 { margin-top: 3rem !important; }
  .mr-lg-5, .mx-lg-5 { margin-right: 3rem !important; }
  .mb-lg-5, .my-lg-5 { margin-bottom: 3rem !important; }
  .ml-lg-5, .mx-lg-5 { margin-left: 3rem !important; }
  .p-lg-0 { padding: 0px !important; }
  .pt-lg-0, .py-lg-0 { padding-top: 0px !important; }
  .pr-lg-0, .px-lg-0 { padding-right: 0px !important; }
  .pb-lg-0, .py-lg-0 { padding-bottom: 0px !important; }
  .pl-lg-0, .px-lg-0 { padding-left: 0px !important; }
  .p-lg-1 { padding: 0.25rem !important; }
  .pt-lg-1, .py-lg-1 { padding-top: 0.25rem !important; }
  .pr-lg-1, .px-lg-1 { padding-right: 0.25rem !important; }
  .pb-lg-1, .py-lg-1 { padding-bottom: 0.25rem !important; }
  .pl-lg-1, .px-lg-1 { padding-left: 0.25rem !important; }
  .p-lg-2 { padding: 0.5rem !important; }
  .pt-lg-2, .py-lg-2 { padding-top: 0.5rem !important; }
  .pr-lg-2, .px-lg-2 { padding-right: 0.5rem !important; }
  .pb-lg-2, .py-lg-2 { padding-bottom: 0.5rem !important; }
  .pl-lg-2, .px-lg-2 { padding-left: 0.5rem !important; }
  .p-lg-3 { padding: 1rem !important; }
  .pt-lg-3, .py-lg-3 { padding-top: 1rem !important; }
  .pr-lg-3, .px-lg-3 { padding-right: 1rem !important; }
  .pb-lg-3, .py-lg-3 { padding-bottom: 1rem !important; }
  .pl-lg-3, .px-lg-3 { padding-left: 1rem !important; }
  .p-lg-4 { padding: 1.5rem !important; }
  .pt-lg-4, .py-lg-4 { padding-top: 1.5rem !important; }
  .pr-lg-4, .px-lg-4 { padding-right: 1.5rem !important; }
  .pb-lg-4, .py-lg-4 { padding-bottom: 1.5rem !important; }
  .pl-lg-4, .px-lg-4 { padding-left: 1.5rem !important; }
  .p-lg-5 { padding: 3rem !important; }
  .pt-lg-5, .py-lg-5 { padding-top: 3rem !important; }
  .pr-lg-5, .px-lg-5 { padding-right: 3rem !important; }
  .pb-lg-5, .py-lg-5 { padding-bottom: 3rem !important; }
  .pl-lg-5, .px-lg-5 { padding-left: 3rem !important; }
  .m-lg-n1 { margin: -0.25rem !important; }
  .mt-lg-n1, .my-lg-n1 { margin-top: -0.25rem !important; }
  .mr-lg-n1, .mx-lg-n1 { margin-right: -0.25rem !important; }
  .mb-lg-n1, .my-lg-n1 { margin-bottom: -0.25rem !important; }
  .ml-lg-n1, .mx-lg-n1 { margin-left: -0.25rem !important; }
  .m-lg-n2 { margin: -0.5rem !important; }
  .mt-lg-n2, .my-lg-n2 { margin-top: -0.5rem !important; }
  .mr-lg-n2, .mx-lg-n2 { margin-right: -0.5rem !important; }
  .mb-lg-n2, .my-lg-n2 { margin-bottom: -0.5rem !important; }
  .ml-lg-n2, .mx-lg-n2 { margin-left: -0.5rem !important; }
  .m-lg-n3 { margin: -1rem !important; }
  .mt-lg-n3, .my-lg-n3 { margin-top: -1rem !important; }
  .mr-lg-n3, .mx-lg-n3 { margin-right: -1rem !important; }
  .mb-lg-n3, .my-lg-n3 { margin-bottom: -1rem !important; }
  .ml-lg-n3, .mx-lg-n3 { margin-left: -1rem !important; }
  .m-lg-n4 { margin: -1.5rem !important; }
  .mt-lg-n4, .my-lg-n4 { margin-top: -1.5rem !important; }
  .mr-lg-n4, .mx-lg-n4 { margin-right: -1.5rem !important; }
  .mb-lg-n4, .my-lg-n4 { margin-bottom: -1.5rem !important; }
  .ml-lg-n4, .mx-lg-n4 { margin-left: -1.5rem !important; }
  .m-lg-n5 { margin: -3rem !important; }
  .mt-lg-n5, .my-lg-n5 { margin-top: -3rem !important; }
  .mr-lg-n5, .mx-lg-n5 { margin-right: -3rem !important; }
  .mb-lg-n5, .my-lg-n5 { margin-bottom: -3rem !important; }
  .ml-lg-n5, .mx-lg-n5 { margin-left: -3rem !important; }
  .m-lg-auto { margin: auto !important; }
  .mt-lg-auto, .my-lg-auto { margin-top: auto !important; }
  .mr-lg-auto, .mx-lg-auto { margin-right: auto !important; }
  .mb-lg-auto, .my-lg-auto { margin-bottom: auto !important; }
  .ml-lg-auto, .mx-lg-auto { margin-left: auto !important; }
}

@media (min-width: 1200px) {
  .m-xl-0 { margin: 0px !important; }
  .mt-xl-0, .my-xl-0 { margin-top: 0px !important; }
  .mr-xl-0, .mx-xl-0 { margin-right: 0px !important; }
  .mb-xl-0, .my-xl-0 { margin-bottom: 0px !important; }
  .ml-xl-0, .mx-xl-0 { margin-left: 0px !important; }
  .m-xl-1 { margin: 0.25rem !important; }
  .mt-xl-1, .my-xl-1 { margin-top: 0.25rem !important; }
  .mr-xl-1, .mx-xl-1 { margin-right: 0.25rem !important; }
  .mb-xl-1, .my-xl-1 { margin-bottom: 0.25rem !important; }
  .ml-xl-1, .mx-xl-1 { margin-left: 0.25rem !important; }
  .m-xl-2 { margin: 0.5rem !important; }
  .mt-xl-2, .my-xl-2 { margin-top: 0.5rem !important; }
  .mr-xl-2, .mx-xl-2 { margin-right: 0.5rem !important; }
  .mb-xl-2, .my-xl-2 { margin-bottom: 0.5rem !important; }
  .ml-xl-2, .mx-xl-2 { margin-left: 0.5rem !important; }
  .m-xl-3 { margin: 1rem !important; }
  .mt-xl-3, .my-xl-3 { margin-top: 1rem !important; }
  .mr-xl-3, .mx-xl-3 { margin-right: 1rem !important; }
  .mb-xl-3, .my-xl-3 { margin-bottom: 1rem !important; }
  .ml-xl-3, .mx-xl-3 { margin-left: 1rem !important; }
  .m-xl-4 { margin: 1.5rem !important; }
  .mt-xl-4, .my-xl-4 { margin-top: 1.5rem !important; }
  .mr-xl-4, .mx-xl-4 { margin-right: 1.5rem !important; }
  .mb-xl-4, .my-xl-4 { margin-bottom: 1.5rem !important; }
  .ml-xl-4, .mx-xl-4 { margin-left: 1.5rem !important; }
  .m-xl-5 { margin: 3rem !important; }
  .mt-xl-5, .my-xl-5 { margin-top: 3rem !important; }
  .mr-xl-5, .mx-xl-5 { margin-right: 3rem !important; }
  .mb-xl-5, .my-xl-5 { margin-bottom: 3rem !important; }
  .ml-xl-5, .mx-xl-5 { margin-left: 3rem !important; }
  .p-xl-0 { padding: 0px !important; }
  .pt-xl-0, .py-xl-0 { padding-top: 0px !important; }
  .pr-xl-0, .px-xl-0 { padding-right: 0px !important; }
  .pb-xl-0, .py-xl-0 { padding-bottom: 0px !important; }
  .pl-xl-0, .px-xl-0 { padding-left: 0px !important; }
  .p-xl-1 { padding: 0.25rem !important; }
  .pt-xl-1, .py-xl-1 { padding-top: 0.25rem !important; }
  .pr-xl-1, .px-xl-1 { padding-right: 0.25rem !important; }
  .pb-xl-1, .py-xl-1 { padding-bottom: 0.25rem !important; }
  .pl-xl-1, .px-xl-1 { padding-left: 0.25rem !important; }
  .p-xl-2 { padding: 0.5rem !important; }
  .pt-xl-2, .py-xl-2 { padding-top: 0.5rem !important; }
  .pr-xl-2, .px-xl-2 { padding-right: 0.5rem !important; }
  .pb-xl-2, .py-xl-2 { padding-bottom: 0.5rem !important; }
  .pl-xl-2, .px-xl-2 { padding-left: 0.5rem !important; }
  .p-xl-3 { padding: 1rem !important; }
  .pt-xl-3, .py-xl-3 { padding-top: 1rem !important; }
  .pr-xl-3, .px-xl-3 { padding-right: 1rem !important; }
  .pb-xl-3, .py-xl-3 { padding-bottom: 1rem !important; }
  .pl-xl-3, .px-xl-3 { padding-left: 1rem !important; }
  .p-xl-4 { padding: 1.5rem !important; }
  .pt-xl-4, .py-xl-4 { padding-top: 1.5rem !important; }
  .pr-xl-4, .px-xl-4 { padding-right: 1.5rem !important; }
  .pb-xl-4, .py-xl-4 { padding-bottom: 1.5rem !important; }
  .pl-xl-4, .px-xl-4 { padding-left: 1.5rem !important; }
  .p-xl-5 { padding: 3rem !important; }
  .pt-xl-5, .py-xl-5 { padding-top: 3rem !important; }
  .pr-xl-5, .px-xl-5 { padding-right: 3rem !important; }
  .pb-xl-5, .py-xl-5 { padding-bottom: 3rem !important; }
  .pl-xl-5, .px-xl-5 { padding-left: 3rem !important; }
  .m-xl-n1 { margin: -0.25rem !important; }
  .mt-xl-n1, .my-xl-n1 { margin-top: -0.25rem !important; }
  .mr-xl-n1, .mx-xl-n1 { margin-right: -0.25rem !important; }
  .mb-xl-n1, .my-xl-n1 { margin-bottom: -0.25rem !important; }
  .ml-xl-n1, .mx-xl-n1 { margin-left: -0.25rem !important; }
  .m-xl-n2 { margin: -0.5rem !important; }
  .mt-xl-n2, .my-xl-n2 { margin-top: -0.5rem !important; }
  .mr-xl-n2, .mx-xl-n2 { margin-right: -0.5rem !important; }
  .mb-xl-n2, .my-xl-n2 { margin-bottom: -0.5rem !important; }
  .ml-xl-n2, .mx-xl-n2 { margin-left: -0.5rem !important; }
  .m-xl-n3 { margin: -1rem !important; }
  .mt-xl-n3, .my-xl-n3 { margin-top: -1rem !important; }
  .mr-xl-n3, .mx-xl-n3 { margin-right: -1rem !important; }
  .mb-xl-n3, .my-xl-n3 { margin-bottom: -1rem !important; }
  .ml-xl-n3, .mx-xl-n3 { margin-left: -1rem !important; }
  .m-xl-n4 { margin: -1.5rem !important; }
  .mt-xl-n4, .my-xl-n4 { margin-top: -1.5rem !important; }
  .mr-xl-n4, .mx-xl-n4 { margin-right: -1.5rem !important; }
  .mb-xl-n4, .my-xl-n4 { margin-bottom: -1.5rem !important; }
  .ml-xl-n4, .mx-xl-n4 { margin-left: -1.5rem !important; }
  .m-xl-n5 { margin: -3rem !important; }
  .mt-xl-n5, .my-xl-n5 { margin-top: -3rem !important; }
  .mr-xl-n5, .mx-xl-n5 { margin-right: -3rem !important; }
  .mb-xl-n5, .my-xl-n5 { margin-bottom: -3rem !important; }
  .ml-xl-n5, .mx-xl-n5 { margin-left: -3rem !important; }
  .m-xl-auto { margin: auto !important; }
  .mt-xl-auto, .my-xl-auto { margin-top: auto !important; }
  .mr-xl-auto, .mx-xl-auto { margin-right: auto !important; }
  .mb-xl-auto, .my-xl-auto { margin-bottom: auto !important; }
  .ml-xl-auto, .mx-xl-auto { margin-left: auto !important; }
}

.text-monospace { font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }

.text-justify { text-align: justify !important; }

.text-wrap { white-space: normal !important; }

.text-nowrap { white-space: nowrap !important; }

.text-truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.text-left { text-align: left !important; }

.text-right { text-align: right !important; }

.text-center { text-align: center !important; }

@media (min-width: 576px) {
  .text-sm-left { text-align: left !important; }
  .text-sm-right { text-align: right !important; }
  .text-sm-center { text-align: center !important; }
}

@media (min-width: 768px) {
  .text-md-left { text-align: left !important; }
  .text-md-right { text-align: right !important; }
  .text-md-center { text-align: center !important; }
}

@media (min-width: 992px) {
  .text-lg-left { text-align: left !important; }
  .text-lg-right { text-align: right !important; }
  .text-lg-center { text-align: center !important; }
}

@media (min-width: 1200px) {
  .text-xl-left { text-align: left !important; }
  .text-xl-right { text-align: right !important; }
  .text-xl-center { text-align: center !important; }
}

.text-lowercase { text-transform: lowercase !important; }

.text-uppercase { text-transform: uppercase !important; }

.text-capitalize { text-transform: capitalize !important; }

.font-weight-light { font-weight: 300 !important; }

.font-weight-lighter { font-weight: lighter !important; }

.font-weight-normal { font-weight: 400 !important; }

.font-weight-bold { font-weight: 700 !important; }

.font-weight-bolder { font-weight: bolder !important; }

.font-italic { font-style: italic !important; }

.text-white { color: rgb(255, 255, 255) !important; }

.text-primary { color: rgb(0, 123, 255) !important; }

a.text-primary:focus, a.text-primary:hover { color: rgb(0, 86, 179) !important; }

.text-secondary { color: rgb(108, 117, 125) !important; }

a.text-secondary:focus, a.text-secondary:hover { color: rgb(73, 79, 84) !important; }

.text-success { color: rgb(40, 167, 69) !important; }

a.text-success:focus, a.text-success:hover { color: rgb(25, 105, 44) !important; }

.text-info { color: rgb(23, 162, 184) !important; }

a.text-info:focus, a.text-info:hover { color: rgb(15, 102, 116) !important; }

.text-warning { color: rgb(255, 193, 7) !important; }

a.text-warning:focus, a.text-warning:hover { color: rgb(186, 139, 0) !important; }

.text-danger { color: rgb(220, 53, 69) !important; }

a.text-danger:focus, a.text-danger:hover { color: rgb(167, 29, 42) !important; }

.text-light { color: rgb(248, 249, 250) !important; }

a.text-light:focus, a.text-light:hover { color: rgb(203, 211, 218) !important; }

.text-dark { color: rgb(52, 58, 64) !important; }

a.text-dark:focus, a.text-dark:hover { color: rgb(18, 20, 22) !important; }

.text-body { color: rgb(33, 37, 41) !important; }

.text-muted { color: rgb(108, 117, 125) !important; }

.text-black-50 { color: rgba(0, 0, 0, 0.5) !important; }

.text-white-50 { color: rgba(255, 255, 255, 0.5) !important; }

.text-hide { font: 0px / 0 a; color: transparent; text-shadow: none; background-color: transparent; border: 0px; }

.text-decoration-none { text-decoration: none !important; }

.text-reset { color: inherit !important; }

.visible { visibility: visible !important; }

.invisible { visibility: hidden !important; }

@media print {
  *, ::after, ::before { text-shadow: none !important; box-shadow: none !important; }
  a:not(.btn) { text-decoration: underline; }
  abbr[title]::after { content: " (" attr(title) ")"; }
  pre { white-space: pre-wrap !important; }
  blockquote, pre { border: 1px solid rgb(173, 181, 189); break-inside: avoid; }
  thead { display: table-header-group; }
  img, tr { break-inside: avoid; }
  h2, h3, p { orphans: 3; widows: 3; }
  h2, h3 { break-after: avoid; }
  @page { size: a3; }
  body { min-width: 992px !important; }
  .container { min-width: 992px !important; }
  .navbar { display: none; }
  .badge { border: 1px solid rgb(0, 0, 0); }
  .table { border-collapse: collapse !important; }
  .table td, .table th { background-color: rgb(255, 255, 255) !important; }
  .table-bordered td, .table-bordered th { border: 1px solid rgb(222, 226, 230) !important; }
  .table-dark { color: inherit; }
  .table-dark tbody + tbody, .table-dark td, .table-dark th, .table-dark thead th { border-color: rgb(222, 226, 230); }
  .table .thead-dark th { color: inherit; border-color: rgb(222, 226, 230); }
}
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/themes/infomoney/style.css?ver=6.4

@charset "utf-8";

.im-mx-auto { }

.im-m-auto { margin-left: auto; margin-right: auto; }

.im-m-1 { margin: 4px; }

.im-m-2 { margin: 8px; }

.im-m-3 { margin: 16px; }

.im-m-4 { margin: 24px; }

.im-m-5 { margin: 32px; }

.im-m-6 { margin: 40px; }

.im-m-7 { margin: 48px; }

.im-m-8 { margin: 64px; }

.im-m-9 { margin: 80px; }

.im-m-10 { margin: 96px; }

.im-mt-1 { margin-top: 4px; }

.im-mt-2 { margin-top: 8px; }

.im-mt-3 { margin-top: 16px; }

.im-mt-4 { margin-top: 24px; }

.im-mt-5 { margin-top: 32px; }

.im-mt-6 { margin-top: 40px; }

.im-mt-7 { margin-top: 48px; }

.im-mt-8 { margin-top: 64px; }

.im-mt-9 { margin-top: 80px; }

.im-mt-10 { margin-top: 96px; }

.im-mb-1 { margin-bottom: 4px; }

.im-mb-2 { margin-bottom: 8px; }

.im-mb-3 { margin-bottom: 16px; }

.im-mb-4 { margin-bottom: 24px; }

.im-mb-5 { margin-bottom: 32px; }

.im-mb-6 { margin-bottom: 40px; }

.im-mb-7 { margin-bottom: 48px; }

.im-mb-8 { margin-bottom: 64px; }

.im-mb-9 { margin-bottom: 80px; }

.im-mb-10 { margin-bottom: 96px; }

.im-ml-1 { margin-left: 4px; }

.im-ml-2 { margin-left: 8px; }

.im-ml-3 { margin-left: 16px; }

.im-ml-4 { margin-left: 24px; }

.im-ml-5 { margin-left: 32px; }

.im-ml-6 { margin-left: 40px; }

.im-ml-7 { margin-left: 48px; }

.im-ml-8 { margin-left: 64px; }

.im-ml-9 { margin-left: 80px; }

.im-ml-10 { margin-left: 96px; }

.im-mr-1 { margin-right: 4px; }

.im-mr-2 { margin-right: 8px; }

.im-mr-3 { margin-right: 16px; }

.im-mr-4 { margin-right: 24px; }

.im-mr-5 { margin-right: 32px; }

.im-mr-6 { margin-right: 40px; }

.im-mr-7 { margin-right: 48px; }

.im-mr-8 { margin-right: 64px; }

.im-mr-9 { margin-right: 80px; }

.im-mr-10 { margin-right: 96px; }

.im-p-1 { padding: 4px; }

.im-p-2 { padding: 8px; }

.im-p-3 { padding: 16px; }

.im-p-4 { padding: 24px; }

.im-p-5 { padding: 32px; }

.im-p-6 { padding: 40px; }

.im-p-7 { padding: 48px; }

.im-p-8 { padding: 64px; }

.im-p-9 { padding: 80px; }

.im-p-10 { padding: 96px; }

.im-px-1 { padding-top: 4px; padding-bottom: 4px; }

.im-px-2 { padding-top: 8px; padding-bottom: 8px; }

.im-px-3 { padding-top: 16px; padding-bottom: 16px; }

.im-px-4 { padding-top: 24px; padding-bottom: 24px; }

.im-px-5 { padding-top: 32px; padding-bottom: 32px; }

.im-px-6 { padding-top: 40px; padding-bottom: 40px; }

.im-px-7 { padding-top: 48px; padding-bottom: 48px; }

.im-px-8 { padding-top: 64px; padding-bottom: 64px; }

.im-px-9 { padding-top: 80px; padding-bottom: 80px; }

.im-px-10 { padding-top: 96px; padding-bottom: 96px; }

.im-py-1 { padding-left: 4px; padding-right: 4px; }

.im-py-2 { padding-left: 8px; padding-right: 8px; }

.im-py-3 { padding-left: 16px; padding-right: 16px; }

.im-py-4 { padding-left: 24px; padding-right: 24px; }

.im-py-5 { padding-left: 32px; padding-right: 32px; }

.im-py-6 { padding-left: 40px; padding-right: 40px; }

.im-py-7 { padding-left: 48px; padding-right: 48px; }

.im-py-8 { padding-left: 64px; padding-right: 64px; }

.im-py-9 { padding-left: 80px; padding-right: 80px; }

.im-py-10 { padding-left: 96px; padding-right: 96px; }

.im-pt-1 { padding-top: 4px; }

.im-pt-2 { padding-top: 8px; }

.im-pt-3 { padding-top: 16px; }

.im-pt-4 { padding-top: 24px; }

.im-pt-5 { padding-top: 32px; }

.im-pt-6 { padding-top: 40px; }

.im-pt-7 { padding-top: 48px; }

.im-pt-8 { padding-top: 64px; }

.im-pt-9 { padding-top: 80px; }

.im-pt-10 { padding-top: 96px; }

.im-pb-1 { padding-bottom: 4px; }

.im-pb-2 { padding-bottom: 8px; }

.im-pb-3 { padding-bottom: 16px; }

.im-pb-4 { padding-bottom: 24px; }

.im-pb-5 { padding-bottom: 32px; }

.im-pb-6 { padding-bottom: 40px; }

.im-pb-7 { padding-bottom: 48px; }

.im-pb-8 { padding-bottom: 64px; }

.im-pb-9 { padding-bottom: 80px; }

.im-pb-10 { padding-bottom: 96px; }

.im-pl-1 { padding-left: 4px; }

.im-pl-2 { padding-left: 8px; }

.im-pl-3 { padding-left: 16px; }

.im-pl-4 { padding-left: 24px; }

.im-pl-5 { padding-left: 32px; }

.im-pl-6 { padding-left: 40px; }

.im-pl-7 { padding-left: 48px; }

.im-pl-8 { padding-left: 64px; }

.im-pl-9 { padding-left: 80px; }

.im-pl-10 { padding-left: 96px; }

.im-pr-1 { padding-right: 4px; }

.im-pr-2 { padding-right: 8px; }

.im-pr-3 { padding-right: 16px; }

.im-pr-4 { padding-right: 24px; }

.im-pr-5 { padding-right: 32px; }

.im-pr-6 { padding-right: 40px; }

.im-pr-7 { padding-right: 48px; }

.im-pr-8 { padding-right: 64px; }

.im-pr-9 { padding-right: 80px; }

.im-pr-10 { padding-right: 96px; }

.material-icons.md-18 { font-size: 18px; }

.material-icons.md-24 { font-size: 24px; }

.material-icons.md-36 { font-size: 36px; }

.material-icons.md-48 { font-size: 48px; }

.fab, .fas { -webkit-font-smoothing: antialiased; display: inline-block; font-style: normal; font-variant: normal; text-rendering: auto; line-height: 1; }

.fa-facebook::before { content: ""; }

.fa-twitter::before { content: ""; }

.fa-whatsapp::before { content: ""; }

.fa-rss::before { content: ""; }

.fa-flipboard::before { content: ""; }

.fa-google::before { content: ""; }

.fa-youtube::before { content: ""; }

.fa-linkedin::before { content: ""; }

.fa-instagram::before { content: ""; }

.fa-soundcloud::before { content: ""; }

.fa-spotify::before { content: ""; }

.fa-telegram-plane::before { content: ""; }

.fa-pinterest::before { content: ""; }

.fa-envelope::before { content: ""; }

.fa-shopping-cart::before { content: ""; }

.fa-caret-down::before { content: ""; }

@font-face { font-family: "Font Awesome 5 Brands"; font-style: normal; font-weight: 400; src: local("Font Awesome 5 Brands"), local("Font-Awesome"), url("assets/fontawesome/fa-brands-400.woff") format("woff"); font-display: swap; }

.fab { font-family: "Font Awesome 5 Brands"; }

@font-face { font-family: "Font Awesome 5 Free"; font-style: normal; font-weight: 900; src: local("Font Awesome 5 Brands"), local("Font-Awesome"), url("assets/fontawesome/fa-solid-900.woff") format("woff"); font-display: swap; }

.fas { font-family: "Font Awesome 5 Free"; font-weight: 900; }

:root { --sapphire:#0091FF; --apatite:#32C5FF; --ruby:#FF5252; --xpamber:#F7B500; --amazonite:#44D7B6; --lightgray:#F5F7F8; --darkgray:#212121; --gray:#6C757D; --gray24:rgba(108, 117, 125, 0.24); --blue:#0091FF; --lightblue:#32C5FF; --yellow:#ffc709; --red:#FF5252; --emerald:#1eb980; --white:#ffffff; }

@keyframes marquee { 
  0% { transform: translate(0px, 0px); }
  100% { transform: translate(-100%, 0px); }
}

* { letter-spacing: normal !important; }

html { scroll-behavior: smooth; }

body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; color: rgb(0, 0, 0); }

body.is-padded { padding-top: 60px; }

a { color: var(--sapphire); }

a:hover { text-decoration: none; }

button:focus { outline: 0px; }

h1 { letter-spacing: -0.02em !important; }

p { font-weight: 400 !important; }

.quotes-header-info div.line-info p { font-weight: 700 !important; }

.href-title { font-size: 16px; font-weight: 400; line-height: 24px; letter-spacing: -0.3px; padding: 16px 0px 0px; margin: 16px 0px 0px; display: flex; border-top: 1px solid rgb(216, 216, 216); }

.href-title span { margin: 0px 4px 0px 0px; }

.href-title strong { margin: 0px 8px 0px 0px; }

.page-title { font-size: 32px; line-height: 32px; letter-spacing: -1.4px; font-weight: 400; }

.page-title span { font-weight: 800; }

.page-title-1 { font-size: 40px; line-height: 48px; font-weight: 700; margin: 0px 0px 24px; color: var(--darkgray); }

.page-title-2 { font-size: 32px; line-height: 32px; letter-spacing: -1.4px; font-weight: 800; }

.page-title-2 span { font-weight: 400; }

.page-title-3 { font-size: 32px; line-height: 32px; letter-spacing: -1.4px; font-weight: 800; }

.section-title { font-size: 24px; line-height: 24px; letter-spacing: -0.4px; padding: 20px 0px 32px; margin-bottom: 0px; border-top: 1px solid rgb(221, 221, 221); position: relative; font-weight: 700; color: rgb(68, 68, 68); }

.page-header { margin: 0px 16px 24px; padding: 0px 0px 20px; flex-basis: calc(100% - 32px); }

.hl-hat { display: block; font-size: 0.875rem; line-height: 16px; margin-bottom: 4px; color: rgb(102, 102, 102); width: 100%; font-weight: 400 !important; }

.hl-hat a { font-weight: 700; }

.post-hat { margin-bottom: 16px; color: var(--gray); display: block; }

.post-hat a { font-weight: 700; }

.hl-title { display: block; }

.hl-title a { color: rgb(0, 0, 0); }

.hl-title a:hover { color: var(--blue); }

.hl-excerpt { margin: 16px 0px 0px; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; font-weight: 400; display: block; }

.hl-excerpt a { color: rgb(33, 33, 33); }

.sticky-top { top: 0.5em; }

.hl-title-category { font-size: 32px; line-height: 36px; font-weight: 700; letter-spacing: -0.01em !important; }

.hl-title-category a { color: rgb(0, 0, 0); letter-spacing: -0.01em !important; }

.hl-title-category-2 { font-size: 20px; line-height: 24px; letter-spacing: -0.5px; font-weight: 700; }

.hl-title-category-2 a { color: rgb(0, 0, 0); }

.hl-description { font-size: 16px; line-height: 24px; margin: 16px 0px 0px; color: rgb(33, 33, 33); }

.hl-title-1 { font-size: 32px; line-height: 36px; letter-spacing: -0.5px; font-weight: 700; }

.hl-title-2 { font-size: 24px; line-height: 28px; font-weight: 700; letter-spacing: -0.01em !important; }

.hl-title-2 a { color: rgb(0, 0, 0); letter-spacing: -0.01em !important; }

.hl-title-3 { font-size: 24px; line-height: 28px; font-weight: 700; letter-spacing: -0.01em !important; }

.hl-title-3 a { color: rgb(17, 17, 17); letter-spacing: -0.01em !important; }

.hl-title-4 { font-size: 20px; line-height: 24px; letter-spacing: -0.5px; font-weight: 700; }

.hl-title-4 a { color: rgb(17, 17, 17); }

.hl-title-5 { font-size: 18px; line-height: 22px; letter-spacing: -0.5px; font-weight: 700; }

.hl-title-5 a { color: rgb(17, 17, 17); }

.hl-title-6 { font-size: 16px; line-height: 20px; letter-spacing: -0.5px; font-weight: 700; }

.hl-title-7 { line-height: 18px; letter-spacing: -0.3px; font-weight: 700; display: flex; font-size: 1rem !important; }

.hl-title-7 i { font-size: 16px; color: rgb(0, 145, 255); margin: 0px 4px 0px 0px; }

.hl-title-7 a { color: rgb(17, 17, 17); }

.hl-title-8 { font-size: 14px; line-height: 16px; font-weight: 600; letter-spacing: -0.1px; color: rgb(17, 17, 17); display: flex; }

.hl-title-8 span { margin: 0px 12px 0px 0px; }

.hl-title-8 i { font-size: 16px; color: rgb(0, 145, 255); margin: 0px 4px 0px 0px; }

.hl-date { display: block; font-size: 12px; line-height: 16px; font-weight: 400; margin-top: 8px; color: var(--gray); }

.article-lead { font-size: 22px; line-height: 28px; letter-spacing: -0.6px; font-weight: 400; margin: 0px 0px 32px; }

.article-terms span { font-size: 14px; font-weight: 700; color: var(--gray); line-height: 1; margin: 16px 0px 0px; }

.article-terms ul { margin: 10px 0px 0px; }

.article-terms ul li { font-size: 12px; line-height: 16px; margin-bottom: 4px; }

.article-terms a { font-weight: 600; font-size: 12px; line-height: 20px; margin-left: 20px; }

.sticky-tags { position: sticky; top: 100px; }

.sticky-tags span { font-size: 12px; line-height: 20px; display: flex; color: var(--gray); align-items: center; }

.sticky-tags span i { font-size: 16px; margin-right: 4px; }

.post-share { display: flex; }

.post-share i.share-icon { font-size: 24px; transform: scaleX(-1); margin: 0px 8px 0px -32px; color: var(--gray); }

.post-share a { display: flex; align-items: center; justify-content: center; color: rgb(255, 255, 255); width: 32px; height: 32px; border-radius: 50%; text-decoration: none; }

.post-share a + a { margin-left: 4px; }

.post-share .post-share-facebook { background-color: rgb(59, 89, 153); }

.post-share .post-share-whatsapp { background-color: rgb(37, 211, 102); }

.post-share .post-share-twitter { background-color: rgb(85, 172, 238); }

.post-share .post-share-linkedin { background-color: rgb(0, 119, 181); }

.post-share .post-share-telegram { background-color: rgb(0, 136, 204); }

.post-share .post-share-flipboard { background-color: rgb(225, 40, 40); }

.post-share .post-share-mail { background-color: rgb(0, 145, 255); }

.brand-image { max-height: 48px; padding: 0px 0px 0px 8px; }

.article-content img { max-width: 100%; height: auto; }

.article-content figure { max-width: calc(100% + 32px); margin: 0px -16px 48px; width: calc(100% + 32px); }

.article-content figure img { height: auto; }

.article-content figure figcaption { font-size: 12px; line-height: 20px; margin: 0px; padding: 16px 16px 0px; color: rgb(108, 117, 125); }

.article-content p iframe { width: 100%; }

.article-content p { font-size: 20px; line-height: 32px; font-weight: 400; letter-spacing: -0.5px; color: rgb(51, 51, 51); margin-bottom: 32px; }

.article-content p strong { font-weight: 700; }

.article-content table { table-layout: fixed; width: 100%; }

.article-content table tr td { overflow: hidden; }

.article-content #comments .fb-comments iframe { width: 100% !important; }

.article-content a { font-weight: 600; }

.article-content blockquote { border-left: 4px solid rgb(221, 221, 221); padding: 0px 0px 16px 32px; }

.article-content blockquote::before { content: "format_quote"; font-family: "Material Icons"; font-size: 48px; margin: 0px 0px 0px -7px; height: 48px; display: flex; align-items: center; }

.article-content blockquote p { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 24px; font-weight: 400; line-height: 36px; letter-spacing: -0.5px; color: rgb(51, 51, 51); margin: 0px; }

.article-content blockquote cite { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; letter-spacing: -0.3px; color: rgb(102, 102, 102); font-style: normal; }

.article-content blockquote cite::before { content: "- "; }

.article-content h3.content-title-quotes { font-weight: 800; font-size: 18px; line-height: 24px; letter-spacing: -0.5px; margin: 16px 0px 0px; }

.article-content table.content-table-quotes td { font-weight: 700; }

.article-content ul { padding: 0px 0px 0px 20px; margin: 0px 0px 32px; }

.article-content ul li { font-size: 20px; line-height: 32px; font-weight: 700; letter-spacing: -0.5px; margin: 16px 0px; }

.article-content ul li a { font-weight: 700; }

.article-content .schema-faq-question, .article-content h2 { font-size: 28px; line-height: 32px; font-weight: 700; letter-spacing: -0.5px; color: rgb(17, 17, 17); margin: 52px 0px 32px; }

.article-content strong { font-weight: 700; }

.disclaimer { background-color: rgb(245, 247, 248); margin: 0px auto 40px; font-size: 14px; line-height: 20px; letter-spacing: -0.3px; color: rgb(33, 33, 33); font-weight: 400; padding: 32px !important; }

.header-brand { display: block; margin-top: 32px; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; line-height: 1 !important; }

.header-brand .container { display: flex; justify-content: space-between; align-items: center; }

.header-brand h1 { font-size: 48px; letter-spacing: -0.03em; font-weight: 700; line-height: 1 !important; }

.header-brand h2 { font-size: 32px; letter-spacing: -1.4px; color: rgb(0, 0, 0); font-weight: 800; margin: 0px; line-height: 1 !important; }

.header-brand .brand-image { display: flex; align-items: center; height: auto; padding: 0px; }

.header-brand .brand-image div { margin: 0px 16px 0px 0px; font-size: 10px; font-weight: 400; letter-spacing: 0px; color: rgb(0, 0, 0); text-transform: uppercase; }

.header-brand .brand-image img { width: auto; height: 48px; }

.brand-menu { font-size: 16px; font-weight: 400; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; line-height: 1 !important; }

.brand-menu a { color: rgb(0, 0, 0); }

.brand-menu a:hover { text-decoration: underline; }

.brand-menu span:first-child { display: none; }

.hat-and-brand { display: flex; justify-content: space-between; align-items: center; margin-bottom: 21px; }

.hat-and-brand .post-hat { margin: 0px; }

.hat-and-brand .post-brand span { margin: 0px 16px 0px 0px; font-size: 11px; line-height: 16px; letter-spacing: 0px; font-weight: 400; text-transform: uppercase; color: rgb(108, 117, 125); }

.hat-and-brand .post-brand a img { max-width: 140px; width: auto; height: auto; }

.social-orbs { display: flex; }

.social-orbs a { display: flex; align-items: center; justify-content: center; color: rgb(255, 255, 255); width: 32px; height: 32px; border-radius: 50%; text-decoration: none; }

.social-orbs .orb-facebook { background: rgb(59, 89, 153); }

.social-orbs .orb-twitter { background: rgb(85, 172, 238); }

.social-orbs .orb-flipboard { background: rgb(225, 40, 47); }

.social-orbs .orb-google { background: rgb(66, 133, 244); }

.social-orbs .orb-whatsapp { background: rgb(37, 211, 102); }

.social-orbs .orb-rss { background: rgb(242, 101, 34); }

.social-orbs a + a { margin-left: 4px; }

.info-spotlight { position: absolute; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; padding: 0px 32px 32px; background: linear-gradient(to top, rgba(0, 0, 0, 0.7) 20%, rgba(0, 0, 0, 0) 60%); top: 0px; z-index: 1; }

.info-spotlight span, .info-spotlight span a { color: rgb(255, 255, 255); }

.cover-link { display: block; position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; background-color: transparent; z-index: 100; }

.image-scale-hover img { transition: all 0.4s ease-in-out 0s; }

.image-scale-hover:hover img { transform: translate(-50%, -50%) scale(1.2); }

.info-no-image .hl-title { font-size: 32px; line-height: 40px; letter-spacing: -1.5px; font-weight: 800; }

.list-share { display: flex; align-items: center; margin: 0px 0px 0px 16px; }

.list-share a { display: flex; align-items: center; justify-content: center; color: rgb(255, 255, 255); width: 32px; height: 32px; border-radius: 50%; text-decoration: none; margin: 0px 4px 0px 0px; }

.list-share a:last-child { margin: 0px; }

.list-share a.twitter { background: rgb(85, 172, 238); }

.list-share a.telegram { background: rgb(0, 136, 204); padding: 0px 2px 0px 0px; }

.list-share a.whatsapp { background: rgb(37, 211, 102); }

.posted-diff { font-size: 12px; line-height: 16px; margin-top: 8px; font-weight: 400; }

.author-thumbnail { position: relative; width: 100%; padding-top: 100%; }

.author-thumbnail .blue-border { background-color: rgb(0, 145, 255); width: 100%; height: 100%; position: absolute; top: 0px; border-radius: 50%; }

.author-thumbnail .white-border { background-color: rgb(255, 255, 255); width: calc(100% - 6px); height: calc(100% - 6px); position: absolute; top: 3px; left: 3px; border-radius: 50%; }

.author-thumbnail .img-author { background-color: rgb(255, 255, 255); width: calc(100% - 10px); height: calc(100% - 10px); position: absolute; top: 5px; left: 5px; border-radius: 50%; overflow: hidden; display: flex; justify-content: center; }

.author-thumbnail .img-author img { width: auto; height: 100%; }

.article-author .author-image-container { width: 44px; margin: 0px 8px 0px 0px; }

.article-author .author-info-container { display: flex; flex-direction: column; justify-content: center; }

.article-author .author-info-container span.author-name { font-size: 16px; line-height: 24px; font-weight: 400; }

.article-author .author-info-container span.author-name a { font-weight: 700; }

.article-author .author-info-container span.author-name img { max-height: 26px; width: auto; }

.article-author .author-info-container span.article-date { font-size: 12px; line-height: 16px; font-weight: 400; color: var(--gray); }

.article-author .author.vcard a { font-weight: 700; }

.article-date .posted-on { display: block; font-size: 12px; line-height: 16px; color: var(--gray); }

.item .article-author .author-info-container .author-name { font-size: 14px; }

.item .article-author .author-image-container { margin: 0px 8px 0px 0px; }

.ct-series-a .ct-line { stroke: rgb(0, 145, 255) !important; stroke-width: 2px !important; }

.ct-series-a .ct-area { fill: rgb(0, 145, 255) !important; }

.ct-bar.ct-threshold-above, .ct-line.ct-threshold-above, .ct-point.ct-threshold-above { stroke: rgb(30, 185, 128) !important; }

.ct-bar.ct-threshold-below, .ct-line.ct-threshold-below, .ct-point.ct-threshold-below { stroke: rgb(255, 82, 82) !important; }

.ct-area.ct-threshold-above { fill: rgb(89, 146, 43) !important; }

.ct-area.ct-threshold-below { fill: rgb(255, 82, 82) !important; }

.ct-label { font-size: 9px !important; color: rgb(102, 102, 102) !important; }

div.ui-datepicker { width: auto; }

.pace { pointer-events: none; user-select: none; }

.pace .pace-progress { background: rgb(0, 145, 255); position: fixed; z-index: 2000; top: 0px; right: 100%; width: 100%; height: 2px; }

.pace-inactive { display: none; }

.widget-header { margin: 0px 0px 32px; display: flex; flex-wrap: wrap; }

.widget-header span.divisor { height: 1px; width: 100%; background-color: rgb(221, 221, 221); }

.widget-header h2 { font-size: 24px; line-height: 24px; letter-spacing: -0.4px; font-weight: 700; color: rgb(68, 68, 68); margin: 20px 0px 0px; }

.widget-header a { display: flex; }

.widget-header a i { line-height: 24px; color: var(--blue); cursor: pointer; margin: 20px 0px 0px 8px; font-size: 18px; }

.widget-header a:hover h2 { color: var(--blue); }

div.container-normal-blocks { padding-left: 0px; }

.category .container-normal-blocks { padding-left: 16px; }

.category .container-normal-blocks .widget-ticker-highlow { padding: 0px; }

.border-t { border-top: 1px solid rgb(221, 221, 221); }

.border-b { border-bottom: 1px solid rgb(221, 221, 221); }

.border-c { border-bottom: 1px solid rgb(168, 168, 168); }

.fill-lightgray { background: var(--lightgray); }

.fill-lightwhite { background: var(--white); }

.border-t-mobile { border-top: 0px; }

table td.positive { color: rgb(30, 185, 128); }

table td.negative { color: rgb(255, 82, 82); }

table p { font-size: 20px; line-height: 32px; letter-spacing: -0.6px; margin-bottom: 32px; color: rgb(51, 51, 51); font-weight: 400; }

table p:nth-last-child(2) { margin-bottom: 0px; }

div.first-line { padding: 0px; margin: 0px 16px; flex-basis: calc(100% - 32px); }

div.first-line span.value { font-weight: 700; font-size: 32px; line-height: 40px; letter-spacing: -0.48px; }

div.first-line span.initials { font-weight: 400; color: rgb(108, 117, 125); font-size: 16px; line-height: 20px; margin: 0px 0px 0px 8px; }

div.first-line span.percentage { font-size: 20px; line-height: 20px; font-weight: 700; color: rgb(30, 185, 128); margin: 0px 0px 0px 8px; }

div.first-line span.percentage.negative { color: rgb(250, 58, 58); }

div.first-line span.updated-at { font-weight: 400; font-size: 12px; line-height: 16px; color: rgb(108, 117, 125); margin: 0px 0px 0px 8px; }

div.first-line em { font-style: initial; }

button.btn-load-more { font-size: 14px; line-height: 16px; letter-spacing: -0.3px; padding: 12px 24px; display: table; border: 1px solid rgb(0, 145, 255); margin: 48px auto; font-weight: 700; background: 0px 0px; color: rgb(0, 145, 255); cursor: pointer; }

img.img-load-more { width: 30px; height: 30px; margin: 20px auto; display: none; }

.img-container { width: 100%; align-self: flex-start; }

.img-container figure { position: relative; overflow: hidden; padding-top: 56.25%; margin: 0px; }

.img-container figure img { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); min-height: 100%; }

.img-container-patrocinados figure { padding: 40px; }

.img-container-patrocinados figure img { max-width: 100%; height: auto; width: auto; max-height: 65px; margin: 0px auto; display: block; }

.img-container-patrocinados:hover + div .hl-title a, .img-container:hover + div .hl-title a { color: var(--sapphire); }

ol.summary { background-color: rgb(245, 247, 248); padding: 32px 32px 32px 48px; }

ol.summary::before { content: "Nesta página"; margin: 0px 0px 16px -16px; display: block; font-size: 20px; font-weight: 700; line-height: 1.2; letter-spacing: -0.8px; }

.container-article-table, .container-default-table { overflow-x: auto; width: 100%; }

.container-article-table table, .container-default-table table { margin: 0px 5px 10px 0px; display: inline-table; width: initial !important; }

.container-default-table::-webkit-scrollbar { display: none; }

.article-content table, table.default-table { min-width: calc(100% - 32px) !important; }

.article-content table thead, table.default-table thead { border-bottom: 1px solid var(--gray); }

.article-content table thead th, table.default-table thead th { font-weight: 400; font-size: 10px; line-height: 22px; padding: 8px 5px; color: var(--gray); text-transform: uppercase; text-align: right; }

.article-content table thead th:first-child, table.default-table thead th:first-child { text-align: left; }

.article-content table thead th.sorting, table.default-table thead th.sorting { background-image: none; }

.article-content table thead .sorting_asc, .article-content table thead .sorting_desc, table.default-table thead .sorting_asc, table.default-table thead .sorting_desc { background-position: right bottom; }

.article-content table tbody tr, table.default-table tbody tr { background-color: transparent; }

.article-content table tbody tr:hover, table.default-table tbody tr:hover { background-color: rgb(245, 247, 248); }

.article-content table tbody td, table.default-table tbody td { font-weight: 400; font-size: 13px; line-height: 22px; color: var(--darkgray); padding: 8px 5px; text-align: right; border-bottom: 1px solid rgba(108, 117, 125, 0.24); }

.article-content table tbody td a, table.default-table tbody td a { font-size: 13px; line-height: 24px; letter-spacing: -0.3px; font-weight: 700; color: rgb(0, 145, 255); margin: 0px; }

.article-content table tbody td:first-child, table.default-table tbody td:first-child { text-align: left; }

.article-content table tbody td.strong, table.default-table tbody td.strong { font-weight: 600; }

.article-content table tbody td.dual, table.default-table tbody td.dual { display: flex; flex-direction: column; }

.article-content table tbody td.dual span:nth-child(2), table.default-table tbody td.dual span:nth-child(2) { font-size: 12px; line-height: 16px; color: rgb(108, 117, 125); }

.article-content table tbody td.positive, table.default-table tbody td.positive { color: rgb(30, 185, 128); }

.article-content table tbody td.negative, table.default-table tbody td.negative { color: rgb(255, 82, 82); }

.article-content table tbody td.negative, .article-content table tbody td.positive, table.default-table tbody td.negative, table.default-table tbody td.positive { font-weight: 600; }

.table-subtitle { font-size: 12px; }

.posted-diff { font-size: 12px; line-height: 16px; margin-top: 8px; font-weight: 400; }

.down-app { display: flex; flex-wrap: wrap; }

.down-app h6 { flex-basis: 100%; }

.down-app a img { height: 40px; width: auto; }

.down-app a + a { margin-left: 20px; }

button.export_data_table { display: flex; border: none; background: 0px 0px; float: right; cursor: pointer; }

button.export_data_table i { margin: 0px 7px 0px 0px; }

button.export_data_table i, button.export_data_table span { font-size: 13px; line-height: 16px; letter-spacing: -0.3px; font-weight: 600; color: rgb(0, 145, 255); }

button.default-btn-ok { background-color: rgb(0, 145, 255); color: rgb(255, 255, 255); padding: 14px; font-size: 14px; line-height: 16px; font-weight: 700; border: none; cursor: pointer; }

button.default-btn-cancel { background: 0px 0px; border: none; font-weight: 600; cursor: pointer; }

@supports (-ms-ime-align:auto) {
  .material-icons { font-feature-settings: "liga"; }
}

@media screen and (max-width: 991px) {
  body.is-padded-mobile { padding-top: 48px; }
  .page-title-1 { font-size: 28px; line-height: 32px; letter-spacing: -1.2px; }
  .page-header { margin: 0px 16px 24px; padding: 0px 0px 24px; }
  .page-header .page-title-2 { font-size: 24px; line-height: 24px; letter-spacing: -0.7px; }
  .hl-title-2 { font-size: 20px; line-height: 24px; letter-spacing: -0.6px; }
  .section-title { font-size: 20px; letter-spacing: -0.33px; }
  .article-lead { font-size: 18px; line-height: 24px; letter-spacing: -0.3px; margin: 0px 0px 16px; }
  .article-terms span { font-size: 24px; font-weight: 900; margin: 24px 0px 0px; }
  .article-terms ul { margin: 14px 0px 0px; }
  .article-terms a { font-size: 16px; }
  .sticky-tags span { font-size: 24px; line-height: 24px; font-weight: 400; letter-spacing: -1px; color: rgb(33, 33, 33); }
  .sticky-tags span i { display: none; }
  .sticky-tags ul { margin-top: 16px; }
  .sticky-tags ul li a { font-weight: 700; font-size: 18px; line-height: 28px; letter-spacing: -0.3px; margin: 0px; text-decoration: underline; }
  .article-content figure figcaption { line-height: 16px; }
  .article-content p { font-size: 18px; line-height: 28px; }
  .article-content .container-article-table, .article-content .container-default-table { margin: 0px -16px; width: calc(100% + 32px); }
  .article-content .container-article-table table, .article-content .container-default-table table { margin: 0px 16px 10px; }
  .article-content table tr td { font-size: 12px; }
  .article-content blockquote { padding: 0px 0px 16px 16px; }
  .article-content blockquote p { font-size: 20px; line-height: 28px; }
  .disclaimer { padding: 24px 16px !important; }
  .header-brand { margin-top: 16px; display: list-item; }
  .header-brand .container { flex-direction: column; align-items: baseline; }
  .header-brand h1 { order: 1; font-size: 32px; letter-spacing: -0.01em; font-weight: 700; margin-bottom: 0px; }
  .header-brand h2 { font-size: 24px; line-height: 1; letter-spacing: -0.7px; }
  .header-brand .brand-image { order: 0; flex-direction: column; justify-content: flex-end; align-items: flex-start; display: flex; }
  .header-brand .brand-image div { margin: 0px 0px 8px; font-size: 10px; line-height: 1; }
  .header-brand .brand-image img { width: auto; height: 32px; }
  .hat-and-brand { flex-direction: column; }
  .hat-and-brand .post-hat { align-self: flex-start; margin: 25px 0px 0px; }
  .hat-and-brand .post-brand { order: -1; align-self: flex-end; }
  .info-spotlight { position: relative; background: 0px 0px; padding: 0px 16px 16px; }
  .info-spotlight .hl-hat { color: rgb(108, 117, 125); }
  .info-spotlight .hl-title a { color: rgb(0, 0, 0); }
  .hl-title-5 { font-size: 20px; line-height: 24px; }
  .border-t-mobile { border-top: 1px solid rgba(0, 0, 0, 0.12); }
  .border-b-mobile-none { border: none; }
  .widget-header h2 { font-size: 20px; letter-spacing: -0.33px; }
  div.container-normal-blocks { padding-left: 0px; padding-right: 0px; }
  .category .container-normal-blocks .items { padding-right: 16px; }
}

.comdinheiro { margin: 34px 0px 24px; display: flex; align-items: center; }

.comdinheiro p { font-size: 12px; margin: 0px 7px 0px 0px; }

.comdinheiro a img { height: 36px; }

h1, h2 { scroll-margin-top: 70px; }

#cta-automatico a, #cta-automatico p { font-style: italic; font-weight: 700 !important; }

.footer { background: rgb(18, 18, 18); padding: 80px 0px; }

.footer-top { color: rgb(255, 255, 255); }

.footer-map { color: rgb(255, 255, 255); }

.footer-map ul { display: flex; justify-content: space-between; }

.footer-map ul li a { color: rgb(108, 117, 125); }

.footer-map ul li ul { display: list-item; }

.footer-map ul li ul li a { color: rgb(245, 247, 248); font-weight: 400; }

.footer-map li a { color: rgb(245, 247, 248); font-weight: 700; font-size: 12px; line-height: 24px; }

.footer-map li a:hover { color: rgb(255, 255, 255); }

.footer-top .title-call { width: 200px; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; font-style: normal; font-stretch: normal; line-height: 1.25; letter-spacing: -0.6px; color: rgb(108, 117, 125); }

.footer-menu-extra { font-size: 12px; line-height: 16px; color: rgb(108, 117, 125); padding-bottom: 40px; }

.footer-menu-extra .logo-footer { width: 140px; margin: 0px 0px 24px; display: block; }

.footer-menu-extra ul { margin: 0px; padding: 0px; }

.footer-menu-extra ul li.menu-item { padding: 5px; list-style: none; display: inline-block; }

.footer-menu-extra ul li.menu-item a { color: rgb(245, 247, 248); font-size: 12px; line-height: 16px; font-weight: 600; }

.footer-menu-extra ul li.menu-item a:hover { color: rgb(255, 255, 255); cursor: pointer; }

.footer-menu-extra ul li:first-child { padding: 5px 5px 5px 0px; }

.footer-menu-extra #menu-rodape-institucional { display: inline-flex; }

.footer-social { display: flex; align-items: center; }

.footer-social a { display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; color: rgba(255, 255, 255, 0.9); background: rgba(255, 255, 255, 0.12); font-size: 18px; }

.footer-social a:hover { color: rgb(255, 255, 255); background: rgba(255, 255, 255, 0.2); }

.footer-social a + a { margin-left: 12px; }

.footer-disclaimer { font-size: 10px; line-height: 18px; font-weight: 600; color: rgb(108, 117, 125); margin: 40px 0px 0px; padding: 48px 0px 0px; border-top: 1px solid rgba(255, 255, 255, 0.12); }

.footer-disclaimer b { color: rgba(255, 255, 255, 0.6); font-weight: 600; }

.footer-disclaimer div { padding: 0px; }

.newsletter-footer { background-color: rgb(245, 247, 248); padding: 48px 0px; margin: 48px 0px 0px; display: none; }

.newsletter-footer .newsletter-form { width: 688px; margin: 0px auto; text-align: center; }

.newsletter-footer .newsletter-form .title { font-size: 24px; line-height: 28px; font-weight: 900; letter-spacing: -1px; color: var(--black); }

.newsletter-footer .newsletter-form p { letter-spacing: -0.3px; margin: 8px 0px 0px; }

.newsletter-footer .newsletter-form form { margin: 16px 0px 0px; display: flex; }

.newsletter-footer .newsletter-form form input#email-footer { flex-grow: 1; margin: 0px 16px 0px 41px; padding: 0px 16px; line-height: 16px; letter-spacing: -0.3px; }

.newsletter-footer .newsletter-form form input#submit-btn { margin: 0px 41px 0px 0px; background-color: rgb(0, 145, 255); border: none; padding: 18px 32px; font-size: 16px; line-height: 1; font-weight: 700; letter-spacing: -0.3px; border-radius: 0px; }

.newsletter-footer .newsletter-form #status-footer { padding: 10px 0px 0px; display: block; }

.down-app { display: flex; flex-wrap: wrap; }

.down-app h6 { flex-basis: 100%; }

.down-app a img { height: 40px; width: auto; }

.down-app a + a { margin-left: 20px; }

@media screen and (max-width: 991px) {
  .newsletter-footer .newsletter-form { width: 100%; padding: 0px 16px; }
  .newsletter-footer .newsletter-form p { font-size: 14px; line-height: 20px; }
  .newsletter-footer .newsletter-form form input#email-footer { margin: 0px 4px 0px 0px; width: calc(100% - 130px); }
  .newsletter-footer .newsletter-form form input#submit-btn { padding: 18px 24px; margin: 0px; }
  .footer-map ul { flex-direction: column; margin: 0px 0px 36px; }
  .footer-map ul li { margin: 36px 0px 0px; }
  .footer-map ul li ul { margin: 0px; }
  .footer-map ul li ul li { margin: 0px; }
  .footer-social { margin: 0px 0px 36px; }
}

.header { position: fixed; top: 0px; left: 0px; width: 100%; height: 48px; z-index: 1000; transition: all 0.2s ease-in-out 0s; background: rgb(33, 33, 33); }

.header .logo-link { margin: 13px 0px 7px 16px; }

.header .logo-link .logo { max-height: 28px; }

.header .menu-open { color: rgba(255, 255, 255, 0.6); }

.header .menu-open:hover { color: rgb(255, 255, 255); }

.header .nav-topics i { color: rgb(0, 145, 255); }

.header .nav-topics a { color: rgba(255, 255, 255, 0.9); }

.header .nav-topics a:hover { color: rgb(255, 255, 255); }

.header .nav-topics span { color: rgb(255, 255, 255); }

.header .header-action { color: rgba(255, 255, 255, 0.6); }

.header .header-action:hover { color: rgb(255, 255, 255); }

.header-full { display: none; }

.header-full .logo-link { padding: 15px 0px 5px; }

.header-full .logo-link .logo { max-height: 48px; }

.header-full .nav-topics i { color: var(--blue); }

.header-full .nav-topics a { color: rgb(17, 17, 17); }

.header-full .nav-topics a:hover { color: var(--blue); }

.header-full .header-action { color: var(--gray); }

.header-full .header-action:hover { color: var(--darkgray); }

.header-full .color-lightblue { color: var(--darkgray) !important; }

.header-action { display: flex; align-items: center; justify-content: center; width: 24px; height: 24px; transition: all 0.2s ease-in-out 0s; cursor: pointer; }

.header-action:hover { text-decoration: none; }

.container-nav-topics { background-color: rgb(249, 249, 249); }

.nav-topics { height: 40px; }

.nav-topics i { font-size: 18px; }

.nav-topics a { font-size: 14px; line-height: 16px; font-weight: 400; letter-spacing: -0.2px; }

.nav-topics a:hover { text-decoration: none; }

.nav-topics span { margin: 0px 10px; }

.color-lightblue { color: var(--lightblue) !important; }

.container-header-small { position: sticky; top: 0px; z-index: 9999; }

.container-header-small div.header-full { display: none; }

.container-header-small div.header { transform: none; position: relative; }

.container-search-header { display: none; position: fixed; top: 0px; left: 0px; width: 100%; height: 1000%; background-color: rgb(255, 255, 255); z-index: 2000; animation: 0.5s ease 0s 1 normal none running fadein; }

.container-search-header .header-search { height: 48px; border-bottom: 1px solid rgb(221, 221, 221); display: flex; justify-content: space-between; }

.container-search-header .header-search img { height: 28px; margin: 13px 0px 7px 16px; cursor: pointer; }

.container-search-header .header-search button { background: 0px 0px; border: none; height: 24px; width: 24px; padding: 0px; margin: 12px 16px 12px 0px; cursor: pointer; }

.container-search-header .header-search button i { color: rgb(102, 102, 102); }

.container-search-header .header-search button:hover i { color: rgb(33, 33, 33); }

.container-search-header .container { height: 100vh; margin: -48px auto 0px; display: flex; align-items: center; }

.container-search-header .container .row { flex-basis: calc(100% + 32px); }

.container-search-header .container .row form#header-search { display: flex; }

.container-search-header .container .row form#header-search input[type="text"] { width: 100%; background: 0px 0px; border-width: 0px 0px 1px; border-color: rgb(221, 221, 221); font-size: 24px; font-weight: 700; line-height: 36px; height: 72px; padding: 18px 0px; }

.container-search-header .container .row form#header-search input[type="text"]:focus { outline: 0px; border-color: rgb(0, 145, 255); }

.container-search-header .container .row form#header-search input[type="text"]::placeholder { color: rgb(204, 204, 204); }

.container-search-header .container .row form#header-search button { background: 0px 0px; height: 72px; border-width: 0px 0px 1px; border-color: rgb(221, 221, 221); border-style: solid; cursor: pointer; }

.container-search-header .container .row form#header-search button i { font-size: 26px; color: rgb(204, 204, 204); }

.container-search-header .container .row form#header-search input[type="text"]:focus ~ button { border-color: rgb(0, 145, 255); }

.container-search-header .container .row form#header-search input[type="text"]:focus ~ button i { color: rgb(0, 145, 255); }

.container-search-header .container .row .topics-search { padding-top: 20px; }

.container-search-header .container .row .topics-search div { padding: 10px 16px; display: flex; }

.container-search-header .container .row .topics-search div i { color: rgb(0, 145, 255); font-size: 18px; }

.container-search-header .container .row .topics-search div a { font-size: 16px; font-weight: 600; line-height: 20px; letter-spacing: -0.3px; color: rgb(17, 17, 17); margin: 0px 0px 0px 16px; }

.container-search-header .container .row .topics-search div a:hover { color: rgb(0, 145, 255); }

@media (min-width: 992px) {
  .header { transform: translateY(-100%); }
  .header.is-visible { transform: translateY(0px); }
  .header-full { display: block; }
}

@media screen and (max-width: 991px) {
  .container-search-header .container { margin: 0px; align-items: start; }
  .container-search-header .container .row form#header-search { margin: 16px 0px 0px; }
  .container-search-header .container .row form#header-search input[type="text"] { font-size: 18px; }
  .container-search-header .container .row .topics-search div { padding: 10px 0px; }
}

@keyframes fadein { 
  0% { opacity: 0; }
  100% { opacity: 1; }
}

#menu-side { position: fixed; top: 0px; left: -320px; width: 320px; height: 100%; z-index: 2147483647; background-color: rgb(0, 0, 0); overflow-y: scroll; transition: left 0.25s ease-in-out 0s; }

#menu-side .menu-header { height: 48px; }

#menu-side .menu-header #menu-close { cursor: pointer; }

#menu-side .menu-header #menu-close i { width: 24px; height: 24px; float: right; color: rgba(255, 255, 255, 0.6); font-size: 24px; margin: 12px 16px 0px 0px; transition: all 0.2s ease-in-out 0s; }

#menu-side .menu-header #menu-close:hover i { color: rgb(255, 255, 255); }

#menu-side .topics-menu { padding: 8px 0px; border-bottom: 1px solid rgba(255, 255, 255, 0.12); }

#menu-side .topics-menu a { padding: 8px 16px; display: flex; }

#menu-side .topics-menu a i { color: rgb(0, 145, 255); font-size: 24px; }

#menu-side .topics-menu a p { font-size: 13px; font-weight: 600; line-height: 20px; color: rgba(255, 255, 255, 0.7); margin: 2px 0px 2px 16px; }

#menu-side .topics-menu a:hover { background-color: rgba(255, 255, 255, 0.02); }

#menu-side .topics-menu a:hover p { color: rgb(255, 255, 255); }

#menu-side ul { cursor: pointer; margin: 0px; }

#menu-side ul li { padding: 0px; }

#menu-side ul li a { font-size: 13px; line-height: 20px; font-weight: 600; color: rgba(255, 255, 255, 0.7); }

#menu-side ul li ul { background-color: rgba(255, 255, 255, 0.1); overflow: hidden; max-height: 0px; transition: max-height 0.5s ease 0s; }

#menu-side ul li ul li a { padding: 10px 32px; display: block; }

#menu-side ul li:hover { background-color: rgba(255, 255, 255, 0.02); }

#menu-side ul li:hover a { color: rgb(255, 255, 255); }

#menu-side > ul > li.menu-item-has-children::before { content: "keyboard_arrow_down"; font-family: "Material Icons"; color: rgba(255, 255, 255, 0.7); position: absolute; right: 16px; z-index: -1; font-size: 24px; line-height: 40px; }

#menu-side > ul > li.menu-item-has-children:hover { background-color: rgba(255, 255, 255, 0.02); }

#menu-side > ul > li.menu-item-has-children:hover a, #menu-side > ul > li.menu-item-has-children:hover::before { color: rgb(255, 255, 255); }

#menu-side > ul > li.menu-item-has-children:hover ul li a { color: rgba(255, 255, 255, 0.7); }

#menu-side > ul > li.menu-item-has-children:hover ul li a:hover { color: rgb(255, 255, 255); }

#menu-side > ul > li.menu-item-has-children.opened::before { content: "keyboard_arrow_up"; }

#menu-side > ul > li.menu-item-has-children.opened ul { transition: max-height 0.5s ease 0s; padding: 8px 0px; }

#menu-side > ul > li > a { padding: 10px 16px; display: block; }

#menu-side::-webkit-scrollbar { width: 0px !important; }

#menu-side.opened { transition: left 0.25s ease-in-out 0s; left: 0px; }

@media screen and (max-width: 320px) {
  #menu-side { width: 100%; }
}

.container, .container-fluid { padding-right: 16px; padding-left: 16px; }

.container { max-width: 1280px; }

.row { margin-right: -16px; margin-left: -16px; }

.container.row { margin-right: auto; margin-left: auto; padding-right: 0px; padding-left: 0px; }

figure { margin: 0px; }

.img-fluid { width: 100%; }

.col, .col-1, .col-10, .col-11, .col-12, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-auto, .col-lg, .col-lg-1, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-auto, .col-md, .col-md-1, .col-md-10, .col-md-11, .col-md-12, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-auto, .col-sm, .col-sm-1, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-auto, .col-xl, .col-xl-1, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-auto { padding-right: 16px; padding-left: 16px; }

.mt-2, .my-2 { margin-top: 12px !important; }

.mb-2, .my-2 { margin-bottom: 12px !important; }

.mt-5, .my-5 { margin-top: 40px !important; }

.mb-5, .my-5 { margin-bottom: 40px !important; }

.pt-5, .py-5 { padding-top: 5rem !important; }

.pb-5, .py-5 { padding-bottom: 5rem !important; }

.mt-1, .my-1 { margin-top: 4px !important; }

.mb-1, .my-1 { margin-bottom: 4px !important; }

@media (min-width: 992px) {
  .m-lg-0 { margin: 0px !important; }
  .mt-lg-0, .my-lg-0 { margin-top: 0px !important; }
  .pt-lg-2, .py-lg-2 { padding-top: 12px !important; }
  .pb-lg-2, .py-lg-2 { padding-bottom: 12px !important; }
  .mb-lg-4, .my-lg-4 { margin-bottom: 1.5rem !important; }
  .mt-lg-5, .my-lg-5 { margin-top: 40px !important; }
  .mb-lg-5, .my-lg-5 { margin-bottom: 40px !important; }
}

.userPanel { position: relative; }

.userPanel .login-header { display: none; padding: 15px 16px 17px; cursor: pointer; }

.userPanel .login-header i, .userPanel .login-header p { color: rgba(255, 255, 255, 0.9); }

.userPanel .login-header p { margin: 0px 24px 0px 16px; font-size: 16px; line-height: 24px; letter-spacing: -0.3px; }

.userPanel .login-header a { display: flex; }

.userPanel .login-header::before { content: "keyboard_arrow_down"; font-family: "Material Icons"; color: rgba(255, 255, 255, 0.7); position: absolute; right: 16px; font-size: 24px; line-height: 24px; }

.userPanel .login-header.not-logged::before { content: ""; display: none; }

.userPanel .login-options { display: none; color: rgb(255, 255, 255); }

.userPanel.active .login-header::before { content: "keyboard_arrow_up"; }

.userPanel.active .login-options { display: block; }

.header, .header-full { z-index: 1030; }

.header .userPanel, .header-full .userPanel { margin: 0px 24px 0px 0px; }

.header .userPanel .login-header, .header-full .userPanel .login-header { padding: 8px; }

.header .userPanel .login-header p, .header-full .userPanel .login-header p { font-size: 13px; letter-spacing: -0.2px; margin: 0px 24px 0px 4px; }

.header .userPanel .login-header::before, .header-full .userPanel .login-header::before { content: "arrow_drop_down"; right: 8px; }

.header .userPanel .login-header.not-logged p, .header-full .userPanel .login-header.not-logged p { margin: 0px 4px; }

.header .userPanel .login-options, .header-full .userPanel .login-options { position: absolute; background-color: rgb(255, 255, 255); box-shadow: rgba(0, 0, 0, 0.5) 0px 2px 4px 0px; padding: 8px 0px; z-index: 9; min-width: 150px; }

.header .userPanel .login-options li, .header-full .userPanel .login-options li { padding: 12px 16px; list-style: none; }

.header .userPanel .login-options li a, .header-full .userPanel .login-options li a { font-size: 14px; line-height: 16px; letter-spacing: -0.2px; color: rgb(33, 33, 33); font-weight: 600; }

.header .userPanel .login-options li:hover, .header-full .userPanel .login-options li:hover { background-color: rgb(240, 240, 240); }

.header .userPanel.active .login-header::before, .header-full .userPanel.active .login-header::before { content: "arrow_drop_up"; }

.header:not(.is-visible) .userPanel { display: none; }

.container-header-small .header:not(.is-visible) .userPanel { display: block; }

.header-full .userPanel { position: absolute; right: 40px; }

.header-full .userPanel .login-header i, .header-full .userPanel .login-header p { color: rgb(102, 102, 102); }

.header-full .userPanel .login-header::before { color: rgb(33, 33, 33); }

.header-full .userPanel .login-header:hover { background-color: rgb(240, 240, 240); }

.header-full .userPanel .login-header:hover i, .header-full .userPanel .login-header:hover p { color: rgb(33, 33, 33); }

.header .userPanel .login-header:hover { background-color: rgba(255, 255, 255, 0.1); }

#menu-side .userPanel .login-header { background-color: rgba(255, 255, 255, 0.15); }

#menu-side .userPanel .login-options { background-color: rgba(255, 255, 255, 0.1); padding: 0px; }

#menu-side .userPanel .login-options li { list-style: none; padding: 10px 16px; }

@media screen and (max-width: 991px) {
  .header .userPanel, .header-full .userPanel { display: none; }
  .container-header-small .header:not(.is-visible) .userPanel { display: none; }
}

.item-list { align-items: center; padding: 20px 0px; margin: 0px; }

.item-list div.img { flex-basis: 25%; overflow: hidden; margin-right: 16px; margin-left: 0px; }

.item-list div.img figure { position: relative; width: 100%; height: 100%; padding-top: 56.25%; margin: 0px; background-color: rgb(0, 0, 0); }

.item-list div.img figure img { position: absolute; top: 0px; left: 0px; bottom: 0px; right: 0px; display: block; height: auto; max-height: 100%; width: auto; max-width: 100%; margin: auto; }

.item-list div.info { flex-basis: calc(75% - 48px); margin-left: 16px; }

@media screen and (max-width: 991px) {
  .item-list { padding: 16px 0px; border-bottom: 1px solid rgba(0, 0, 0, 0.12); margin: 0px; }
  .item-list div.img { margin-right: 16px; margin-left: 0px; }
  .item-list div.info { flex-basis: calc(75% - 16px); margin-left: 0px; }
  .item-list div.info .hl-title { font-size: 18px; line-height: 22px; letter-spacing: -0.8px; }
  div.item-list:nth-last-child(2) { border-bottom: none; }
}

#infiniteScroll div.row.item:first-child { padding-top: 0px !important; }

#infiniteScroll #infinite-handle { display: flex; }

#infiniteScroll #infinite-handle span, #infiniteScroll #infinite-handle span:hover { background-color: var(--blue); width: 100%; text-align: center; color: rgb(255, 255, 255); font-size: 14px; line-height: 1; font-weight: 600; border-radius: 2px; padding: 16px; margin: 24px auto 0px; }

#infiniteScroll #infinite-handle span button, #infiniteScroll #infinite-handle span:hover button { font-size: 14px; }

#infiniteScroll #infinite-handle span:hover { box-shadow: rgba(0, 0, 0, 0.3) 0px 1px 2px; }

#infiniteScroll .infinite-loader { margin: 32px auto; height: 46px; display: flex; }

#infiniteScroll .infinite-loader .spinner { margin: 22px auto; top: initial !important; left: initial !important; }

@media screen and (max-width: 991px) {
  #infiniteScroll #infinite-handle span, #infiniteScroll #infinite-handle span:hover { margin: 22px auto; }
}

.im-data-tables-nav { padding: 12px 0px 0px; display: flex; justify-content: space-between; position: relative; }

.im-data-tables-nav ul { margin-left: 0px; margin-top: 0px; padding-left: 0px; }

.im-data-tables-nav ul li { display: inline-block; vertical-align: top; margin-right: 8px; }

.im-data-tables-nav ul li:last-of-type { margin-right: 0px; }

.im-data-tables-nav ul li button { background: rgb(255, 255, 255); height: 32px; display: block; color: rgb(0, 0, 0); font-size: 14px; text-align: center; border: 1px solid rgb(224, 224, 224); border-radius: 16px; cursor: pointer; padding: 0px 16px; }

.im-data-tables-nav ul li button.active, .im-data-tables-nav ul li button:hover { background: rgba(0, 102, 255, 0.08); color: rgb(0, 102, 255); border: 1px solid rgba(0, 102, 255, 0.48); }

.im-data-tables-nav .table-buttons { padding-right: 8px; }

.im-data-tables-nav .table-buttons button { background: 0px 0px; border: none; display: inline-block; vertical-align: top; padding: 0px; cursor: pointer; margin-right: 20px; }

.im-data-tables-nav .table-buttons button:last-of-type { margin-right: 0px; }

.im-data-tables-nav .table-buttons button span { color: rgb(82, 82, 82); font-size: 21px; }

.im-data-tables-nav .data-tables-search-bar { background-color: rgb(244, 244, 244); width: 100%; height: 48px; position: absolute; top: 0px; left: 0px; display: none; }

.im-data-tables-nav .data-tables-search-bar input { background-color: rgb(244, 244, 244); width: 100%; height: 100%; font-size: 16px; color: rgb(0, 0, 0); padding: 0px 0px 0px 48px; border: none; }

.im-data-tables-nav .data-tables-search-bar input::-webkit-input-placeholder { color: rgb(141, 141, 141); }

.im-data-tables-nav .data-tables-search-bar .material-search-icon { position: absolute; top: 14px; left: 16px; font-size: 21px; color: rgb(0, 0, 0); }

.im-data-tables-nav .data-tables-search-bar .btn-close-data-tables-search-bar { position: absolute; top: 12px; right: 16px; font-size: 21px; color: rgb(0, 0, 0); }

.im-data-tables-pagination { display: flex; justify-content: flex-end; border-bottom: 1px solid rgb(224, 224, 224); }

.im-data-tables-pagination .pagination-result { font-size: 14px; padding-top: 13px; padding-right: 24px; }

.im-data-tables-pagination .pagination-buttons { margin-left: 0px; margin-top: 0px; padding-left: 0px; }

.im-data-tables-pagination .pagination-buttons button { background: 0px 0px; display: inline-block; vertical-align: top; cursor: pointer; width: 48px; height: 48px; border: none; padding: 0px; }

.im-data-tables-pagination .pagination-buttons button span { font-size: 21px; display: block; margin: 0px auto; }

.im-data-tables-pagination .pagination-buttons button.disabled { cursor: default; }

.im-data-tables-pagination .pagination-buttons button.disabled span { opacity: 0.3; }

.im-data-tables { width: 100%; max-width: 1024px; cursor: default; }

.im-data-tables thead tr { border-bottom: 1px solid rgb(224, 224, 224); }

.im-data-tables thead tr th { font-size: 12px; font-weight: 400; height: 48px; vertical-align: middle; text-align: right; letter-spacing: 0.03em; color: rgb(0, 0, 0); }

.im-data-tables thead tr th a { color: rgb(0, 0, 0); display: block; }

.im-data-tables thead tr th:first-of-type { text-align: left; }

.im-data-tables thead tr th .material-icons { font-size: 18px; display: inline-block; vertical-align: top; }

.im-data-tables tbody tr td, .im-data-tables tbody tr th { height: 64px; border-bottom: 1px solid rgb(224, 224, 224); vertical-align: middle; font-size: 14px; color: rgb(0, 0, 0); font-weight: 400; text-align: right; letter-spacing: 0.04em; padding-left: 16px; }

.im-data-tables tbody tr td.number, .im-data-tables tbody tr th.number { letter-spacing: 0.04em; }

.im-data-tables tbody tr td a, .im-data-tables tbody tr th a { color: rgb(0, 0, 0); padding: 0px; display: inline-block; }

.im-data-tables tbody tr td .ticker-name, .im-data-tables tbody tr th .ticker-name { display: block; line-height: 110%; }

.im-data-tables tbody tr td .ticker-name strong, .im-data-tables tbody tr th .ticker-name strong { font-weight: 700; display: block; }

.im-data-tables tbody tr td .xp-risk, .im-data-tables tbody tr th .xp-risk { display: inline-block; width: 32px; height: 32px; color: rgb(255, 255, 255); font-size: 14px; font-weight: 700; text-align: center; padding-top: 5px; letter-spacing: 0.03em; }

.im-data-tables tbody tr td .xp-risk.yellow, .im-data-tables tbody tr th .xp-risk.yellow { background-color: rgb(224, 173, 0); }

.im-data-tables tbody tr td .xp-risk.orange, .im-data-tables tbody tr th .xp-risk.orange { background-color: rgb(215, 123, 10); }

.im-data-tables tbody tr td .xp-risk.red, .im-data-tables tbody tr th .xp-risk.red { background-color: rgb(204, 51, 51); }

.im-data-tables tbody tr td .variation, .im-data-tables tbody tr th .variation { display: inline-block; width: 69px; height: 32px; color: rgb(255, 255, 255); font-size: 14px; text-align: center; padding-top: 6px; letter-spacing: 0.04em; }

.im-data-tables tbody tr td .variation.up, .im-data-tables tbody tr th .variation.up { background-color: rgb(243, 248, 244); color: rgb(19, 115, 51); }

.im-data-tables tbody tr td .variation.down, .im-data-tables tbody tr th .variation.down { background-color: rgb(250, 243, 243); color: rgb(165, 14, 14); }

.im-data-tables tbody tr th { text-align: left; padding-left: 0px !important; }

.im-data-tables.sm thead tr th { height: 32px; }

.im-data-tables.sm tbody tr td, .im-data-tables.sm tbody tr th { height: 48px; }

.im-data-tables.sm tbody tr th { padding-left: 8px; }

.im-data-tables.xs thead tr th { height: 24px; }

.im-data-tables.xs tbody tr td, .im-data-tables.xs tbody tr th { height: 40px; }

.im-data-tables.xs tbody tr th { padding-left: 4px; }
------MultipartBoundary--Anmt2sljSTW5R0WcMjvjsiYWT6XQCBHd4lqN4LO0OI----
Content-Type: application/font-woff
Content-Transfer-Encoding: binary
Content-Location: https://www.infomoney.com.br/wp-content/themes/infomoney/assets/fontawesome/fa-brands-400.woff

wOFF
  """


  lista_paises = list()
  lista_compra = list()
  lista_venda = list()
  Banco_Infomoney = dict()
  Tabela_Cambio = list()

  Soup = BeautifulSoup(html_text, 'html.parser')
  table = Soup.select_one('tbody')

  lista_paises = table.select('tr td:nth-of-type(1)')
  lista_compra = table.select('tr td:nth-of-type(3)')
  lista_venda = table.select('tr td:nth-of-type(4)')

  for c in range(0,len(lista_compra)):
    Banco_Infomoney['pais'] = Extrair_Tag.extrair_tag(lista_paises[c])
    Banco_Infomoney['compra'] = Extrair_Tag.extrair_tag(lista_compra[c])
    Banco_Infomoney['venda'] = Extrair_Tag.extrair_tag(lista_venda[c])

    Tabela_Cambio.append(Banco_Infomoney.copy())