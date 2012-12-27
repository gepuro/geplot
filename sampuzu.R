#!/usr/bin/Rscript

config <- read.table("stdin", stringsAsFactors=FALSE, sep="\t")
filename <- config$V1
xlab <- config$V2
ylab <- config$V3
main <- config$V4
usegrid <- config$V5
type <- config$V6

dat <- read.csv(paste("./data/", filename, sep=""), header=FALSE)

png(file=paste("./graph/", filename, ".png", sep=""))
plot(dat$V1, dat$V2, xlab=xlab, ylab=ylab, main=main, type=type)
if( usegrid == 1 ){
  grid()
}
dev.off()
