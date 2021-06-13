print('[Module] Journal loaded.')

def receive_income(amount):
    """[summary: prints out the amount recived]

    Args:
        amount ([float]): [price]
    """
    print('[Journal] Received R{0:.2f}'.format(amount))


def pay_expense(amount):
    """[summary: prints out the amount paid by customer]

    Args:
        amount ([float]): [price paid]
    """
    print('[Journal] Paid R{0:.2f}'.format(amount))