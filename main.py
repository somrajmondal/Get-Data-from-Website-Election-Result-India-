import pandas
wiki=pandas.read_html('https://en.wikipedia.org/wiki/2019_Indian_general_election')
#print(wiki)
election=wiki[2]
#print(election)


candi_1=election[1]
#print(candi_1)
candi_1_name=candi_1[1]
#print(candi_1_name)
candi_1_Seats=candi_1[5]
#print(candi_1_Seats)

candi_2=election[2]
#print(candi_2)
candi_2_name=candi_2[1]
#print(candi_2_name)
candi_2_Seats=candi_2[5]
#print(candi_2_Seats)

if candi_2_Seats<candi_1_Seats:
    print(f'{candi_2_name} has got {candi_2_Seats} and won the election')
else:
    print(f'{candi_1_name} has got {candi_1_Seats} and won the election')
