#!/usr/bin/env python3
import time,os,sys,logger

source_file=sys.argv[1]
formated_source_file=source_file.split('/')[-1]
backup_dir='/root/lizhixin/python/lesson04/backup/backup_dir/'
backup_to_file='''%s%s_%s.tar.gz'''%(backup_dir,formated_source_file,time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime()))
print(backup_to_file)
def run_backup(runtime='now',exclude_file_name='None'):
	if len(sys.argv)==4:
		print("----------------exclue file mode-----------------")
		if sys.argv[2]=='-X':
			exclude_file_name=sys.argv[3]
			backup_cmd="tar -zcvfX %s %s %s"%(backup_to_file,excludee_file_name,source_file)
	else:
		print('-----------Normal mode-------------')
		backup_cmd="tar -zcvf %s %s "%(backup_to_file,source_file)
	run_command=os.system(backup_cmd)
	if run_command==0:
		logger.record_log("Full backup","Success","N/A","test")
	else:
		logger.record_log("Full backup","Failure","N/A","test")



run_backup()
