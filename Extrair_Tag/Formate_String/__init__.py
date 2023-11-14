def formate_string(text):
    if '\t' in text: 
        text_format = str(text).replace('\t', '')
        text = text_format
        
    if '\n' in text:
        text_format = str(text).replace('\n','')
        
    return text_format.strip()