import requests
from bs4 import BeautifulSoup
from Extrair_Tag import extrair_tag


class BAI_Europa():
  """html_text = requests.get('https://www.bancobaieuropa.pt/pt-pt/informacoes/cambios-taxas').text"""
  
  html_text = """
  From: <Saved by Blink>
Snapshot-Content-Location: https://www.bancobaieuropa.pt/pt-pt/informacoes/cambios-taxas
Subject: =?utf-8?Q?C=C3=A2mbios=20e=20Taxas=20|=20Banco=20BAI=20EUROPA?=
Date: Sat, 7 Jan 2023 13:35:42 -0000
MIME-Version: 1.0
Content-Type: multipart/related;
	type="text/html";
	boundary="----MultipartBoundary--N1Eay4lcYYX2rGjcUEmGmPPUBN3bWjvqvPv2iZl2Wh----"


------MultipartBoundary--N1Eay4lcYYX2rGjcUEmGmPPUBN3bWjvqvPv2iZl2Wh----
Content-Type: text/html
Content-ID: <frame-D3FA16A8B342B7A029BDAC0AD3F58730@mhtml.blink>
Content-Transfer-Encoding: binary
Content-Location: https://www.bancobaieuropa.pt/pt-pt/informacoes/cambios-taxas

<!-- THEME DEBUG --><!-- THEME HOOK: 'html' --><!-- FILE NAME SUGGESTIONS:
   * html--node--118.html.twig
   * html--node--%.html.twig
   * html--node.html.twig
   x html.html.twig
--><!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/layout/html.html.twig' --><!DOCTYPE html><html lang="pt-pt" dir="ltr" prefix="content: http://purl.org/rss/1.0/modules/content/  dc: http://purl.org/dc/terms/  foaf: http://xmlns.com/foaf/0.1/  og: http://ogp.me/ns#  rdfs: http://www.w3.org/2000/01/rdf-schema#  schema: http://schema.org/  sioc: http://rdfs.org/sioc/ns#  sioct: http://rdfs.org/sioc/types#  skos: http://www.w3.org/2004/02/skos/core#  xsd: http://www.w3.org/2001/XMLSchema# " class=" js cookies no-ie8compat serviceworker svg websockets canvas canvastext no-userdata video multiplebgs rgba placeholder inlinesvg no-ambientlight inputsearchevent csscalc cssgradients opacity supports svgasimg touchevents checked displaytable display-table fontface cssinvalid lastchild no-nthchild mediaqueries textshadow bgpositionxy backgroundsize bgsizecover borderimage borderradius boxshadow boxsizing flexbox flexboxlegacy no-flexboxtweener flexwrap csstransforms csstransforms3d preserve3d csstransitions objectfit object-fit no-csshyphens softhyphens no-softhyphensfind"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    


<meta name="Generator" content="Drupal 9 (https://www.drupal.org)">
<meta name="MobileOptimized" content="width">
<meta name="HandheldFriendly" content="true">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="https://www.bancobaieuropa.pt/favicon.ico" type="image/vnd.microsoft.icon">
<link rel="alternate" hreflang="pt-pt" href="https://www.bancobaieuropa.pt/pt-pt/informacoes/cambios-taxas">
<link rel="canonical" href="https://www.bancobaieuropa.pt/pt-pt/informacoes/cambios-taxas">
<link rel="shortlink" href="https://www.bancobaieuropa.pt/pt-pt/node/118">

    <title>Câmbios e Taxas | Banco BAI EUROPA</title>
    <link rel="stylesheet" media="all" href="https://www.bancobaieuropa.pt/sites/default/files/css/css_kcpJl2G6pY5K3VUDCOc-bNWZUn5aisTSW0wP2rqcOn8.css">
<link rel="stylesheet" media="all" href="https://www.bancobaieuropa.pt/sites/default/files/css/css_ofkCQpVkjjc6khOxEuEyLdWe4ZwZWluOU2CcMbEV4Ew.css">

    
  </head>
  <body>
        <!--
    <a href="#main-content" class="visually-hidden focusable">
          </a>
    -->
    
    

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'off_canvas_page_wrapper' -->
<!-- BEGIN OUTPUT from 'core/modules/system/templates/off-canvas-page-wrapper.html.twig' -->
  <div class="dialog-off-canvas-main-canvas" data-off-canvas-main-canvas="">
    

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'page' -->
<!-- FILE NAME SUGGESTIONS:
   * page--node--118.html.twig
   * page--node--%.html.twig
   * page--node.html.twig
   x page.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/page.html.twig' -->
<div class="baieu-site-container">
  <div class="devmsg">
  

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   * block--baieu-account-menu.html.twig
   * block--system-menu-block--account.html.twig
   x block--system-menu-block.html.twig
   * block--system.html.twig
   * block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->
<div class="navigation_blocks">
  

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'menu__account' -->
<!-- FILE NAME SUGGESTIONS:
   x menu--account.html.twig
   x menu--account.html.twig
   * menu.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/menu--account.html.twig' -->

<div class="login">
    
            <ul>
                  <li>
          <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/user/login" data-drupal-link-system-path="user/login">Entrar</a>
                  </li>
          </ul>
        

    
</div>

<!-- END OUTPUT from 'themes/custom/baieu/menu--account.html.twig' -->


</div>

<!-- END OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->


</div>


<div class="top-bar">
  <div class="top-bar-2">
    <ul>
      <li>
        <div class="ib-link ib-link-context-institucional">
          <a id="iba" data-toggle="modal" data-target="#exampleModalCenter">
            <ul>
              <li>
                <img id="lock-bai-europa-directo" src="https://www.bancobaieuropa.pt/themes/custom/baieu/images/ICONS/lock.png" alt="BAI EUROPA DIRECTO">
              </li>

              <li>
                BAI EUROPA DIRECTO
              </li>
            </ul>
          </a>
        </div>
      </li>
    </ul>
  </div>
</div>


<div class="main-header">
  <div class="main-header-2">
  <ul>
      <li>
                <div class="header-baieu-branding">
          

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   * block--baieu-branding.html.twig
   x block--system-branding-block.html.twig
   * block--system.html.twig
   * block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/block/block--system-branding-block.html.twig' -->
<div id="block-baieu-branding">
  
    
        <h1 class="logo logo-context-institucional">
      <a href="https://www.bancobaieuropa.pt/index.php/pt-pt" title="Início" rel="home">
        <img src="https://www.bancobaieuropa.pt/sites/default/files/logo.png" alt="Início">
      </a>
    </h1>
      
</div>

<!-- END OUTPUT from 'themes/custom/baieu/templates/block/block--system-branding-block.html.twig' -->


        </div>
      </li>




      <li>
          <div class="header-links">
            <ul>
              <li><a href="https://www.bancobaieuropa.pt/institucional/onde-estamos"><img src="https://www.bancobaieuropa.pt/themes/custom/baieu/images/ICONS/location.png" alt="Onde estamos"><!--<i class="material-icons">place</i>--><span></span></a></li>
              <li><img id="header_links_line_separator" src="https://www.bancobaieuropa.pt/themes/custom/baieu/images/ICONS/line-separador.png" alt="separator"></li>
              <li><a href="https://www.bancobaieuropa.pt/contact/contacte_nos"><img src="https://www.bancobaieuropa.pt/themes/custom/baieu/images/ICONS/comment.png" alt="Apoio a Cliente"><!--<i class="material-icons">call</i>--><span></span></a></li>
            </ul>
          </div>
      </li>



      <li>
        <div class="pesquisar">
          <a href="https://www.bancobaieuropa.pt/search/pesquisar">
            <img class="pesquisar-azul" src="https://www.bancobaieuropa.pt/themes/custom/baieu/images/ICONS/pesquisar-azul.png" alt="Pesquisar">
            <img class="pesquisar-branco" src="https://www.bancobaieuropa.pt/themes/custom/baieu/images/ICONS/pesquisar.png" alt="Pesquisar">
            <!--<i class="header-icon material-icons">search</i>-->
            <span>Procurar</span></a>
        </div>
      </li>




    </ul>


  </div>










  </div>


</div>

<div class="main-navigation context-institucional-main-navigation"><div class=" menu-mobile menu-fechado"></div>
  <div class="main-navigation-2">
    

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'region' -->
<!-- FILE NAME SUGGESTIONS:
   * region--main-navigation.html.twig
   x region.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/layout/region.html.twig' -->
  <div>
    

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   * block--mainnavigation.html.twig
   * block--system-menu-block--main.html.twig
   x block--system-menu-block.html.twig
   * block--system.html.twig
   * block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->
<div class="navigation_blocks">
  

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'menu__main' -->
<!-- FILE NAME SUGGESTIONS:
   * menu--main.html.twig
   x menu.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->

              <ul>
              <li>
        <a data-drupal-link-system-path="informacoes/abertura-conta" class="links-primeiro-nivel">Abertura de Conta</a>
              </li>
          <li>
        <a data-drupal-link-system-path="empresas" class="links-primeiro-nivel">Empresas</a>
                                <ul>
              <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/empresas/depositos_a_ordem" data-drupal-link-system-path="node/41">Depósitos à Ordem</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/empresas/depositos_a_prazo" data-drupal-link-system-path="node/42">Depósitos a Prazo</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/empresas/solucoes_de_credito" title="Descubra as nossas soluções de crédito criadas a pensar na sua empresa" data-drupal-link-system-path="node/43">Soluções de Crédito</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/empresas/trade_finance" data-drupal-link-system-path="node/46">Trade Finance</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/empresas/solucoes_de_credito/servicos_tesouraria" data-drupal-link-system-path="node/48">Serviços de Tesouraria</a>
              </li>
        </ul>
  
              </li>
          <li>
        <a data-drupal-link-system-path="particulares" class="links-primeiro-nivel">Particulares</a>
                                <ul>
              <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/particulares/depositos_a_ordem" data-drupal-link-system-path="node/37">Depósitos à Ordem</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/particulares/depositos_a_prazo" data-drupal-link-system-path="node/38">Depósitos a Prazo</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/particulares/descoberto_autorizado" data-drupal-link-system-path="node/39">Descoberto Autorizado</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/particulares/servicos-minimos" title="Conta de Serviços mínimos bancários" data-drupal-link-system-path="node/158">Conta de Serviços Mínimos Bancários</a>
              </li>
        </ul>
  
              </li>
          <li>
        <a data-drupal-link-system-path="banca_investimento" class="links-primeiro-nivel">Banca de Investimento</a>
                                <ul>
              <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/banca_investimento/corporate_finance" data-drupal-link-system-path="node/58">Corporate Finance</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/banca_investimento/financiamentos_estruturados" data-drupal-link-system-path="node/57">Structured Finance</a>
              </li>
        </ul>
  
              </li>
          <li>
        <a data-drupal-link-system-path="institucional" class="links-primeiro-nivel">Institucional</a>
                                <ul>
              <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/institucional/quem-somos" data-drupal-link-system-path="node/16">Quem Somos</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/institucional/onde-estamos" data-drupal-link-system-path="node/17">Onde Estamos</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/institucional/orgaos-sociais" data-drupal-link-system-path="node/18">Órgãos Sociais</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/institucional/goveno-societario" data-drupal-link-system-path="node/19">Governo Societário</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/institucional/informacao_financeira" data-drupal-link-system-path="node/89">Informação Financeira</a>
              </li>
        </ul>
  
              </li>
          <li>
        <a data-drupal-link-system-path="node/91" class="links-primeiro-nivel">Informações</a>
                                <ul>
              <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/adesao-bai-directo" data-drupal-link-system-path="node/71">Adesão BAI Europa directo</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/newsletters-e-artigos?field_publicar_em_target_id=39" data-drupal-link-query="{&quot;field_publicar_em_target_id&quot;:&quot;39&quot;}" data-drupal-link-system-path="informacoes/newsletters-e-artigos">Newsletters e Artigos</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/notas-informativas" data-drupal-link-system-path="node/200">Notas Informativas</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/relatorios-conjuntura-economica" data-drupal-link-system-path="node/201">Relatórios de Conjuntura Económica</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/cambios-taxas" data-drupal-link-system-path="node/118" class="is-active">Câmbios e Taxas</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/sites/default/files/2020-11/Servico_de_Mudanca_de_Conta_Bancaria_PT.pdf">Mudança de Conta</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/precario" data-drupal-link-system-path="node/35">Preçário</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/privacidade" data-drupal-link-system-path="node/116">Privacidade</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/institucional/informacao-legal-regulamentar" data-drupal-link-system-path="institucional/informacao-legal-regulamentar">Informação Legal e Regulamentar</a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/openbanking" data-drupal-link-system-path="node/168">Open Banking </a>
              </li>
          <li class="links-segundo-nivel">
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/seguranca-online" data-drupal-link-system-path="node/402">Segurança Online</a>
              </li>
        </ul>
  
              </li>
        </ul>
  


<!-- END OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->


</div>

<!-- END OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->


  </div>

<!-- END OUTPUT from 'themes/custom/baieu/templates/layout/region.html.twig' -->


  </div>
</div>

<!-- Modal -->
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLongTitle">BAI Europa Directo</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">×</span>
        </button>
      </div>
      <div class="modal-body">
        <div class="row">

          <a href="https://emp.bancobaieuropa.pt/" target="_blank" class="a-ib-modal-link">
            <div class="ib-modal-link empresas-ib-modal-link">
              <p>Empresas</p>
            </div>
          </a>

          <a href="https://priv.bancobaieuropa.pt/" target="_blank" class="a-ib-modal-link">
            <div class="ib-modal-link">
              <p>Particulares</p>
            </div>
          </a>

        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Voltar</button>
      </div>
    </div>
  </div>
</div>
  

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'region' -->
<!-- FILE NAME SUGGESTIONS:
   * region--content.html.twig
   x region.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/layout/region.html.twig' -->
  <div>
    <div data-drupal-messages-fallback="" class="hidden"></div>

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   * block--baieu-content.html.twig
   * block--system-main-block.html.twig
   * block--system.html.twig
   x block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/block/block.html.twig' -->
<div id="block-baieu-content"><div id="bock-baieu-veil"></div>
  
    
      

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'node' -->
<!-- FILE NAME SUGGESTIONS:
   * node--118--full.html.twig
   * node--118.html.twig
   * node--article--full.html.twig
   * node--article.html.twig
   * node--full.html.twig
   x node.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/node.html.twig' -->

      
              <div class="no-image-breadcrumb">
        

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   x block--system-breadcrumb-block.html.twig
   * block--system.html.twig
   * block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/block--system-breadcrumb-block.html.twig' -->
  <div class="breadcrumb-baie">
    <div class="breadcrumb-baie-2 breadcrumb-baie-2-context-institucional">
      <ul>
        <li>
          <div>
            

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'breadcrumb' -->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/navigation/breadcrumb.html.twig' -->
  <nav role="navigation" aria-labelledby="system-breadcrumb">
    <h2 id="system-breadcrumb" class="visually-hidden">Navegação estrutural</h2>
    <ol>
          <li>
                  <a href="https://www.bancobaieuropa.pt/pt-pt">Início</a>
              </li>
          <li>
                  <a href="https://www.bancobaieuropa.pt/pt-pt/informacoes">Informações</a>
              </li>
          <li>
                  Câmbios e Taxas
              </li>
        </ol>
  </nav>

<!-- END OUTPUT from 'themes/custom/baieu/templates/navigation/breadcrumb.html.twig' -->


          </div>
        </li>
      </ul>
    </div>
  </div>

<!-- END OUTPUT from 'themes/custom/baieu/block--system-breadcrumb-block.html.twig' -->


      </div>
    
  

  <div class="baieu-page-content" id="baieu-page-content">
    <div class="baieu-page-content-2">

      <div data-history-node-id="118" role="article" about="/pt-pt/informacoes/cambios-taxas" typeof="schema:Article" class="node">
        
                  <h2>

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'field' -->
<!-- FILE NAME SUGGESTIONS:
   * field--node--title--article.html.twig
   x field--node--title.html.twig
   * field--node--article.html.twig
   * field--title.html.twig
   * field--string.html.twig
   * field.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/field/field--node--title.html.twig' -->
<div class="titulo context-titulo-institucional">
  <span property="schema:name">Câmbios e Taxas</span>
</div>

<!-- END OUTPUT from 'themes/custom/baieu/templates/field/field--node--title.html.twig' -->

</h2>
                

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'rdf_metadata' -->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/misc/rdf-metadata.html.twig' -->
  <span property="schema:name" content="Câmbios e Taxas" class="hidden"></span>

<!-- END OUTPUT from 'themes/custom/baieu/templates/misc/rdf-metadata.html.twig' -->






          <div class="node">
                        
            

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'field' -->
<!-- FILE NAME SUGGESTIONS:
   * field--node--body--article.html.twig
   * field--node--body.html.twig
   * field--node--article.html.twig
   * field--body.html.twig
   * field--text-with-summary.html.twig
   x field.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/field/field.html.twig' -->

            <div property="schema:text" class="article-body article-context-institucional"><div class="cambiostaxas"><div class="cambiosdivisas"><h3>Câmbios Divisas</h3><table><tbody><tr><th>MOEDA</th><th>VENDA</th><th>COMPRA</th></tr><tr><td>EUR/USD</td><td>1.0833</td><td>1.0199</td></tr><tr><td>EUR/ZAR</td><td>19.01129</td><td>17.1922</td></tr><tr><td>EUR/GBP</td><td>0.93</td><td>0.841</td></tr></tbody></table><br></div><div class="notasmoedas"><br><h3>Câmbios Notas/Moedas</h3><table><tbody><tr><th>MOEDA</th><th>VENDA</th><th>COMPRA</th></tr><tr><td>EUR/USD</td><td>1.0833</td><td>1.0199</td></tr><tr><td>EUR/AOA</td><td>556.048</td><td>513.27599</td></tr><tr><td>EUR/GBP</td><td>0.93</td><td>0.93</td></tr></tbody></table></div><br><p>Atualizado dia: 07/01/2023 às 09:00:02</p></div></div>
      
<!-- END OUTPUT from 'themes/custom/baieu/templates/field/field.html.twig' -->


            
            
            
            
	    
	    
          </div>



      </div>

    </div>
  </div>





















<!-- END OUTPUT from 'themes/custom/baieu/node.html.twig' -->


  </div>

<!-- END OUTPUT from 'themes/custom/baieu/templates/block/block.html.twig' -->


  </div>

<!-- END OUTPUT from 'themes/custom/baieu/templates/layout/region.html.twig' -->


                          <div class="footer">
    <div class="footer-2">

      <div class="contactos footercol">
        <h1>Contactos</h1>
        

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   * block--contactos.html.twig
   * block--system-menu-block--footer.html.twig
   x block--system-menu-block.html.twig
   * block--system.html.twig
   * block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->
<div class="navigation_blocks">
  

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'menu__footer' -->
<!-- FILE NAME SUGGESTIONS:
   * menu--footer.html.twig
   x menu.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->

              <ul>
              <li>
        <a href="https://www.bancobaieuropa.pt/pt-pt/contact/contacte_nos" title="Contacte-nos" data-drupal-link-system-path="contact/contacte_nos">Contacte-nos</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/pt-pt/institucional/onde-estamos" data-drupal-link-system-path="node/17">Onde Estamos</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/pt-pt/contact/sugestao_reclamacao_informacao" data-drupal-link-system-path="contact/sugestao_reclamacao_informacao">Sugestões, Reclamações e Informações</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/pt-pt/portal_de_etica" data-drupal-link-system-path="node/445">Portal de Ética</a>
              </li>
          <li>
        <a href="https://priv.bancobaieuropa.pt/">BAI EUROPA DIRECTO - Particulares</a>
              </li>
          <li>
        <a href="https://emp.bancobaieuropa.pt/">BAI EUROPA DIRECTO - Empresas</a>
              </li>
          <li>
        <a href="http://www.bancobai.ao/">BAI Angola</a>
              </li>
          <li>
        <a href="http://www.bancobai.cv/">BAI Cabo Verde</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/pt-pt/recrutamento" title="Recrutamento" data-drupal-link-system-path="node/121">Recrutamento</a>
              </li>
        </ul>
  


<!-- END OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->


</div>

<!-- END OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->


      </div>
      <div class="informacaoutil footercol">
        <h1>Informação Útil</h1>
        

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   * block--informacaoutil.html.twig
   * block--system-menu-block--informacao-util.html.twig
   x block--system-menu-block.html.twig
   * block--system.html.twig
   * block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->
<div class="navigation_blocks">
  

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'menu__informacao_util' -->
<!-- FILE NAME SUGGESTIONS:
   * menu--informacao-util.html.twig
   x menu.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->

              <ul>
              <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/abertura-conta" data-drupal-link-system-path="informacoes/abertura-conta">Abertura de Conta</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/adesao-bai-directo" data-drupal-link-system-path="node/71">Adesão BAI Directo</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/artigos" data-drupal-link-system-path="informacoes/artigos">Artigos</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/boletins_economicos" data-drupal-link-system-path="node/59">Boletins Económicos</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/sites/default/files/2018-07/Servico_Mudanca_Conta_Bancaria.pdf">Mudança de Conta</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/precario" data-drupal-link-system-path="node/35">Preçário</a>
              </li>
          <li>
        <a href="https://www.livroreclamacoes.pt/">Livro de Reclamações</a>
              </li>
        </ul>
  


<!-- END OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->


</div>

<!-- END OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->


      </div>
      <div class="informacaolegal footercol">
        <h1>Informação Legal</h1>
        

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'block' -->
<!-- FILE NAME SUGGESTIONS:
   * block--informacaolegal.html.twig
   * block--system-menu-block--informacao-legal.html.twig
   x block--system-menu-block.html.twig
   * block--system.html.twig
   * block.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->
<div class="navigation_blocks">
  

<!-- THEME DEBUG -->
<!-- THEME HOOK: 'menu__informacao_legal' -->
<!-- FILE NAME SUGGESTIONS:
   * menu--informacao-legal.html.twig
   x menu.html.twig
-->
<!-- BEGIN OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->

              <ul>
              <li>
        <a href="http://www.bancobaieuropa.pt/sites/default/files/2019-12/direitos-pagamentos-europa.pdf">Direitos quando efectua pagamentos na Europa</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/sites/default/files/2018-03/direitos_e_deveres_dos_consumidores_credito.pdf">Direitos e Deveres dos Consumidores</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/sites/default/files/2018-03/depositos_bancarios_direitos_deveres.pdf">Direitos e Deveres dos Depositantes</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/sites/default/files/2021-03/ficha_%20de_informacao_depositante.pdf">Ficha de Informação de Depositante</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/incumprimento_de_contratos_de_credito" data-drupal-link-system-path="node/76">Incumprimento de Contratos de Crédito</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/regras_sobre_seguranca" data-drupal-link-system-path="node/75">Regras sobre Segurança</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/resolucao_de_litigios" data-drupal-link-system-path="node/77">Resolução de Litígios</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/particulares/servicos-minimos" title="Conta de Serviços mínimos bancários" data-drupal-link-system-path="node/158">Conta de Serviços mínimos bancários</a>
              </li>
          <li>
        <a href="https://www.bancobaieuropa.pt/index.php/pt-pt/informacoes/privacidade" data-drupal-link-system-path="node/116">Privacidade</a>
              </li>
        </ul>
  


<!-- END OUTPUT from 'themes/custom/baieu/templates/navigation/menu.html.twig' -->


</div>

<!-- END OUTPUT from 'themes/custom/baieu/block--system-menu-block.html.twig' -->


      </div>

      <div id="disclaimer">
  <div class="devmsg">
    Versão 1.00.00 - 19-02-2018
  </div>
  <div class="direitos_reservados">
    Banco BAI Europa, S.A. ©.<span> Todos os direitos reservados.</span>
  </div>
</div>
    </div>

  </div>
</div>






    
  
  
  
      
              
                            
                            
  

<!-- END OUTPUT from 'themes/custom/baieu/page.html.twig' -->


  

<!-- END OUTPUT from 'core/modules/system/templates/off-canvas-page-wrapper.html.twig' -->


    
    


  



<!-- END OUTPUT from 'themes/custom/baieu/templates/layout/html.html.twig' -->

</body></html>
------MultipartBoundary--N1Eay4lcYYX2rGjcUEmGmPPUBN3bWjvqvPv2iZl2Wh----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.bancobaieuropa.pt/sites/default/files/css/css_kcpJl2G6pY5K3VUDCOc-bNWZUn5aisTSW0wP2rqcOn8.css

@charset "utf-8";

.ajax-progress { display: inline-block; padding: 1px 5px 2px; }

[dir="rtl"] .ajax-progress { float: right; }

.ajax-progress-throbber .throbber { display: inline; padding: 1px 6px 2px; background: url("/core/misc/throbber-active.gif") 0px center no-repeat transparent; }

.ajax-progress-throbber .message { display: inline; padding: 1px 5px 2px; }

tr .ajax-progress-throbber .throbber { margin: 0px 2px; }

.ajax-progress-bar { width: 16em; }

.ajax-progress-fullscreen { position: fixed; z-index: 1000; top: 48.5%; left: 49%; width: 24px; height: 24px; padding: 4px; opacity: 0.9; border-radius: 7px; background-color: rgb(35, 35, 35); background-image: url("/core/misc/loading-small.gif"); background-repeat: no-repeat; background-position: center center; }

[dir="rtl"] .ajax-progress-fullscreen { right: 49%; left: auto; }

.text-align-left { text-align: left; }

.text-align-right { text-align: right; }

.text-align-center { text-align: center; }

.text-align-justify { text-align: justify; }

.align-left { float: left; }

.align-right { float: right; }

.align-center { display: block; margin-right: auto; margin-left: auto; }

.js input.form-autocomplete { background-image: url("/core/misc/throbber-inactive.png"); background-repeat: no-repeat; background-position: 100% center; }

.js[dir="rtl"] input.form-autocomplete { background-position: 0% center; }

.js input.form-autocomplete.ui-autocomplete-loading { background-image: url("/core/misc/throbber-active.gif"); background-position: 100% center; }

.js[dir="rtl"] input.form-autocomplete.ui-autocomplete-loading { background-position: 0% center; }

.fieldgroup { padding: 0px; border-width: 0px; }

.container-inline div, .container-inline label { display: inline-block; }

.container-inline .details-wrapper { display: block; }

.container-inline .hidden { display: none; }

.clearfix::after { display: table; clear: both; content: ""; }

.js details:not([open]) .details-wrapper { display: none; }

.hidden { display: none; }

.visually-hidden { overflow: hidden; clip: rect(1px, 1px, 1px, 1px); width: 1px; height: 1px; overflow-wrap: normal; position: absolute !important; }

.visually-hidden.focusable:active, .visually-hidden.focusable:focus { overflow: visible; clip: auto; width: auto; height: auto; position: static !important; }

.invisible { visibility: hidden; }

.item-list__comma-list, .item-list__comma-list li { display: inline; }

.item-list__comma-list { margin: 0px; padding: 0px; }

.item-list__comma-list li::after { content: ", "; }

.item-list__comma-list li:last-child::after { content: ""; }

.js .js-hide { display: none; }

.js-show { display: none; }

.js .js-show { display: block; }

.nowrap { white-space: nowrap; }

.position-container { position: relative; }

.progress { position: relative; }

.progress__track { min-width: 100px; max-width: 100%; height: 16px; margin-top: 5px; border: 1px solid; background-color: rgb(255, 255, 255); }

.progress__bar { width: 3%; min-width: 3%; max-width: 100%; height: 16px; background-color: rgb(0, 0, 0); }

.progress__description, .progress__percentage { overflow: hidden; margin-top: 0.2em; color: rgb(85, 85, 85); font-size: 0.875em; }

.progress__description { float: left; }

[dir="rtl"] .progress__description { float: right; }

.progress__percentage { float: right; }

[dir="rtl"] .progress__percentage { float: left; }

.progress--small .progress__track { height: 7px; }

.progress--small .progress__bar { height: 7px; background-size: 20px 20px; }

.reset-appearance { margin: 0px; padding: 0px; border: 0px none; background: transparent; line-height: inherit; -webkit-appearance: none; }

.resize-none { resize: none; }

.resize-vertical { min-height: 2em; resize: vertical; }

.resize-horizontal { max-width: 100%; resize: horizontal; }

.resize-both { max-width: 100%; min-height: 2em; resize: both; }

table.sticky-header { z-index: 500; top: 0px; margin-top: 0px; background-color: rgb(255, 255, 255); }

.system-status-counter__status-icon { display: inline-block; width: 25px; height: 25px; vertical-align: middle; }

.system-status-counter__status-icon::before { display: block; width: 100%; height: 100%; content: ""; background-repeat: no-repeat; background-position: center 2px; background-size: 16px; }

.system-status-counter__status-icon--error::before { background-image: url("/core/misc/icons/e32700/error.svg"); }

.system-status-counter__status-icon--warning::before { background-image: url("/core/misc/icons/e29700/warning.svg"); }

.system-status-counter__status-icon--checked::before { background-image: url("/core/misc/icons/73b355/check.svg"); }

.system-status-report-counters__item { width: 100%; margin-bottom: 0.5em; padding: 0.5em 0px; text-align: center; white-space: nowrap; background-color: rgba(0, 0, 0, 0.063); }

@media screen and (min-width: 60em) {
  .system-status-report-counters { display: flex; flex-wrap: wrap; justify-content: space-between; }
  .system-status-report-counters__item--half-width { width: 49%; }
  .system-status-report-counters__item--third-width { width: 33%; }
}

.system-status-general-info__item { margin-top: 1em; padding: 0px 1em 1em; border: 1px solid rgb(204, 204, 204); }

.system-status-general-info__item-title { border-bottom: 1px solid rgb(204, 204, 204); }

body.drag { cursor: move; }

tr.region-title { font-weight: bold; }

tr.region-message { color: rgb(153, 153, 153); }

tr.region-populated { display: none; }

tr.add-new .tabledrag-changed { display: none; }

.draggable a.tabledrag-handle { float: left; overflow: hidden; height: 1.7em; margin-left: -1em; cursor: move; text-decoration: none; }

[dir="rtl"] .draggable a.tabledrag-handle { float: right; margin-right: -1em; margin-left: 0px; }

a.tabledrag-handle:hover { text-decoration: none; }

a.tabledrag-handle .handle { width: 14px; height: 14px; margin: -0.4em 0.5em 0px; padding: 0.42em 0.5em; background: url("/core/misc/icons/787878/move.svg") 6px 7px no-repeat; }

a.tabledrag-handle:hover .handle, a.tabledrag-handle:focus .handle { background-image: url("/core/misc/icons/000000/move.svg"); }

.touchevents .draggable td { padding: 0px 10px; }

.touchevents .draggable .menu-item__link { display: inline-block; padding: 10px 0px; }

.touchevents a.tabledrag-handle { width: 40px; height: 44px; }

.touchevents a.tabledrag-handle .handle { height: 21px; background-position: 40% 19px; }

[dir="rtl"] .touch a.tabledrag-handle .handle { background-position: right 40% top 19px; }

.touchevents .draggable.drag a.tabledrag-handle .handle { background-position: 50% -32px; }

.tabledrag-toggle-weight-wrapper { text-align: right; }

[dir="rtl"] .tabledrag-toggle-weight-wrapper { text-align: left; }

.indentation { float: left; width: 20px; height: 1.7em; margin: -0.4em 0.2em -0.4em -0.4em; padding: 0.42em 0px 0.42em 0.6em; }

[dir="rtl"] .indentation { float: right; margin: -0.4em -0.4em -0.4em 0.2em; padding: 0.42em 0.6em 0.42em 0px; }

.tablesort { display: inline-block; width: 16px; height: 16px; background-size: 100%; }

.tablesort--asc { background-image: url("/core/misc/icons/787878/twistie-down.svg"); }

.tablesort--desc { background-image: url("/core/misc/icons/787878/twistie-up.svg"); }

div.tree-child { background: url("/core/misc/tree.png") 11px center no-repeat; }

div.tree-child-last { background: url("/core/misc/tree-bottom.png") 11px center no-repeat; }

[dir="rtl"] div.tree-child, [dir="rtl"] div.tree-child-last { background-position: -65px center; }

div.tree-child-horizontal { background: url("/core/misc/tree.png") -11px center no-repeat; }
------MultipartBoundary--N1Eay4lcYYX2rGjcUEmGmPPUBN3bWjvqvPv2iZl2Wh----
Content-Type: text/css
Content-Transfer-Encoding: binary
Content-Location: https://www.bancobaieuropa.pt/sites/default/files/css/css_ofkCQpVkjjc6khOxEuEyLdWe4ZwZWluOU2CcMbEV4Ew.css

@charset "utf-8";

html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video { border: 0px; font: inherit; vertical-align: baseline; margin: 0px; padding: 0px; }

article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section { display: block; }

body { line-height: 1; }

ol, ul { list-style: none; }

blockquote, q { quotes: none; }

blockquote::before, blockquote::after, q::before, q::after { content: none; }

table { border-collapse: collapse; border-spacing: 0px; }

@font-face { font-family: "Material Icons"; font-style: normal; font-weight: 400; src: local("Material Icons"), local("MaterialIcons-Regular"), url("/themes/custom/baieu/woff/MaterialIcons-Regular.woff2") format("woff2"), url("/themes/custom/baieu/woff/MaterialIcons-Regular.woff") format("woff"), url("/themes/custom/baieu/woff/MaterialIcons-Regular.ttf") format("truetype"); }

@font-face { font-family: rubik-light; src: url("/themes/custom/baieu/woff/rubik/Rubik-Light.WOFF") format("woff"), url("/themes/custom/baieu/woff/rubik/Rubik-Light.ttf") format("truetype"); }

@font-face { font-family: rubik-regular; src: url("/themes/custom/baieu/woff/rubik/Rubik-Regular.WOFF") format("woff"), url("/themes/custom/baieu/woff/rubik/Rubik-Regular.ttf") format("truetype"); }

@font-face { font-family: rubik-medium; src: url("/themes/custom/baieu/woff/rubik/Rubik-Regular.WOFF") format("woff"), url("/themes/custom/baieu/woff/rubik/Rubik-Regular.ttf") format("truetype"); }

@font-face { font-family: rubik-bold; src: url("/themes/custom/baieu/woff/rubik/Rubik-Regular.WOFF") format("woff"), url("/themes/custom/baieu/woff/rubik/Rubik-Regular.ttf") format("truetype"); }

.material-icons, .breadcrumb-baie-2 ol li::before, .menu-aberto::before, .menu-fechado::before { font-family: "Material Icons"; font-weight: normal; font-style: normal; font-size: 24px; line-height: 1; letter-spacing: normal; text-transform: none; display: inline-block; white-space: nowrap; overflow-wrap: normal; direction: ltr; -webkit-font-smoothing: antialiased; text-rendering: optimizelegibility; font-feature-settings: "liga"; }

html { height: 100%; box-sizing: border-box; }

*, ::before, ::after { box-sizing: inherit; }

body { -webkit-font-smoothing: antialiased; background: rgb(255, 255, 255); height: 100%; font-family: rubik-regular; }

p, span { font-family: rubik-regular; }

a { color: white; text-decoration: none; }

a:hover { color: white; text-decoration: none; }

* { box-sizing: border-box; }

em { font-style: italic; }

.small { font-size: small; }

.center { text-align: center; }

* html .clearfix { height: 1%; overflow: visible; }

* + html .clearfix { min-height: 1%; }

.clearfix::after { clear: both; content: "."; display: block; height: 0px; visibility: hidden; }

.clr { clear: both; }

.devmsg { display: none; }

h1 { font-size: 35px; font-weight: bold; margin-bottom: 10px; margin-top: 10px; color: rgb(28, 55, 101); }

h2 { font-size: 25px; font-weight: bold; margin-bottom: 10px; margin-top: 10px; color: rgb(28, 55, 101); }

p { font-size: medium; font-family: rubik-regular; }

.pagecontent { margin-top: 60px; }

#block-baieu-content { margin-bottom: 40px; min-height: 390px; }

.col-md-12 { padding: 0px !important; }

@media screen and (min-width: 1420px) {
  .col-xl-9 { margin-left: 12.5% !important; }
}

.row { margin-left: 0px !important; margin-right: 0px !important; }

.file--application-pdf { line-height: 32px; height: 32px; }

.file--application-pdf a { margin-bottom: 10px; display: block; font-size: 18px; color: rgb(28, 55, 101); cursor: pointer; vertical-align: middle; padding-left: 15px; text-decoration: none !important; }

.file--application-pdf a::before { background-image: url("/themes/custom/baieu/images/pdf.png"); background-size: 32px 32px; height: 32px; width: 32px; display: inline-block; content: ""; margin-right: 14px; vertical-align: middle; }

.context-titulo-particulares span { color: rgb(54, 160, 205) !important; }

.context-titulo-empresas span { color: rgb(101, 113, 116) !important; }

.context-titulo-institucional span { color: rgb(0, 46, 94) !important; }

.context-titulo-banca-investimento span { color: rgb(148, 139, 117) !important; }

.titulo, .js-quickedit-page-title { margin-top: 50px; font-size: 25px; color: dimgray; margin-bottom: 20px; }

.titulo span, .js-quickedit-page-title span { position: relative; left: 1px; color: rgb(0, 46, 94); font-weight: 400; font-family: rubik-regular; text-transform: uppercase; font-size: 25px; }

.listas-links div, .view-list div { line-height: 32px; height: 32px; margin-bottom: 20px; }

.listas-links div a, .view-list div a { float: left; display: block; font-size: 18px; color: rgb(28, 55, 101); cursor: pointer; vertical-align: middle; padding-left: 15px; text-decoration: none !important; }

.listas-links div a:hover, .view-list div a:hover { text-decoration: underline !important; }

.listas-links div a:hover::before, .view-list div a:hover::before { background-image: url("/themes/custom/baieu/images/folder-open.png"); }

.view-list span span a { width: 100%; margin-bottom: 15px; float: left; display: block; font-size: 18px; color: rgb(28, 55, 101); cursor: pointer; vertical-align: middle; padding-left: 15px; text-decoration: none !important; }

.view-list span span a::before { background-image: url("/themes/custom/baieu/images/folder.png"); background-size: 32px 32px; height: 32px; width: 32px; display: inline-block; content: ""; margin-right: 14px; vertical-align: middle; }

.view-list span span a:hover { text-decoration: underline !important; }

.view-list span span a:hover::before { background-image: url("/themes/custom/baieu/images/folder-open.png"); }

.container { margin: 0px auto !important; }

.baieu-site-container { position: relative; }

.baieu-page-content { padding-bottom: 0px; top: -60px; position: relative; }

.baieu-page-content-2 { width: 1005px; top: -22vw; margin: 0px auto; display: table; }

@media (max-width: 1005px) {
  .baieu-page-content-2 { width: 100vw; }
}

@media (min-width: 1700px) {
}

.myview { width: 1005px; margin: 0px auto; display: table; }

@media (max-width: 1005px) {
  .myview { width: 100vw; }
}

.body-abertura-conta p { font-family: rubik-regular; color: rgb(101, 113, 116); }

.body-abertura-conta table tbody tr td { padding-left: 10px; padding-top: 10px; text-align: center; background-color: rgb(233, 236, 239); vertical-align: middle; }

.body-abertura-conta table tbody tr th { background-color: rgb(28, 55, 101); color: white; line-height: 15px; height: 47px; vertical-align: middle; font-weight: 600; width: 18vw; min-width: 78px; text-align: center; padding: 8px; }

.body-abertura-conta, .body-abertura-conta th, .body-abertura-conta td { border: 5px solid white; }

.titulo { position: relative; font-weight: 400; font-family: rubik-regular; text-transform: uppercase; font-size: 25px; left: 0%; color: rgb(0, 46, 94) !important; }

.titulo a { height: 40px; line-height: 24px; font-size: 25px; font-family: rubik-regular; text-align: justify; word-break: break-word; position: relative; left: 0%; text-decoration: none; font-weight: bold; color: rgb(101, 113, 116) !important; }

.titulo a:hover { text-decoration: none; color: rgb(101, 113, 116) !important; }

.separador-resultados-pesquisa-2 { width: 1005px; margin: 0px auto; display: table; }

@media (max-width: 1005px) {
  .separador-resultados-pesquisa-2 { margin-left: 2vw; }
}

.view-box { position: relative; float: left; width: 316px; height: 207px; background-color: rgb(0, 46, 94); margin-left: 1%; cursor: pointer; overflow: hidden; margin-top: 25px; }

.view-box:hover { background-color: rgb(0, 147, 213); }

.view-box-title { width: 80%; }

.view-box-title a { height: 40px; line-height: 24px; font-size: 18px; font-family: rubik-regular; text-align: justify; word-break: break-word; position: relative; left: 10%; color: white; text-decoration: none; }

.view-box-title a:hover { text-decoration: none; color: white; }

.view-box-image-thumbnail { background-image: url("/themes/custom/baieu/images/ICONS/button.png"); background-size: 140px 40px; }

.view-box-image-thumbnail::after { content: "Saiba mais"; }

@media not all, not all {
  .view-box-image-thumbnail::after { display: none; }
}

.view-box-image-thumbnail img { display: none; height: 150px; width: auto; }

#edit-help-link, #edit-advanced { display: none; }

.form-item label::after { content: "" !important; }

#edit-basic { margin-top: 30px; margin-bottom: 30px; }

#search-form #edit-keys { width: 35vh; margin-right: 15px; line-height: 40px; height: 40px; padding-left: 12px; }

#search-form #edit-submit { position: relative; top: -1px; }

.separador-resultados-pesquisa { font-size: 14px; color: dimgray; margin-bottom: 20px; }

.separador-resultados-pesquisa span { position: relative; left: 1px; }

.separador-resultados-pesquisa::after { display: block; position: relative; top: 20px; left: 0px; content: ""; border-top: 1px dotted rgb(221, 221, 221); width: 50%; margin: 0px; transform: translateY(-1rem); }

#msg-resultados-pesquisa, #msg-sem-resultados-pesquisa { display: none; }

.search-result-title { font-size: 22px; }

.search-result__snippet { font-size: 16px; }

.search-result { margin-top: 40px; padding-left: 45px; }

.tabela-onde-estamos { width: 1024px; }

@media (max-width: 1200px) {
  .tabela-onde-estamos { width: 100%; }
}

.map { width: 1024px !important; }

@media (max-width: 1200px) {
  .map { width: 100% !important; }
}

.no-image-breadcrumb { position: absolute; top: -18px; }

.breadcrumb-block-addedby-twigtweak { position: absolute; }

.breadcrumb-baie { border-bottom: 2px solid rgb(234, 233, 233); height: 55px; position: absolute; width: 100%; }

@media screen and (max-height: 1200px) {
  .breadcrumb-baie { max-height: 750px; }
}

.breadcrumb-baie-2 { width: 1005px; display: table; margin: 0px auto; background-color: transparent; padding-left: 0px; font-size: 12px; text-align: left; }

.breadcrumb-baie-2 ol li:first-child::before { content: ""; margin-left: 0px; margin-right: 0px; }

.breadcrumb-baie-2 ol { height: 50px; line-height: 50px; margin-bottom: 0px; }

.breadcrumb-baie-2 ol li { height: 50px; line-height: 50px; display: inline; color: rgb(28, 55, 101); }

.breadcrumb-baie-2 ol li a { height: 50px; line-height: 50px; vertical-align: middle; color: rgb(28, 55, 101); }

.breadcrumb-baie-2 ol li::before { content: "chevron_right"; margin-left: 10px; margin-right: 10px; font-size: 20px; position: relative; color: rgb(28, 55, 101); top: 8px; }

.breadcrumb-baie-2-context-particulares ol li { color: rgb(54, 160, 205); }

.breadcrumb-baie-2-context-empresas ol li { color: rgb(101, 113, 116); }

.breadcrumb-baie-2-context-institucional ol li { color: rgb(0, 46, 94); }

.breadcrumb-baie-2-context-banca-investimento ol li { color: rgb(148, 139, 117); }

.breadcrumb-baie-2-context-particulares ol li a { color: rgb(54, 160, 205); }

.breadcrumb-baie-2-context-empresas ol li a { color: rgb(101, 113, 116); }

.breadcrumb-baie-2-context-institucional ol li a { color: rgb(0, 46, 94); }

.breadcrumb-baie-2-context-banca-investimento ol li a { color: rgb(148, 139, 117); }

.breadcrumb-baie-2-context-particulares ol li::before { color: rgb(54, 160, 205); }

.breadcrumb-baie-2-context-empresas ol li::before { color: rgb(101, 113, 116); }

.breadcrumb-baie-2-context-institucional ol li::before { color: rgb(0, 46, 94); }

.breadcrumb-baie-2-context-banca-investimento ol li::before { color: rgb(148, 139, 117); }

.contact-form { padding-left: 20px; }

.empresas-ib-modal-link { background-image: url("/themes/custom/baieu/images/empresas.jpg") !important; }

.a-ib-modal-link { text-decoration: none; width: 50%; height: 150px; }

.a-ib-modal-link:hover { text-decoration: none; }

.ib-modal-link { display: inline-block; width: 188px; height: 150px; margin: 5px; background-image: url("/themes/custom/baieu/images/particulares2.jpg"); background-repeat: no-repeat; background-size: auto 150px; }

.ib-modal-link p { width: 100%; text-align: center; background: rgba(0, 0, 0, 0.5); position: relative; z-index: 2; color: white; font-size: 20px; font-weight: 400; }

.mymodal-link { color: white !important; }

a:not([href]):not([tabindex]) { color: white !important; }

@media screen and (max-width: 600px) {
  a:not([href]):not([tabindex]) { color: rgb(28, 55, 101) !important; }
}

.ib-link { background-color: rgb(54, 160, 205); width: 100%; height: 100%; font-size: 13px; }

.ib-link-context-particulares { background-color: rgb(54, 160, 205) !important; }

.ib-link-context-empresas { background-color: rgb(101, 113, 116) !important; }

.ib-link-context-institucional { background-color: rgb(0, 46, 94) !important; }

.ib-link-context-banca-investimentos { background-color: rgb(148, 139, 117) !important; }

a#iba { cursor: pointer; }

#iba:hover { text-decoration: none; }

.noticias-saibamais { position: absolute; border: 2px solid rgb(255, 255, 255); border-radius: 88px; color: white; font-family: rubik-regular; font-size: 14px; height: 40px; line-height: 37px; width: 159px; vertical-align: middle; text-align: center; bottom: 20px; left: 6%; }

.noticias-saibamais a { color: white; text-decoration: none; }

.noticias-saibamais a:hover { color: white; text-decoration: none; }

.noticias-data { padding-top: 25px; margin-bottom: 13px; font-size: 15px; font-family: rubik-regular; color: white; text-align: left; margin-left: 10%; }

.noticias-data a { color: white; text-decoration: none; }

.noticias-data a:hover { color: white; text-decoration: none; }

#user-login-form { margin-left: 24%; }

.myform { width: 100%; }

.myform .myform2 { width: 1005px; margin: 0px auto; display: table; }

@media (max-width: 1004px) {
  .myform .myform2 { width: 100%; margin-left: 2%; }
}

.view-agregadora { width: 1005px; display: table; margin: 0px auto; }

.ver-mais-link:hover { text-decoration: none; }

.article-body a:not([href]):not([tabindex]) { color: black !important; }

.visually-hidden { display: none !important; }

.pdf-myline { max-width: 95vw; }

.texto-consentimento p { font-size: 16px; color: rgb(101, 113, 116); font-style: italic; }

.texto-consentimento a { text-decoration: none; color: rgb(101, 113, 116); }

.texto-consentimento a:hover { color: rgb(101, 113, 116); text-decoration: none; }

.description { position: absolute; background-color: lightyellow; font-size: 12px; bottom: 10px; left: 23%; width: 221px; opacity: 0.8; display: none; }

.form-item { position: relative; margin-bottom: 30px; }

.form-item:hover .description { display: block; }

.form-item label { font-weight: 600; width: 100%; color: rgb(28, 55, 101); }

.form-item label::after { content: ":"; }

.form-submit { background-color: rgb(28, 55, 101); color: white; outline: none; border: none; height: 40px; width: 100px; text-transform: uppercase; font-size: 12px; font-weight: 600; }

.form-submit:hover { background-color: rgb(0, 147, 213); }

.form-item-field-contacte-nos-0-value label { font-size: 25px; color: dimgray; }

.form-item-field-contacte-nos-0-value label::after { display: block; position: relative; top: 20px; left: 0px; content: ""; border-top: 2px solid rgb(221, 221, 221); width: 50%; margin: 0px; transform: translateY(-1rem); }

.form-item-field-contacte-nos-0-value input { display: none; }

.form-item-field-canal-de-denuncias-0-value label { font-size: 25px; color: dimgray; }

.form-item-field-canal-de-denuncias-0-value label::after { display: block; position: relative; top: 20px; left: 0px; content: ""; border-top: 2px solid rgb(221, 221, 221); width: 50%; margin: 0px; transform: translateY(-1rem); }

.form-item-field-canal-de-denuncias-0-value input { display: none; }

.top-bar { width: 100%; border-bottom: 2px solid rgb(221, 221, 221); }

.top-bar-2 { width: 1005px; display: table; margin: 0px auto; text-align: right; }

@media (max-width: 1005px) {
  .top-bar-2 { width: 98vw; }
}

.top-bar-2 ul { list-style: none; margin: 0px auto; }

.top-bar-2 ul li { display: inline-block; }

.top-bar-2 ul li div { background-color: rgb(28, 55, 101); line-height: 46px; padding-left: 10px; padding-right: 10px; vertical-align: middle; }

#iba img { padding-right: 5px; position: relative; top: -3px; }

.header-baieu-branding { width: 100%; }

.main-header { background-color: white !important; }

.main-header-2 { width: 1005px; display: table; margin: 0px auto; }

@media (max-width: 1005px) {
  .main-header-2 { width: 100vw; }
}

.main-header-2 ul { list-style: none; margin: 0px; left: 33vw; }

@media (max-width: 600px) {
  .main-header-2 ul { width: 43vw; position: relative; }
}

.main-header-2 ul li { display: inline-block; }

.header-links { position: relative; right: -539px; top: 7px; }

@media (max-width: 1036px) {
  .header-links { position: absolute; right: 11px; top: 67px; }
}

@media (max-width: 600px) {
  .header-links { display: none; }
}

.header-links ul li { display: inline-block; }

i { padding-right: 5px; padding-left: 5px; font-size: 32px !important; position: relative !important; top: 10px !important; }

.logo { z-index: 999999999; }

.logo img { max-height: 70px; top: 0px; position: relative; }

@media (max-width: 767px) {
  .logo img { margin-left: 0px; }
}

.logo-context-particulares img { content: url("/themes/custom/baieu/images/logo/logo-azul.png"); }

.logo-context-empresas img { content: url("/themes/custom/baieu/images/logo/logo-cinzento.png"); }

.logo-context-institucional img { content: url("/themes/custom/baieu/images/logo/logo-azul.png"); }

.logo-context-banca-investimento img { max-height: 63px; content: url("/themes/custom/baieu/images/logo/logo-dourado.png"); }

.menu-aberto::before { content: "close" !important; }

.menu-fechado::before { content: "menu" !important; }

.main-navigation { position: relative; top: -16px; width: 100%; height: 50px; background-color: rgba(0, 46, 94, 0.53); background-size: cover; z-index: 999; }

.main-navigation-2 { display: table; margin: 0px auto; }

.main-navigation-2 ul { width: 1005px; text-align: left; }

.main-navigation-2 ul li { vertical-align: top; display: inline-block; padding-right: 25px; }

.main-navigation-2 ul li a:hover { opacity: 0.7; color: white; text-decoration: none; }

.main-navigation-2 ul li a::after { margin-left: 11px; margin-bottom: 1px; background-image: url("/themes/custom/baieu/images/ICONS/Triangle.png"); background-size: 8px 8px; display: inline-block; width: 8px; height: 7px; content: ""; }

@media (min-width: 601px) {
  .main-navigation-2 ul li:hover ul { display: block; }
  .main-navigation-2 ul li:hover ul li { display: block; }
}

.main-navigation-2 ul li ul { display: none; padding-bottom: 30px; background-color: white; width: 280px; overflow: hidden; position: absolute; }

.main-navigation-2 ul li ul li { display: none; background-color: transparent; padding-left: 5%; height: 29px; line-height: 29px; }

.main-navigation-2 ul li ul li a { font-family: rubik-regular; font-size: 12px; overflow-wrap: break-word; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: rgb(28, 55, 101) !important; }

.main-navigation-2 ul li ul li a:hover { text-decoration: underline; }

.main-navigation-2 ul li ul li a::after { content: ""; }

.main-navigation-2 a { display: block; color: rgb(255, 255, 255); font-weight: 400; font-size: 16px; text-decoration: none; height: 50px; line-height: 50px; text-align: left; }

.main-navigation-2 a:hover { text-decoration: underline; }

#block-baieu-branding { height: 76px; }

.header-links li { content: ""; float: right; }

.header-links a { font-size: 13px; color: rgb(0, 46, 94); }

@media screen and (max-width: 840px) {
  .header-links a { font-size: 0px; }
}

.header-links a:hover { text-decoration: underline; }

.header-links a img { margin-right: 6px; margin-left: 6px; }

.ib { color: rgb(28, 55, 101); position: relative; top: -6px; padding-left: 0px !important; padding-right: 0px !important; }

.ib i { font-size: 20px !important; padding: 0px !important; }

.pesquisar-azul { display: none; }

.pesquisar-branco { display: inline-block; }

.pesquisar { position: relative; right: -444px; top: 50px; height: 35px; vertical-align: middle; font-size: 13px; z-index: 9999; }

@media not all, not all {
  .pesquisar a { position: relative; top: 49px; }
}

@media (max-width: 1036px) {
  .pesquisar { position: absolute; right: 12px; top: 120px; }
}

.pesquisar a { color: white !important; }

.pesquisar img { width: 21px; margin-right: 17px; }

#header_links_line_separator { height: 28px; width: 1px; margin-left: 10px; margin-right: 10px; }

.aviso-homepage { display: none; }

.carousel { margin-top: 50px; }

.thumbnail-carousel { display: none; }

@media screen and (max-width: 600px) {
  .thumbnail-carousel { display: block !important; }
}

.image-carousel { display: block; }

@media screen and (max-width: 600px) {
  .image-carousel { display: none !important; }
}

.homepage { height: auto; font-size: 11px; position: relative; top: -55px; }

.homepage_content { padding-top: 0px; }

@media screen and (max-width: 1500px) {
  .col-xl-9, .col-lg-12 { padding-left: 0px !important; padding-right: 0px !important; }
}

.hidden-attributes { display: none; }

.container div #block-baieu-content { margin-top: 0px; }

@media screen and (max-width: 600px) {
  .carousel-control-prev, .carousel-control-next { width: 10% !important; }
}

.carousel-indicators { max-width: 450px; height: 33px; margin-left: 0% !important; margin-right: 0px !important; padding-right: 0px !important; left: 58% !important; bottom: 114px !important; }

.carousel-indicators li { width: 21px !important; height: 21px !important; border-radius: 20px !important; border: 2px solid rgb(255, 255, 255) !important; margin-left: 5px !important; background-color: transparent !important; }

.carousel-indicators .active { background-color: rgb(255, 255, 255) !important; opacity: 1 !important; }

@media screen and (max-width: 600px) {
  .carousel-indicators li { display: none; }
}

.image-carousel { position: relative; overflow: hidden; text-align: center; width: 100%; height: auto; }

@media (max-width: 1435px) {
  .image-carousel { width: 1435px !important; height: 586px !important; }
}

@media (max-width: 1200px) {
  .image-carousel { transform: translate(-15vw, 0%); }
}

@media (max-width: 960px) {
  .image-carousel { transform: translate(-22vw, 0%); }
}

@media (max-width: 925px) {
  .image-carousel { transform: translate(-30vw, 0%); }
}

.ver-mais { position: relative; bottom: 246px; text-align: center; font-size: 20px; color: white; font-family: rubik-medium; z-index: 2; }

.content-banner { top: -65px; width: 100%; height: auto; position: relative; }

@media (max-width: 1500px) {
  .content-banner { max-height: 550px; }
}

@media (max-width: 1600px) and (min-width: 1501px) {
  .content-banner { max-height: 600px; }
}

@media (max-width: 1700px) and (min-width: 1601px) {
  .content-banner { max-height: 650px; }
}

.content-banner .content-banner-image { position: relative; overflow: hidden; text-align: center; }

.content-banner .content-banner-image .cimg img { width: 100%; height: auto; }

@media (max-width: 1200px) {
  .content-banner .content-banner-image .cimg img { transform: translate(-15vw, 0%); }
}

@media (max-width: 960px) {
  .content-banner .content-banner-image .cimg img { transform: translate(-22vw, 0%); }
}

.content-banner .seta-ver-mais { position: relative; bottom: 13px; color: white; margin-top: 10px; }

.content-banner .seta-ver-mais img { position: relative; height: auto; transform: rotate(-90deg); }

.content-banner .content-banner-text { text-align: left; position: absolute; width: 100%; top: 0px; vertical-align: middle; }

@media screen and (max-height: 1200px) {
  .content-banner .content-banner-text { max-height: 750px; }
}

@media (max-width: 1005px) {
  .content-banner .content-banner-text { left: 2%; }
}

.content-banner .content-banner-text .content-banner-text-2 { width: 1005px; display: table; margin: 0px auto; height: 100%; padding-top: 10%; }

@media screen and (max-height: 1200px) {
  .content-banner .content-banner-text .content-banner-text-2 { max-height: 750px; }
}

.content-banner .banner-titulo { color: white; font-size: 72px; font-family: rubik-regular; width: 73%; letter-spacing: -3.88px; }

@media (min-width: 1005px) {
  .content-banner .banner-titulo { line-height: 77px; }
}

.content-banner .banner-subtitulo { padding-top: 1vw; }

.content-banner .banner-subtitulo span { font-family: rubik-light; font-size: 48px; letter-spacing: -0.18px; line-height: 45px; }

.content-banner .banner-subtitulo p { font-family: rubik-light; font-size: 48px; letter-spacing: -0.18px; line-height: 45px; }

.content-banner-secundary-navigation { position: absolute; bottom: 176px; z-index: 2; width: 100vw; }

@media not all, not all {
  .content-banner-secundary-navigation { bottom: 129px; }
}

.content-banner-secundary-navigation .secundary-navigation { position: absolute; bottom: initial; }

.secundary-navigation { width: 100%; z-index: 999; position: absolute; background-color: rgba(0, 46, 94, 0.53); bottom: 0px; }

.secundary-navigation-context-particulares { background-color: rgba(54, 160, 205, 0.53); }

.secundary-navigation-context-empresas { background-color: rgba(101, 113, 116, 0.53); }

.secundary-navigation-context-institucional { background-color: rgba(0, 46, 94, 0.53); }

.secundary-navigation-context-banca-investimento { background-color: rgba(148, 139, 117, 0.53); }

.secundary-navigation-2 { width: 1005px; display: table; margin: 0px auto; }

.secundary-navigation-2 ul { margin-right: 0px; margin-bottom: 0px; margin-top: 0px; min-width: 696px; list-style: none; }

.secundary-navigation-2 li { display: inline-block; width: 246px; }

.secundary-navigation-2 a { display: block; color: rgb(255, 255, 255); font-size: 20px; font-weight: 600; text-decoration: none; height: 96px; line-height: 80px; text-align: center; position: relative; padding-left: 15px; padding-right: 15px; opacity: 1 !important; }

@media screen and (max-width: 492px) {
  .secundary-navigation-2 a { padding-left: 26px; }
}

.secundary-navigation-2 a:hover { color: white; cursor: pointer; }

.secundary-navigation-2 a img { height: 72%; margin-top: 8%; width: auto; position: absolute; left: 0px; }

@media (max-width: 1100px) {
  .secundary-navigation a { font-size: 14px; }
}

@media (max-width: 975px) {
  .secundary-navigation a { font-size: 14px; }
  .secundary-navigation img { display: none; }
  .secundary-navigation-2 li { width: 24vw; }
  .secundary-navigation-title { left: 20px; }
  .secundary-navigation-subtitle { left: 20px; }
}

.homepage-floating-texts a { color: white; }

.homepage-floating-texts a:hover { color: white; text-decoration: none !important; }

.homepage-floating-texts span { color: white; }

.homepage-floating-texts span:hover { color: white; text-decoration: none !important; }

.homepage-floating-title { position: absolute; top: 0px; bottom: 0px; margin-top: 5%; margin-bottom: 80px; font-family: rubik-medium; font-size: 60px; color: white; left: 24%; line-height: 60px; }

@media (min-width: 1200px) {
  .homepage-floating-message { position: absolute; top: 300px; width: 34%; left: 24%; color: white; font-size: 44px; font-family: rubik-regular; font-weight: normal; line-height: 47px; }
  .homepage-floating-saibamais { position: relative; top: 0px; bottom: 0px; left: 0px; width: 180px; height: 51px; line-height: 51px; margin-top: 5%; border: 2px solid rgb(255, 255, 255); border-radius: 88px; opacity: 0.95; vertical-align: middle; text-align: center; font-family: rubik-medium; font-size: 16px; color: rgb(255, 255, 255); letter-spacing: -0.18px; }
}

.homepage-floating-message { position: absolute; top: 300px; width: 34%; left: 24%; color: white; font-size: 44px; font-family: rubik-regular; font-weight: normal; line-height: 47px; }

.homepage-floating-saibamais { position: relative; top: 0px; bottom: 0px; left: 0px; width: 180px; height: 51px; line-height: 51px; margin-top: 5%; border: 2px solid rgb(255, 255, 255); border-radius: 88px; opacity: 0.95; vertical-align: middle; text-align: center; font-family: rubik-medium; font-size: 16px; color: rgb(255, 255, 255); letter-spacing: -0.18px; }

.carousel-control-prev { background: linear-gradient(to left, rgba(255, 0, 0, 0), rgba(0, 0, 0, 0.4)); }

.carousel-control-prev-icon { position: relative; right: -32%; background-image: url("/themes/custom/baieu/images/ICONS/chevron-right.png") !important; height: 40px !important; }

.carousel-control-next-icon { transform: rotate(180deg); position: relative; left: -32%; background-image: url("/themes/custom/baieu/images/ICONS/chevron-right.png") !important; height: 40px !important; }

.carousel-control-next { background: linear-gradient(to right, rgba(255, 0, 0, 0), rgba(0, 0, 0, 0.4)); }

@media screen and (max-width: 600px) {
  .carousel-control-prev-icon, .carousel-control-next-icon { position: relative; top: -50px; }
}

@media (max-width: 1200px) and (min-width: 992px) {
  .col-lg-12 { margin-left: 0px !important; }
}

.secundary-navigation-title { position: absolute; top: 0px; left: 79px; font-size: 13px; font-family: rubik-medium; }

.secundary-navigation-title:hover { text-decoration: underline; }

.secundary-navigation-subtitle { position: absolute; font-weight: 400; top: 25px; left: 79px; font-size: 12px; }

.homepage_content-2 { width: 1005px; display: table; margin: 0px auto; }

.footer { height: auto; min-height: 250px; position: relative; width: 100%; clear: both; left: 0px; bottom: 0px; right: 0px; background-color: rgb(243, 243, 243); color: rgb(89, 89, 89); padding-top: 46px; z-index: 999; }

.footer div { vertical-align: top; }

.footer ul { list-style: none; margin: 0px auto; padding-right: 5vw; }

.footer ul li { display: inline; }

.footer a { display: block; margin-top: 5px; height: 32px; line-height: 32px; color: rgb(89, 89, 89); text-decoration: none; text-align: left; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; width: auto; vertical-align: middle; }

.footer a:hover { text-decoration: underline; }

.footer .direitos_reservados { width: 100%; text-align: left; font-size: 13px; line-height: 50px; padding-top: 10px; }

.login { position: absolute; left: 25%; color: red; }

.login li { float: left; }

.login li a { height: 10px; font-size: 14px !important; }

.footercol { display: inline-block; }

.footercol h1 { font-size: 15px; color: rgb(89, 89, 89); }

.footer-2 { width: 1005px; display: table; margin: 0px auto; }

.views-view-grid.horizontal.cols-3.clearfix { left: 2px; position: relative; }

.destaques-column { position: relative; max-width: 310px; min-width: 298px; margin-top: 10px; margin-left: 1%; margin-bottom: 30px; overflow: hidden; height: 309px; float: left; }

.destaques-column:hover { background-color: rgb(129, 166, 202); }

.destaques-title { padding: 15px 5px 5px 35px; z-index: 3; position: relative; top: -41%; background-color: rgba(0, 46, 94, 0.53); }

.destaques-title a { text-decoration: none; text-transform: uppercase; font-size: 17px; color: white; padding-top: 5px; font-family: rubik-medium; }

.destaques-title a:hover { text-decoration: none; color: white; }

.destaques-image { padding-bottom: 0px; padding-top: 0px; overflow: hidden; background-color: rgb(255, 255, 255); }

.destaques-image a img { height: auto; min-height: 309px; width: 100%; object-fit: cover; overflow: hidden; }

.destaques-body { height: 120px; padding-left: 35px; padding-right: 1px; margin-bottom: 10px; padding-top: 5px; font-size: 14px; font-family: rubik-regular; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 3; position: relative; top: -41%; background-color: rgba(0, 46, 94, 0.53); color: white; }

.destaques-body p { font-size: 14px; }

.saibamais { display: none; padding-left: 10px; position: absolute; top: 366px; }

.saibamais a { line-height: 20px; height: 40px; width: 115px; padding: 10px; font-weight: bold; color: white; font-family: monospace; text-transform: uppercase; text-decoration: none; background-color: rgb(18, 54, 125); opacity: 0.9; }

.node { margin-top: 35px; }

#views-exposed-form-newsletters-e-artigos-page-1 .js-form-item { display: inline-flex; }

#views-exposed-form-newsletters-e-artigos-page-1 .js-form-item label { padding: 10px; }

#views-exposed-form-newsletters-e-artigos-page-1 .form-actions { display: block; float: right; padding: 10px; }

.article-context-empresas h3 { color: rgb(101, 113, 116) !important; }

.article-context-particulares h3 { color: rgb(101, 113, 116) !important; }

.article-context-banca-investimento h3 { color: rgb(101, 113, 116) !important; }

.article-context-institucional h3 { color: rgb(101, 113, 116) !important; }

.article-body { color: rgb(89, 89, 89); font-size: 13px; }

.article-body p { color: rgb(89, 89, 89); line-height: 1.5em; font-size: 13px !important; }

.article-body span { color: rgb(89, 89, 89); font-size: 13px !important; }

.article-body ol li a { font-weight: 600; line-height: 50px; }

.article-body h4 { margin-top: 10px; font-size: 20px; }

.article-body h4 a img { position: relative; top: 7px; margin-right: 10px; }

.article-body a img { margin-bottom: 20px; margin-right: 10px; }

.article-body h3 { color: rgb(28, 55, 101); font-size: 20px; }

.article-body table tbody tr th { background-color: rgb(28, 55, 101); color: white; line-height: 30px; height: 30px; vertical-align: middle; font-weight: 600; width: 10vw; min-width: 78px; text-align: center; }

.article-body table tbody tr td { padding-left: 10px; padding-top: 10px; text-align: center; }

.article-body table, .article-body th, .article-body td { border: 1px solid black; }

.livro img { float: left; margin-right: 10px; }

.info-fix { position: relative; top: -95px; }

@media (max-width: 600px) {
  #block-baieu-branding { width: 100%; }
  .col-md-2 { padding: 0px !important; }
  .col-lg-12 { padding: 0px !important; }
  .thumbnail-carousel { width: 100vw; }
  .logo { position: absolute; top: 0px; }
  .logo img { top: -54px !important; }
  .logo a { text-decoration: none; text-align: center; }
  .logo a:hover { text-decoration: none; }
  .logo a img { width: 50vw; left: 1vw; max-width: 174px; }
  .header-links { z-index: 9999; position: fixed; top: 0px; right: 0px; width: auto; display: none !important; }
  .header-links ul li { float: left; width: 30px; padding-right: 40px; line-height: 40px !important; height: 40px !important; }
  .header-links ul li a { height: 40px; line-height: 40px; vertical-align: middle; padding: 10px 0px 0px; }
}

@media screen and (max-width: 320px) and (max-width: 600px) {
  .header-links ul li { padding-right: 30px; width: 35px; }
  .header-links ul li i { padding-left: 0px; top: 0px !important; font-size: 25px !important; }
}

@media (max-width: 600px) {
  .pesquisar { display: none; }
  a#iba { font-size: 10px; }
  #iba img { padding-right: 10px; position: relative; float: left; top: 1px; }
  #block-baieu-content { margin-top: 88px; margin-bottom: 0px; }
  #bock-baieu-veil { background-color: rgb(234, 234, 234); height: 300%; width: 100%; z-index: 3; display: none; position: absolute; }
  .titulo, .js-quickedit-page-title { padding-left: 10px; }
  .homepage { top: -171px; }
  .homepage_content-2 { width: 100vw; }
  #homepage-floating-texts { position: relative; top: -68vw; }
  .homepage-floating-title { position: relative; top: -11vw; line-height: 40px; width: 75vw; left: 4vw; bottom: 0px; margin-bottom: 0px; font-family: rubik-medium; font-size: 35px; color: white; display: block; }
  .homepage-floating-message { position: relative; width: 75vw; left: 4vw; top: -10vw; color: white; font-size: 21px; font-family: rubik-regular; font-weight: normal; display: block; line-height: 30px !important; }
  .homepage-floating-saibamais { display: none; position: relative; top: 0px; bottom: 0px; left: 0px; width: 145px; height: 41px; line-height: 38px; margin-top: 9%; border: 2px solid rgb(255, 255, 255); border-radius: 88px; opacity: 0.95; vertical-align: middle; text-align: center; font-family: rubik-medium; font-size: 14px; color: rgb(255, 255, 255); letter-spacing: -0.18px; }
  .menu-aberto::before, .menu-fechado::before { float: right; z-index: 998; display: block; font-size: 30px; width: 30px; height: 49px; line-height: 49px; vertical-align: middle; background-color: white; background-image: none; position: relative; top: 0px; right: 5px; color: rgb(0, 46, 94); }
  .main-navigation { background-image: none; background-color: transparent; top: 0px; position: absolute; }
  .main-navigation div { width: 100%; }
  .main-navigation div:nth-child(2) { display: none; }
  .main-navigation ul { margin-bottom: 0px; }
  .main-navigation ul li { height: auto; background: none white; width: 100%; z-index: 998 !important; }
  .main-navigation ul li a { color: rgb(28, 55, 101); text-align: left; padding-left: 10px; border: 1px solid darkgray; }
  .main-navigation-2 ul { width: 100vw; }
  .main-navigation-2 ul li a::after { display: none; }
  .links-primeiro-nivel { color: rgb(28, 55, 101) !important; }
  .links-segundo-nivel { background-image: none !important; background-color: white !important; padding-left: 20px !important; font-weight: normal !important; }
  .links-segundo-nivel a { color: black !important; }
  .top-bar { border-bottom: none; }
  .top-bar-2 { width: auto; float: left; }
  .top-bar-2 ul li { color: white; width: 122px; text-align: left; display: block; }
  .top-bar-2 ul li div { background-color: rgb(28, 55, 101); padding-left: 30px; padding-top: 14px; width: 137px; height: 51px; line-height: initial; position: relative; z-index: 9999; }
}

@media (max-width: 375px) and (max-width: 600px) {
  .top-bar-2 ul li div { background-color: rgb(28, 55, 101); padding-left: 9px; padding-top: 14px; width: 107px; height: 51px; line-height: initial; }
}

@media (max-width: 600px) {
  .secundary-navigation li { display: table; }
  .secundary-navigation li a { font-size: 12px; display: table-cell; line-height: 17px; vertical-align: middle; padding-left: 5px; }
}

@media (max-width: 600px) {
  .secundary-navigation-2 { width: 100vw; display: none; }
  .secundary-navigation-2 ul { min-width: 0px; }
}

@media (max-width: 600px) {
  .destaques-column { margin-left: 7px; max-width: 89%; }
  .article-body, .listas-links, .livro, .listas-body, .listas-pdf { padding-left: 10px; padding-right: 10px; }
  .footer { height: auto; position: relative; top: -20vw; padding-right: 0px; z-index: 2 !important; }
  .footer ul { padding-right: 0px; }
  .footer h1 { font-weight: 600; text-align: center; }
}

@media (max-width: 600px) {
  .footer-2 { width: 100vw; }
}

@media (max-width: 600px) {
  .footercol { width: 100vw; padding-top: 20px; }
  .footercol ul { padding-top: 10px; }
  .footercol ul li { vertical-align: top; margin-bottom: 5px; }
  .footercol ul li a { height: 40px; line-height: 100%; text-align: center !important; }
  .footercol ul li a::before { content: none !important; }
  .footercol h1 { font-size: 15px; color: rgb(0, 147, 213); }
  .direitos_reservados { width: 100%; padding-left: 2%; padding-right: 0%; }
  .direitos_reservados span { width: 100%; }
  .map { width: 100%; }
  .tabela-onde-estamos { width: 100%; }
  .view-box { float: left; width: 280px; height: 247px; margin-left: 6%; }
  .view-box-image-thumbnail img { max-height: 100%; max-width: 100%; overflow: hidden; }
  textarea { width: 100%; }
  .form-item input { width: 100%; }
  .myform { padding-left: 5px; padding-right: 5px; }
  .noticias-saibamais { left: 19%; }
  .carousel { position: relative; height: 84vw; }
  .carousel-control-prev, .carousel-control-next { display: none !important; }
  .carousel-item a:hover { text-decoration: none; }
  .carousel-bullets-div { position: relative; top: 0px; height: 0px; line-height: 0px; }
  .carousel-indicators { top: 77vw; width: 100vw; right: 0px; bottom: 10px; z-index: 15; display: flex; justify-content: center; padding-left: 0px; margin-right: 15%; margin-left: 15%; position: relative !important; left: 0px !important; }
  .carousel-indicators li { position: relative; display: block; flex: 0 1 auto; margin-right: 3px; text-indent: -999px; width: 15px !important; height: 15px !important; border-radius: 20px !important; border: 2px solid rgb(255, 255, 255) !important; margin-left: 5px !important; background-color: transparent !important; }
  .main-navigation-2 ul li ul { padding-bottom: 0px; padding-left: 0px; margin-left: 0px; width: 100vw; overflow: hidden; position: absolute; }
  .main-navigation-2 ul li ul li { padding-left: 5%; height: 50px; line-height: 50px; width: 100%; }
  .content-banner { top: -171px; }
  .content-banner .content-banner-image .cimg img { transform: translate(0%, 0%); width: 100vw; height: auto; }
  .content-banner .banner-titulo { color: white; font-size: 24px; font-family: rubik-medium; width: 70vw; line-height: 24px; letter-spacing: -0.88px; }
  .content-banner .content-banner-text .content-banner-text-2 { width: 100vw; display: table; margin: 0px auto; height: auto; padding-top: 13px; }
  .content-banner .banner-subtitulo { padding-top: 3vw; }
  .content-banner .banner-subtitulo p { font-family: rubik-light; font-size: 18px; letter-spacing: -0.18px; line-height: 18px; }
  .content-banner .banner-subtitulo span { font-family: rubik-light; font-size: 18px; letter-spacing: -0.18px; line-height: 1px; position: relative; left: -12px; }
  .ver-mais { display: none; position: relative; bottom: 16vw; text-align: center; font-size: 10px; color: white; background-color: red; font-family: rubik-medium; z-index: 2; }
  .breadcrumb-baie-2 ol li:first-child::before { content: ""; margin-left: 4vw; margin-right: 0px; }
  .baieu-page-content { padding-bottom: 0px; top: 1px; position: relative; }
  .baieu-page-content-2 { width: 100vw; position: relative; top: -22vw; left: 2vw; margin-left: 0vw; }
  .no-image-breadcrumb { position: relative; top: -40.5vw; margin-bottom: 0px; border-top: 1px solid; }
  .ib-modal-link { box-shadow: none; width: 154px; }
  .file--application-pdf a { font-size: 12px; }
  .content-banner .content-banner-text { height: 0px; }
  .view-agregadora { display: table; margin: 0px auto; position: relative; top: -160px; width: 100% !important; }
}

@media (max-width: 450px) and (min-width: 400px) {
  .destaques-image a img { width: 92vw; }
  .destaques-title { top: -44vw; }
  .destaques-body { top: -44vw; }
}

@media (max-width: 840px) {
  .pesquisar { position: absolute; right: 105px; top: 62px; }
  .pesquisar a { color: rgb(0, 46, 94) !important; }
  .pesquisar a ::after { background-image: url("/themes/custom/baieu/images/ICONS/line-separador.png"); display: inline-block; width: 1px; height: 27px; content: ""; margin-left: 10px; position: relative; top: 7px; }
  .pesquisar-azul { display: inline-block; }
  .pesquisar-branco { display: none; }
}

.context-particulares-main-navigation { background-color: rgba(54, 160, 205, 0.53); }

@media (max-width: 600px) {
  .context-particulares-main-navigation { background-color: transparent !important; }
}

.context-institucional-main-navigation { background-color: rgba(0, 46, 94, 0.53); }

@media (max-width: 600px) {
  .context-institucional-main-navigation { background-color: transparent !important; }
}

.context-empresas-main-navigation { background-color: rgba(101, 113, 116, 0.53); }

@media (max-width: 600px) {
  .context-empresas-main-navigation { background-color: transparent !important; }
}

.context-banca-investimento-main-navigation { background-color: rgba(148, 139, 117, 0.53); }

@media (max-width: 600px) {
  .context-banca-investimento-main-navigation { background-color: transparent !important; }
}

.context-particulares-view-box { background-color: rgba(54, 160, 205, 0.53) !important; }

.context-empresas-view-box { background-color: rgba(101, 113, 116, 0.53) !important; }

.context-institucional-view-box { background-color: rgba(0, 46, 94, 0.53) !important; }

.context-banca-investimento-view-box { background-color: rgba(148, 139, 117, 0.53) !important; }

.view-agregadora .view-box div { width: 100%; height: 100%; text-align: center; }

.view-agregadora .view-box div .view-box-title { position: relative; width: 100%; line-height: 100%; vertical-align: middle; }

.view-agregadora .view-box div .view-box-title a { line-height: 200px; font-size: 18px; font-family: rubik-medium; vertical-align: middle; position: relative; color: white; left: 0px; text-decoration: none; }

.view-agregadora .view-box-image-thumbnail::after { content: ""; }

@media (max-width: 900px) and (min-width: 601px) {
  .homepage-floating-title { font-size: 50px; line-height: 60px; width: 66vw; top: 9vw; }
  .homepage-floating-message { font-size: 34px; line-height: 47px; width: 60vw; top: 28vw; }
  .homepage_content-2 { width: 100vw; }
  .secundary-navigation-2 li { width: 24vw; }
  .secundary-navigation-title { left: 20px; }
  .secundary-navigation-subtitle { left: 20px; }
}

@media (max-width: 1200px) and (min-width: 901px) {
  .homepage-floating-message { position: absolute; top: 208px; width: 40vw; left: 24%; color: white; font-size: 38px; font-family: rubik-regular; line-height: 40px; }
  .homepage-floating-title { position: absolute; top: 0px; bottom: 0px; margin-top: 5%; margin-bottom: 80px; font-family: rubik-medium; font-size: 60px; color: white; left: 24%; }
}

.orgaos_sociais_content { margin-bottom: 25px; }

.orgaos_sociais_content .node div div { margin-bottom: 10px; }

.orgaos_sociais_content .node div div div { margin-bottom: 0px; }

.orgaos-sociais { height: auto; font-size: 11px; position: relative; top: 0px; }

.orgaos-sociais-view-row { height: 80px; width: 150px; border: 1px solid rgb(28, 55, 101); font-size: 11px; position: relative; top: 0px; }

.cargo { font-size: 40px; letter-spacing: 1px; margin-bottom: 20px; font-weight: 100; color: rgb(101, 113, 116); font-family: rubik-regular; }

.foto_perfil { position: relative; background-repeat: no-repeat; background-size: cover; background-position: center center; height: 238px; width: 238px; display: block; float: left; }

.banner { background-color: blue; background-image: url("/themes/custom/baieu/images/img_bolinhas.png"); background-size: cover; height: 237px; width: calc(100% - 242px); float: right; padding: 58px 0px; margin-top: 0px; }

.cargo-baieu { font-size: 28px; letter-spacing: 1px; margin-bottom: 20px; font-weight: 100; color: white; font-family: rubik-regular; padding-left: 30px; margin-top: -55px; }

.nome-span { font-size: 35px; line-height: 28px; letter-spacing: 0.8px; color: white; float: left; clear: both; padding-left: 15px; }

.name-span { font-size: 32px; line-height: 28px; letter-spacing: 0.8px; color: white; float: left; clear: both; }

.biografia { color: rgb(101, 113, 116); font-size: 24px; letter-spacing: 0.7px; line-height: 65px; border-bottom: 1px solid rgb(229, 229, 229); width: 180px; margin-bottom: 15px; font-family: rubik-regular; }

.data_eleicao { color: rgb(101, 113, 116); font-size: 12px; }

.nacionalidade { color: rgb(101, 113, 116); font-size: 12px; font-family: rubik-regular; }

.posicao { color: rgb(101, 113, 116); font-size: 12px; font-family: rubik-regular; }

.qualificacoes { color: rgb(101, 113, 116); font-size: 12px; font-family: rubik-regular; }

.experiencia { color: rgb(101, 113, 116); font-size: 12px; text-align: justify; font-family: rubik-regular; }

.orgaos_socias_content { padding-top: 0px; }

.orgaos_sociais_content-2 { width: 1070px; display: table; margin: 0px auto; }

.value { color: rgb(89, 89, 89); font-size: 12px; margin-bottom: 10px; text-align: justify; }

.foto-perfil-banner { display: block; height: 238px; }

.orgaos-sociais-page-contet { margin-top: -140px; }

.orgaos-sociais-view-row { height: 88px; width: 240px; max-width: 240px; border: 1px solid rgb(165, 200, 241); box-sizing: border-box; font-size: 11px; position: relative; top: 0px; margin-right: 10px; margin-bottom: 20px; display: inline-table; padding: 10px; margin-top: 30px; background-color: rgb(0, 46, 94); }

.orgaos-sociais-pessoas { display: inline-table; }

a { color: white; text-decoration: none; }

a :hover { text-decoration: none; }

.orgaos-sociais-tipo-cargo { display: block; color: white; font-family: rubik-regular; font-size: 12px; letter-spacing: 0.8px; text-align: center; width: 215px; margin-top: 0px; height: 18px; }

.nome-orgaos-sociais { color: white; text-align: center; font-family: rubik-regular; font-size: 14px; width: 215px; height: 5px; margin-top: 18px; padding-bottom: 40px; }

.nome-orgaos-sociais a { text-decoration: none; color: white; }

.nome-orgaos-sociais a:hover { text-decoration: none; color: white; }

th { background-color: rgb(28, 55, 101); color: white; line-height: 15px; height: 20px; vertical-align: middle; font-weight: 600; width: 10vw; min-width: 78px; text-align: center; }

td { width: 250px; max-width: 300px; height: 27px; max-height: 30px; padding: 10px; background-color: rgb(233, 236, 239); color: rgb(0, 66, 119); text-align: center; vertical-align: middle; }

.article-body table tbody tr td { padding-left: 10px; padding-top: 10px; text-align: center; background-color: rgb(233, 236, 239); vertical-align: middle; }

.article-body table tbody tr th { background-color: rgb(28, 55, 101); color: white; text-align: center; line-height: 15px; height: 20px; vertical-align: middle; font-weight: 600; width: 400px; min-width: 78px; }

:root { --blue:#007bff; --indigo:#6610f2; --purple:#6f42c1; --pink:#e83e8c; --red:#dc3545; --orange:#fd7e14; --yellow:#ffc107; --green:#28a745; --teal:#20c997; --cyan:#17a2b8; --white:#fff; --gray:#6c757d; --gray-dark:#343a40; --primary:#007bff; --secondary:#6c757d; --success:#28a745; --info:#17a2b8; --warning:#ffc107; --danger:#dc3545; --light:#f8f9fa; --dark:#343a40; --breakpoint-xs:0; --breakpoint-sm:576px; --breakpoint-md:768px; --breakpoint-lg:992px; --breakpoint-xl:1420px; --font-family-sans-serif:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; --font-family-monospace:SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace; }

*, ::before, ::after { box-sizing: border-box; }

html { font-family: sans-serif; line-height: 1.15; text-size-adjust: 100%; -webkit-tap-highlight-color: transparent; }

article, aside, dialog, figcaption, figure, footer, header, hgroup, main, nav, section { display: block; }

body { margin: 0px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"; font-size: 1rem; font-weight: 400; line-height: 1.5; color: rgb(33, 37, 41); text-align: left; background-color: rgb(255, 255, 255); }

[tabindex="-1"]:focus { outline: 0px !important; }

hr { box-sizing: content-box; height: 0px; overflow: visible; }

h1, h2, h3, h4, h5, h6 { margin-top: 0px; margin-bottom: 0.5rem; }

p { margin-top: 0px; margin-bottom: 1rem; }

abbr[title], abbr[data-original-title] { text-decoration: underline dotted; cursor: help; border-bottom: 0px; }

address { margin-bottom: 1rem; font-style: normal; line-height: inherit; }

ol, ul, dl { margin-top: 0px; margin-bottom: 1rem; }

ol ol, ul ul, ol ul, ul ol { margin-bottom: 0px; }

dt { font-weight: 700; }

dd { margin-bottom: 0.5rem; margin-left: 0px; }

blockquote { margin: 0px 0px 1rem; }

dfn { font-style: italic; }

b, strong { font-weight: bolder; }

small { font-size: 80%; }

sub, sup { position: relative; font-size: 75%; line-height: 0; vertical-align: baseline; }

sub { bottom: -0.25em; }

sup { top: -0.5em; }

a { color: rgb(0, 123, 255); text-decoration: none; background-color: transparent; }

a:hover { color: rgb(0, 86, 179); text-decoration: underline; }

a:not([href]):not([tabindex]) { color: inherit; text-decoration: none; }

a:not([href]):not([tabindex]):hover, a:not([href]):not([tabindex]):focus { color: inherit; text-decoration: none; }

a:not([href]):not([tabindex]):focus { outline: 0px; }

pre, code, kbd, samp { font-family: monospace, monospace; font-size: 1em; }

pre { margin-top: 0px; margin-bottom: 1rem; overflow: auto; }

figure { margin: 0px 0px 1rem; }

img { vertical-align: middle; border-style: none; }

svg:not(:root) { overflow: hidden; }

table { border-collapse: collapse; }

caption { padding-top: 0.75rem; padding-bottom: 0.75rem; color: rgb(108, 117, 125); text-align: left; caption-side: bottom; }

th { text-align: inherit; }

label { display: inline-block; margin-bottom: 0.5rem; }

button { border-radius: 0px; }

button:focus { outline: -webkit-focus-ring-color auto 5px; }

input, button, select, optgroup, textarea { margin: 0px; font-family: inherit; font-size: inherit; line-height: inherit; }

button, input { overflow: visible; }

button, select { text-transform: none; }

button, html [type="button"], [type="reset"], [type="submit"] { -webkit-appearance: button; }

input[type="radio"], input[type="checkbox"] { box-sizing: border-box; padding: 0px; }

input[type="date"], input[type="time"], input[type="datetime-local"], input[type="month"] { -webkit-appearance: listbox; }

textarea { overflow: auto; resize: vertical; }

fieldset { min-width: 0px; padding: 0px; margin: 0px; border: 0px; }

legend { display: block; width: 100%; max-width: 100%; padding: 0px; margin-bottom: 0.5rem; font-size: 1.5rem; line-height: inherit; color: inherit; white-space: normal; }

progress { vertical-align: baseline; }

[type="number"]::-webkit-inner-spin-button, [type="number"]::-webkit-outer-spin-button { height: auto; }

[type="search"] { outline-offset: -2px; -webkit-appearance: none; }

[type="search"]::-webkit-search-cancel-button, [type="search"]::-webkit-search-decoration { -webkit-appearance: none; }

::-webkit-file-upload-button { font: inherit; -webkit-appearance: button; }

output { display: inline-block; }

summary { display: list-item; cursor: pointer; }

template { display: none; }

[hidden] { display: none !important; }

h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 { margin-bottom: 0.5rem; font-family: inherit; font-weight: 500; line-height: 1.2; color: inherit; }

h1, .h1 { font-size: 2.5rem; }

h2, .h2 { font-size: 2rem; }

h3, .h3 { font-size: 1.75rem; }

h4, .h4 { font-size: 1.5rem; }

h5, .h5 { font-size: 1.25rem; }

h6, .h6 { font-size: 1rem; }

.lead { font-size: 1.25rem; font-weight: 300; }

.display-1 { font-size: 6rem; font-weight: 300; line-height: 1.2; }

.display-2 { font-size: 5.5rem; font-weight: 300; line-height: 1.2; }

.display-3 { font-size: 4.5rem; font-weight: 300; line-height: 1.2; }

.display-4 { font-size: 3.5rem; font-weight: 300; line-height: 1.2; }

hr { margin-top: 1rem; margin-bottom: 1rem; border-width: 1px 0px 0px; border-right-style: initial; border-bottom-style: initial; border-left-style: initial; border-right-color: initial; border-bottom-color: initial; border-left-color: initial; border-image: initial; border-top-style: solid; border-top-color: rgba(0, 0, 0, 0.1); }

small, .small { font-size: 80%; font-weight: 400; }

mark, .mark { padding: 0.2em; background-color: rgb(252, 248, 227); }

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

code, kbd, pre, samp { font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }

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

@media (min-width: 1420px) {
  .container { max-width: 1140px; }
}

.container-fluid { width: 100%; padding-right: 15px; padding-left: 15px; margin-right: auto; margin-left: auto; }

.row { display: flex; flex-wrap: wrap; margin-right: -15px; margin-left: -15px; }

.no-gutters { margin-right: 0px; margin-left: 0px; }

.no-gutters > .col, .no-gutters > [class*="col-"] { padding-right: 0px; padding-left: 0px; }

.col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col, .col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm, .col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md, .col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg, .col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl, .col-xl-auto { position: relative; width: 100%; min-height: 1px; padding-right: 15px; padding-left: 15px; }

.col { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }

.col-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }

.col-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }

.col-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }

.col-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }

.col-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }

.col-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }

.col-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }

.col-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }

.col-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }

.col-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }

.col-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }

.col-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }

.col-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }

.order-first { order: -1; }

.order-last { -webkit-box-ordinal-group: 14; order: 13; }

.order-0 { -webkit-box-ordinal-group: 1; order: 0; }

.order-1 { -webkit-box-ordinal-group: 2; order: 1; }

.order-2 { -webkit-box-ordinal-group: 3; order: 2; }

.order-3 { -webkit-box-ordinal-group: 4; order: 3; }

.order-4 { -webkit-box-ordinal-group: 5; order: 4; }

.order-5 { -webkit-box-ordinal-group: 6; order: 5; }

.order-6 { -webkit-box-ordinal-group: 7; order: 6; }

.order-7 { -webkit-box-ordinal-group: 8; order: 7; }

.order-8 { -webkit-box-ordinal-group: 9; order: 8; }

.order-9 { -webkit-box-ordinal-group: 10; order: 9; }

.order-10 { -webkit-box-ordinal-group: 11; order: 10; }

.order-11 { -webkit-box-ordinal-group: 12; order: 11; }

.order-12 { -webkit-box-ordinal-group: 13; order: 12; }

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
  .col-sm { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-sm-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-sm-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-sm-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-sm-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-sm-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-sm-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-sm-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-sm-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-sm-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-sm-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-sm-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-sm-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-sm-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-sm-first { order: -1; }
  .order-sm-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-sm-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-sm-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-sm-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-sm-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-sm-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-sm-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-sm-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-sm-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-sm-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-sm-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-sm-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-sm-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-sm-12 { -webkit-box-ordinal-group: 13; order: 12; }
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
  .col-md { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-md-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-md-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-md-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-md-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-md-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-md-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-md-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-md-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-md-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-md-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-md-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-md-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-md-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-md-first { order: -1; }
  .order-md-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-md-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-md-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-md-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-md-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-md-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-md-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-md-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-md-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-md-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-md-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-md-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-md-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-md-12 { -webkit-box-ordinal-group: 13; order: 12; }
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
  .col-lg { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-lg-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-lg-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-lg-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-lg-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-lg-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-lg-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-lg-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-lg-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-lg-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-lg-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-lg-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-lg-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-lg-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-lg-first { order: -1; }
  .order-lg-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-lg-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-lg-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-lg-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-lg-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-lg-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-lg-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-lg-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-lg-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-lg-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-lg-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-lg-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-lg-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-lg-12 { -webkit-box-ordinal-group: 13; order: 12; }
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

@media (min-width: 1420px) {
  .col-xl { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-xl-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-xl-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-xl-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-xl-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-xl-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-xl-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-xl-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-xl-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-xl-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-xl-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-xl-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-xl-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-xl-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-xl-first { order: -1; }
  .order-xl-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-xl-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-xl-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-xl-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-xl-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-xl-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-xl-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-xl-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-xl-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-xl-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-xl-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-xl-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-xl-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-xl-12 { -webkit-box-ordinal-group: 13; order: 12; }
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

.table { width: 100%; max-width: 100%; margin-bottom: 1rem; background-color: transparent; }

.table th, .table td { padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230); }

.table thead th { vertical-align: bottom; border-bottom: 2px solid rgb(222, 226, 230); }

.table tbody + tbody { border-top: 2px solid rgb(222, 226, 230); }

.table .table { background-color: rgb(255, 255, 255); }

.table-sm th, .table-sm td { padding: 0.3rem; }

.table-bordered { border: 1px solid rgb(222, 226, 230); }

.table-bordered th, .table-bordered td { border: 1px solid rgb(222, 226, 230); }

.table-bordered thead th, .table-bordered thead td { border-bottom-width: 2px; }

.table-striped tbody tr:nth-of-type(2n+1) { background-color: rgba(0, 0, 0, 0.05); }

.table-hover tbody tr:hover { background-color: rgba(0, 0, 0, 0.075); }

.table-primary, .table-primary > th, .table-primary > td { background-color: rgb(184, 218, 255); }

.table-hover .table-primary:hover { background-color: rgb(159, 205, 255); }

.table-hover .table-primary:hover > td, .table-hover .table-primary:hover > th { background-color: rgb(159, 205, 255); }

.table-secondary, .table-secondary > th, .table-secondary > td { background-color: rgb(214, 216, 219); }

.table-hover .table-secondary:hover { background-color: rgb(200, 203, 207); }

.table-hover .table-secondary:hover > td, .table-hover .table-secondary:hover > th { background-color: rgb(200, 203, 207); }

.table-success, .table-success > th, .table-success > td { background-color: rgb(195, 230, 203); }

.table-hover .table-success:hover { background-color: rgb(177, 223, 187); }

.table-hover .table-success:hover > td, .table-hover .table-success:hover > th { background-color: rgb(177, 223, 187); }

.table-info, .table-info > th, .table-info > td { background-color: rgb(190, 229, 235); }

.table-hover .table-info:hover { background-color: rgb(171, 221, 229); }

.table-hover .table-info:hover > td, .table-hover .table-info:hover > th { background-color: rgb(171, 221, 229); }

.table-warning, .table-warning > th, .table-warning > td { background-color: rgb(255, 238, 186); }

.table-hover .table-warning:hover { background-color: rgb(255, 232, 161); }

.table-hover .table-warning:hover > td, .table-hover .table-warning:hover > th { background-color: rgb(255, 232, 161); }

.table-danger, .table-danger > th, .table-danger > td { background-color: rgb(245, 198, 203); }

.table-hover .table-danger:hover { background-color: rgb(241, 176, 183); }

.table-hover .table-danger:hover > td, .table-hover .table-danger:hover > th { background-color: rgb(241, 176, 183); }

.table-light, .table-light > th, .table-light > td { background-color: rgb(253, 253, 254); }

.table-hover .table-light:hover { background-color: rgb(236, 236, 246); }

.table-hover .table-light:hover > td, .table-hover .table-light:hover > th { background-color: rgb(236, 236, 246); }

.table-dark, .table-dark > th, .table-dark > td { background-color: rgb(198, 200, 202); }

.table-hover .table-dark:hover { background-color: rgb(185, 187, 190); }

.table-hover .table-dark:hover > td, .table-hover .table-dark:hover > th { background-color: rgb(185, 187, 190); }

.table-active, .table-active > th, .table-active > td { background-color: rgba(0, 0, 0, 0.075); }

.table-hover .table-active:hover { background-color: rgba(0, 0, 0, 0.075); }

.table-hover .table-active:hover > td, .table-hover .table-active:hover > th { background-color: rgba(0, 0, 0, 0.075); }

.table .thead-dark th { color: rgb(255, 255, 255); background-color: rgb(33, 37, 41); border-color: rgb(50, 56, 62); }

.table .thead-light th { color: rgb(73, 80, 87); background-color: rgb(233, 236, 239); border-color: rgb(222, 226, 230); }

.table-dark { color: rgb(255, 255, 255); background-color: rgb(33, 37, 41); }

.table-dark th, .table-dark td, .table-dark thead th { border-color: rgb(50, 56, 62); }

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

.form-control { display: block; width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; line-height: 1.5; color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s; }

.form-control:focus { color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); border-color: rgb(128, 189, 255); outline: 0px; box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.form-control::-webkit-input-placeholder { color: rgb(108, 117, 125); opacity: 1; }

.form-control::placeholder { color: rgb(108, 117, 125); opacity: 1; }

.form-control:disabled, .form-control[readonly] { background-color: rgb(233, 236, 239); opacity: 1; }

select.form-control:not([size]):not([multiple]) { height: calc(2.25rem + 2px); }

.form-control-file, .form-control-range { display: block; width: 100%; }

.col-form-label { padding-top: calc(0.375rem + 1px); padding-bottom: calc(0.375rem + 1px); margin-bottom: 0px; font-size: inherit; line-height: 1.5; }

.col-form-label-lg { padding-top: calc(0.5rem + 1px); padding-bottom: calc(0.5rem + 1px); font-size: 1.25rem; line-height: 1.5; }

.col-form-label-sm { padding-top: calc(0.25rem + 1px); padding-bottom: calc(0.25rem + 1px); font-size: 0.875rem; line-height: 1.5; }

.form-control-plaintext { display: block; width: 100%; padding-top: 0.375rem; padding-bottom: 0.375rem; margin-bottom: 0px; line-height: 1.5; background-color: transparent; border-style: solid; border-color: transparent; border-image: initial; border-width: 1px 0px; }

.form-control-plaintext.form-control-sm, .input-group-sm > .form-control-plaintext.form-control, .input-group-sm > .input-group-prepend > .form-control-plaintext.input-group-text, .input-group-sm > .input-group-append > .form-control-plaintext.input-group-text, .input-group-sm > .input-group-prepend > .form-control-plaintext.btn, .input-group-sm > .input-group-append > .form-control-plaintext.btn, .form-control-plaintext.form-control-lg, .input-group-lg > .form-control-plaintext.form-control, .input-group-lg > .input-group-prepend > .form-control-plaintext.input-group-text, .input-group-lg > .input-group-append > .form-control-plaintext.input-group-text, .input-group-lg > .input-group-prepend > .form-control-plaintext.btn, .input-group-lg > .input-group-append > .form-control-plaintext.btn { padding-right: 0px; padding-left: 0px; }

.form-control-sm, .input-group-sm > .form-control, .input-group-sm > .input-group-prepend > .input-group-text, .input-group-sm > .input-group-append > .input-group-text, .input-group-sm > .input-group-prepend > .btn, .input-group-sm > .input-group-append > .btn { padding: 0.25rem 0.5rem; font-size: 0.875rem; line-height: 1.5; border-radius: 0.2rem; }

select.form-control-sm:not([size]):not([multiple]), .input-group-sm > select.form-control:not([size]):not([multiple]), .input-group-sm > .input-group-prepend > select.input-group-text:not([size]):not([multiple]), .input-group-sm > .input-group-append > select.input-group-text:not([size]):not([multiple]), .input-group-sm > .input-group-prepend > select.btn:not([size]):not([multiple]), .input-group-sm > .input-group-append > select.btn:not([size]):not([multiple]) { height: calc(1.8125rem + 2px); }

.form-control-lg, .input-group-lg > .form-control, .input-group-lg > .input-group-prepend > .input-group-text, .input-group-lg > .input-group-append > .input-group-text, .input-group-lg > .input-group-prepend > .btn, .input-group-lg > .input-group-append > .btn { padding: 0.5rem 1rem; font-size: 1.25rem; line-height: 1.5; border-radius: 0.3rem; }

select.form-control-lg:not([size]):not([multiple]), .input-group-lg > select.form-control:not([size]):not([multiple]), .input-group-lg > .input-group-prepend > select.input-group-text:not([size]):not([multiple]), .input-group-lg > .input-group-append > select.input-group-text:not([size]):not([multiple]), .input-group-lg > .input-group-prepend > select.btn:not([size]):not([multiple]), .input-group-lg > .input-group-append > select.btn:not([size]):not([multiple]) { height: calc(2.875rem + 2px); }

.form-group { margin-bottom: 1rem; }

.form-text { display: block; margin-top: 0.25rem; }

.form-row { display: flex; flex-wrap: wrap; margin-right: -5px; margin-left: -5px; }

.form-row > .col, .form-row > [class*="col-"] { padding-right: 5px; padding-left: 5px; }

.form-check { position: relative; display: block; padding-left: 1.25rem; }

.form-check-input { position: absolute; margin-top: 0.3rem; margin-left: -1.25rem; }

.form-check-input:disabled ~ .form-check-label { color: rgb(108, 117, 125); }

.form-check-label { margin-bottom: 0px; }

.form-check-inline { display: inline-flex; -webkit-box-align: center; align-items: center; padding-left: 0px; margin-right: 0.75rem; }

.form-check-inline .form-check-input { position: static; margin-top: 0px; margin-right: 0.3125rem; margin-left: 0px; }

.valid-feedback { display: none; width: 100%; margin-top: 0.25rem; font-size: 80%; color: rgb(40, 167, 69); }

.valid-tooltip { position: absolute; top: 100%; z-index: 5; display: none; max-width: 100%; padding: 0.5rem; margin-top: 0.1rem; font-size: 0.875rem; line-height: 1; color: rgb(255, 255, 255); background-color: rgba(40, 167, 69, 0.8); border-radius: 0.2rem; }

.was-validated .form-control:valid, .form-control.is-valid, .was-validated .custom-select:valid, .custom-select.is-valid { border-color: rgb(40, 167, 69); }

.was-validated .form-control:valid:focus, .form-control.is-valid:focus, .was-validated .custom-select:valid:focus, .custom-select.is-valid:focus { border-color: rgb(40, 167, 69); box-shadow: rgba(40, 167, 69, 0.25) 0px 0px 0px 0.2rem; }

.was-validated .form-control:valid ~ .valid-feedback, .was-validated .form-control:valid ~ .valid-tooltip, .form-control.is-valid ~ .valid-feedback, .form-control.is-valid ~ .valid-tooltip, .was-validated .custom-select:valid ~ .valid-feedback, .was-validated .custom-select:valid ~ .valid-tooltip, .custom-select.is-valid ~ .valid-feedback, .custom-select.is-valid ~ .valid-tooltip { display: block; }

.was-validated .form-check-input:valid ~ .form-check-label, .form-check-input.is-valid ~ .form-check-label { color: rgb(40, 167, 69); }

.was-validated .form-check-input:valid ~ .valid-feedback, .was-validated .form-check-input:valid ~ .valid-tooltip, .form-check-input.is-valid ~ .valid-feedback, .form-check-input.is-valid ~ .valid-tooltip { display: block; }

.was-validated .custom-control-input:valid ~ .custom-control-label, .custom-control-input.is-valid ~ .custom-control-label { color: rgb(40, 167, 69); }

.was-validated .custom-control-input:valid ~ .custom-control-label::before, .custom-control-input.is-valid ~ .custom-control-label::before { background-color: rgb(113, 221, 138); }

.was-validated .custom-control-input:valid ~ .valid-feedback, .was-validated .custom-control-input:valid ~ .valid-tooltip, .custom-control-input.is-valid ~ .valid-feedback, .custom-control-input.is-valid ~ .valid-tooltip { display: block; }

.was-validated .custom-control-input:valid:checked ~ .custom-control-label::before, .custom-control-input.is-valid:checked ~ .custom-control-label::before { background-color: rgb(52, 206, 87); }

.was-validated .custom-control-input:valid:focus ~ .custom-control-label::before, .custom-control-input.is-valid:focus ~ .custom-control-label::before { box-shadow: rgb(255, 255, 255) 0px 0px 0px 1px, rgba(40, 167, 69, 0.25) 0px 0px 0px 0.2rem; }

.was-validated .custom-file-input:valid ~ .custom-file-label, .custom-file-input.is-valid ~ .custom-file-label { border-color: rgb(40, 167, 69); }

.was-validated .custom-file-input:valid ~ .custom-file-label::before, .custom-file-input.is-valid ~ .custom-file-label::before { border-color: inherit; }

.was-validated .custom-file-input:valid ~ .valid-feedback, .was-validated .custom-file-input:valid ~ .valid-tooltip, .custom-file-input.is-valid ~ .valid-feedback, .custom-file-input.is-valid ~ .valid-tooltip { display: block; }

.was-validated .custom-file-input:valid:focus ~ .custom-file-label, .custom-file-input.is-valid:focus ~ .custom-file-label { box-shadow: rgba(40, 167, 69, 0.25) 0px 0px 0px 0.2rem; }

.invalid-feedback { display: none; width: 100%; margin-top: 0.25rem; font-size: 80%; color: rgb(220, 53, 69); }

.invalid-tooltip { position: absolute; top: 100%; z-index: 5; display: none; max-width: 100%; padding: 0.5rem; margin-top: 0.1rem; font-size: 0.875rem; line-height: 1; color: rgb(255, 255, 255); background-color: rgba(220, 53, 69, 0.8); border-radius: 0.2rem; }

.was-validated .form-control:invalid, .form-control.is-invalid, .was-validated .custom-select:invalid, .custom-select.is-invalid { border-color: rgb(220, 53, 69); }

.was-validated .form-control:invalid:focus, .form-control.is-invalid:focus, .was-validated .custom-select:invalid:focus, .custom-select.is-invalid:focus { border-color: rgb(220, 53, 69); box-shadow: rgba(220, 53, 69, 0.25) 0px 0px 0px 0.2rem; }

.was-validated .form-control:invalid ~ .invalid-feedback, .was-validated .form-control:invalid ~ .invalid-tooltip, .form-control.is-invalid ~ .invalid-feedback, .form-control.is-invalid ~ .invalid-tooltip, .was-validated .custom-select:invalid ~ .invalid-feedback, .was-validated .custom-select:invalid ~ .invalid-tooltip, .custom-select.is-invalid ~ .invalid-feedback, .custom-select.is-invalid ~ .invalid-tooltip { display: block; }

.was-validated .form-check-input:invalid ~ .form-check-label, .form-check-input.is-invalid ~ .form-check-label { color: rgb(220, 53, 69); }

.was-validated .form-check-input:invalid ~ .invalid-feedback, .was-validated .form-check-input:invalid ~ .invalid-tooltip, .form-check-input.is-invalid ~ .invalid-feedback, .form-check-input.is-invalid ~ .invalid-tooltip { display: block; }

.was-validated .custom-control-input:invalid ~ .custom-control-label, .custom-control-input.is-invalid ~ .custom-control-label { color: rgb(220, 53, 69); }

.was-validated .custom-control-input:invalid ~ .custom-control-label::before, .custom-control-input.is-invalid ~ .custom-control-label::before { background-color: rgb(239, 162, 169); }

.was-validated .custom-control-input:invalid ~ .invalid-feedback, .was-validated .custom-control-input:invalid ~ .invalid-tooltip, .custom-control-input.is-invalid ~ .invalid-feedback, .custom-control-input.is-invalid ~ .invalid-tooltip { display: block; }

.was-validated .custom-control-input:invalid:checked ~ .custom-control-label::before, .custom-control-input.is-invalid:checked ~ .custom-control-label::before { background-color: rgb(228, 96, 109); }

.was-validated .custom-control-input:invalid:focus ~ .custom-control-label::before, .custom-control-input.is-invalid:focus ~ .custom-control-label::before { box-shadow: rgb(255, 255, 255) 0px 0px 0px 1px, rgba(220, 53, 69, 0.25) 0px 0px 0px 0.2rem; }

.was-validated .custom-file-input:invalid ~ .custom-file-label, .custom-file-input.is-invalid ~ .custom-file-label { border-color: rgb(220, 53, 69); }

.was-validated .custom-file-input:invalid ~ .custom-file-label::before, .custom-file-input.is-invalid ~ .custom-file-label::before { border-color: inherit; }

.was-validated .custom-file-input:invalid ~ .invalid-feedback, .was-validated .custom-file-input:invalid ~ .invalid-tooltip, .custom-file-input.is-invalid ~ .invalid-feedback, .custom-file-input.is-invalid ~ .invalid-tooltip { display: block; }

.was-validated .custom-file-input:invalid:focus ~ .custom-file-label, .custom-file-input.is-invalid:focus ~ .custom-file-label { box-shadow: rgba(220, 53, 69, 0.25) 0px 0px 0px 0.2rem; }

.form-inline { display: flex; -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row wrap; -webkit-box-align: center; align-items: center; }

.form-inline .form-check { width: 100%; }

@media (min-width: 576px) {
  .form-inline label { display: flex; -webkit-box-align: center; align-items: center; -webkit-box-pack: center; justify-content: center; margin-bottom: 0px; }
  .form-inline .form-group { display: flex; -webkit-box-flex: 0; flex: 0 0 auto; -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row wrap; -webkit-box-align: center; align-items: center; margin-bottom: 0px; }
  .form-inline .form-control { display: inline-block; width: auto; vertical-align: middle; }
  .form-inline .form-control-plaintext { display: inline-block; }
  .form-inline .input-group { width: auto; }
  .form-inline .form-check { display: flex; -webkit-box-align: center; align-items: center; -webkit-box-pack: center; justify-content: center; width: auto; padding-left: 0px; }
  .form-inline .form-check-input { position: relative; margin-top: 0px; margin-right: 0.25rem; margin-left: 0px; }
  .form-inline .custom-control { -webkit-box-align: center; align-items: center; -webkit-box-pack: center; justify-content: center; }
  .form-inline .custom-control-label { margin-bottom: 0px; }
}

.btn { display: inline-block; font-weight: 400; text-align: center; white-space: nowrap; vertical-align: middle; user-select: none; border: 1px solid transparent; padding: 0.375rem 0.75rem; font-size: 1rem; line-height: 1.5; border-radius: 0.25rem; transition: color 0.15s ease-in-out 0s, background-color 0.15s ease-in-out 0s, border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s; }

.btn:hover, .btn:focus { text-decoration: none; }

.btn:focus, .btn.focus { outline: 0px; box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.btn.disabled, .btn:disabled { opacity: 0.65; }

.btn:not(:disabled):not(.disabled) { cursor: pointer; }

.btn:not(:disabled):not(.disabled):active, .btn:not(:disabled):not(.disabled).active { background-image: none; }

a.btn.disabled, fieldset:disabled a.btn { pointer-events: none; }

.btn-primary { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-primary:hover { color: rgb(255, 255, 255); background-color: rgb(0, 105, 217); border-color: rgb(0, 98, 204); }

.btn-primary:focus, .btn-primary.focus { box-shadow: rgba(0, 123, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-primary.disabled, .btn-primary:disabled { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-primary:not(:disabled):not(.disabled):active, .btn-primary:not(:disabled):not(.disabled).active, .show > .btn-primary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(0, 98, 204); border-color: rgb(0, 92, 191); }

.btn-primary:not(:disabled):not(.disabled):active:focus, .btn-primary:not(:disabled):not(.disabled).active:focus, .show > .btn-primary.dropdown-toggle:focus { box-shadow: rgba(0, 123, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-secondary { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-secondary:hover { color: rgb(255, 255, 255); background-color: rgb(90, 98, 104); border-color: rgb(84, 91, 98); }

.btn-secondary:focus, .btn-secondary.focus { box-shadow: rgba(108, 117, 125, 0.5) 0px 0px 0px 0.2rem; }

.btn-secondary.disabled, .btn-secondary:disabled { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-secondary:not(:disabled):not(.disabled):active, .btn-secondary:not(:disabled):not(.disabled).active, .show > .btn-secondary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(84, 91, 98); border-color: rgb(78, 85, 91); }

.btn-secondary:not(:disabled):not(.disabled):active:focus, .btn-secondary:not(:disabled):not(.disabled).active:focus, .show > .btn-secondary.dropdown-toggle:focus { box-shadow: rgba(108, 117, 125, 0.5) 0px 0px 0px 0.2rem; }

.btn-success { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-success:hover { color: rgb(255, 255, 255); background-color: rgb(33, 136, 56); border-color: rgb(30, 126, 52); }

.btn-success:focus, .btn-success.focus { box-shadow: rgba(40, 167, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-success.disabled, .btn-success:disabled { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-success:not(:disabled):not(.disabled):active, .btn-success:not(:disabled):not(.disabled).active, .show > .btn-success.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(30, 126, 52); border-color: rgb(28, 116, 48); }

.btn-success:not(:disabled):not(.disabled):active:focus, .btn-success:not(:disabled):not(.disabled).active:focus, .show > .btn-success.dropdown-toggle:focus { box-shadow: rgba(40, 167, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-info { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-info:hover { color: rgb(255, 255, 255); background-color: rgb(19, 132, 150); border-color: rgb(17, 122, 139); }

.btn-info:focus, .btn-info.focus { box-shadow: rgba(23, 162, 184, 0.5) 0px 0px 0px 0.2rem; }

.btn-info.disabled, .btn-info:disabled { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-info:not(:disabled):not(.disabled):active, .btn-info:not(:disabled):not(.disabled).active, .show > .btn-info.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(17, 122, 139); border-color: rgb(16, 112, 127); }

.btn-info:not(:disabled):not(.disabled):active:focus, .btn-info:not(:disabled):not(.disabled).active:focus, .show > .btn-info.dropdown-toggle:focus { box-shadow: rgba(23, 162, 184, 0.5) 0px 0px 0px 0.2rem; }

.btn-warning { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-warning:hover { color: rgb(33, 37, 41); background-color: rgb(224, 168, 0); border-color: rgb(211, 158, 0); }

.btn-warning:focus, .btn-warning.focus { box-shadow: rgba(255, 193, 7, 0.5) 0px 0px 0px 0.2rem; }

.btn-warning.disabled, .btn-warning:disabled { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-warning:not(:disabled):not(.disabled):active, .btn-warning:not(:disabled):not(.disabled).active, .show > .btn-warning.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(211, 158, 0); border-color: rgb(198, 149, 0); }

.btn-warning:not(:disabled):not(.disabled):active:focus, .btn-warning:not(:disabled):not(.disabled).active:focus, .show > .btn-warning.dropdown-toggle:focus { box-shadow: rgba(255, 193, 7, 0.5) 0px 0px 0px 0.2rem; }

.btn-danger { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-danger:hover { color: rgb(255, 255, 255); background-color: rgb(200, 35, 51); border-color: rgb(189, 33, 48); }

.btn-danger:focus, .btn-danger.focus { box-shadow: rgba(220, 53, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-danger.disabled, .btn-danger:disabled { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-danger:not(:disabled):not(.disabled):active, .btn-danger:not(:disabled):not(.disabled).active, .show > .btn-danger.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(189, 33, 48); border-color: rgb(178, 31, 45); }

.btn-danger:not(:disabled):not(.disabled):active:focus, .btn-danger:not(:disabled):not(.disabled).active:focus, .show > .btn-danger.dropdown-toggle:focus { box-shadow: rgba(220, 53, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-light { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-light:hover { color: rgb(33, 37, 41); background-color: rgb(226, 230, 234); border-color: rgb(218, 224, 229); }

.btn-light:focus, .btn-light.focus { box-shadow: rgba(248, 249, 250, 0.5) 0px 0px 0px 0.2rem; }

.btn-light.disabled, .btn-light:disabled { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-light:not(:disabled):not(.disabled):active, .btn-light:not(:disabled):not(.disabled).active, .show > .btn-light.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(218, 224, 229); border-color: rgb(211, 217, 223); }

.btn-light:not(:disabled):not(.disabled):active:focus, .btn-light:not(:disabled):not(.disabled).active:focus, .show > .btn-light.dropdown-toggle:focus { box-shadow: rgba(248, 249, 250, 0.5) 0px 0px 0px 0.2rem; }

.btn-dark { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-dark:hover { color: rgb(255, 255, 255); background-color: rgb(35, 39, 43); border-color: rgb(29, 33, 36); }

.btn-dark:focus, .btn-dark.focus { box-shadow: rgba(52, 58, 64, 0.5) 0px 0px 0px 0.2rem; }

.btn-dark.disabled, .btn-dark:disabled { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-dark:not(:disabled):not(.disabled):active, .btn-dark:not(:disabled):not(.disabled).active, .show > .btn-dark.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(29, 33, 36); border-color: rgb(23, 26, 29); }

.btn-dark:not(:disabled):not(.disabled):active:focus, .btn-dark:not(:disabled):not(.disabled).active:focus, .show > .btn-dark.dropdown-toggle:focus { box-shadow: rgba(52, 58, 64, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-primary { color: rgb(0, 123, 255); background-color: transparent; background-image: none; border-color: rgb(0, 123, 255); }

.btn-outline-primary:hover { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-outline-primary:focus, .btn-outline-primary.focus { box-shadow: rgba(0, 123, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-primary.disabled, .btn-outline-primary:disabled { color: rgb(0, 123, 255); background-color: transparent; }

.btn-outline-primary:not(:disabled):not(.disabled):active, .btn-outline-primary:not(:disabled):not(.disabled).active, .show > .btn-outline-primary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.btn-outline-primary:not(:disabled):not(.disabled):active:focus, .btn-outline-primary:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-primary.dropdown-toggle:focus { box-shadow: rgba(0, 123, 255, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-secondary { color: rgb(108, 117, 125); background-color: transparent; background-image: none; border-color: rgb(108, 117, 125); }

.btn-outline-secondary:hover { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-outline-secondary:focus, .btn-outline-secondary.focus { box-shadow: rgba(108, 117, 125, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-secondary.disabled, .btn-outline-secondary:disabled { color: rgb(108, 117, 125); background-color: transparent; }

.btn-outline-secondary:not(:disabled):not(.disabled):active, .btn-outline-secondary:not(:disabled):not(.disabled).active, .show > .btn-outline-secondary.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); border-color: rgb(108, 117, 125); }

.btn-outline-secondary:not(:disabled):not(.disabled):active:focus, .btn-outline-secondary:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-secondary.dropdown-toggle:focus { box-shadow: rgba(108, 117, 125, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-success { color: rgb(40, 167, 69); background-color: transparent; background-image: none; border-color: rgb(40, 167, 69); }

.btn-outline-success:hover { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-outline-success:focus, .btn-outline-success.focus { box-shadow: rgba(40, 167, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-success.disabled, .btn-outline-success:disabled { color: rgb(40, 167, 69); background-color: transparent; }

.btn-outline-success:not(:disabled):not(.disabled):active, .btn-outline-success:not(:disabled):not(.disabled).active, .show > .btn-outline-success.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); border-color: rgb(40, 167, 69); }

.btn-outline-success:not(:disabled):not(.disabled):active:focus, .btn-outline-success:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-success.dropdown-toggle:focus { box-shadow: rgba(40, 167, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-info { color: rgb(23, 162, 184); background-color: transparent; background-image: none; border-color: rgb(23, 162, 184); }

.btn-outline-info:hover { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-outline-info:focus, .btn-outline-info.focus { box-shadow: rgba(23, 162, 184, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-info.disabled, .btn-outline-info:disabled { color: rgb(23, 162, 184); background-color: transparent; }

.btn-outline-info:not(:disabled):not(.disabled):active, .btn-outline-info:not(:disabled):not(.disabled).active, .show > .btn-outline-info.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); border-color: rgb(23, 162, 184); }

.btn-outline-info:not(:disabled):not(.disabled):active:focus, .btn-outline-info:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-info.dropdown-toggle:focus { box-shadow: rgba(23, 162, 184, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-warning { color: rgb(255, 193, 7); background-color: transparent; background-image: none; border-color: rgb(255, 193, 7); }

.btn-outline-warning:hover { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-outline-warning:focus, .btn-outline-warning.focus { box-shadow: rgba(255, 193, 7, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-warning.disabled, .btn-outline-warning:disabled { color: rgb(255, 193, 7); background-color: transparent; }

.btn-outline-warning:not(:disabled):not(.disabled):active, .btn-outline-warning:not(:disabled):not(.disabled).active, .show > .btn-outline-warning.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); border-color: rgb(255, 193, 7); }

.btn-outline-warning:not(:disabled):not(.disabled):active:focus, .btn-outline-warning:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-warning.dropdown-toggle:focus { box-shadow: rgba(255, 193, 7, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-danger { color: rgb(220, 53, 69); background-color: transparent; background-image: none; border-color: rgb(220, 53, 69); }

.btn-outline-danger:hover { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-outline-danger:focus, .btn-outline-danger.focus { box-shadow: rgba(220, 53, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-danger.disabled, .btn-outline-danger:disabled { color: rgb(220, 53, 69); background-color: transparent; }

.btn-outline-danger:not(:disabled):not(.disabled):active, .btn-outline-danger:not(:disabled):not(.disabled).active, .show > .btn-outline-danger.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); border-color: rgb(220, 53, 69); }

.btn-outline-danger:not(:disabled):not(.disabled):active:focus, .btn-outline-danger:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-danger.dropdown-toggle:focus { box-shadow: rgba(220, 53, 69, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-light { color: rgb(248, 249, 250); background-color: transparent; background-image: none; border-color: rgb(248, 249, 250); }

.btn-outline-light:hover { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-outline-light:focus, .btn-outline-light.focus { box-shadow: rgba(248, 249, 250, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-light.disabled, .btn-outline-light:disabled { color: rgb(248, 249, 250); background-color: transparent; }

.btn-outline-light:not(:disabled):not(.disabled):active, .btn-outline-light:not(:disabled):not(.disabled).active, .show > .btn-outline-light.dropdown-toggle { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); border-color: rgb(248, 249, 250); }

.btn-outline-light:not(:disabled):not(.disabled):active:focus, .btn-outline-light:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-light.dropdown-toggle:focus { box-shadow: rgba(248, 249, 250, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-dark { color: rgb(52, 58, 64); background-color: transparent; background-image: none; border-color: rgb(52, 58, 64); }

.btn-outline-dark:hover { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-outline-dark:focus, .btn-outline-dark.focus { box-shadow: rgba(52, 58, 64, 0.5) 0px 0px 0px 0.2rem; }

.btn-outline-dark.disabled, .btn-outline-dark:disabled { color: rgb(52, 58, 64); background-color: transparent; }

.btn-outline-dark:not(:disabled):not(.disabled):active, .btn-outline-dark:not(:disabled):not(.disabled).active, .show > .btn-outline-dark.dropdown-toggle { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); border-color: rgb(52, 58, 64); }

.btn-outline-dark:not(:disabled):not(.disabled):active:focus, .btn-outline-dark:not(:disabled):not(.disabled).active:focus, .show > .btn-outline-dark.dropdown-toggle:focus { box-shadow: rgba(52, 58, 64, 0.5) 0px 0px 0px 0.2rem; }

.btn-link { font-weight: 400; color: rgb(0, 123, 255); background-color: transparent; }

.btn-link:hover { color: rgb(0, 86, 179); text-decoration: underline; background-color: transparent; border-color: transparent; }

.btn-link:focus, .btn-link.focus { text-decoration: underline; border-color: transparent; box-shadow: none; }

.btn-link:disabled, .btn-link.disabled { color: rgb(108, 117, 125); }

.btn-lg, .btn-group-lg > .btn { padding: 0.5rem 1rem; font-size: 1.25rem; line-height: 1.5; border-radius: 0.3rem; }

.btn-sm, .btn-group-sm > .btn { padding: 0.25rem 0.5rem; font-size: 0.875rem; line-height: 1.5; border-radius: 0.2rem; }

.btn-block { display: block; width: 100%; }

.btn-block + .btn-block { margin-top: 0.5rem; }

input[type="submit"].btn-block, input[type="reset"].btn-block, input[type="button"].btn-block { width: 100%; }

.fade { opacity: 0; transition: opacity 0.15s linear 0s; }

.fade.show { opacity: 1; }

.collapse { display: none; }

.collapse.show { display: block; }

tr.collapse.show { display: table-row; }

tbody.collapse.show { display: table-row-group; }

.collapsing { position: relative; height: 0px; overflow: hidden; transition: height 0.35s ease 0s; }

.dropup, .dropdown { position: relative; }

.dropdown-toggle::after { display: inline-block; width: 0px; height: 0px; margin-left: 0.255em; vertical-align: 0.255em; content: ""; border-width: 0.3em 0.3em 0px; border-top-style: solid; border-top-color: initial; border-right-style: solid; border-right-color: transparent; border-bottom-style: initial; border-bottom-color: initial; border-left-style: solid; border-left-color: transparent; }

.dropdown-toggle:empty::after { margin-left: 0px; }

.dropdown-menu { position: absolute; top: 100%; left: 0px; z-index: 1000; display: none; float: left; min-width: 10rem; padding: 0.5rem 0px; margin: 0.125rem 0px 0px; font-size: 1rem; color: rgb(33, 37, 41); text-align: left; list-style: none; background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgba(0, 0, 0, 0.15); border-radius: 0.25rem; }

.dropup .dropdown-menu { margin-top: 0px; margin-bottom: 0.125rem; }

.dropup .dropdown-toggle::after { display: inline-block; width: 0px; height: 0px; margin-left: 0.255em; vertical-align: 0.255em; content: ""; border-width: 0px 0.3em 0.3em; border-top-style: initial; border-top-color: initial; border-right-style: solid; border-right-color: transparent; border-bottom-style: solid; border-bottom-color: initial; border-left-style: solid; border-left-color: transparent; }

.dropup .dropdown-toggle:empty::after { margin-left: 0px; }

.dropright .dropdown-menu { margin-top: 0px; margin-left: 0.125rem; }

.dropright .dropdown-toggle::after { display: inline-block; width: 0px; height: 0px; margin-left: 0.255em; vertical-align: 0.255em; content: ""; border-top: 0.3em solid transparent; border-bottom: 0.3em solid transparent; border-left: 0.3em solid; }

.dropright .dropdown-toggle:empty::after { margin-left: 0px; }

.dropright .dropdown-toggle::after { vertical-align: 0px; }

.dropleft .dropdown-menu { margin-top: 0px; margin-right: 0.125rem; }

.dropleft .dropdown-toggle::after { display: inline-block; width: 0px; height: 0px; margin-left: 0.255em; vertical-align: 0.255em; content: ""; }

.dropleft .dropdown-toggle::after { display: none; }

.dropleft .dropdown-toggle::before { display: inline-block; width: 0px; height: 0px; margin-right: 0.255em; vertical-align: 0.255em; content: ""; border-top: 0.3em solid transparent; border-right: 0.3em solid; border-bottom: 0.3em solid transparent; }

.dropleft .dropdown-toggle:empty::after { margin-left: 0px; }

.dropleft .dropdown-toggle::before { vertical-align: 0px; }

.dropdown-divider { height: 0px; margin: 0.5rem 0px; overflow: hidden; border-top: 1px solid rgb(233, 236, 239); }

.dropdown-item { display: block; width: 100%; padding: 0.25rem 1.5rem; clear: both; font-weight: 400; color: rgb(33, 37, 41); text-align: inherit; white-space: nowrap; background-color: transparent; border: 0px; }

.dropdown-item:hover, .dropdown-item:focus { color: rgb(22, 24, 27); text-decoration: none; background-color: rgb(248, 249, 250); }

.dropdown-item.active, .dropdown-item:active { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(0, 123, 255); }

.dropdown-item.disabled, .dropdown-item:disabled { color: rgb(108, 117, 125); background-color: transparent; }

.dropdown-menu.show { display: block; }

.dropdown-header { display: block; padding: 0.5rem 1.5rem; margin-bottom: 0px; font-size: 0.875rem; color: rgb(108, 117, 125); white-space: nowrap; }

.btn-group, .btn-group-vertical { position: relative; display: inline-flex; vertical-align: middle; }

.btn-group > .btn, .btn-group-vertical > .btn { position: relative; -webkit-box-flex: 0; flex: 0 1 auto; }

.btn-group > .btn:hover, .btn-group-vertical > .btn:hover { z-index: 1; }

.btn-group > .btn:focus, .btn-group > .btn:active, .btn-group > .btn.active, .btn-group-vertical > .btn:focus, .btn-group-vertical > .btn:active, .btn-group-vertical > .btn.active { z-index: 1; }

.btn-group .btn + .btn, .btn-group .btn + .btn-group, .btn-group .btn-group + .btn, .btn-group .btn-group + .btn-group, .btn-group-vertical .btn + .btn, .btn-group-vertical .btn + .btn-group, .btn-group-vertical .btn-group + .btn, .btn-group-vertical .btn-group + .btn-group { margin-left: -1px; }

.btn-toolbar { display: flex; flex-wrap: wrap; -webkit-box-pack: start; justify-content: flex-start; }

.btn-toolbar .input-group { width: auto; }

.btn-group > .btn:first-child { margin-left: 0px; }

.btn-group > .btn:not(:last-child):not(.dropdown-toggle), .btn-group > .btn-group:not(:last-child) > .btn { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.btn-group > .btn:not(:first-child), .btn-group > .btn-group:not(:first-child) > .btn { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.dropdown-toggle-split { padding-right: 0.5625rem; padding-left: 0.5625rem; }

.dropdown-toggle-split::after { margin-left: 0px; }

.btn-sm + .dropdown-toggle-split, .btn-group-sm > .btn + .dropdown-toggle-split { padding-right: 0.375rem; padding-left: 0.375rem; }

.btn-lg + .dropdown-toggle-split, .btn-group-lg > .btn + .dropdown-toggle-split { padding-right: 0.75rem; padding-left: 0.75rem; }

.btn-group-vertical { -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; -webkit-box-align: start; align-items: flex-start; -webkit-box-pack: center; justify-content: center; }

.btn-group-vertical .btn, .btn-group-vertical .btn-group { width: 100%; }

.btn-group-vertical > .btn + .btn, .btn-group-vertical > .btn + .btn-group, .btn-group-vertical > .btn-group + .btn, .btn-group-vertical > .btn-group + .btn-group { margin-top: -1px; margin-left: 0px; }

.btn-group-vertical > .btn:not(:last-child):not(.dropdown-toggle), .btn-group-vertical > .btn-group:not(:last-child) > .btn { border-bottom-right-radius: 0px; border-bottom-left-radius: 0px; }

.btn-group-vertical > .btn:not(:first-child), .btn-group-vertical > .btn-group:not(:first-child) > .btn { border-top-left-radius: 0px; border-top-right-radius: 0px; }

.btn-group-toggle > .btn, .btn-group-toggle > .btn-group > .btn { margin-bottom: 0px; }

.btn-group-toggle > .btn input[type="radio"], .btn-group-toggle > .btn input[type="checkbox"], .btn-group-toggle > .btn-group > .btn input[type="radio"], .btn-group-toggle > .btn-group > .btn input[type="checkbox"] { position: absolute; clip: rect(0px, 0px, 0px, 0px); pointer-events: none; }

.input-group { position: relative; display: flex; flex-wrap: wrap; -webkit-box-align: stretch; align-items: stretch; width: 100%; }

.input-group > .form-control, .input-group > .custom-select, .input-group > .custom-file { position: relative; -webkit-box-flex: 1; flex: 1 1 auto; width: 1%; margin-bottom: 0px; }

.input-group > .form-control:focus, .input-group > .custom-select:focus, .input-group > .custom-file:focus { z-index: 3; }

.input-group > .form-control + .form-control, .input-group > .form-control + .custom-select, .input-group > .form-control + .custom-file, .input-group > .custom-select + .form-control, .input-group > .custom-select + .custom-select, .input-group > .custom-select + .custom-file, .input-group > .custom-file + .form-control, .input-group > .custom-file + .custom-select, .input-group > .custom-file + .custom-file { margin-left: -1px; }

.input-group > .form-control:not(:last-child), .input-group > .custom-select:not(:last-child) { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.input-group > .form-control:not(:first-child), .input-group > .custom-select:not(:first-child) { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.input-group > .custom-file { display: flex; -webkit-box-align: center; align-items: center; }

.input-group > .custom-file:not(:last-child) .custom-file-label, .input-group > .custom-file:not(:last-child) .custom-file-label::before { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.input-group > .custom-file:not(:first-child) .custom-file-label, .input-group > .custom-file:not(:first-child) .custom-file-label::before { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.input-group-prepend, .input-group-append { display: flex; }

.input-group-prepend .btn, .input-group-append .btn { position: relative; z-index: 2; }

.input-group-prepend .btn + .btn, .input-group-prepend .btn + .input-group-text, .input-group-prepend .input-group-text + .input-group-text, .input-group-prepend .input-group-text + .btn, .input-group-append .btn + .btn, .input-group-append .btn + .input-group-text, .input-group-append .input-group-text + .input-group-text, .input-group-append .input-group-text + .btn { margin-left: -1px; }

.input-group-prepend { margin-right: -1px; }

.input-group-append { margin-left: -1px; }

.input-group-text { display: flex; -webkit-box-align: center; align-items: center; padding: 0.375rem 0.75rem; margin-bottom: 0px; font-size: 1rem; font-weight: 400; line-height: 1.5; color: rgb(73, 80, 87); text-align: center; white-space: nowrap; background-color: rgb(233, 236, 239); border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; }

.input-group-text input[type="radio"], .input-group-text input[type="checkbox"] { margin-top: 0px; }

.input-group > .input-group-prepend > .btn, .input-group > .input-group-prepend > .input-group-text, .input-group > .input-group-append:not(:last-child) > .btn, .input-group > .input-group-append:not(:last-child) > .input-group-text, .input-group > .input-group-append:last-child > .btn:not(:last-child):not(.dropdown-toggle), .input-group > .input-group-append:last-child > .input-group-text:not(:last-child) { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }

.input-group > .input-group-append > .btn, .input-group > .input-group-append > .input-group-text, .input-group > .input-group-prepend:not(:first-child) > .btn, .input-group > .input-group-prepend:not(:first-child) > .input-group-text, .input-group > .input-group-prepend:first-child > .btn:not(:first-child), .input-group > .input-group-prepend:first-child > .input-group-text:not(:first-child) { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }

.custom-control { position: relative; display: block; min-height: 1.5rem; padding-left: 1.5rem; }

.custom-control-inline { display: inline-flex; margin-right: 1rem; }

.custom-control-input { position: absolute; z-index: -1; opacity: 0; }

.custom-control-input:checked ~ .custom-control-label::before { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); }

.custom-control-input:focus ~ .custom-control-label::before { box-shadow: rgb(255, 255, 255) 0px 0px 0px 1px, rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.custom-control-input:active ~ .custom-control-label::before { color: rgb(255, 255, 255); background-color: rgb(179, 215, 255); }

.custom-control-input:disabled ~ .custom-control-label { color: rgb(108, 117, 125); }

.custom-control-input:disabled ~ .custom-control-label::before { background-color: rgb(233, 236, 239); }

.custom-control-label { margin-bottom: 0px; }

.custom-control-label::before { position: absolute; top: 0.25rem; left: 0px; display: block; width: 1rem; height: 1rem; pointer-events: none; content: ""; user-select: none; background-color: rgb(222, 226, 230); }

.custom-control-label::after { position: absolute; top: 0.25rem; left: 0px; display: block; width: 1rem; height: 1rem; content: ""; background-repeat: no-repeat; background-position: center center; background-size: 50% 50%; }

.custom-checkbox .custom-control-label::before { border-radius: 0.25rem; }

.custom-checkbox .custom-control-input:checked ~ .custom-control-label::before { background-color: rgb(0, 123, 255); }

.custom-checkbox .custom-control-input:checked ~ .custom-control-label::after { background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3E%3Cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3E%3C/svg%3E"); }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::before { background-color: rgb(0, 123, 255); }

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::after { background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3E%3Cpath stroke='%23fff' d='M0 2h4'/%3E%3C/svg%3E"); }

.custom-checkbox .custom-control-input:disabled:checked ~ .custom-control-label::before { background-color: rgba(0, 123, 255, 0.5); }

.custom-checkbox .custom-control-input:disabled:indeterminate ~ .custom-control-label::before { background-color: rgba(0, 123, 255, 0.5); }

.custom-radio .custom-control-label::before { border-radius: 50%; }

.custom-radio .custom-control-input:checked ~ .custom-control-label::before { background-color: rgb(0, 123, 255); }

.custom-radio .custom-control-input:checked ~ .custom-control-label::after { background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3E%3Ccircle r='3' fill='%23fff'/%3E%3C/svg%3E"); }

.custom-radio .custom-control-input:disabled:checked ~ .custom-control-label::before { background-color: rgba(0, 123, 255, 0.5); }

.custom-select { display: inline-block; width: 100%; height: calc(2.25rem + 2px); padding: 0.375rem 1.75rem 0.375rem 0.75rem; line-height: 1.5; color: rgb(73, 80, 87); vertical-align: middle; background: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3E%3Cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3E%3C/svg%3E") right 0.75rem center / 8px 10px no-repeat rgb(255, 255, 255); border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; -webkit-appearance: none; }

.custom-select:focus { border-color: rgb(128, 189, 255); outline: 0px; box-shadow: rgba(0, 0, 0, 0.075) 0px 1px 2px inset, rgba(128, 189, 255, 0.5) 0px 0px 5px; }

.custom-select[multiple], .custom-select[size]:not([size="1"]) { height: auto; padding-right: 0.75rem; background-image: none; }

.custom-select:disabled { color: rgb(108, 117, 125); background-color: rgb(233, 236, 239); }

.custom-select-sm { height: calc(1.8125rem + 2px); padding-top: 0.375rem; padding-bottom: 0.375rem; font-size: 75%; }

.custom-select-lg { height: calc(2.875rem + 2px); padding-top: 0.375rem; padding-bottom: 0.375rem; font-size: 125%; }

.custom-file { position: relative; display: inline-block; width: 100%; height: calc(2.25rem + 2px); margin-bottom: 0px; }

.custom-file-input { position: relative; z-index: 2; width: 100%; height: calc(2.25rem + 2px); margin: 0px; opacity: 0; }

.custom-file-input:focus ~ .custom-file-control { border-color: rgb(128, 189, 255); box-shadow: rgba(0, 123, 255, 0.25) 0px 0px 0px 0.2rem; }

.custom-file-input:focus ~ .custom-file-control::before { border-color: rgb(128, 189, 255); }

.custom-file-input:lang(en) ~ .custom-file-label::after { content: "Browse"; }

.custom-file-label { position: absolute; top: 0px; right: 0px; left: 0px; z-index: 1; height: calc(2.25rem + 2px); padding: 0.375rem 0.75rem; line-height: 1.5; color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); border: 1px solid rgb(206, 212, 218); border-radius: 0.25rem; }

.custom-file-label::after { position: absolute; top: 0px; right: 0px; bottom: 0px; z-index: 3; display: block; height: calc((2.25rem + 2px) - 2px); padding: 0.375rem 0.75rem; line-height: 1.5; color: rgb(73, 80, 87); content: "Browse"; background-color: rgb(233, 236, 239); border-left: 1px solid rgb(206, 212, 218); border-radius: 0px 0.25rem 0.25rem 0px; }

.nav { display: flex; flex-wrap: wrap; padding-left: 0px; margin-bottom: 0px; list-style: none; }

.nav-link { display: block; padding: 0.5rem 1rem; }

.nav-link:hover, .nav-link:focus { text-decoration: none; }

.nav-link.disabled { color: rgb(108, 117, 125); }

.nav-tabs { border-bottom: 1px solid rgb(222, 226, 230); }

.nav-tabs .nav-item { margin-bottom: -1px; }

.nav-tabs .nav-link { border: 1px solid transparent; border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }

.nav-tabs .nav-link:hover, .nav-tabs .nav-link:focus { border-color: rgb(233, 236, 239) rgb(233, 236, 239) rgb(222, 226, 230); }

.nav-tabs .nav-link.disabled { color: rgb(108, 117, 125); background-color: transparent; border-color: transparent; }

.nav-tabs .nav-link.active, .nav-tabs .nav-item.show .nav-link { color: rgb(73, 80, 87); background-color: rgb(255, 255, 255); border-color: rgb(222, 226, 230) rgb(222, 226, 230) rgb(255, 255, 255); }

.nav-tabs .dropdown-menu { margin-top: -1px; border-top-left-radius: 0px; border-top-right-radius: 0px; }

.nav-pills .nav-link { border-radius: 0.25rem; }

.nav-pills .nav-link.active, .nav-pills .show > .nav-link { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); }

.nav-fill .nav-item { -webkit-box-flex: 1; flex: 1 1 auto; text-align: center; }

.nav-justified .nav-item { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; text-align: center; }

.tab-content > .tab-pane { display: none; }

.tab-content > .active { display: block; }

.navbar { position: relative; display: flex; flex-wrap: wrap; -webkit-box-align: center; align-items: center; -webkit-box-pack: justify; justify-content: space-between; padding: 0.5rem 1rem; }

.navbar > .container, .navbar > .container-fluid { display: flex; flex-wrap: wrap; -webkit-box-align: center; align-items: center; -webkit-box-pack: justify; justify-content: space-between; }

.navbar-brand { display: inline-block; padding-top: 0.3125rem; padding-bottom: 0.3125rem; margin-right: 1rem; font-size: 1.25rem; line-height: inherit; white-space: nowrap; }

.navbar-brand:hover, .navbar-brand:focus { text-decoration: none; }

.navbar-nav { display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; padding-left: 0px; margin-bottom: 0px; list-style: none; }

.navbar-nav .nav-link { padding-right: 0px; padding-left: 0px; }

.navbar-nav .dropdown-menu { position: static; float: none; }

.navbar-text { display: inline-block; padding-top: 0.5rem; padding-bottom: 0.5rem; }

.navbar-collapse { flex-basis: 100%; -webkit-box-flex: 1; flex-grow: 1; -webkit-box-align: center; align-items: center; }

.navbar-toggler { padding: 0.25rem 0.75rem; font-size: 1.25rem; line-height: 1; background-color: transparent; border: 1px solid transparent; border-radius: 0.25rem; }

.navbar-toggler:hover, .navbar-toggler:focus { text-decoration: none; }

.navbar-toggler:not(:disabled):not(.disabled) { cursor: pointer; }

.navbar-toggler-icon { display: inline-block; width: 1.5em; height: 1.5em; vertical-align: middle; content: ""; background: center center / 100% 100% no-repeat; }

@media (max-width: 575.98px) {
  .navbar-expand-sm > .container, .navbar-expand-sm > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 576px) {
  .navbar-expand-sm { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row nowrap; -webkit-box-pack: start; justify-content: flex-start; }
  .navbar-expand-sm .navbar-nav { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-direction: row; }
  .navbar-expand-sm .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-sm .navbar-nav .dropdown-menu-right { right: 0px; left: auto; }
  .navbar-expand-sm .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-sm > .container, .navbar-expand-sm > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-sm .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-sm .navbar-toggler { display: none; }
  .navbar-expand-sm .dropup .dropdown-menu { top: auto; bottom: 100%; }
}

@media (max-width: 767.98px) {
  .navbar-expand-md > .container, .navbar-expand-md > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 768px) {
  .navbar-expand-md { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row nowrap; -webkit-box-pack: start; justify-content: flex-start; }
  .navbar-expand-md .navbar-nav { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-direction: row; }
  .navbar-expand-md .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-md .navbar-nav .dropdown-menu-right { right: 0px; left: auto; }
  .navbar-expand-md .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-md > .container, .navbar-expand-md > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-md .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-md .navbar-toggler { display: none; }
  .navbar-expand-md .dropup .dropdown-menu { top: auto; bottom: 100%; }
}

@media (max-width: 991.98px) {
  .navbar-expand-lg > .container, .navbar-expand-lg > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 992px) {
  .navbar-expand-lg { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row nowrap; -webkit-box-pack: start; justify-content: flex-start; }
  .navbar-expand-lg .navbar-nav { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-direction: row; }
  .navbar-expand-lg .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-lg .navbar-nav .dropdown-menu-right { right: 0px; left: auto; }
  .navbar-expand-lg .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-lg > .container, .navbar-expand-lg > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-lg .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-lg .navbar-toggler { display: none; }
  .navbar-expand-lg .dropup .dropdown-menu { top: auto; bottom: 100%; }
}

@media (max-width: 1199.98px) {
  .navbar-expand-xl > .container, .navbar-expand-xl > .container-fluid { padding-right: 0px; padding-left: 0px; }
}

@media (min-width: 1420px) {
  .navbar-expand-xl { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row nowrap; -webkit-box-pack: start; justify-content: flex-start; }
  .navbar-expand-xl .navbar-nav { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-direction: row; }
  .navbar-expand-xl .navbar-nav .dropdown-menu { position: absolute; }
  .navbar-expand-xl .navbar-nav .dropdown-menu-right { right: 0px; left: auto; }
  .navbar-expand-xl .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }
  .navbar-expand-xl > .container, .navbar-expand-xl > .container-fluid { flex-wrap: nowrap; }
  .navbar-expand-xl .navbar-collapse { flex-basis: auto; display: flex !important; }
  .navbar-expand-xl .navbar-toggler { display: none; }
  .navbar-expand-xl .dropup .dropdown-menu { top: auto; bottom: 100%; }
}

.navbar-expand { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row nowrap; -webkit-box-pack: start; justify-content: flex-start; }

.navbar-expand > .container, .navbar-expand > .container-fluid { padding-right: 0px; padding-left: 0px; }

.navbar-expand .navbar-nav { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-direction: row; }

.navbar-expand .navbar-nav .dropdown-menu { position: absolute; }

.navbar-expand .navbar-nav .dropdown-menu-right { right: 0px; left: auto; }

.navbar-expand .navbar-nav .nav-link { padding-right: 0.5rem; padding-left: 0.5rem; }

.navbar-expand > .container, .navbar-expand > .container-fluid { flex-wrap: nowrap; }

.navbar-expand .navbar-collapse { flex-basis: auto; display: flex !important; }

.navbar-expand .navbar-toggler { display: none; }

.navbar-expand .dropup .dropdown-menu { top: auto; bottom: 100%; }

.navbar-light .navbar-brand { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-brand:hover, .navbar-light .navbar-brand:focus { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-nav .nav-link { color: rgba(0, 0, 0, 0.5); }

.navbar-light .navbar-nav .nav-link:hover, .navbar-light .navbar-nav .nav-link:focus { color: rgba(0, 0, 0, 0.7); }

.navbar-light .navbar-nav .nav-link.disabled { color: rgba(0, 0, 0, 0.3); }

.navbar-light .navbar-nav .show > .nav-link, .navbar-light .navbar-nav .active > .nav-link, .navbar-light .navbar-nav .nav-link.show, .navbar-light .navbar-nav .nav-link.active { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-toggler { color: rgba(0, 0, 0, 0.5); border-color: rgba(0, 0, 0, 0.1); }

.navbar-light .navbar-toggler-icon { background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E"); }

.navbar-light .navbar-text { color: rgba(0, 0, 0, 0.5); }

.navbar-light .navbar-text a { color: rgba(0, 0, 0, 0.9); }

.navbar-light .navbar-text a:hover, .navbar-light .navbar-text a:focus { color: rgba(0, 0, 0, 0.9); }

.navbar-dark .navbar-brand { color: rgb(255, 255, 255); }

.navbar-dark .navbar-brand:hover, .navbar-dark .navbar-brand:focus { color: rgb(255, 255, 255); }

.navbar-dark .navbar-nav .nav-link { color: rgba(255, 255, 255, 0.5); }

.navbar-dark .navbar-nav .nav-link:hover, .navbar-dark .navbar-nav .nav-link:focus { color: rgba(255, 255, 255, 0.75); }

.navbar-dark .navbar-nav .nav-link.disabled { color: rgba(255, 255, 255, 0.25); }

.navbar-dark .navbar-nav .show > .nav-link, .navbar-dark .navbar-nav .active > .nav-link, .navbar-dark .navbar-nav .nav-link.show, .navbar-dark .navbar-nav .nav-link.active { color: rgb(255, 255, 255); }

.navbar-dark .navbar-toggler { color: rgba(255, 255, 255, 0.5); border-color: rgba(255, 255, 255, 0.1); }

.navbar-dark .navbar-toggler-icon { background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(255, 255, 255, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E"); }

.navbar-dark .navbar-text { color: rgba(255, 255, 255, 0.5); }

.navbar-dark .navbar-text a { color: rgb(255, 255, 255); }

.navbar-dark .navbar-text a:hover, .navbar-dark .navbar-text a:focus { color: rgb(255, 255, 255); }

.card { position: relative; display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; min-width: 0px; overflow-wrap: break-word; background-color: rgb(255, 255, 255); background-clip: border-box; border: 1px solid rgba(0, 0, 0, 0.125); border-radius: 0.25rem; }

.card > hr { margin-right: 0px; margin-left: 0px; }

.card > .list-group:first-child .list-group-item:first-child { border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }

.card > .list-group:last-child .list-group-item:last-child { border-bottom-right-radius: 0.25rem; border-bottom-left-radius: 0.25rem; }

.card-body { -webkit-box-flex: 1; flex: 1 1 auto; padding: 1.25rem; }

.card-title { margin-bottom: 0.75rem; }

.card-subtitle { margin-top: -0.375rem; margin-bottom: 0px; }

.card-text:last-child { margin-bottom: 0px; }

.card-link:hover { text-decoration: none; }

.card-link + .card-link { margin-left: 1.25rem; }

.card-header { padding: 0.75rem 1.25rem; margin-bottom: 0px; background-color: rgba(0, 0, 0, 0.03); border-bottom: 1px solid rgba(0, 0, 0, 0.125); }

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

.card-deck { display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; }

.card-deck .card { margin-bottom: 15px; }

@media (min-width: 576px) {
  .card-deck { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row wrap; margin-right: -15px; margin-left: -15px; }
  .card-deck .card { display: flex; -webkit-box-flex: 1; flex: 1 0 0%; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; margin-right: 15px; margin-bottom: 0px; margin-left: 15px; }
}

.card-group { display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; }

.card-group > .card { margin-bottom: 15px; }

@media (min-width: 576px) {
  .card-group { -webkit-box-orient: horizontal; -webkit-box-direction: normal; flex-flow: row wrap; }
  .card-group > .card { -webkit-box-flex: 1; flex: 1 0 0%; margin-bottom: 0px; }
  .card-group > .card + .card { margin-left: 0px; border-left: 0px; }
  .card-group > .card:first-child { border-top-right-radius: 0px; border-bottom-right-radius: 0px; }
  .card-group > .card:first-child .card-img-top, .card-group > .card:first-child .card-header { border-top-right-radius: 0px; }
  .card-group > .card:first-child .card-img-bottom, .card-group > .card:first-child .card-footer { border-bottom-right-radius: 0px; }
  .card-group > .card:last-child { border-top-left-radius: 0px; border-bottom-left-radius: 0px; }
  .card-group > .card:last-child .card-img-top, .card-group > .card:last-child .card-header { border-top-left-radius: 0px; }
  .card-group > .card:last-child .card-img-bottom, .card-group > .card:last-child .card-footer { border-bottom-left-radius: 0px; }
  .card-group > .card:only-child { border-radius: 0.25rem; }
  .card-group > .card:only-child .card-img-top, .card-group > .card:only-child .card-header { border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }
  .card-group > .card:only-child .card-img-bottom, .card-group > .card:only-child .card-footer { border-bottom-right-radius: 0.25rem; border-bottom-left-radius: 0.25rem; }
  .card-group > .card:not(:first-child):not(:last-child):not(:only-child) { border-radius: 0px; }
  .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-img-top, .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-img-bottom, .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-header, .card-group > .card:not(:first-child):not(:last-child):not(:only-child) .card-footer { border-radius: 0px; }
}

.card-columns .card { margin-bottom: 0.75rem; }

@media (min-width: 576px) {
  .card-columns { column-count: 3; column-gap: 1.25rem; }
  .card-columns .card { display: inline-block; width: 100%; }
}

.breadcrumb { display: flex; flex-wrap: wrap; padding: 0.75rem 1rem; margin-bottom: 1rem; list-style: none; background-color: rgb(233, 236, 239); border-radius: 0.25rem; }

.breadcrumb-item + .breadcrumb-item::before { display: inline-block; padding-right: 0.5rem; padding-left: 0.5rem; color: rgb(108, 117, 125); content: "/"; }

.breadcrumb-item + .breadcrumb-item:hover::before { text-decoration: underline; }

.breadcrumb-item + .breadcrumb-item:hover::before { text-decoration: none; }

.breadcrumb-item.active { color: rgb(108, 117, 125); }

.pagination { display: flex; padding-left: 0px; list-style: none; border-radius: 0.25rem; }

.page-link { position: relative; display: block; padding: 0.5rem 0.75rem; margin-left: -1px; line-height: 1.25; color: rgb(0, 123, 255); background-color: rgb(255, 255, 255); border: 1px solid rgb(222, 226, 230); }

.page-link:hover { color: rgb(0, 86, 179); text-decoration: none; background-color: rgb(233, 236, 239); border-color: rgb(222, 226, 230); }

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

.badge:empty { display: none; }

.btn .badge { position: relative; top: -1px; }

.badge-pill { padding-right: 0.6em; padding-left: 0.6em; border-radius: 10rem; }

.badge-primary { color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); }

.badge-primary[href]:hover, .badge-primary[href]:focus { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(0, 98, 204); }

.badge-secondary { color: rgb(255, 255, 255); background-color: rgb(108, 117, 125); }

.badge-secondary[href]:hover, .badge-secondary[href]:focus { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(84, 91, 98); }

.badge-success { color: rgb(255, 255, 255); background-color: rgb(40, 167, 69); }

.badge-success[href]:hover, .badge-success[href]:focus { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(30, 126, 52); }

.badge-info { color: rgb(255, 255, 255); background-color: rgb(23, 162, 184); }

.badge-info[href]:hover, .badge-info[href]:focus { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(17, 122, 139); }

.badge-warning { color: rgb(33, 37, 41); background-color: rgb(255, 193, 7); }

.badge-warning[href]:hover, .badge-warning[href]:focus { color: rgb(33, 37, 41); text-decoration: none; background-color: rgb(211, 158, 0); }

.badge-danger { color: rgb(255, 255, 255); background-color: rgb(220, 53, 69); }

.badge-danger[href]:hover, .badge-danger[href]:focus { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(189, 33, 48); }

.badge-light { color: rgb(33, 37, 41); background-color: rgb(248, 249, 250); }

.badge-light[href]:hover, .badge-light[href]:focus { color: rgb(33, 37, 41); text-decoration: none; background-color: rgb(218, 224, 229); }

.badge-dark { color: rgb(255, 255, 255); background-color: rgb(52, 58, 64); }

.badge-dark[href]:hover, .badge-dark[href]:focus { color: rgb(255, 255, 255); text-decoration: none; background-color: rgb(29, 33, 36); }

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

.progress-bar { display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; -webkit-box-pack: center; justify-content: center; color: rgb(255, 255, 255); text-align: center; background-color: rgb(0, 123, 255); transition: width 0.6s ease 0s; }

.progress-bar-striped { background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent); background-size: 1rem 1rem; }

.progress-bar-animated { animation: 1s linear 0s infinite normal none running progress-bar-stripes; }

.media { display: flex; -webkit-box-align: start; align-items: flex-start; }

.media-body { -webkit-box-flex: 1; flex: 1 1 0%; }

.list-group { display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; padding-left: 0px; margin-bottom: 0px; }

.list-group-item-action { width: 100%; color: rgb(73, 80, 87); text-align: inherit; }

.list-group-item-action:hover, .list-group-item-action:focus { color: rgb(73, 80, 87); text-decoration: none; background-color: rgb(248, 249, 250); }

.list-group-item-action:active { color: rgb(33, 37, 41); background-color: rgb(233, 236, 239); }

.list-group-item { position: relative; display: block; padding: 0.75rem 1.25rem; margin-bottom: -1px; background-color: rgb(255, 255, 255); border: 1px solid rgba(0, 0, 0, 0.125); }

.list-group-item:first-child { border-top-left-radius: 0.25rem; border-top-right-radius: 0.25rem; }

.list-group-item:last-child { margin-bottom: 0px; border-bottom-right-radius: 0.25rem; border-bottom-left-radius: 0.25rem; }

.list-group-item:hover, .list-group-item:focus { z-index: 1; text-decoration: none; }

.list-group-item.disabled, .list-group-item:disabled { color: rgb(108, 117, 125); background-color: rgb(255, 255, 255); }

.list-group-item.active { z-index: 2; color: rgb(255, 255, 255); background-color: rgb(0, 123, 255); border-color: rgb(0, 123, 255); }

.list-group-flush .list-group-item { border-right: 0px; border-left: 0px; border-radius: 0px; }

.list-group-flush:first-child .list-group-item:first-child { border-top: 0px; }

.list-group-flush:last-child .list-group-item:last-child { border-bottom: 0px; }

.list-group-item-primary { color: rgb(0, 64, 133); background-color: rgb(184, 218, 255); }

.list-group-item-primary.list-group-item-action:hover, .list-group-item-primary.list-group-item-action:focus { color: rgb(0, 64, 133); background-color: rgb(159, 205, 255); }

.list-group-item-primary.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(0, 64, 133); border-color: rgb(0, 64, 133); }

.list-group-item-secondary { color: rgb(56, 61, 65); background-color: rgb(214, 216, 219); }

.list-group-item-secondary.list-group-item-action:hover, .list-group-item-secondary.list-group-item-action:focus { color: rgb(56, 61, 65); background-color: rgb(200, 203, 207); }

.list-group-item-secondary.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(56, 61, 65); border-color: rgb(56, 61, 65); }

.list-group-item-success { color: rgb(21, 87, 36); background-color: rgb(195, 230, 203); }

.list-group-item-success.list-group-item-action:hover, .list-group-item-success.list-group-item-action:focus { color: rgb(21, 87, 36); background-color: rgb(177, 223, 187); }

.list-group-item-success.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(21, 87, 36); border-color: rgb(21, 87, 36); }

.list-group-item-info { color: rgb(12, 84, 96); background-color: rgb(190, 229, 235); }

.list-group-item-info.list-group-item-action:hover, .list-group-item-info.list-group-item-action:focus { color: rgb(12, 84, 96); background-color: rgb(171, 221, 229); }

.list-group-item-info.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(12, 84, 96); border-color: rgb(12, 84, 96); }

.list-group-item-warning { color: rgb(133, 100, 4); background-color: rgb(255, 238, 186); }

.list-group-item-warning.list-group-item-action:hover, .list-group-item-warning.list-group-item-action:focus { color: rgb(133, 100, 4); background-color: rgb(255, 232, 161); }

.list-group-item-warning.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(133, 100, 4); border-color: rgb(133, 100, 4); }

.list-group-item-danger { color: rgb(114, 28, 36); background-color: rgb(245, 198, 203); }

.list-group-item-danger.list-group-item-action:hover, .list-group-item-danger.list-group-item-action:focus { color: rgb(114, 28, 36); background-color: rgb(241, 176, 183); }

.list-group-item-danger.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(114, 28, 36); border-color: rgb(114, 28, 36); }

.list-group-item-light { color: rgb(129, 129, 130); background-color: rgb(253, 253, 254); }

.list-group-item-light.list-group-item-action:hover, .list-group-item-light.list-group-item-action:focus { color: rgb(129, 129, 130); background-color: rgb(236, 236, 246); }

.list-group-item-light.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(129, 129, 130); border-color: rgb(129, 129, 130); }

.list-group-item-dark { color: rgb(27, 30, 33); background-color: rgb(198, 200, 202); }

.list-group-item-dark.list-group-item-action:hover, .list-group-item-dark.list-group-item-action:focus { color: rgb(27, 30, 33); background-color: rgb(185, 187, 190); }

.list-group-item-dark.list-group-item-action.active { color: rgb(255, 255, 255); background-color: rgb(27, 30, 33); border-color: rgb(27, 30, 33); }

.close { float: right; font-size: 1.5rem; font-weight: 700; line-height: 1; color: rgb(0, 0, 0); text-shadow: rgb(255, 255, 255) 0px 1px 0px; opacity: 0.5; }

.close:hover, .close:focus { color: rgb(0, 0, 0); text-decoration: none; opacity: 0.75; }

.close:not(:disabled):not(.disabled) { cursor: pointer; }

button.close { padding: 0px; background-color: transparent; border: 0px; -webkit-appearance: none; }

.modal-open { overflow: hidden; }

.modal { position: fixed; top: 0px; right: 0px; bottom: 0px; left: 0px; z-index: 1050; display: none; overflow: hidden; outline: 0px; }

.modal-open .modal { overflow: hidden auto; }

.modal-dialog { position: relative; width: auto; margin: 0.5rem; pointer-events: none; }

.modal.fade .modal-dialog { transition: transform 0.3s ease-out 0s, -webkit-transform 0.3s ease-out 0s; transform: translate(0px, -25%); }

.modal.show .modal-dialog { transform: translate(0px, 0px); }

.modal-dialog-centered { display: flex; -webkit-box-align: center; align-items: center; min-height: calc(100% - 1rem); }

.modal-content { position: relative; display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; flex-direction: column; width: 100%; pointer-events: auto; background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 0.3rem; outline: 0px; }

.modal-backdrop { position: fixed; top: 0px; right: 0px; bottom: 0px; left: 0px; z-index: 1040; background-color: rgb(0, 0, 0); }

.modal-backdrop.fade { opacity: 0; }

.modal-backdrop.show { opacity: 0.5; }

.modal-header { display: flex; -webkit-box-align: start; align-items: flex-start; -webkit-box-pack: justify; justify-content: space-between; padding: 1rem; border-bottom: 1px solid rgb(233, 236, 239); border-top-left-radius: 0.3rem; border-top-right-radius: 0.3rem; }

.modal-header .close { padding: 1rem; margin: -1rem -1rem -1rem auto; }

.modal-title { margin-bottom: 0px; line-height: 1.5; }

.modal-body { position: relative; -webkit-box-flex: 1; flex: 1 1 auto; padding: 1rem; }

.modal-footer { display: flex; -webkit-box-align: center; align-items: center; -webkit-box-pack: end; justify-content: flex-end; padding: 1rem; border-top: 1px solid rgb(233, 236, 239); }

.modal-footer > :not(:first-child) { margin-left: 0.25rem; }

.modal-footer > :not(:last-child) { margin-right: 0.25rem; }

.modal-scrollbar-measure { position: absolute; top: -9999px; width: 50px; height: 50px; overflow: scroll; }

@media (min-width: 576px) {
  .modal-dialog { max-width: 500px; margin: 1.75rem auto; }
  .modal-dialog-centered { min-height: calc(100% - 3.5rem); }
  .modal-sm { max-width: 300px; }
}

@media (min-width: 992px) {
  .modal-lg { max-width: 800px; }
}

.tooltip { position: absolute; z-index: 1070; display: block; margin: 0px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"; font-style: normal; font-weight: 400; line-height: 1.5; text-align: start; text-decoration: none; text-shadow: none; text-transform: none; letter-spacing: normal; word-break: normal; word-spacing: normal; white-space: normal; line-break: auto; font-size: 0.875rem; overflow-wrap: break-word; opacity: 0; }

.tooltip.show { opacity: 0.9; }

.tooltip .arrow { position: absolute; display: block; width: 0.8rem; height: 0.4rem; }

.tooltip .arrow::before { position: absolute; content: ""; border-color: transparent; border-style: solid; }

.bs-tooltip-top, .bs-tooltip-auto[x-placement^="top"] { padding: 0.4rem 0px; }

.bs-tooltip-top .arrow, .bs-tooltip-auto[x-placement^="top"] .arrow { bottom: 0px; }

.bs-tooltip-top .arrow::before, .bs-tooltip-auto[x-placement^="top"] .arrow::before { top: 0px; border-width: 0.4rem 0.4rem 0px; border-top-color: rgb(0, 0, 0); }

.bs-tooltip-right, .bs-tooltip-auto[x-placement^="right"] { padding: 0px 0.4rem; }

.bs-tooltip-right .arrow, .bs-tooltip-auto[x-placement^="right"] .arrow { left: 0px; width: 0.4rem; height: 0.8rem; }

.bs-tooltip-right .arrow::before, .bs-tooltip-auto[x-placement^="right"] .arrow::before { right: 0px; border-width: 0.4rem 0.4rem 0.4rem 0px; border-right-color: rgb(0, 0, 0); }

.bs-tooltip-bottom, .bs-tooltip-auto[x-placement^="bottom"] { padding: 0.4rem 0px; }

.bs-tooltip-bottom .arrow, .bs-tooltip-auto[x-placement^="bottom"] .arrow { top: 0px; }

.bs-tooltip-bottom .arrow::before, .bs-tooltip-auto[x-placement^="bottom"] .arrow::before { bottom: 0px; border-width: 0px 0.4rem 0.4rem; border-bottom-color: rgb(0, 0, 0); }

.bs-tooltip-left, .bs-tooltip-auto[x-placement^="left"] { padding: 0px 0.4rem; }

.bs-tooltip-left .arrow, .bs-tooltip-auto[x-placement^="left"] .arrow { right: 0px; width: 0.4rem; height: 0.8rem; }

.bs-tooltip-left .arrow::before, .bs-tooltip-auto[x-placement^="left"] .arrow::before { left: 0px; border-width: 0.4rem 0px 0.4rem 0.4rem; border-left-color: rgb(0, 0, 0); }

.tooltip-inner { max-width: 200px; padding: 0.25rem 0.5rem; color: rgb(255, 255, 255); text-align: center; background-color: rgb(0, 0, 0); border-radius: 0.25rem; }

.popover { position: absolute; top: 0px; left: 0px; z-index: 1060; display: block; max-width: 276px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"; font-style: normal; font-weight: 400; line-height: 1.5; text-align: start; text-decoration: none; text-shadow: none; text-transform: none; letter-spacing: normal; word-break: normal; word-spacing: normal; white-space: normal; line-break: auto; font-size: 0.875rem; overflow-wrap: break-word; background-color: rgb(255, 255, 255); background-clip: padding-box; border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 0.3rem; }

.popover .arrow { position: absolute; display: block; width: 1rem; height: 0.5rem; margin: 0px 0.3rem; }

.popover .arrow::before, .popover .arrow::after { position: absolute; display: block; content: ""; border-color: transparent; border-style: solid; }

.bs-popover-top, .bs-popover-auto[x-placement^="top"] { margin-bottom: 0.5rem; }

.bs-popover-top .arrow, .bs-popover-auto[x-placement^="top"] .arrow { bottom: calc((0.5rem + 1px) * -1); }

.bs-popover-top .arrow::before, .bs-popover-auto[x-placement^="top"] .arrow::before, .bs-popover-top .arrow::after, .bs-popover-auto[x-placement^="top"] .arrow::after { border-width: 0.5rem 0.5rem 0px; }

.bs-popover-top .arrow::before, .bs-popover-auto[x-placement^="top"] .arrow::before { bottom: 0px; border-top-color: rgba(0, 0, 0, 0.25); }

.bs-popover-top .arrow::after, .bs-popover-auto[x-placement^="top"] .arrow::after { bottom: 1px; border-top-color: rgb(255, 255, 255); }

.bs-popover-right, .bs-popover-auto[x-placement^="right"] { margin-left: 0.5rem; }

.bs-popover-right .arrow, .bs-popover-auto[x-placement^="right"] .arrow { left: calc((0.5rem + 1px) * -1); width: 0.5rem; height: 1rem; margin: 0.3rem 0px; }

.bs-popover-right .arrow::before, .bs-popover-auto[x-placement^="right"] .arrow::before, .bs-popover-right .arrow::after, .bs-popover-auto[x-placement^="right"] .arrow::after { border-width: 0.5rem 0.5rem 0.5rem 0px; }

.bs-popover-right .arrow::before, .bs-popover-auto[x-placement^="right"] .arrow::before { left: 0px; border-right-color: rgba(0, 0, 0, 0.25); }

.bs-popover-right .arrow::after, .bs-popover-auto[x-placement^="right"] .arrow::after { left: 1px; border-right-color: rgb(255, 255, 255); }

.bs-popover-bottom, .bs-popover-auto[x-placement^="bottom"] { margin-top: 0.5rem; }

.bs-popover-bottom .arrow, .bs-popover-auto[x-placement^="bottom"] .arrow { top: calc((0.5rem + 1px) * -1); }

.bs-popover-bottom .arrow::before, .bs-popover-auto[x-placement^="bottom"] .arrow::before, .bs-popover-bottom .arrow::after, .bs-popover-auto[x-placement^="bottom"] .arrow::after { border-width: 0px 0.5rem 0.5rem; }

.bs-popover-bottom .arrow::before, .bs-popover-auto[x-placement^="bottom"] .arrow::before { top: 0px; border-bottom-color: rgba(0, 0, 0, 0.25); }

.bs-popover-bottom .arrow::after, .bs-popover-auto[x-placement^="bottom"] .arrow::after { top: 1px; border-bottom-color: rgb(255, 255, 255); }

.bs-popover-bottom .popover-header::before, .bs-popover-auto[x-placement^="bottom"] .popover-header::before { position: absolute; top: 0px; left: 50%; display: block; width: 1rem; margin-left: -0.5rem; content: ""; border-bottom: 1px solid rgb(247, 247, 247); }

.bs-popover-left, .bs-popover-auto[x-placement^="left"] { margin-right: 0.5rem; }

.bs-popover-left .arrow, .bs-popover-auto[x-placement^="left"] .arrow { right: calc((0.5rem + 1px) * -1); width: 0.5rem; height: 1rem; margin: 0.3rem 0px; }

.bs-popover-left .arrow::before, .bs-popover-auto[x-placement^="left"] .arrow::before, .bs-popover-left .arrow::after, .bs-popover-auto[x-placement^="left"] .arrow::after { border-width: 0.5rem 0px 0.5rem 0.5rem; }

.bs-popover-left .arrow::before, .bs-popover-auto[x-placement^="left"] .arrow::before { right: 0px; border-left-color: rgba(0, 0, 0, 0.25); }

.bs-popover-left .arrow::after, .bs-popover-auto[x-placement^="left"] .arrow::after { right: 1px; border-left-color: rgb(255, 255, 255); }

.popover-header { padding: 0.5rem 0.75rem; margin-bottom: 0px; font-size: 1rem; color: inherit; background-color: rgb(247, 247, 247); border-bottom: 1px solid rgb(235, 235, 235); border-top-left-radius: calc(0.3rem - 1px); border-top-right-radius: calc(0.3rem - 1px); }

.popover-header:empty { display: none; }

.popover-body { padding: 0.5rem 0.75rem; color: rgb(33, 37, 41); }

.carousel { position: relative; }

.carousel-inner { position: relative; width: 100%; overflow: hidden; }

.carousel-item { position: relative; display: none; -webkit-box-align: center; align-items: center; width: 100%; transition: transform 0.6s ease 0s, -webkit-transform 0.6s ease 0s; backface-visibility: hidden; perspective: 1000px; }

.carousel-item.active, .carousel-item-next, .carousel-item-prev { display: block; }

.carousel-item-next, .carousel-item-prev { position: absolute; top: 0px; }

.carousel-item-next.carousel-item-left, .carousel-item-prev.carousel-item-right { transform: translateX(0px); }

@supports (-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d) {
  .carousel-item-next.carousel-item-left, .carousel-item-prev.carousel-item-right { transform: translate3d(0px, 0px, 0px); }
}

.carousel-item-next, .active.carousel-item-right { transform: translateX(100%); }

@supports (-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d) {
  .carousel-item-next, .active.carousel-item-right { transform: translate3d(100%, 0px, 0px); }
}

.carousel-item-prev, .active.carousel-item-left { transform: translateX(-100%); }

@supports (-webkit-transform-style:preserve-3d) or (transform-style:preserve-3d) {
  .carousel-item-prev, .active.carousel-item-left { transform: translate3d(-100%, 0px, 0px); }
}

.carousel-control-prev, .carousel-control-next { position: absolute; top: 0px; bottom: 0px; display: flex; -webkit-box-align: center; align-items: center; -webkit-box-pack: center; justify-content: center; width: 15%; color: rgb(255, 255, 255); text-align: center; opacity: 0.5; }

.carousel-control-prev:hover, .carousel-control-prev:focus, .carousel-control-next:hover, .carousel-control-next:focus { color: rgb(255, 255, 255); text-decoration: none; outline: 0px; opacity: 0.9; }

.carousel-control-prev { left: 0px; }

.carousel-control-next { right: 0px; }

.carousel-control-prev-icon, .carousel-control-next-icon { display: inline-block; width: 20px; height: 20px; background: center center / 100% 100% no-repeat transparent; }

.carousel-control-prev-icon { background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E"); }

.carousel-control-next-icon { background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23fff' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E"); }

.carousel-indicators { position: absolute; right: 0px; bottom: 10px; left: 0px; z-index: 15; display: flex; -webkit-box-pack: center; justify-content: center; padding-left: 0px; margin-right: 15%; margin-left: 15%; list-style: none; }

.carousel-indicators li { position: relative; -webkit-box-flex: 0; flex: 0 1 auto; width: 30px; height: 3px; margin-right: 3px; margin-left: 3px; text-indent: -999px; background-color: rgba(255, 255, 255, 0.5); }

.carousel-indicators li::before { position: absolute; top: -10px; left: 0px; display: inline-block; width: 100%; height: 10px; content: ""; }

.carousel-indicators li::after { position: absolute; bottom: -10px; left: 0px; display: inline-block; width: 100%; height: 10px; content: ""; }

.carousel-indicators .active { background-color: rgb(255, 255, 255); }

.carousel-caption { position: absolute; right: 15%; bottom: 20px; left: 15%; z-index: 10; padding-top: 20px; padding-bottom: 20px; color: rgb(255, 255, 255); text-align: center; }

.align-baseline { vertical-align: baseline !important; }

.align-top { vertical-align: top !important; }

.align-middle { vertical-align: middle !important; }

.align-bottom { vertical-align: bottom !important; }

.align-text-bottom { vertical-align: text-bottom !important; }

.align-text-top { vertical-align: text-top !important; }

.bg-primary { background-color: rgb(0, 123, 255) !important; }

a.bg-primary:hover, a.bg-primary:focus, button.bg-primary:hover, button.bg-primary:focus { background-color: rgb(0, 98, 204) !important; }

.bg-secondary { background-color: rgb(108, 117, 125) !important; }

a.bg-secondary:hover, a.bg-secondary:focus, button.bg-secondary:hover, button.bg-secondary:focus { background-color: rgb(84, 91, 98) !important; }

.bg-success { background-color: rgb(40, 167, 69) !important; }

a.bg-success:hover, a.bg-success:focus, button.bg-success:hover, button.bg-success:focus { background-color: rgb(30, 126, 52) !important; }

.bg-info { background-color: rgb(23, 162, 184) !important; }

a.bg-info:hover, a.bg-info:focus, button.bg-info:hover, button.bg-info:focus { background-color: rgb(17, 122, 139) !important; }

.bg-warning { background-color: rgb(255, 193, 7) !important; }

a.bg-warning:hover, a.bg-warning:focus, button.bg-warning:hover, button.bg-warning:focus { background-color: rgb(211, 158, 0) !important; }

.bg-danger { background-color: rgb(220, 53, 69) !important; }

a.bg-danger:hover, a.bg-danger:focus, button.bg-danger:hover, button.bg-danger:focus { background-color: rgb(189, 33, 48) !important; }

.bg-light { background-color: rgb(248, 249, 250) !important; }

a.bg-light:hover, a.bg-light:focus, button.bg-light:hover, button.bg-light:focus { background-color: rgb(218, 224, 229) !important; }

.bg-dark { background-color: rgb(52, 58, 64) !important; }

a.bg-dark:hover, a.bg-dark:focus, button.bg-dark:hover, button.bg-dark:focus { background-color: rgb(29, 33, 36) !important; }

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

@media (min-width: 1420px) {
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

.embed-responsive .embed-responsive-item, .embed-responsive iframe, .embed-responsive embed, .embed-responsive object, .embed-responsive video { position: absolute; top: 0px; bottom: 0px; left: 0px; width: 100%; height: 100%; border: 0px; }

.embed-responsive-21by9::before { padding-top: 42.8571%; }

.embed-responsive-16by9::before { padding-top: 56.25%; }

.embed-responsive-4by3::before { padding-top: 75%; }

.embed-responsive-1by1::before { padding-top: 100%; }

.flex-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }

.flex-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }

.flex-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }

.flex-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }

.flex-wrap { flex-wrap: wrap !important; }

.flex-nowrap { flex-wrap: nowrap !important; }

.flex-wrap-reverse { flex-wrap: wrap-reverse !important; }

.justify-content-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }

.justify-content-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }

.justify-content-center { -webkit-box-pack: center !important; justify-content: center !important; }

.justify-content-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }

.justify-content-around { justify-content: space-around !important; }

.align-items-start { -webkit-box-align: start !important; align-items: flex-start !important; }

.align-items-end { -webkit-box-align: end !important; align-items: flex-end !important; }

.align-items-center { -webkit-box-align: center !important; align-items: center !important; }

.align-items-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }

.align-items-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }

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
  .flex-sm-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-sm-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-sm-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-sm-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-sm-wrap { flex-wrap: wrap !important; }
  .flex-sm-nowrap { flex-wrap: nowrap !important; }
  .flex-sm-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-sm-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-sm-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-sm-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-sm-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-sm-around { justify-content: space-around !important; }
  .align-items-sm-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-sm-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-sm-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-sm-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-sm-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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
  .flex-md-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-md-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-md-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-md-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-md-wrap { flex-wrap: wrap !important; }
  .flex-md-nowrap { flex-wrap: nowrap !important; }
  .flex-md-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-md-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-md-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-md-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-md-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-md-around { justify-content: space-around !important; }
  .align-items-md-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-md-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-md-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-md-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-md-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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
  .flex-lg-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-lg-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-lg-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-lg-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-lg-wrap { flex-wrap: wrap !important; }
  .flex-lg-nowrap { flex-wrap: nowrap !important; }
  .flex-lg-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-lg-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-lg-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-lg-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-lg-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-lg-around { justify-content: space-around !important; }
  .align-items-lg-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-lg-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-lg-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-lg-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-lg-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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

@media (min-width: 1420px) {
  .flex-xl-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-xl-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-xl-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-xl-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-xl-wrap { flex-wrap: wrap !important; }
  .flex-xl-nowrap { flex-wrap: nowrap !important; }
  .flex-xl-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-xl-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-xl-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-xl-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-xl-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-xl-around { justify-content: space-around !important; }
  .align-items-xl-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-xl-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-xl-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-xl-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-xl-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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

@media (min-width: 1420px) {
  .float-xl-left { float: left !important; }
  .float-xl-right { float: right !important; }
  .float-xl-none { float: none !important; }
}

.position-static { position: static !important; }

.position-relative { position: relative !important; }

.position-absolute { position: absolute !important; }

.position-fixed { position: fixed !important; }

.position-sticky { position: sticky !important; }

.fixed-top { position: fixed; top: 0px; right: 0px; left: 0px; z-index: 1030; }

.fixed-bottom { position: fixed; right: 0px; bottom: 0px; left: 0px; z-index: 1030; }

@supports (position:-webkit-sticky) or (position:sticky) {
  .sticky-top { position: sticky; top: 0px; z-index: 1020; }
}

.sr-only { position: absolute; width: 1px; height: 1px; padding: 0px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; clip-path: inset(50%); border: 0px; }

.sr-only-focusable:active, .sr-only-focusable:focus { position: static; width: auto; height: auto; overflow: visible; clip: auto; white-space: normal; clip-path: none; }

.w-25 { width: 25% !important; }

.w-50 { width: 50% !important; }

.w-75 { width: 75% !important; }

.w-100 { width: 100% !important; }

.h-25 { height: 25% !important; }

.h-50 { height: 50% !important; }

.h-75 { height: 75% !important; }

.h-100 { height: 100% !important; }

.mw-100 { max-width: 100% !important; }

.mh-100 { max-height: 100% !important; }

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
  .m-lg-auto { margin: auto !important; }
  .mt-lg-auto, .my-lg-auto { margin-top: auto !important; }
  .mr-lg-auto, .mx-lg-auto { margin-right: auto !important; }
  .mb-lg-auto, .my-lg-auto { margin-bottom: auto !important; }
  .ml-lg-auto, .mx-lg-auto { margin-left: auto !important; }
}

@media (min-width: 1420px) {
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
  .m-xl-auto { margin: auto !important; }
  .mt-xl-auto, .my-xl-auto { margin-top: auto !important; }
  .mr-xl-auto, .mx-xl-auto { margin-right: auto !important; }
  .mb-xl-auto, .my-xl-auto { margin-bottom: auto !important; }
  .ml-xl-auto, .mx-xl-auto { margin-left: auto !important; }
}

.text-justify { text-align: justify !important; }

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

@media (min-width: 1420px) {
  .text-xl-left { text-align: left !important; }
  .text-xl-right { text-align: right !important; }
  .text-xl-center { text-align: center !important; }
}

.text-lowercase { text-transform: lowercase !important; }

.text-uppercase { text-transform: uppercase !important; }

.text-capitalize { text-transform: capitalize !important; }

.font-weight-light { font-weight: 300 !important; }

.font-weight-normal { font-weight: 400 !important; }

.font-weight-bold { font-weight: 700 !important; }

.font-italic { font-style: italic !important; }

.text-white { color: rgb(255, 255, 255) !important; }

.text-primary { color: rgb(0, 123, 255) !important; }

a.text-primary:hover, a.text-primary:focus { color: rgb(0, 98, 204) !important; }

.text-secondary { color: rgb(108, 117, 125) !important; }

a.text-secondary:hover, a.text-secondary:focus { color: rgb(84, 91, 98) !important; }

.text-success { color: rgb(40, 167, 69) !important; }

a.text-success:hover, a.text-success:focus { color: rgb(30, 126, 52) !important; }

.text-info { color: rgb(23, 162, 184) !important; }

a.text-info:hover, a.text-info:focus { color: rgb(17, 122, 139) !important; }

.text-warning { color: rgb(255, 193, 7) !important; }

a.text-warning:hover, a.text-warning:focus { color: rgb(211, 158, 0) !important; }

.text-danger { color: rgb(220, 53, 69) !important; }

a.text-danger:hover, a.text-danger:focus { color: rgb(189, 33, 48) !important; }

.text-light { color: rgb(248, 249, 250) !important; }

a.text-light:hover, a.text-light:focus { color: rgb(218, 224, 229) !important; }

.text-dark { color: rgb(52, 58, 64) !important; }

a.text-dark:hover, a.text-dark:focus { color: rgb(29, 33, 36) !important; }

.text-muted { color: rgb(108, 117, 125) !important; }

.text-hide { font: 0px / 0 a; color: transparent; text-shadow: none; background-color: transparent; border: 0px; }

.visible { visibility: visible !important; }

.invisible { visibility: hidden !important; }

@media print {
  *, ::before, ::after { text-shadow: none !important; box-shadow: none !important; }
  a:not(.btn) { text-decoration: underline; }
  abbr[title]::after { content: " (" attr(title) ")"; }
  pre { white-space: pre-wrap !important; }
  pre, blockquote { border: 1px solid rgb(153, 153, 153); break-inside: avoid; }
  thead { display: table-header-group; }
  tr, img { break-inside: avoid; }
  p, h2, h3 { orphans: 3; widows: 3; }
  h2, h3 { break-after: avoid; }
  @page { size: a3; }
  body { min-width: 992px !important; }
  .container { min-width: 992px !important; }
  .navbar { display: none; }
  .badge { border: 1px solid rgb(0, 0, 0); }
  .table { border-collapse: collapse !important; }
  .table td, .table th { background-color: rgb(255, 255, 255) !important; }
  .table-bordered th, .table-bordered td { border: 1px solid rgb(221, 221, 221) !important; }
}

html { box-sizing: border-box; }

*, ::before, ::after { box-sizing: inherit; }

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

@media (min-width: 1420px) {
  .container { max-width: 1140px; }
}

.container-fluid { width: 100%; padding-right: 15px; padding-left: 15px; margin-right: auto; margin-left: auto; }

.row { display: flex; flex-wrap: wrap; margin-right: -15px; margin-left: -15px; }

.no-gutters { margin-right: 0px; margin-left: 0px; }

.no-gutters > .col, .no-gutters > [class*="col-"] { padding-right: 0px; padding-left: 0px; }

.col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col, .col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm, .col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md, .col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg, .col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl, .col-xl-auto { position: relative; width: 100%; min-height: 1px; padding-right: 15px; padding-left: 15px; }

.col { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }

.col-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }

.col-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }

.col-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }

.col-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }

.col-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }

.col-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }

.col-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }

.col-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }

.col-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }

.col-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }

.col-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }

.col-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }

.col-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }

.order-first { order: -1; }

.order-last { -webkit-box-ordinal-group: 14; order: 13; }

.order-0 { -webkit-box-ordinal-group: 1; order: 0; }

.order-1 { -webkit-box-ordinal-group: 2; order: 1; }

.order-2 { -webkit-box-ordinal-group: 3; order: 2; }

.order-3 { -webkit-box-ordinal-group: 4; order: 3; }

.order-4 { -webkit-box-ordinal-group: 5; order: 4; }

.order-5 { -webkit-box-ordinal-group: 6; order: 5; }

.order-6 { -webkit-box-ordinal-group: 7; order: 6; }

.order-7 { -webkit-box-ordinal-group: 8; order: 7; }

.order-8 { -webkit-box-ordinal-group: 9; order: 8; }

.order-9 { -webkit-box-ordinal-group: 10; order: 9; }

.order-10 { -webkit-box-ordinal-group: 11; order: 10; }

.order-11 { -webkit-box-ordinal-group: 12; order: 11; }

.order-12 { -webkit-box-ordinal-group: 13; order: 12; }

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
  .col-sm { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-sm-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-sm-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-sm-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-sm-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-sm-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-sm-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-sm-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-sm-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-sm-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-sm-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-sm-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-sm-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-sm-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-sm-first { order: -1; }
  .order-sm-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-sm-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-sm-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-sm-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-sm-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-sm-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-sm-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-sm-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-sm-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-sm-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-sm-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-sm-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-sm-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-sm-12 { -webkit-box-ordinal-group: 13; order: 12; }
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
  .col-md { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-md-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-md-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-md-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-md-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-md-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-md-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-md-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-md-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-md-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-md-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-md-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-md-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-md-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-md-first { order: -1; }
  .order-md-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-md-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-md-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-md-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-md-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-md-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-md-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-md-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-md-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-md-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-md-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-md-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-md-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-md-12 { -webkit-box-ordinal-group: 13; order: 12; }
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
  .col-lg { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-lg-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-lg-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-lg-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-lg-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-lg-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-lg-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-lg-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-lg-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-lg-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-lg-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-lg-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-lg-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-lg-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-lg-first { order: -1; }
  .order-lg-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-lg-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-lg-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-lg-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-lg-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-lg-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-lg-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-lg-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-lg-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-lg-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-lg-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-lg-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-lg-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-lg-12 { -webkit-box-ordinal-group: 13; order: 12; }
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

@media (min-width: 1420px) {
  .col-xl { flex-basis: 0px; -webkit-box-flex: 1; flex-grow: 1; max-width: 100%; }
  .col-xl-auto { -webkit-box-flex: 0; flex: 0 0 auto; width: auto; max-width: none; }
  .col-xl-1 { -webkit-box-flex: 0; flex: 0 0 8.33333%; max-width: 8.33333%; }
  .col-xl-2 { -webkit-box-flex: 0; flex: 0 0 16.6667%; max-width: 16.6667%; }
  .col-xl-3 { -webkit-box-flex: 0; flex: 0 0 25%; max-width: 25%; }
  .col-xl-4 { -webkit-box-flex: 0; flex: 0 0 33.3333%; max-width: 33.3333%; }
  .col-xl-5 { -webkit-box-flex: 0; flex: 0 0 41.6667%; max-width: 41.6667%; }
  .col-xl-6 { -webkit-box-flex: 0; flex: 0 0 50%; max-width: 50%; }
  .col-xl-7 { -webkit-box-flex: 0; flex: 0 0 58.3333%; max-width: 58.3333%; }
  .col-xl-8 { -webkit-box-flex: 0; flex: 0 0 66.6667%; max-width: 66.6667%; }
  .col-xl-9 { -webkit-box-flex: 0; flex: 0 0 75%; max-width: 75%; }
  .col-xl-10 { -webkit-box-flex: 0; flex: 0 0 83.3333%; max-width: 83.3333%; }
  .col-xl-11 { -webkit-box-flex: 0; flex: 0 0 91.6667%; max-width: 91.6667%; }
  .col-xl-12 { -webkit-box-flex: 0; flex: 0 0 100%; max-width: 100%; }
  .order-xl-first { order: -1; }
  .order-xl-last { -webkit-box-ordinal-group: 14; order: 13; }
  .order-xl-0 { -webkit-box-ordinal-group: 1; order: 0; }
  .order-xl-1 { -webkit-box-ordinal-group: 2; order: 1; }
  .order-xl-2 { -webkit-box-ordinal-group: 3; order: 2; }
  .order-xl-3 { -webkit-box-ordinal-group: 4; order: 3; }
  .order-xl-4 { -webkit-box-ordinal-group: 5; order: 4; }
  .order-xl-5 { -webkit-box-ordinal-group: 6; order: 5; }
  .order-xl-6 { -webkit-box-ordinal-group: 7; order: 6; }
  .order-xl-7 { -webkit-box-ordinal-group: 8; order: 7; }
  .order-xl-8 { -webkit-box-ordinal-group: 9; order: 8; }
  .order-xl-9 { -webkit-box-ordinal-group: 10; order: 9; }
  .order-xl-10 { -webkit-box-ordinal-group: 11; order: 10; }
  .order-xl-11 { -webkit-box-ordinal-group: 12; order: 11; }
  .order-xl-12 { -webkit-box-ordinal-group: 13; order: 12; }
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

@media (min-width: 1420px) {
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

.flex-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }

.flex-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }

.flex-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }

.flex-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }

.flex-wrap { flex-wrap: wrap !important; }

.flex-nowrap { flex-wrap: nowrap !important; }

.flex-wrap-reverse { flex-wrap: wrap-reverse !important; }

.justify-content-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }

.justify-content-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }

.justify-content-center { -webkit-box-pack: center !important; justify-content: center !important; }

.justify-content-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }

.justify-content-around { justify-content: space-around !important; }

.align-items-start { -webkit-box-align: start !important; align-items: flex-start !important; }

.align-items-end { -webkit-box-align: end !important; align-items: flex-end !important; }

.align-items-center { -webkit-box-align: center !important; align-items: center !important; }

.align-items-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }

.align-items-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }

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
  .flex-sm-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-sm-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-sm-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-sm-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-sm-wrap { flex-wrap: wrap !important; }
  .flex-sm-nowrap { flex-wrap: nowrap !important; }
  .flex-sm-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-sm-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-sm-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-sm-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-sm-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-sm-around { justify-content: space-around !important; }
  .align-items-sm-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-sm-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-sm-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-sm-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-sm-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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
  .flex-md-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-md-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-md-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-md-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-md-wrap { flex-wrap: wrap !important; }
  .flex-md-nowrap { flex-wrap: nowrap !important; }
  .flex-md-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-md-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-md-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-md-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-md-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-md-around { justify-content: space-around !important; }
  .align-items-md-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-md-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-md-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-md-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-md-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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
  .flex-lg-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-lg-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-lg-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-lg-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-lg-wrap { flex-wrap: wrap !important; }
  .flex-lg-nowrap { flex-wrap: nowrap !important; }
  .flex-lg-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-lg-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-lg-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-lg-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-lg-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-lg-around { justify-content: space-around !important; }
  .align-items-lg-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-lg-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-lg-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-lg-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-lg-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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

@media (min-width: 1420px) {
  .flex-xl-row { -webkit-box-orient: horizontal !important; -webkit-box-direction: normal !important; flex-direction: row !important; }
  .flex-xl-column { -webkit-box-orient: vertical !important; -webkit-box-direction: normal !important; flex-direction: column !important; }
  .flex-xl-row-reverse { -webkit-box-orient: horizontal !important; -webkit-box-direction: reverse !important; flex-direction: row-reverse !important; }
  .flex-xl-column-reverse { -webkit-box-orient: vertical !important; -webkit-box-direction: reverse !important; flex-direction: column-reverse !important; }
  .flex-xl-wrap { flex-wrap: wrap !important; }
  .flex-xl-nowrap { flex-wrap: nowrap !important; }
  .flex-xl-wrap-reverse { flex-wrap: wrap-reverse !important; }
  .justify-content-xl-start { -webkit-box-pack: start !important; justify-content: flex-start !important; }
  .justify-content-xl-end { -webkit-box-pack: end !important; justify-content: flex-end !important; }
  .justify-content-xl-center { -webkit-box-pack: center !important; justify-content: center !important; }
  .justify-content-xl-between { -webkit-box-pack: justify !important; justify-content: space-between !important; }
  .justify-content-xl-around { justify-content: space-around !important; }
  .align-items-xl-start { -webkit-box-align: start !important; align-items: flex-start !important; }
  .align-items-xl-end { -webkit-box-align: end !important; align-items: flex-end !important; }
  .align-items-xl-center { -webkit-box-align: center !important; align-items: center !important; }
  .align-items-xl-baseline { -webkit-box-align: baseline !important; align-items: baseline !important; }
  .align-items-xl-stretch { -webkit-box-align: stretch !important; align-items: stretch !important; }
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

*, ::before, ::after { box-sizing: border-box; }

html { font-family: sans-serif; line-height: 1.15; text-size-adjust: 100%; -webkit-tap-highlight-color: transparent; }

article, aside, dialog, figcaption, figure, footer, header, hgroup, main, nav, section { display: block; }

body { margin: 0px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"; font-size: 1rem; font-weight: 400; line-height: 1.5; color: rgb(33, 37, 41); text-align: left; background-color: rgb(255, 255, 255); }

[tabindex="-1"]:focus { outline: 0px !important; }

hr { box-sizing: content-box; height: 0px; overflow: visible; }

h1, h2, h3, h4, h5, h6 { margin-top: 0px; margin-bottom: 0.5rem; }

p { margin-top: 0px; margin-bottom: 1rem; }

abbr[title], abbr[data-original-title] { text-decoration: underline dotted; cursor: help; border-bottom: 0px; }

address { margin-bottom: 1rem; font-style: normal; line-height: inherit; }

ol, ul, dl { margin-top: 0px; margin-bottom: 1rem; }

ol ol, ul ul, ol ul, ul ol { margin-bottom: 0px; }

dt { font-weight: 700; }

dd { margin-bottom: 0.5rem; margin-left: 0px; }

blockquote { margin: 0px 0px 1rem; }

dfn { font-style: italic; }

b, strong { font-weight: bolder; }

small { font-size: 80%; }

sub, sup { position: relative; font-size: 75%; line-height: 0; vertical-align: baseline; }

sub { bottom: -0.25em; }

sup { top: -0.5em; }

a { color: rgb(0, 123, 255); text-decoration: none; background-color: transparent; }

a:hover { color: rgb(0, 86, 179); text-decoration: underline; }

a:not([href]):not([tabindex]) { color: inherit; text-decoration: none; }

a:not([href]):not([tabindex]):hover, a:not([href]):not([tabindex]):focus { color: inherit; text-decoration: none; }

a:not([href]):not([tabindex]):focus { outline: 0px; }

pre, code, kbd, samp { font-family: monospace, monospace; font-size: 1em; }

pre { margin-top: 0px; margin-bottom: 1rem; overflow: auto; }

figure { margin: 0px 0px 1rem; }

img { vertical-align: middle; border-style: none; }

svg:not(:root) { overflow: hidden; }

table { border-collapse: collapse; }

caption { padding-top: 0.75rem; padding-bottom: 0.75rem; color: rgb(108, 117, 125); text-align: left; caption-side: bottom; }

th { text-align: inherit; }

label { display: inline-block; margin-bottom: 0.5rem; }

button { border-radius: 0px; }

button:focus { outline: -webkit-focus-ring-color auto 5px; }

input, button, select, optgroup, textarea { margin: 0px; font-family: inherit; font-size: inherit; line-height: inherit; }

button, input { overflow: visible; }

button, select { text-transform: none; }

button, html [type="button"], [type="reset"], [type="submit"] { -webkit-appearance: button; }

input[type="radio"], input[type="checkbox"] { box-sizing: border-box; padding: 0px; }

input[type="date"], input[type="time"], input[type="datetime-local"], input[type="month"] { -webkit-appearance: listbox; }

textarea { overflow: auto; resize: vertical; }

fieldset { min-width: 0px; padding: 0px; margin: 0px; border: 0px; }

legend { display: block; width: 100%; max-width: 100%; padding: 0px; margin-bottom: 0.5rem; font-size: 1.5rem; line-height: inherit; color: inherit; white-space: normal; }

progress { vertical-align: baseline; }

[type="number"]::-webkit-inner-spin-button, [type="number"]::-webkit-outer-spin-button { height: auto; }

[type="search"] { outline-offset: -2px; -webkit-appearance: none; }

[type="search"]::-webkit-search-cancel-button, [type="search"]::-webkit-search-decoration { -webkit-appearance: none; }

::-webkit-file-upload-button { font: inherit; -webkit-appearance: button; }

output { display: inline-block; }

summary { display: list-item; cursor: pointer; }

template { display: none; }

[hidden] { display: none !important; }

.view-box-square-title { width: 100%; line-height: 209px; text-align: center; position: relative; }

.view-box-square-title a { left: 0px !important; }
------MultipartBoundary--N1Eay4lcYYX2rGjcUEmGmPPUBN3bWjvqvPv2iZl2Wh----
Content-Type: font/woff2
Content-Transfer-Encoding: binary
Content-Location: https://www.bancobaieuropa.pt/themes/custom/baieu/woff/MaterialIcons-Regular.woff2

wOF2"""


  Soup = BeautifulSoup(html_text ,'html.parser')

  lista_paises = list()
  lista_compra = list()
  lista_venda = list()
  Tabela_Cambio = list()
  #
  lista_paises_2 = list()
  lista_compra_2 = list()
  lista_venda_2 = list()
  Tabela_Cambio_2 = list()
  Banco_BAIEuropa = dict()

  table_1 = Soup.findChild('div',attrs={'class':'cambiosdivisas'})
  table_2 = Soup.findChild('div', attrs={'class':'notasmoedas'})

  lista_paises = table_1.select('table tbody tr td:nth-of-type(1)')
  lista_venda = table_1.select('table tbody tr td:nth-of-type(2)')
  lista_compra = table_1.select('table tbody tr td:nth-of-type(3)')

  lista_paises_2 = table_2.select('table tbody tr td:nth-of-type(1)')
  lista_venda_2 = table_2.select('table tbody tr td:nth-of-type(2)')
  lista_compra_2 = table_2.select('table tbody tr td:nth-of-type(3)')

  for c in range(0, len(lista_compra)):
    Banco_BAIEuropa['pais'] = extrair_tag(lista_paises[c])
    Banco_BAIEuropa['compra'] = extrair_tag(lista_compra[c])
    Banco_BAIEuropa['venda'] = extrair_tag(lista_venda[c])

    Tabela_Cambio.append(Banco_BAIEuropa.copy())

    Banco_BAIEuropa['pais'] = extrair_tag(lista_paises_2[c])
    Banco_BAIEuropa['compra'] = extrair_tag(lista_compra_2[c])
    Banco_BAIEuropa['venda'] = extrair_tag(lista_venda_2[c])
    
    Tabela_Cambio_2.append(Banco_BAIEuropa.copy())
  for value in Tabela_Cambio_2:
    Tabela_Cambio.append(value)

