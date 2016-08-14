def tower(disks,start=1,end=3):
	if disks:
		tower(disks=disks-1,start=6-start-end,end=end)
		print("Moved disk {} from peg {} to peg {}".format(disks,start,end))
		tower(disks=disks-1,start=start,end=6-start-end)
tower(3)