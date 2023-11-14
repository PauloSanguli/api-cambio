def extrair_tag(tag):
    texto_tag = str(tag)

    pos_init = int(texto_tag.find('>'))+1
    pos_fin = texto_tag.rfind('<')

    texto = texto_tag[pos_init:pos_fin]
    return texto