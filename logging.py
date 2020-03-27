from datetime import datetime

def record(action, who = 'none'):
    """
    Records excution of <action> by <who>
    """
    log = open('pyxi.log', 'a+', encoding='utf8')
    date = datetime.today().strftime('%d/%m/%Y_%H:%M:%S')
    log.write(f'[{date}][{action}][{who}]\n')
    log.close()
