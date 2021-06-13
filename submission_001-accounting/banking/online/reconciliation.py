import requests

print('[Module] online.Reconciliation loaded.')

def do_reconciliation():
    """[summary: prints output and requests made]
    """
    print('Doing Online Bank reconciliation.')
    response = requests.get('https://www.wethinkcode.co.za')
    print(response.status_code)