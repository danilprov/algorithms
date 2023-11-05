from Tester import Tester
from LuckyTicket import LuckyTickets

path = 'resources/'
task = LuckyTickets()

tst = Tester(task, path)
tst.run_tests()