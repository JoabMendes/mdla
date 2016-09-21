library(TraMineR)

#Read from csv
behaviours <- read.csv(file="~/workspace/mdla_sedis/kdd_1/4_data_mining/TraMineR/test.csv", header=FALSE)

#Transform into state sequences
#http://traminer.unige.ch/doc/seqdef.html
behaviours.seq <- seqdef(behaviours, informat="STS")

#Transforma into event sequences (without transictions)
#http://traminer.unige.ch/doc/seqecreate.html
behaviours.seqe <- seqecreate(behaviours.seq, teven="state")

#Fiding the frequent subsequences (Frequency = 51%)
#http://traminer.unige.ch/doc/seqefsub.html
fbsubseq <- seqefsub(behaviours.seqe, pMinSupport=0.51)

#export to data frame http://stackoverflow.com/questions/25654008/traminer-subseqelist-export-to-data-frame
plot(fbsubseq, col="cyan")
#plot(fsubseq[1:15], col = "cyan")

#Covert the object subseq as characte (eachonce)(Compressed format)
char_columns <- as.character(fbsubseq$subseq)

#Gives a split for "-" in every line
decom <- seqdecomp(char_columns)

#decom.seq = seqdef(decom, informat="STS")
#seqiplot(decom.seq , withlegend = True, title="Frequent event sequences 50% Frquence")
#write.csv(decom, file="/home/mercosul/joab_workspace/mdla_sedis/kdd_1/4_data_mining/TraMineR/test_frequent_subsequences.csv", row.name=FALSE, na="")

write.table(decom, file="~/workspace/mdla_sedis/kdd_1/4_data_mining/TraMineR/test_frequent_subsequences.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
