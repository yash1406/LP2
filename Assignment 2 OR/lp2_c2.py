from pprint import pprint

tasks = dict()
f = open('cpm.txt')

for l in f:
    data=list(l.split(','))
    for i in range(len(data)):
        tasks['task'+ str(data[0])]= dict()
        tasks['task'+ str(data[0])]['id'] = data[0]
        tasks['task'+ str(data[0])]['name'] = data[1]
        tasks['task'+ str(data[0])]['duration'] = data[2]
        if(data[3] != "\n"):
            tasks['task'+ str(data[0])]['dependencies'] = list(data[3].strip().split(';'))
        else:
            tasks['task'+ str(data[0])]['dependencies'] = ['-1']
        tasks['task'+ str(data[0])]['ES'] = 0
        tasks['task'+ str(data[0])]['EF'] = 0
        tasks['task'+ str(data[0])]['LS'] = 0
        tasks['task'+ str(data[0])]['LF'] = 0
        tasks['task'+ str(data[0])]['float'] = 0
        tasks['task'+ str(data[0])]['isCritical'] = False

pprint(tasks["task6"])

# Forward Pass

for tf in tasks.keys():
    if('-1' in tasks[tf]['dependencies']):
        tasks[tf]['ES'] = 0
        tasks[tf]['EF'] = (tasks[tf]['duration'])
    else:
        for t in tasks.keys():
            for d in tasks[t]['dependencies']:
                if(d != '-1' and len(tasks[t]['dependencies']) == 1):
                    tasks[t]['ES'] = int(tasks['task'+ str(d)]['EF'])
                    tasks[t]['EF'] = int(tasks[t]['ES']) + int(tasks[t]['duration'])
                elif(d !='-1'):
                    if(int(tasks['task'+d]['EF']) > int(tasks[t]['ES'])):
                        tasks[t]['ES'] = int(tasks['task'+ str(d)]['EF'])
                        tasks[t]['EF'] = int(tasks[t]['ES']) + int(tasks[t]['duration'])

lis=list(tasks.keys())
lis.reverse()

# Backward Pass

for tb in lis:
    if(tb==lis[0]):
        tasks[tb]['LF']=tasks[tb]['EF']
        tasks[tb]['LS']=tasks[tb]['ES']
        
    for d in tasks[tb]['dependencies']:
        if(d != '-1'):
            if(tasks['task'+ d]['LF'] == 0): #check if the the dependency is already analyzed
                tasks['task'+ d]['LF'] = int(tasks[tb]['LS'])
                tasks['task'+ d]['LS'] = int(tasks['task'+ d]['LF']) - int(tasks['task'+ d]['duration'])
                tasks['task'+ d]['float'] = int(tasks['task'+ d]['LF']) - int(tasks['task'+ d]['EF'])
            if(int(tasks['task'+ d]['LF']) >int(tasks[tb]['LS'])):
                tasks['task'+ d]['LF'] = int(tasks[tb]['LS'])
                tasks['task'+ d]['LS'] = int(tasks['task'+ d]['LF']) - int(tasks['task'+ d]['duration'])
                tasks['task'+ d]['float'] = int(tasks['task'+ d]['LF']) - int(tasks['task'+ d]['EF'])
            

# Critical Path

print('tid\t name\t dur\t ES\t EF\t LS\t LF\t float\t isCritical')
for task in tasks:
    if(tasks[task]['float'] == 0):
        tasks[task]['isCritical'] = True
    print(str(tasks[task]['id']) +'\t'+str(tasks[task]['name']) +'\t'+str(tasks[task]['duration']) +'\t'+str(tasks[task]['ES']) +'\t'+str(tasks[task]['EF']) +'\t'+str(tasks[task]['LS']) +'\t'+str(tasks[task]['LF']) +'\t'+str(tasks[task]['float']) +'\t'+str(tasks[task]['isCritical']))




