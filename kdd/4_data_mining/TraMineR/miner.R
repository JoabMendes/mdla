library(TraMineR)

#Read from csv
behaviours <- read.csv(file="~/workspace/mdla_sedis/kdd_1/4_data_mining/TraMineR/input.csv", header=FALSE)
print(" =========== Read sequences ========= ")
#Transform into state sequences
#http://traminer.unige.ch/doc/seqdef.html
behaviours.seq <- seqdef(behaviours, informat="STS")
print(" =========== Defined sequences ========= ")

#Transforma into event sequences (without transictions)
#http://traminer.unige.ch/doc/seqecreate.html
behaviours.seqe <- seqecreate(behaviours.seq, teven="state")
print(" =========== Turned into event sequences ========= ")

#Fiding the frequent subsequences (Frequency = 51%)
#http://traminer.unige.ch/doc/seqefsub.html
fbsubseq <- seqefsub(behaviours.seqe, pMinSupport=0.51)
print(" =========== Found the frequente subsequences ========= ")

#export to data frame http://stackoverflow.com/questions/25654008/traminer-subseqelist-export-to-data-frame
#plot(fbsubseq[1:20], col = "cyan")
#plot(fsubseq[1:15], col = "cyan")

#Covert the object subseq as characte (eachonce)(Compressed format)
char_columns <- as.character(fbsubseq$subseq)

#Gives a split for "-" in every line
decom <- seqdecomp(char_columns)

#decom.seq = seqdef(decom, informat="STS")
#seqiplot(decom.seq , withlegend = True, title="Frequent event sequences 50% Frquence")

#Writing results on csv
print(" =========== saving ========= ")
write.table(decom, file="~/workspace/mdla_sedis/kdd_1/4_data_mining/TraMineR/frequent_subsequences.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
