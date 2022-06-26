


def get_nf_icon(status_code):

    if status_code >= 200 and status_code <= 299:
        return ''
    elif status_code >= 300 and status_code <= 399:
        return ''
    elif status_code >= 500 and status_code <= 599:
        return ''
    elif status_code >= 600 and status_code <= 699:
        return '流'
    elif status_code >= 700 and status_code <= 799:
        return ''
    elif status_code >= 800:
        return ''
    

