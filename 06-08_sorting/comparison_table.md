| algo                        | N^i   | time (ms)   | time (ms)   | time (ms)   | time (ms)   | cmp's     | cmp's     | cmp's     | cmp's     | asg's     | asg's     | asg's     | asg's     |
|-----------------------------|-------|-------------|-------------|-------------|-------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|                             |       | 0.random    | 1.digits    | 2.sorted    | 3.revers    | 0.random  | 1.digits  | 2.sorted  | 3.revers  | 0.random  | 1.digits  | 2.sorted  | 3.revers  |
| 0.BubbleSort                | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 0.BubbleSort                | 1     | 0           | 0           | 0           | 0           | 45        | 45        | 45        | 45        | 48        | 63        | 27        | 135       |
| 0.BubbleSort                | 2     | 3           | 4           | 2           | 3           | 4950      | 4950      | 4950      | 4950      | 6471      | 7203      | 261       | 14850     |
| 0.BubbleSort                | 3     | 354         | 269         | 194         | 462         | 499500    | 499500    | 499500    | 499500    | 742467    | 684651    | 19812     | 1498500   |
| 0.BubbleSort                | 4     | 33978       | 29720       | 19918       | 44750       | 49995000  | 49995000  | 49995000  | 49995000  | 75865872  | 67414506  | 1999176   | 149985000 |
| 0.BubbleSort                | 5     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 0.BubbleSort                | 6     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 0.BubbleSort                | 7     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 1.InsertionSort             | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 1.InsertionSort             | 1     | 0           | 0           | 0           | 0           | 24        | 28        | 18        | 45        | 48        | 63        | 27        | 135       |
| 1.InsertionSort             | 2     | 2           | 4           | 0           | 5           | 2253      | 2498      | 186       | 4950      | 6471      | 7203      | 261       | 14850     |
| 1.InsertionSort             | 3     | 219         | 927         | 6           | 619         | 248479    | 229214    | 7603      | 499500    | 742467    | 684651    | 19812     | 1498500   |
| 1.InsertionSort             | 4     | 23704       | 23418       | 631         | 53003       | 25298615  | 22481500  | 676391    | 49995000  | 75865872  | 67414506  | 1999176   | 149985000 |
| 1.InsertionSort             | 5     | timeout     | timeout     | 61943       | timeout     | --        | --        | 65348997  | --        | --        | --        | 195746994 | --        |
| 1.InsertionSort             | 6     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 1.InsertionSort             | 7     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 2.InsertionSortShift        | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 2.InsertionSortShift        | 1     | 0           | 0           | 0           | 0           | 24        | 28        | 18        | 45        | 34        | 39        | 27        | 63        |
| 2.InsertionSortShift        | 2     | 1           | 1           | 0           | 3           | 2253      | 2498      | 186       | 4950      | 2355      | 2599      | 285       | 5148      |
| 2.InsertionSortShift        | 3     | 142         | 128         | 4           | 318         | 248479    | 229214    | 7603      | 499500    | 249487    | 230215    | 8602      | 501498    |
| 2.InsertionSortShift        | 4     | 14596       | 13067       | 393         | 28885       | 25298615  | 22481500  | 676391    | 49995000  | 25308622  | 22491500  | 686390    | 50014998  |
| 2.InsertionSortShift        | 5     | timeout     | timeout     | 38405       | timeout     | --        | --        | 65348997  | --        | --        | --        | 65448996  | --        |
| 2.InsertionSortShift        | 6     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 2.InsertionSortShift        | 7     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 3.InsertionSortBinarySearch | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 3.InsertionSortBinarySearch | 1     | 0           | 0           | 0           | 0           | 24        | 22        | 25        | 22        | 34        | 39        | 27        | 63        |
| 3.InsertionSortBinarySearch | 2     | 1           | 1           | 0           | 1           | 546       | 550       | 573       | 516       | 2355      | 2637      | 285       | 5148      |
| 3.InsertionSortBinarySearch | 3     | 70          | 64          | 4           | 124         | 8754      | 8788      | 8841      | 8475      | 249487    | 230697    | 8602      | 501498    |
| 3.InsertionSortBinarySearch | 4     | 7104        | 6154        | 216         | 13629       | 120526    | 120788    | 120884    | 117726    | 25308622  | 22496337  | 686390    | 50014998  |
| 3.InsertionSortBinarySearch | 5     | timeout     | timeout     | 18426       | timeout     | --        | --        | 1540849   | --        | --        | --        | 65448996  | --        |
| 3.InsertionSortBinarySearch | 6     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 3.InsertionSortBinarySearch | 7     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 4.ShellSort                 | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 4.ShellSort                 | 1     | 0           | 0           | 0           | 0           | 29        | 32        | 22        | 27        | 30        | 45        | 3         | 39        |
| 4.ShellSort                 | 2     | 1           | 0           | 0           | 0           | 877       | 691       | 590       | 668       | 1239      | 684       | 261       | 780       |
| 4.ShellSort                 | 3     | 9           | 5           | 5           | 6           | 15296     | 10449     | 10710     | 11716     | 23445     | 8589      | 8166      | 14100     |
| 4.ShellSort                 | 4     | 197         | 81          | 108         | 108         | 267306    | 153568    | 176309    | 172578    | 457458    | 112719    | 169422    | 187680    |
| 4.ShellSort                 | 5     | 3602        | 987         | 2005        | 1396        | 4562610   | 1860949   | 2833579   | 2244585   | 9339837   | 1204296   | 4004910   | 2533680   |
| 4.ShellSort                 | 6     | 56292       | 11817       | 27636       | 16042       | 68027835  | 22383596  | 38939516  | 26357530  | 151592142 | 14369463  | 62863278  | 28072512  |
| 4.ShellSort                 | 7     | timeout     | 142264      | timeout     | 191306      | --        | 270196822 | --        | 317626219 | --        | 162761751 | --        | 322878528 |
| 5.SelectionSort             | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 5.SelectionSort             | 1     | 0           | 0           | 0           | 0           | 54        | 54        | 54        | 54        | 27        | 27        | 27        | 27        |
| 5.SelectionSort             | 2     | 1           | 2           | 1           | 1           | 5049      | 5049      | 5049      | 5049      | 297       | 297       | 297       | 297       |
| 5.SelectionSort             | 3     | 104         | 122         | 107         | 101         | 500499    | 500499    | 500499    | 500499    | 2997      | 2997      | 2997      | 2997      |
| 5.SelectionSort             | 4     | 10828       | 11103       | 11410       | 10944       | 50004999  | 50004999  | 50004999  | 50004999  | 29997     | 29997     | 29997     | 29997     |
| 5.SelectionSort             | 5     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 5.SelectionSort             | 6     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 5.SelectionSort             | 7     | timeout     | timeout     | timeout     | timeout     | --        | --        | --        | --        | --        | --        | --        | --        |
| 6.HeapSort                  | 0     | 0           | 2           | 0           | 0           | 2         | 2         | 2         | 2         | 0         | 0         | 0         | 0         |
| 6.HeapSort                  | 1     | 0           | 0           | 0           | 0           | 66        | 64        | 68        | 52        | 84        | 81        | 87        | 63        |
| 6.HeapSort                  | 2     | 1           | 1           | 1           | 0           | 1282      | 1148      | 1390      | 1132      | 1773      | 1572      | 1935      | 1548      |
| 6.HeapSort                  | 3     | 8           | 10          | 11          | 8           | 19130     | 17542     | 20360     | 17632     | 27195     | 24813     | 29040     | 24948     |
| 6.HeapSort                  | 4     | 137         | 123         | 148         | 128         | 258444    | 235388    | 272960    | 243392    | 372666    | 338082    | 394440    | 350088    |
| 6.HeapSort                  | 5     | 1846        | 1573        | 1851        | 1667        | 3250006   | 2941026   | 3397240   | 3094868   | 4725009   | 4261539   | 4945860   | 4492302   |
| 6.HeapSort                  | 6     | 22528       | 18735       | 22215       | 20208       | 39093040  | 35221124  | 40530392  | 37666816  | 57139560  | 51331686  | 59295588  | 55000224  |
| 6.HeapSort                  | 7     | timeout     | 220182      | 258301      | 239743      | --        | 412421996 | 473211848 | 443824856 | --        | 603632994 | 694817772 | 650737284 |
| 7.QuickSort                 | 0     | 0           | 1           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 7.QuickSort                 | 1     | 0           | 0           | 0           | 0           | 73        | 66        | 62        | 78        | 24        | 21        | 3         | 15        |
| 7.QuickSort                 | 2     | 0           | 0           | 1           | 2           | 1264      | 1256      | 2915      | 5298      | 465       | 258       | 3         | 150       |
| 7.QuickSort                 | 3     | 7           | 23          | 34          | 169         | 19879     | 57656     | 99199     | 502998    | 7023      | 2496      | 54        | 1500      |
| 7.QuickSort                 | 4     | 110         | 1851        | 537         | 17297       | 270654    | 5077758   | 1536702   | 50029998  | 93714     | 23649     | 1062      | 15000     |
| 7.QuickSort                 | 5     | 1411        | 174023      | 6357        | timeout     | 3418060   | 500780850 | 17703879  | --        | 1157847   | 241281    | 15270     | --        |
| 7.QuickSort                 | 6     | 17642       | timeout     | 85058       | timeout     | 40975583  | --        | 239901466 | --        | 13916412  | --        | 195558    | --        |
| 7.QuickSort                 | 7     | 207557      | timeout     | timeout     | timeout     | 470743568 | --        | --        | --        | 162361386 | --        | --        | --        |
| 8.QuickSortLomuto           | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 8.QuickSortLomuto           | 1     | 0           | 0           | 0           | 0           | 31        | 31        | 48        | 54        | 72        | 45        | 129       | 87        |
| 8.QuickSortLomuto           | 2     | 0           | 1           | 2           | 3           | 690       | 880       | 2760      | 5049      | 1155      | 2250      | 8148      | 7647      |
| 8.QuickSortLomuto           | 3     | 6           | 39          | 135         | 275         | 11404     | 54477     | 175339    | 500499    | 16197     | 155970    | 477348    | 751497    |
| 8.QuickSortLomuto           | 4     | 91          | 4068        | 363         | 28051       | 155089    | 5038978   | 802285    | 50004999  | 251610    | 15071970  | 581355    | 75014997  |
| 8.QuickSortLomuto           | 5     | 1234        | timeout     | 10425       | timeout     | 2065627   | --        | 17718857  | --        | 3168309   | --        | 28927680  | --        |
| 8.QuickSortLomuto           | 6     | 15196       | timeout     | 149288      | timeout     | 25482502  | --        | 262302136 | --        | 38832207  | --        | 405635235 | --        |
| 8.QuickSortLomuto           | 7     | 186044      | timeout     | timeout     | timeout     | 302644940 | --        | --        | --        | 452452449 | --        | --        | --        |
| 9.MergeSort                 | 0     | 0           | 0           | 0           | 0           | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| 9.MergeSort                 | 1     | 0           | 0           | 0           | 0           | 23        | 22        | 22        | 15        | 68        | 68        | 68        | 68        |
| 9.MergeSort                 | 2     | 1           | 1           | 1           | 0           | 543       | 547       | 397       | 316       | 1344      | 1344      | 1344      | 1344      |
| 9.MergeSort                 | 3     | 8           | 8           | 7           | 6           | 8721      | 8488      | 6645      | 4932      | 19952     | 19952     | 19952     | 19952     |
| 9.MergeSort                 | 4     | 108         | 118         | 116         | 104         | 120481    | 116872    | 101839    | 64608     | 267232    | 267232    | 267232    | 267232    |
| 9.MergeSort                 | 5     | 1473        | 1456        | 1448        | 1218        | 1536652   | 1483484   | 1341875   | 815024    | 3337856   | 3337856   | 3337856   | 3337856   |
| 9.MergeSort                 | 6     | 18428       | 17209       | 17053       | 14502       | 18674508  | 17970393  | 16606871  | 9884992   | 39902848  | 39902848  | 39902848  | 39902848  |
| 9.MergeSort                 | 7     | 223124      | 200539      | 199555      | 165142      | 220101952 | 211522718 | 200958059 | 114434624 | 466445568 | 466445568 | 466445568 | 466445568 |