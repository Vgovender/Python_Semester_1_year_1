import user.authentication
import transactions.journal
# import banking.reconciliation
# import banking.fvb.reconciliation
# import banking.ubsa.reconciliation
# import banking.online.reconciliation
import sys
import banking


if __name__ == "__main__":
    """[summary: main, calls all modules requested]
    """
    if len(sys.argv) >= 1:
        len_of_argv = len(sys.argv)
        for i in range(1,len_of_argv):
            print(sys.argv[i])

    user.authentication.authenticate_user()
    amount = 100.00
    transactions.journal.receive_income(amount)
    transactions.journal.pay_expense(amount)
    # banking.reconciliation.do_reconciliation()
    banking.fvb.reconciliation.do_reconciliation()
    # banking.ubsa.reconciliation.do_reconciliation()
    # banking.online.reconciliation.do_reconciliation()
    # help("modules")
    