
joblist = []
plist = []
M={}
rec_calls = 0

def p(job_ind):
	for j in range(job_ind,-1,-1):
		if joblist[j][1] <= joblist[job_ind][0]:
			return j
	return -1

def compute_opt(j):
	global rec_calls
	rec_calls += 1
	if j == -1: 
		return 0
	else:
		return max(joblist[j][2] + compute_opt(plist[j]), compute_opt(j-1))

def M_compute_opt(j):
	global rec_calls
	rec_calls += 1
	if M[j]==None:
		M[j] = max(joblist[j][2] + M_compute_opt(plist[j]), M_compute_opt(j-1))
	return M[j]

def mem_wis(jobs):
	global joblist
	global plist
	global M
	 
	for e in range(len(jobs)):
		M[e] = None
	M[-1]=0
	joblist = jobs
	joblist = sorted(joblist, key=lambda tup: tup[1])
	plist = [p(i) for i in range(len(joblist))]
	return M_compute_opt(len(joblist)-1)

def rec_wis(jobs):
	global joblist
	global plist
	joblist = jobs

	if len(joblist) == 0: return 0
	if len(joblist) == 1: return joblist[0][2]

	joblist = sorted(joblist, key=lambda tup: tup[1])
	plist = [p(i) for i in range(len(joblist))]
	
	return compute_opt(len(joblist)-1)

def iterative_compute_opt(n):
	global M
	M[-1] = 0
	for j in range(n):
		M[j] = max(joblist[j][2] + M[p(j)], M[j-1])
		

def iter_wis(jobs):
	global joblist
	global plist
	joblist = sorted(jobs, key=lambda tup: tup[1])
	iterative_compute_opt(len(joblist))
	return max(M.values())

lworse = [(1,3,1),(2,5,1),(4,7,1),(6,9,1),(8,11,1),(10,13,1),(12,15,1)]
lnormal = [(1,4,1), (3,5,1),(0,6,1),(4,7,1),(3,8,1),(5,9,1),(6,10,1),(8,11,1)]
lworse = []
r= raw_input()
for n in range(20):

	for i in range(n):
		t = (i,i+2,1)
		lworse.append(t)
	print n, "<<<<<<<<<<<<<<<<"
	rec_wis(lworse)
	print rec_calls	, "rec_wis"
	rec_calls = 0	
	mem_wis(lworse)
	print rec_calls	,"mem_wis"
	print iter_wis(lworse)
	print "<<<<<<<<<<<<<<<<<<<<"





			
