import os,glob

chunks = ["10178_5000000","5000001_10000000","10000001_15000000","15000001_20000000","20000001_25000000","25000001_30000000","30000001_35000000","35000001_40000000","40000001_45000000","45000001_50000000","50000001_55000000","55000001_60000000","60000001_65000000","65000001_70000000","70000001_75000000","75000001_80000000","80000001_85000000","85000001_90000000","90000001_95000000","95000001_100000000","100000001_105000000","105000001_110000000","110000001_115000000","115000001_120000000","117000001_121485368","142535440_147000000","147000001_152000000","152000001_157000000","157000001_162000000","162000001_167000000","167000001_172000000","172000001_177000000","177000001_182000000","182000001_187000000","187000001_192000000","192000001_197000000","197000001_202000000","202000001_207000000","207000001_212000000","212000001_217000000","217000001_222000000","222000001_227000000","227000001_232000000","232000001_237000000","237000001_242000000","242000001_247000000","245000001_249240543"]

infoDir = "ID_info/"
mafDir = "frq/"

#chr1_192000001_197000000_using.KRG1KGP.haptovcf.ref_eagle.phased.vcftovcf.impute5.imputation.vcf.gz.frq
#chr1_110000001_115000000_using.KRG1KGP.haptovcf.ref_eagle.phased.vcftovcf.impute5.imputation.vcf.gz_ID_info.txt

#freq
 #CHR                                                                                        SNP   A1   A2          MAF  NCHROBS
 #  1                                                                            1:207000057:T:C    C    T            0    20000
 #  1                                                                             chr1-207000060    A    G       0.3386    20000

#iID_info
#ID	INFO
#1:247000099_G/C	0.482
#1:247000128_C/A	0
outDir = "ID_info_maf/"
os.system("mkdir "+outDir)
def main():
    infos = glob.glob(infoDir + "*txt")
    for info in infos:
        frq = info.replace(infoDir,mafDir).replace("_ID_info.txt",".frq")
        out = open(info.replace(infoDir,outDir).replace("_ID_info.txt","._ID_info.withMAF.txt"),"w")
        info_in = open(info,'r')
        frq_in = open(frq,'r')
        into_header = info_in.readline()
        frq_header = frq_in.readline()
        while True:
            info_line = info_in.readline()
            frq_line = frq_in.readline()
#            if not (info_line and frq_line):
            if not info_line:
                break
            chrom,snp,A1,A2,MAF,NCHROBS = frq_line.replace("\n","").split()
            if float(MAF) > 0.5:
                MAF = 1 - float(MAF)
            out.write(info_line.replace("\n","")+"\t"+MAF +"\n")
        info_in.close()
        frq_in.close()
        out.close()

main()
