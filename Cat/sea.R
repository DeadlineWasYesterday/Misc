library(DESeq2)
library(dplyr)
library(ggplot2)
library(gplots)
library(AnnotationHub)
library(AnnotationDbi)

setwd('../Downloads/')

countData = read.csv('c.tsv', header=1, sep = '\t')
rownames(countData)=countData$Gene
countData = countData[,-1]

countData = countData[,1:8]

countData = countData[rowSums(countData) > 0,]

par(mar=c(5.1, 4.1, 4.1, 2.1))
barplot(colSums(countData), las=3)

hist(countData$c16, br=100)

plot(logcountData[,2], logcountData[,4])

plot(logcountData[,2], logcountData[,1])

treatment = rep('dm', 8)

colData = as.data.frame(cbind(colnames(countData), treatment))
colData

dds = DESeqDataSetFromMatrix(countData = countData, 
                             colData = colData,
                             design = ~1)
dds = DESeq(dds)

nrow(dds)

dds <- estimateSizeFactors(dds)

nc <- counts(dds, normalized = TRUE)

ch1 <- rowSums(nc[,1:8])

hist(log10(ch1))

ggplot(mapping = aes(log2(ch1 + 0.001))) + 
  geom_histogram(colour = 4, fill = "blue", 
                 bins = 300)

ggsave('ch1.png', scale = 3)


countData = read.csv('c.tsv', header=1, sep = '\t')
rownames(countData)=countData$Gene
countData = countData[,-1]
countData = countData[,9:16]
countData = countData[rowSums(countData) > 0,]

treatment = rep('dm', 8)

colData = as.data.frame(cbind(colnames(countData), treatment))

dds = DESeqDataSetFromMatrix(countData = countData, 
                             colData = colData,
                             design = ~1)
dds = DESeq(dds)

dds <- estimateSizeFactors(dds)

nc <- counts(dds, normalized = TRUE)

ch1 <- rowSums(nc[,1:8])

ggplot(mapping = aes(log2(ch1 + 0.001))) + 
  geom_histogram(colour = 4, fill = "blue", 
                 bins = 300)

ggsave('ch2.png', scale = 3)




ggplot(mapping = aes(log2(read.csv('c.tsv', header=1, sep = '\t')[,13]))) + 
  geom_histogram(colour = 4, fill = "blue", 
                 bins = 300)

library(edgeR)

y <- DGEList(counts = countData, group = rep('dm', 16))
keep <- filterByExpr(y)
y <- y[keep,,keep.lib.sizes=FALSE]
y <- calcNormFactors(y)

y$counts
group <- factor(rep(1, 16))
design <- model.matrix(~group)


tl = read.delim('tl.tsv', header = FALSE)
ct = read.csv('c.tsv', header=1, sep = '\t')

rownames(ct)=ct$Gene
ct = ct[,-1]

#ct <- ct[1:8]
#ct <- ct[9:16]

par(mar=c(5.1, 4.1, 4.1, 2.1))
barplot(colSums(ct), las=3)


ct <- ct + 0.001
ct = ct[tl$V1,]

ct2 <- ct/tl$V2

ct2 <- ct2*1000

ct3 <- sweep(ct2, 2, colSums(ct2), `/`)

ct3  <- ct3*1000000

write.table(ct3, 'cg.tsv', sep = '\t', col.names = FALSE)
