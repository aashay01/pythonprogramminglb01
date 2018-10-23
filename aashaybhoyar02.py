from easygui import  *
2  import sys
3  list_m = []
4  sum = 0
5  while 1:
6      msgbox("Hello, world!")
7      msg ="Choose a product from below"
8      title = "E-bazaar"
9      choices = ["Ice cream", "Biscuits", "Soap"]
10      choice = choicebox(msg, title, choices)
11      msgbox("You chose: " + str(choice))
12      if (choice == "Ice cream"):
13          msg =  "Which flavour?"
14          title = "Ice cream flavour"
15          choices = ["Chocolate","Vanilla"]
16          choice = choicebox(msg,title,choices)
17          msgbox("You chose: "+str(choice))
18          if (choice == "Chocolate"):
19               msg = "Which vendor?"
20               title = "Select vendor"
21               choices = ["Suresh = $4.50","Ramesh = $5.50"]
22               choice = choicebox(msg,title,choices)
23               msgbox("You chose: "+str(choice))
24               if (choice == "Suresh = $4.50"):
25                  sum+=4.50
26               else:
27                  sum+=5.50
28               list_m = [choice]
29          else:
30               msg = "For vanilla, Which vendor?"
31               title = "Select vendor"
32               choices = ["Suresh = $3.50","Ramesh = $4.50"]
33               choice = choicebox(msg,title,choices)
34               msgbox("You chose: "+str(choice))
35               if (choice == "Suresh = $3.50"):
36                  sum+=3.50
37               else:
38                  sum+=4.50
39               list_m = [choice]
40      elif (choice == "Biscuits"):
41          msg = "Which Brand?"
42          title = "Select brand"
43          choices = ["Parle-G","Jim Jam"]
44          choice = choicebox(msg,title,choices)
45          if (choice == "Jim Jam"):
46               msg = "Which vendor?"
47               title = "Select vendor"
48               choices = ["Suresh = $4","Ramesh  $5"]
49               choice = choicebox(msg,title,choices)
50               msgbox("You chose: "+str(choice))
51               if (choice == "Suresh = $4"):
52                  sum+=4
53               else:
54                  sum+=5
55               list_m.append(choice)
56          elif (choice == "Parle-G") :
57               msg = "Which vendor?"
58               title = "Select vendor"
59               choices = ["Suresh = $3","Ramesh = $2"]
60               choice = choicebox(msg,title,choices)
61               msgbox("You chose: "+str(choice))
62               if (choice == "Suresh = $3"):
63                  sum+=3
64               else:
65                  sum+=2
66               list_m.append(choice)
67      elif (choice == "Soap"):
68          msg = "Which brand?"
69          title = "Select brand"
70          choices = ["Lux","Dove"]
71          choice = choicebox(msg,title,choices)
72          msgbox("You chose: "+str(choice))
73          if (choice == "Lux"):
74               msg = "Which vendor?"
75               title = "Select vendor"
76               choices = ["Suresh = $3","Ramesh = $2"]
77               choice = choicebox(msg,title,choices)
78               msgbox("You chose: "+str(choice))
79               if (choice == "Suresh = $3"):
80                  sum+=3
81               else:
82                  sum+=2
83               list_m.append(choice)
84          else:
85               msg = "Which vendor?"
86               title = "Select vendor"
87               choices = ["Suresh = $3.4","Ramesh = $4.3"]
88               choice = choicebox(msg,title,choices)
89               msgbox("You chose: "+str(choice))
90               if (choice == "Suresh = $3.4"):
91                  sum+=3.4
92               else:
93                  sum+=4.3
94               list_m.append(choice)
95      if ccbox('Would you like to continue?', 'Add to cart'):     # show a Continue/Cancel dialog
96          pass  # user chose Continue
97          #print(sum)
98          #print(list_m)
99      else:
100          print(sum)
101          print(list_m)
102          sys.exit(0)
