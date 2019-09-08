import os
import csv

#Some things in life are bad,
#They can really make you mad.

pypoll_csv = os.path.join("election_data.csv")

#Other things just make you swear and curse.

votes_by_candidate = {}
candidate_votes = 0 
candidate_total_votes = 0

#When you're chewing on life's gristle,
#Don't grumble, give a whistle!
#And this'll help things turn out for the best ... 
   
votes = []
            #Always look on the bright side of life
candidates = []
                #If life seems jolly rotten - There's something you've forgotten
                #And that's to laugh and smile and dance and sing      
votes_by_percent = []
                #When you're feeling in the dumps
                 #Don't be silly, chumps
Who_wunnit = []

#Just purse your lips and whistle - that's the thing
      #And ... 
          #Always look on the bright side of life 

with open(pypoll_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    #And...Always look on the bright side of life!

    for row in csvreader:
        
          candidate_total_votes += 1
          if (row[2]) in votes_by_candidate.keys():
               votes_by_candidate [row[2]] = votes_by_candidate [row[2]] + 1
          else:
               votes_by_candidate [row[2]] = 1 

 #For life is quite absurd              
          
for key, value in votes_by_candidate.items():
      candidates.append(key)
      votes.append(value)

#And death's the final word

total_votes = sum(votes)

#You must always face the curtain with a bow

for x in votes:
     votes_by_percent.append(round(x/total_votes*100 , 1))

     #Forget about your sin
     #Give the audience a grin

zipit = list(zip(candidates, votes, votes_by_percent))

#Enjoy it - it's your last chance anyhow!

for name in zipit:
    if max(votes) == name[1]:
        Who_wunnit.append(name[0])
        
       #So always look on the bright side of death   

print ("Election Results")

       #Just before you draw your terminal breath
print ("----------------------------")
print ("Total Votes: " + str(total_votes))
print ("----------------------------")
print (str(zipit))
print ("----------------------------")
print ("Winner: " + str(Who_wunnit))
print ("----------------------------")

#Life's a piece of ship 
#When you look at it
#Life's a laugh and death's a joke, it's true 


output_file = os.path.join("Poll_data_final.csv")

#You'll see it's all a show
     #Keep 'em laughin' as you go
           #Just remember that the last laugh is on you
                 # And....

with open(output_file , "w") as file:

#Always look on the bright side of life!

      file.writelines ("Election Results" + "\n")
      file.writelines ("----------------------------" + "\n")
      file.writelines ("Total Votes: " + str(total_votes) + "\n")
      file.writelines ("----------------------------" + "\n")
      file.writelines (str(zipit) + "\n")
      file.writelines ("----------------------------" + "\n")
      file.writelines ("Winner!!!! " + "  Khan  " + "\n")
      file.writelines ("----------------------------" + "\n")
 