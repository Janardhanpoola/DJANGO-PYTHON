import glob,os,re,shutil

os.chdir("C:/Users/jpoola/Pictures/Camera Roll")

master_dir=os.getcwd()
print(master_dir)

all_files=os.listdir()

rem_list=['docs &certis','github-recovery-codes.txt','TCS docs']

[all_files.remove(i) for i in rem_list]

#print(all_files)


payslip_2020,payslip_2021=[i for i in all_files if re.search(r'Payslip.*_2020',i)],[i for i in all_files if re.search(r'Payslip.*_2021',i)]

Taxst,PF=[i for i in all_files if re.search("Annual.*",i)],[i for i in all_files if re.search("Provident.*|PF.*",i)]

#print(payslip_2020,payslip_2021)

print(Taxst,PF)

subdir="/TCS docs/"

os.chdir(master_dir+subdir+"payslips/payslips_2020")

for i in payslip_2020:
    shutil.move(os.path.join(master_dir,i),os.getcwd())

os.chdir(master_dir+subdir+"payslips/payslips_2021")

for i in payslip_2021:
    shutil.move(master_dir+i,os.getcwd())



new_dirs=['Tax statements','PF docs']

for i in new_dirs:
    if not os.path.exists(master_dir+subdir+i):
        os.mkdir(i)


for i in Taxst:
    shutil.move(os.path.join(master_dir,i),master_dir+subdir+'Tax statements')

for i in PF:
    shutil.move(os.path.join(master_dir,i),master_dir+subdir+'PF docs')

os.chdir(master_dir+subdir+'Tax statements')





