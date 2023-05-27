[1] you should replace the paths of anything i imported using " pandas.read_table() " to read the "txt" files and put it in the full form

=> goto the file "txt" in the folder you received
=> click on the toolbar and copy ... you should get something like that [E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\Submission]
=> add the file name at the end and don't forget the ".txt" ,, e.g. [E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\Submission\tickets.txt]
=> replace every path in the files both [utils.py & operations.py] 
=> don't delete the 'r' before intializing the paths , e.g. r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\Submission\tickets.txt"

e.g. :

the old function with the old path : 
		movies_df = pd.read_table(r"E:\Studium\Season 2023\[4] Mai\Freelancing\Upwork\Python Expert - Proposal\movies.txt",
                    delimiter=", ",
                    header=None,
                    names=index_col_movies)

the new path [imaginairy] ==> E:\documents\movies.txt

the supposed form :
			movies_df = pd.read_table(r"E:\documents\movies.txt",
                    delimiter=", ",
                    header=None,
                    names=index_col_movies)

[2] All the Methods, Classes , Extra Attributes, Extra Functions , All the Choices till HD level are done
EXCEPT: choice number 10 

[3] in "utils.py" delete the first comment lines as it's the initialization of the Developer not to get captured

[4] Good Luck in ur Assignment :)