N,M,K = map(int,input().split())

woman_team = N//2
man_team = M

team_count = min(woman_team,man_team)
intern = (N-team_count*2) + (man_team-team_count)

while K > intern :
    intern+=3
    team_count-=1

print(team_count) 