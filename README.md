# listsToTableString

This function is useful for someone if they want to print list elements with beautiful style. There are some options and we will see them with examples.

* [General information](#General)
* [Count Elements](#Show_Count)
* [Show Titles](#Titles)
* [Left Side](#Left_Side)

## General 

First we put as argument every list or tuple we want to print.


	example
		cities = ('Athens','Thessaloniki','Patra','Heraklion','Larissa')
		census_1991 = [772.072, 383.967, 152.570, 115.270]
		region = ("Attica","Macedonia","Western Greece","Crete","Thessaly")
		
		print( listsToTableString(cities,census_1991,region) )
	result
		|Athens       |772.072 |Attica         |
		|Thessaloniki |383.967 |Macedonia      |
		|Patra        |152.57  |Western Greece |
		|Heraklion    |115.27  |Crete          |
		|Larissa      |        |Thessaly       |

## Show_Count

We can show count of each row. Just set show_count=True.

	example
		cities = ('Athens','Thessaloniki','Patra','Heraklion','Larissa')
		census_1991 = [772.072, 383.967, 152.570, 115.270]
		region = ("Attica","Macedonia","Western Greece","Crete","Thessaly")
		
		print( listsToTableString(cities,census_1991,region,show_count=True) )
	result
		|1 |Athens       |772.072 |Attica         |
		|2 |Thessaloniki |383.967 |Macedonia      |
		|3 |Patra        |152.57  |Western Greece |
		|4 |Heraklion    |115.27  |Crete          |
		|5 |Larissa      |        |Thessaly       |


## Titles

Usually we want a title so we can present data better. We append tuple or list argument as titles.
Warning! If we use show_count we must define a title for it.

	example
		cities = ('Athens','Thessaloniki','Patra','Heraklion','Larissa')
		census_1991 = [772.072, 383.967, 152.570, 115.270]
		
		region = ("Attica","Macedonia","Western Greece","Crete","Thessaly")

		print( listsToTableString(cities,census_1991,region,show_count=True,titles=("Count","Cities","Census 1991","Region")) )

	result
		|Count |Cities       |Census 1991 |Region         |
		|------|-------------|------------|---------------|
		|1     |Athens       |772.072     |Attica         |
		|2     |Thessaloniki |383.967     |Macedonia      |
		|3     |Patra        |152.57      |Western Greece |
		|4     |Heraklion    |115.27      |Crete          |
		|5     |Larissa      |            |Thessaly       |


## Left_Side

By default all elements are in left side. This can change by setting left_side=False

	example
		cities = ('Athens','Thessaloniki','Patra','Heraklion','Larissa')
		census_1991 = [772.072, 383.967, 152.570, 115.270]
		region = ("Attica","Macedonia","Western Greece","Crete","Thessaly")

		print( listsToTableString(cities,census_1991,region,show_count=True,titles=("Count","Cities","Census 1991","Region"),left_side=False) )

	result
		|Count |Cities       |Census 1991 |Region         |
		|------|-------------|------------|---------------|
		|     1|       Athens|     772.072|         Attica|
		|     2| Thessaloniki|     383.967|      Macedonia|
		|     3|        Patra|      152.57| Western Greece|
		|     4|    Heraklion|      115.27|          Crete|
		|     5|      Larissa|            |       Thessaly|











		
