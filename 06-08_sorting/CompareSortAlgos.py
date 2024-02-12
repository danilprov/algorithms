import time
import signal
import pandas as pd
import sys
sys.setrecursionlimit(10**6)

from BubbleSort import BubbleSort
from InsertionSort import InsertionSort, InsertionSortShift, InsertionSortBinarySearch
from ShellSort import ShellSort
from SelectionSort import SelectionSort
from HeapSort import HeapSort
from QuickSort import QuickSort, QuickSortLomuto
from MergeSort import MergeSort
from Tester import Tester

path = 'resources/'
sort = BubbleSort
final_df = pd.DataFrame()
test_candidates = [BubbleSort, InsertionSort, InsertionSortShift, InsertionSortBinarySearch,
                   ShellSort, SelectionSort, HeapSort, QuickSort, QuickSortLomuto, MergeSort]
#test_candidates = [QuickSort, QuickSortLomuto]


for (i, algo) in enumerate(test_candidates):
    sort = algo
    tst = Tester(sort, path)
    output = tst.run_tests()
    for key, inner_dict in output.items():
        temp_df = pd.DataFrame.from_dict(inner_dict, orient='index', columns=['time (ms)', "cmp's", "asg's"])
        # Add a column for the key
        temp_df['data type'] = key
        temp_df['algo'] = str(i) + '.' + sort.__name__
        # Concatenate the temporary DataFrame with the main DataFrame
        final_df = pd.concat([final_df, temp_df])


final_df.reset_index(inplace=True)
final_df.rename(columns={'index': 'N^i'}, inplace=True)
final_df = final_df[['algo', 'data type', 'N^i', 'time (ms)', "cmp's", "asg's"]]
final_df = final_df.sort_values(['algo','data type', 'N^i'])
final_df = final_df.pivot(index=['algo', 'N^i'], columns='data type', values=['time (ms)', "cmp's", "asg's"])

pd.DataFrame.reset_header = lambda df : df.swapaxes(0,1).reset_index().swapaxes(0,1)
new_df = final_df.reset_index().reset_header().rename(columns={'idx1': '', 'idx2': ''})
new_df.columns = new_df.iloc[0]
new_df = new_df.drop('level_0')

out= new_df.to_markdown(tablefmt='github', index=False)
print(out)
open('comparison_table.md', 'w').write(out)
