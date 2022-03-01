import os
import platform
import re
import logging
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.info('start of the program')


def init_proc_cat_prod(cat_prod_dict):
    cat_prod_dict["ACECLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ADAPTIVEREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["AGGREGATION"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["ALLELE"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["ANOM"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["ANOVA"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["APPEND"] = ("Base SAS", "Data Management")
    cat_prod_dict["APPSRV"] = ("SAS/IntrNet", "SAS ENV")
    cat_prod_dict["ARIMA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["AUTHLIB"] = ("Base SAS", "Data Management")
    cat_prod_dict["AUTOREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["BCHOICE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BGLIMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BINNING"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["BLIMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BMDP"] = ("Base SAS", "Data Management")
    cat_prod_dict["BOM"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["BOXPLOT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["BOXPLOT"] = ("SAS/STAT", "Advanced Analytics")
    cat_prod_dict["BTL"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["BUILD"] = ("SAS/AF", "SAS ENV")
    cat_prod_dict["CALENDAR"] = ("Base SAS", "Data Management")
    cat_prod_dict["CALIS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CALLRFC"] = ("Base SAS", "Data Management")
    cat_prod_dict["CANCORR"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CANDISC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAPABILITY"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["CARDINALITY"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["CARIMA"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CASECONTROL"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["CATALOG"] = ("Base SAS", "Data Management")
    cat_prod_dict["CATMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAUSALGRAPH"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAUSALMED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CAUSALTRT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CCDM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CCOPULA"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CDISC"] = ("Base SAS", "Data Management")
    cat_prod_dict["CESM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CHART"] = ("Base SAS", "Reporting")
    cat_prod_dict["CIMPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["CLP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["CLUSTER"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["CNTSELECT"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["COMPARE"] = ("Base SAS", "Data Management")
    cat_prod_dict["COMPILE"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["COMPUTAB"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["CONTENTS"] = ("Base SAS", "Data Management")
    cat_prod_dict["CONVERT"] = ("Base SAS", "Data Management")
    cat_prod_dict["COPULA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["COPY"] = ("Base SAS", "Data Management")
    cat_prod_dict["CORR"] = ("Base SAS", "Data Management")
    cat_prod_dict["CORRELATION"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["CORRESP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["COUNTREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["CPANEL"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CPM"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["CPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["CQLIM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CSPATIALREG"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["CUSUM"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["CV2VIEW"] = ("Base SAS", "Data Management")
    cat_prod_dict["DATASETS"] = ("Base SAS", "Data Management")
    cat_prod_dict["DATASOURCE"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["DATEKEYS"] = ("Base SAS", "Data Management")
    cat_prod_dict["DB2EXT"] = ("Base SAS", "Data Management")
    cat_prod_dict["DB2UTIL"] = ("Base SAS", "Data Management")
    cat_prod_dict["DBCSTAB"] = ("Base SAS", "Data Management")
    cat_prod_dict["DBF"] = ("Base SAS", "Data Management")
    cat_prod_dict["DBLOAD"] = ("Base SAS", "Data Management")
    cat_prod_dict["DCBSTAB"] = ("Base SAS", "Data Management")
    cat_prod_dict["DELETE"] = ("Base SAS", "Data Management")
    cat_prod_dict["DIF"] = ("Base SAS", "Data Management")
    cat_prod_dict["DISCRIM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["DISPLAY"] = ("Base SAS", "Data Management")
    cat_prod_dict["DISTANCE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["DISTANCE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["DMSRVADM"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DMSRVDATASVC"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DMSRVPROCESSSVC"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DMSSRVPROCESSSVC"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DOCPARSE"] = ("SAS Text Miner", "Analytics")
    cat_prod_dict["DOCUMENT"] = ("Base SAS", "Data Management")
    cat_prod_dict["DOWNLOAD"] = ("SAS/CONNECT", "SAS ENV")
    cat_prod_dict["DQLOCLST"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DQMATCH"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DQSCHEME"] = ("SAS Data Quality Server", "Data Management")
    cat_prod_dict["DS2"] = ("Base SAS", "Advanced Data Management")
    cat_prod_dict["DSTODS2"] = ("Base SAS", "Data Management")
    cat_prod_dict["DTREE"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["ECM"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["ENTROPY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["ESM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["EXPAND"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["EXPLODE"] = ("Base SAS", "Data Management")
    cat_prod_dict["EXPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["FACTEX"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["FACTOR"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FAMILY"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["FASTCLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FCMP"] = ("Base SAS", "Data Management")
    cat_prod_dict["FEDSQL"] = ("Base SAS", "Data Management")
    cat_prod_dict["FMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FONTREG"] = ("Base SAS", "Data Management")
    cat_prod_dict["FORECAST"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["FORMAT"] = ("Base SAS", "Data Management")
    cat_prod_dict["FORMS"] = ("Base SAS", "Data Management")
    cat_prod_dict["FREQ"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["FREQTAB"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["FSBROWSE"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["FSEDIT"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["FSLETTER"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["FSLIST"] = ("Base SAS", "Data Management")
    cat_prod_dict["FSVIEW"] = ("SAS/FSP", "Data Management")
    cat_prod_dict["G3D"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["G3GRID"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GA"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["GAM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GAMMOD"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["GAMPL"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GAMSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["GANNO"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GANTT"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["GAREABAR"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GBARLINE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GCHART"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GCONTOUR"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GDEVICE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GEE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GENESELECT"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["GENMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GEOCODE"] = ("Base SAS", "Reporting")
    cat_prod_dict["GFONT"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GINSIDE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GIS"] = ("SAS/GIS", "Advanced Analytics")
    cat_prod_dict["GKPI"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GLIMMIX"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLMMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLMPOWER"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GLMSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["GMAP"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GOPTIONS"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GPLOT"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GPROJECT"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GRADAR"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GREDUCE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GREMOVE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GREPLAY"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GROOVY"] = ("Base SAS", "Data Management")
    cat_prod_dict["GSLIDE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["GTILE"] = ("SAS/GRAPH", "Reporting")
    cat_prod_dict["HADOOP"] = ("Base SAS", "Data Management")
    cat_prod_dict["HAPLOTYPE"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["HDMD"] = ("Base SAS", "Data Management")
    cat_prod_dict["HP4SCORE"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPBIN"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPBNET"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPBOOLRULE"] = ("SAS Text Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPCANDISC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPCDM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPCLUS"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPCOPULA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPCORR"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPCOUNTREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPDECIDE"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPDMDB"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPDS2"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPEXPORT"] = ("SAS High-Performance Risk", "Advanced Analytics")
    cat_prod_dict["HPF"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFARIMASPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFDIAGNOSE"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFENGINE"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFESMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFEVENTS"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFEXMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFIDMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFMM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPFOREST"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPFRECONCILE"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFREPOSITORY"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFSELECT"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFTEMPRECON"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPFUCMSPEC"] = ("SAS Forecast Server", "Advanced Analytics")
    cat_prod_dict["HPGENSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPIMPUTE"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPLMIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPLOGISTIC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPMIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPNEURAL"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPNLMOD"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPPANEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPPLS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPPRINCOMP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPQLIM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPQUANTSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPREDUCE"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPRISK"] = ("SAS High-Performance Risk", "Advanced Analytics")
    cat_prod_dict["HPSAMPLE"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPSEVERITY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["HPSPLIT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["HPSUMMARY"] = ("Base SAS High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPSVM"] = ("SAS Enterprise Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPTMINE"] = ("SAS Text Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HPTMSCORE"] = ("SAS Text Miner High-Performance Procedures", "Advanced Analytics")
    cat_prod_dict["HTSNP"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["HTTP"] = ("Base SAS", "Data Management")
    cat_prod_dict["ICA"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["ICLIFETEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ICPHREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["IML"] = ("SAS/IML", "Advanced Analytics")
    cat_prod_dict["IMPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["IMSTAT"] = ("SAS LASR Analytic Server", "Advanced Data Management")
    cat_prod_dict["IMXFER"] = ("SAS LASR Analytic Server", "Advanced Data Management")
    cat_prod_dict["INBREED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["INFOMAPS"] = ("Base SAS", "Reporting")
    cat_prod_dict["IOMOPERATE"] = ("SAS Integration Technologies", "SAS ENV")
    cat_prod_dict["IRT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ISHIKAWA"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["ITEMS"] = ("Base SAS", "Data Management")
    cat_prod_dict["JAVAINFO"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["JSON"] = ("Base SAS", "Data Management")
    cat_prod_dict["KCLUS"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["KDE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["KRIGE2D"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LASR"] = ("SAS LASR Analytic Server", "Advanced Analytics")
    cat_prod_dict["LATTICE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LIFEREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LIFETEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LMIXED"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["LOAN"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["LOCALEDATA"] = ("Base SAS", "Data Management")
    cat_prod_dict["LOESS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LOGISTIC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["LOGSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["LUA"] = ("Base SAS", "Data Management")
    cat_prod_dict["MACONTROL"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["MAPIMPORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["MBC"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["MCMC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MDC"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["MDDB"] = ("SAS/MDDB Server", "Reporting")
    cat_prod_dict["MDS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MEANS"] = ("Base SAS", "Analytics")
    cat_prod_dict["METADATA"] = ("Base SAS", "Data Management")
    cat_prod_dict["METALIB"] = ("Base SAS", "Data Management")
    cat_prod_dict["METAOPERATE"] = ("Base SAS", "Data Management")
    cat_prod_dict["MI"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MIANALYZE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MIGRATE"] = ("Base SAS", "Data Management")
    cat_prod_dict["MIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MODECLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MODEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["MODELMATRIX"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["MULTTEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["MVPDIAGNOSE"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["MVPMODEL"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["MVPMONITOR"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["NESTED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["NETDRAW"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["NLIN"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["NLMIXED"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["NLMOD"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["NMF"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["NPAR1WAY"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ODSLIST"] = ("Base SAS", "Reporting")
    cat_prod_dict["ODSTABLE"] = ("Base SAS", "Reporting")
    cat_prod_dict["ODSTEXT"] = ("Base SAS", "Reporting")
    cat_prod_dict["OLAP"] = ("SAS OLAP Server", "Reporting")
    cat_prod_dict["OLAPCONTENTS"] = ("SAS OLAP Server", "Reporting")
    cat_prod_dict["OLAPOPERATE"] = ("SAS OLAP Server", "Reporting")
    cat_prod_dict["OPERATE"] = ("SAS/SHARE", "SAS ENV")
    cat_prod_dict["OPTEX"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["OPTGRAPH"] = ("SAS OPTGRAPH Procedure", "Advanced Analytics")
    cat_prod_dict["OPTIONS"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["OPTLOAD"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["OPTLP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTLSO"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["OPTMILP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTMODEL"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTNET"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["OPTNETWORK"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTQP"] = ("SAS Optimization", "Advanced Analytics")
    cat_prod_dict["OPTSAVE"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["ORTHOREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PANEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["PARETO"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["PARTITION"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PCA"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PDLREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["PDS"] = ("Base SAS", "Data Management")
    cat_prod_dict["PDSCOPY"] = ("Base SAS", "Data Management")
    cat_prod_dict["PHREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PHSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PLAN"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PLM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PLOT"] = ("Base SAS", "Data Management")
    cat_prod_dict["PLS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PLSMOD"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["PM"] = ("SAS/OR", "Advanced Analytics")
    cat_prod_dict["PMENU"] = ("Base SAS", "Data Management")
    cat_prod_dict["POWER"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRESENV"] = ("Base SAS", "Data Management")
    cat_prod_dict["PRINCOMP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRINQUAL"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRINT"] = ("Base SAS", "Reporting")
    cat_prod_dict["PRINTTO"] = ("Base SAS", "Reporting")
    cat_prod_dict["PROBIT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PRODUCT_STATUS"] = ("Base SAS", "SAS ENV")
    cat_prod_dict["PROTO"] = ("Base SAS", "Data Management")
    cat_prod_dict["PRTDEF"] = ("Base SAS", "Data Management")
    cat_prod_dict["PRTEXP"] = ("Base SAS", "Data Management")
    cat_prod_dict["PSMATCH"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["PSMOOTH"] = ("SAS/Genetics", "Advanced Analytics")
    cat_prod_dict["PWENCODE"] = ("Base SAS", "Data Management")
    cat_prod_dict["QDEVICE"] = ("Base SAS", "Data Management")
    cat_prod_dict["QLIM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["QTRSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["QUANTLIFE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["QUANTREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["QUANTSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["QUEST"] = ("SAS/ACCESS", "Data Management")
    cat_prod_dict["RANK"] = ("Base SAS", "Data Management")
    cat_prod_dict["RAREEVENTS"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["RDC"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RDPOOL"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RDSEC"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RECOMMEND"] = ("SAS LASR Analytic Server", "Advanced Analytics")
    cat_prod_dict["REG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["REGISTRY"] = ("Base SAS", "Data Management")
    cat_prod_dict["REGSELECT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["RELEASE"] = ("Base SAS", "Data Management")
    cat_prod_dict["RELIABILITY"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["REPORT"] = ("Base SAS", "Reporting")
    cat_prod_dict["RISK"] = ("SAS Risk Dimensions", "Advanced Analytics")
    cat_prod_dict["RMSTREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["ROBUSTREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["RSREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["S3"] = ("Base SAS", "Data Management")
    cat_prod_dict["SANDWICH"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["SCA"] = ("Base SAS", "Data Management")
    cat_prod_dict["SCAPROC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SCORE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SCOREACCEL"] = ("Base SAS", "Analytics")
    cat_prod_dict["SEQDESIGN"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SEQTEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SERVER"] = ("SAS/SHARE", "SAS ENV")
    cat_prod_dict["SEVERITY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SEVSELECT"] = ("SAS Econometrics", "Advanced Analytics")
    cat_prod_dict["SGDESIGN"] = ("Base SAS", "Analytics")
    cat_prod_dict["SGMAP"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGPANEL"] = ("Base SAS", "Analytics")
    cat_prod_dict["SGPIE"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGPLOT"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGRENDER"] = ("Base SAS", "Reporting")
    cat_prod_dict["SGSCATTER"] = ("Base SAS", "Reporting")
    cat_prod_dict["SHEWHART"] = ("SAS/QC", "Advanced Analytics")
    cat_prod_dict["SIM2D"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SIMILARITY"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SIMLIN"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SIMNORMAL"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SIMSYSTEM"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["SOAP"] = ("Base SAS", "Data Management")
    cat_prod_dict["SORT"] = ("Base SAS", "Data Management")
    cat_prod_dict["SOURCE"] = ("Base SAS", "Data Management")
    cat_prod_dict["SPATIALREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SPC"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["SPDO"] = ("SAS Scalable Performance Data Server", "Data Management")
    cat_prod_dict["SPECTRA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["SPP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SQL"] = ("Base SAS", "Data Management")
    cat_prod_dict["SQOOP"] = ("Base SAS", "Data Management")
    cat_prod_dict["SSM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["STANDARD"] = ("Base SAS", "Data Management")
    cat_prod_dict["STATESPACE"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["STDIZE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["STDRATE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["STEPDISC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["STP"] = ("SAS Integration Technologies", "SAS ENV")
    cat_prod_dict["STREAM"] = ("Base SAS", "Data Management")
    cat_prod_dict["SUMMARY"] = ("Base SAS", "Analytics")
    cat_prod_dict["SURVEYFREQ"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYIMPUTE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYLOGISTIC"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYMEANS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYPHREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SURVEYSELECT"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["SYSLIN"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TABULATE"] = ("Base SAS", "Reporting")
    cat_prod_dict["TAPECOPY"] = ("Base SAS", "Data Management")
    cat_prod_dict["TAPELABEL"] = ("Base SAS", "Data Management")
    cat_prod_dict["TEMPLATE"] = ("Base SAS", "Data Management")
    cat_prod_dict["TIMEDATA"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TIMEID"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TIMEPLOT"] = ("Base SAS", "Analytics")
    cat_prod_dict["TIMESERIES"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TMODEL"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TPSPLINE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["TRANSPOSE"] = ("Base SAS", "Analytics")
    cat_prod_dict["TRANSREG"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["TRANTAB"] = ("Base SAS", "Data Management")
    cat_prod_dict["TREE"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["TREESPLIT"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["TSCSREG"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["TTEST"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["UCM"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["UNIVARIATE"] = ("Base SAS", "Analytics")
    cat_prod_dict["UPLOAD"] = ("SAS/CONNECT", "SAS ENV")
    cat_prod_dict["VARCLUS"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["VARCOMP"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["VARIMPUTE"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["VARIOGRAM"] = ("SAS/STAT", "Analytics")
    cat_prod_dict["VARMAX"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["VARREDUCE"] = ("SAS Visual Statistics", "Advanced Analytics")
    cat_prod_dict["VASMP"] = ("SAS LASR Analytic Server", "Advanced Analytics")
    cat_prod_dict["X11"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["X12"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["X13"] = ("SAS/ETS", "Advanced Analytics")
    cat_prod_dict["XSL"] = ("Base SAS", "Data Management")

    # proc_df = pd.read_excel('proc.xls')
    # proc_list = proc_df.values.tolist()
    #
    # for step, proc, prod in proc_list:
    #     print('cat_prod_dict["' + step.encode('utf-8', 'ignore').strip() + '"]=("' + proc.encode('utf-8',
    #     'ignore').strip() + '", "' + prod.encode('utf-8', 'ignore').strip() + '")')

    return cat_prod_dict


def getInventory(current_path, current_folder, visited, file_list):
    if platform.system() == 'Windows':
        current_path = current_path + '\\' + current_folder
    else:
        current_path = current_path + '/' + current_folder

    visited[current_path] = True
    logging.debug("current path is " + current_path)
    folders = []
    current_path_files = os.listdir(current_path)
    for file_or_folder in current_path_files:

        if platform.system() == 'Windows':
            pointedPath = current_path + '\\' + file_or_folder
        else:
            pointedPath = current_path + '/' + file_or_folder
        if os.path.isdir(pointedPath):
            folders.append(file_or_folder)
        else:
            file_list.append((current_path, file_or_folder))

    logging.debug("file list is")
    for filepath, filename in file_list:
        logging.debug(filepath + " " + filename)
    logging.debug("***************************")
    for child_folder in folders:

        if platform.system() == 'Windows':
            pointedPath = current_path + '\\' + child_folder
        else:
            pointedPath = current_path + '/' + child_folder

        if visited.get(pointedPath) is None:
            logging.debug("go down to " + child_folder)
            getInventory(current_path, child_folder, visited, file_list)


def get_sas_file_id(current_path, current_folder, visited, file_list):
    if platform.system() == 'Windows':
        current_path = current_path + '\\' + current_folder
    else:
        current_path = current_path + '/' + current_folder

    visited[current_path] = True
    logging.debug("current path is " + current_path)
    folders = []
    current_path_files = os.listdir(current_path)
    for file_or_folder in current_path_files:
        if platform.system() == 'Windows':
            child_path = current_path + '\\' + file_or_folder
        else:
            child_path = current_path + '/' + file_or_folder

        if os.path.isdir(child_path):
            folders.append(file_or_folder)
        else:

            file_list.append((current_path, file_or_folder))

    for child_folder in folders:

        if platform.system() == 'Windows':
            child_path = current_path + '\\' + child_folder
        else:
            child_path = current_path + '/' + child_folder

        if visited.get(child_path) is None:
            logging.debug("go down to " + child_folder)
            getInventory(current_path, child_folder, visited, file_list)

    sas_file_dict = dict()
    counter = 1
    sas_extensions = ['ddf', 'djf', 'egp', 'sas', 'sas7bcat', 'sas7bdat', 'sas7bitm', 'sc2', 'sct01', 'sd2', 'spds9',
                      'sri', 'ssd01', 'xsq']
    for path, file_name in file_list:
        extension = file_name.split('.')[1]
        if extension in sas_extensions:
            sas_file_dict[file_name] = 'SF_' + str(counter)
            counter+=1
    return sas_file_dict


# read log contents from given file_path
# return log file as a big string
# completed
def get_log_content(file_path):
    file_object = open(file_path)
    file_content = file_object.read()
    file_object.close()
    return file_content


# get all the user name of the given log file
# return a list of usernames
# comment: need to implement multi-user cases (1/14)
def get_user_name(log_content):
    user_name_regex = re.compile(r".*?].*?:(.*) - ")
    user_name_obj = user_name_regex.search(log_content[:1000])
    user_name = user_name_obj.group(1).split('@')
    return user_name[0]


# provide a user's log file content given username and log_content
# comment: need to implement split the log content based on the given user name (1/14)
def get_user_log_content(user, log_content):
    return log_content


# input data: user's log content
# split the user's log content based on SAS file
# make a list of pair of SAS file name and the SAS file's log content
# comment: need to implement SAS file line number part here (1/14)
def get_sas_files(user_log_content):
    sas_content_list = user_log_content.split("%LET _CLIENTPROJECTPATH=")

    sas_content_numbered_list = sas_line_number_counter(sas_content_list)
    sas_file_list = []
    # print(len(sas_content_numbered_list))

    for sas_content in sas_content_numbered_list:
        # print(sas_content[:890])
        program_file_regex = re.compile(r" _SASPROGRAMFILE=(.*);")
        program_file_list = program_file_regex.findall(sas_content)
        # print(program_file_list)

        project_path_regex = re.compile(r" _CLIENTPROJECTPATH=(.*);")
        project_path_list = project_path_regex.findall(sas_content)
        # print(project_path_list)

        if len(program_file_list) != 0 and len(program_file_list[0]) > 3:
            sas_file_list.append(program_file_list[0][1:-1])
        elif len(project_path_list) != 0 and len(project_path_list[0]) > 3:
            sas_file_list.append(project_path_list[0][1:-1])
        else:
            sas_file_list.append("")
        # print("^^^^^^^^")

    zipped_sas_file_content_list = tuple(zip(sas_file_list, sas_content_numbered_list))

    return zipped_sas_file_content_list


def sas_line_number_counter(sas_content_list):
    temp_chunk = ""

    sas_content_numbered_list = []
    sas_full_content_list = []
    # recover the lost part when log file is split
    for count, content in enumerate(sas_content_list):
        if count != 0:
            content = "%LET _CLIENTPROJECTPATH=" + content
        sas_full_content_list.append(content)

    # line number counting for the first part of the sas log file (usually SAS initialization)
    for line_num, line in enumerate(sas_full_content_list[0].splitlines(True)):
        temp_chunk += str(line_num + 1) + "  " + line

    sas_content_numbered_list.append(temp_chunk)

    temp_chunk = ""
    # line number counting for the remaining parts
    for sas_content in sas_full_content_list[1:]:

        line_number_regex = re.compile(r"\n\d\d\d\d-\d\d-.* - (\d+) ")
        line_number_regex_obj = line_number_regex.search(sas_content)
        start_line_number = int(line_number_regex_obj.group(1))

        for line in sas_content.splitlines(True):
            temp_chunk += str(start_line_number - 1) + "  " + line
            start_line_number += 1
        sas_content_numbered_list.append(temp_chunk)
        temp_chunk = ""

    return sas_content_numbered_list


def get_sas_file_line_number(record_content):
    sas_file_line_regex = re.compile(r"(.*)  \d\d\d\d-\d\d-\d\d.*\(Total process time\):")
    sas_file_line_obj = sas_file_line_regex.search(record_content)
    if sas_file_line_obj is None:
        return ""
    else:
        return float(sas_file_line_obj.group(1))


# get input file such as *.csv
# if there is not an input file, then return ""
# completed
def get_input_file_name(sas_file_content):
    input_file_name_regex = re.compile(r"NOTE: The infile \'(.*)\' is:")
    input_file_list = input_file_name_regex.findall(sas_file_content)

    input_file_dict = dict()

    for input_file in input_file_list:
        if not input_file_dict.get(input_file):
            input_file_dict[input_file] = '0'

    input_row_file_name_regex = re.compile(r"NOTE: (.*) records were read from the infile \'(.*)\'.")
    input_row_file_list = input_row_file_name_regex.findall(sas_file_content)

    for row, input_file in input_row_file_list:
        input_file_dict[input_file] = row

    rows = ''
    input_files = ''
    if len(input_file_dict) != 0:
        for input_file, row in input_file_dict.items():
            rows += ';' + row
            input_files += ';' + input_file

    return rows[1:], input_files[1:]


# get SAS Step names such as DATA statement, Procedure SQL, SAS Initialization
# return SAS STEP (such as DATA statement) and SAS Step name (ex)sql, Data
# Completed but need to check if there is any other case regarding SAS Step (1/14)
def get_sas_step_name(sas_file_content):
    sas_step_name_regex = re.compile(r"NOTE: (.*) (.*) used")
    sas_step_name_regex_obj = sas_step_name_regex.search(sas_file_content)

    if sas_step_name_regex_obj is None:
        sas_step = ''
        sas_step_name = ''
    elif sas_step_name_regex_obj.group(1) == 'DATA':
        sas_step = sas_step_name_regex_obj.group(1) + ' ' + sas_step_name_regex_obj.group(2)
        sas_step_name = sas_step_name_regex_obj.group(1)
    elif sas_step_name_regex_obj.group(1) == 'PROCEDURE':
        sas_step = 'PROCEDURE Statement'
        sas_step_name = sas_step_name_regex_obj.group(2)
    elif sas_step_name_regex_obj.group(1) == 'SAS':
        sas_step = 'SAS Initialization'
        sas_step_name = ''
    elif sas_step_name_regex_obj.group(1) == 'The SAS':
        sas_step = 'SAS System'
        sas_step_name = ''
    else:
        sas_step = ''
        sas_step_name = ''
    return sas_step, sas_step_name


# get time infomation
# return execution date and execution time
# completed
def get_time_info(sas_file_content):
    time_info_regex = re.compile(r"(\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d).*real time")
    time_info_regex_obj = time_info_regex.search(sas_file_content)

    if time_info_regex_obj is None:
        print("time info cannot get regex object")
        exc_date = "error"
        exc_time = "error"
    else:
        exc_date = time_info_regex_obj.group(1)
        exc_time = time_info_regex_obj.group(2)

    return exc_date, exc_time


# get process time for cpu time and real time
# return cpu time and real time as second
# comment: need to update the SAS System time part (1/14)
def get_process_time(sas_file_content):
    cpu_time_regex = re.compile(r"cpu time \s+(\d+\.\d+)")
    cpu_time_regex_obj = cpu_time_regex.search(sas_file_content)
    if cpu_time_regex_obj is None:
        cpu_time_regex = re.compile(r"cpu time \s+(\d+:\d+.\d+) ")
        cpu_time_regex_obj = cpu_time_regex.search(sas_file_content)
        cpu_time_list = cpu_time_regex_obj.split(':')
        cpu_time = float(cpu_time_list[0]) * 60 + float(cpu_time_list[1])
    else:
        cpu_time = float(cpu_time_regex_obj.group(1))

    real_time_regex = re.compile(r"real time \s+(\d+\.\d+)")
    real_time_regex_obj = real_time_regex.search(sas_file_content)
    if real_time_regex_obj is None:
        real_time_regex = re.compile(r"real time \s+(\d+:\d+.\d+) ")
        real_time_regex_obj = real_time_regex.search(sas_file_content)
        real_time_list = real_time_regex_obj.split(':')
        real_time = float(real_time_list[0]) * 60 + float(cpu_time_list[1])
    else:
        real_time = float(real_time_regex_obj.group(1))

    return cpu_time, real_time


# get output library and output table from regular log message such as NOTE: ~~
# return output library and output table
# completed for the regular log message
# comment: need to enhance to get information from actual sql query
def get_output_library_table(sas_file_content):
    output_lib_table_regex_1 = re.compile(r"NOTE: The data set (.*)\.(.*) has \d+ observations and \d+ "
                                          r"variables.")
    output_lib_table_list_1 = output_lib_table_regex_1.findall(sas_file_content)

    output_lib_table_regex_2 = re.compile(r"NOTE: SQL view (.*)\.(.*) has been defined.")
    output_lib_table_list_2 = output_lib_table_regex_2.findall(sas_file_content)

    output_lib_table_regex_3 = re.compile(r"NOTE: Table (.*?)\.(.*?) created, with \d+ rows and \d+ columns.")
    output_lib_table_list_3 = output_lib_table_regex_3.findall(sas_file_content)

    output_lib_table_regex_4 = re.compile(r"NOTE: Table (.*?)\.(.*?) has been modified, with \d+ columns.")
    output_lib_table_list_4 = output_lib_table_regex_4.findall(sas_file_content)

    output_lib_table_list = output_lib_table_list_1 + output_lib_table_list_2 + output_lib_table_list_3 + \
                            output_lib_table_list_4

    output_lib = ''
    output_table = ''
    # print(output_lib_table_list)
    if len(output_lib_table_list) != 0:
        for idx, record in enumerate(output_lib_table_list):
            if idx == 0:
                # print(record)
                output_lib += record[0]
                output_table += record[1]
            else:
                output_lib += ';' + record[0]
                output_table += ';' + record[1]

    return output_lib, output_table


# get input library and input table from regular log output such as NOTE: ~
# return input_lib, input_table as string
# Need to enhance to process actual query based process.
def get_input_library_table(sas_file_content):
    input_lib_table_regex_case_one = re.compile(r"NOTE: There were \d+ observations read from the data set (.*)\.(.*).")
    input_lib_table_list = input_lib_table_regex_case_one.findall(sas_file_content)

    input_lib_table_regex_case_two = re.compile(r"NOTE: \d+ rows were updated in (.*)\.(.*).")
    input_lib_table_list += input_lib_table_regex_case_two.findall(sas_file_content)

    input_lib_table_regex_case_three = re.compile(r"NOTE: .*? rows were deleted from (.*)\.(.*).")
    input_lib_table_list += input_lib_table_regex_case_three.findall(sas_file_content)

    input_lib_table_regex_case_four = re.compile(r"NOTE: 1 row was updated in (.*)\.(.*).")
    input_lib_table_list += input_lib_table_regex_case_four.findall(sas_file_content)

    input_lib = ''
    input_table = ''

    seen = set()
    seen_add = seen.add
    input_lib_table_list = [x for x in input_lib_table_list if not (x in seen or seen_add(x))]

    if len(input_lib_table_list) != 0:
        for record in input_lib_table_list:
            input_lib += ';' + record[0]
            input_table += ';' + record[1]

    return input_lib[1:], input_table[1:]


#
# def get_sas_row_read(record_content):
#     input_lib_table_regex_case_one = re.compile(r"NOTE: \d+ rows were updated in (.*\..*).")
#     input_lib_table_list_case_one = input_lib_table_regex_case_one.findall(record_content)
#
#     input_lib = ''
#     input_table = ''
#
#     seen = set()
#     seen_add = seen.add
#     input_lib_table_list_case_one = [x for x in input_lib_table_list_case_one if not (x in seen or seen_add(x))]
#
#     if len(input_lib_table_list_case_one) != 0:
#         for lib_table in input_lib_table_list_case_one:
#
#             lib_table_list = lib_table.split('.')
#             input_lib += ';' + lib_table_list[0]
#             input_table += ';' + lib_table_list[1]
#
#     if input_lib == '':
#         return None, None
#     else:
#         return input_lib[1:], input_table[1:]
#     return None, None


# get number of rows write and output library and output table.
# got the information from three regular log output
# return a list of [rows, libs, tbls] ex) [row1;row2, lib1;lib2, table1; table2]
def get_sas_row_write(record_content):
    rows = libs = tbls = ""

    sas_row_write_regex_case_one = re.compile(r"NOTE: Table (.*)\.(.*) created, with (\d+) rows")
    sas_row_write_regex_case_one_list = sas_row_write_regex_case_one.findall(record_content)
    sas_row_write_regex_case_one_list = [(record[2], record[0], record[1]) for record in
                                         sas_row_write_regex_case_one_list]

    sas_row_write_regex_case_two = re.compile(r"NOTE: (\d+) rows were deleted from (.*)\.(.*).")
    sas_row_write_regex_case_two_list = sas_row_write_regex_case_two.findall(record_content)
    if len(sas_row_write_regex_case_two_list) != 0:
        for record in sas_row_write_regex_case_two_list:
            if record[0] == 'No':
                record[0] = '0'
            rows = ';'.join([rows, str(record[0])])
            libs = ';'.join([libs, str(record[1])])
            tbls = ';'.join([tbls, str(record[2])])

    for record in sas_row_write_regex_case_one_list:
        rows = ';'.join([rows, str(record[0])])
        libs = ';'.join([libs, str(record[1])])
        tbls = ';'.join([tbls, str(record[2])])

    if rows == "":
        return None, None, None
    else:
        return rows[1:], libs[1:], tbls[1:]


def proc_sql_parsing(record_content):
    proc_sql_regex = re.compile(r"(.* INFO .*proc sql)(.+)((?:\n.+)+)(quit?|run?)", re.IGNORECASE)
    proc_sql_regex_list = proc_sql_regex.findall(record_content)

    input_library = []
    input_table = []
    output_library = []
    output_table = []

    if len(proc_sql_regex_list) != 0:
        sql_block = proc_sql_regex_list[0][0] + proc_sql_regex_list[0][2] + proc_sql_regex_list[0][3]
        proc_sql = get_proc_sql(sql_block)

        # print(proc_sql)

        input_library, input_table = get_input_table_from_sql(proc_sql)

        output_library, output_table = get_output_table_from_sql(proc_sql)
    # elif 'proc' in record_content and len(proc_sql_regex_list) == 0:
    #     print("cannot get proc sql")
    #     print(record_content)
    #     print("****************")

    return input_library, input_table, output_library, output_table


def get_proc_sql(sql_block):
    sql_lines = ""

    # MPRINT proc sql case: MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ASC_TRANS_VIEW):   proc sql noprint;
    if sql_lines == "":
        proc_sql_mprint_regex = re.compile(r"(MPRINT\(.*\)\:)(.+)((?:\n.+)+)(NOTE|quit)", re.IGNORECASE)
        proc_sql_mprint_regex_list = proc_sql_mprint_regex.findall(sql_block)
        if len(proc_sql_mprint_regex_list) >= 1:
            sql_lines = proc_sql_mprint_regex_list[0][1].strip() + " "

            mprint_regex = re.compile(r".* - MPRINT\(.*\)\:\s+(.*)")
            general_regex = re.compile(r".* - (.*)")

            mprint_block = proc_sql_mprint_regex_list[0][2]
            for mprint_block_line in mprint_block.splitlines():

                # if 'connect to' in mprint_block_line:
                #     sql_lines = 'pass through'
                #     break
                if '/*' in mprint_block_line or '/**' in mprint_block_line:
                    continue

                if re.match(mprint_regex, mprint_block_line) is not None:
                    mprint_block_line_list = mprint_regex.findall(mprint_block_line)
                else:
                    mprint_block_line_list = general_regex.findall(mprint_block_line)
                # print(mprint_block_line_list)
                if len(mprint_block_line_list) == 1 and mprint_block_line_list != '' and mprint_block_line_list[0][
                                                                                         :4] != 'NOTE' and \
                        mprint_block_line_list[0][:4] != 'SYMB':
                    sql_lines += mprint_block_line_list[0]

    # +proc sql case: hiragana - 874       +proc sql;
    if sql_lines == "":
        sql_block_regex = re.compile(r"(.* - \d+ \s+\+)(.*)")
        for sql_block_line in sql_block.splitlines():
            # if 'connect to' in sql_block_line:
            #     sql_lines = 'pass through'
            #     break
            if '/*' in sql_block_line or '/**' in sql_block_line:
                continue
            filtered_line = sql_block_regex.findall(sql_block_line)
            # print(filtered_line)
            if len(filtered_line) == 1 and len(filtered_line[0]) == 2 and filtered_line[0][1] != '':
                sql_lines += filtered_line[0][1].strip() + " "

    # number proc sql case: Bank2BU@SASBAP - 31         proc sql
    if sql_lines == "":
        proc_sql_num_regex = re.compile(r".* - \d+\s+(.*)")
        for sql_block_line in sql_block.splitlines():
            # if 'connect to' in sql_block_line:
            #     sql_lines = 'pass through'
            #     break
            if '/*' in sql_block_line or '/**' in sql_block_line:
                continue
            filtered_line = proc_sql_num_regex.findall(sql_block_line)

            if len(filtered_line) == 1 and filtered_line[0] != '':
                sql_lines += filtered_line[0].strip() + " "

    if sql_lines[0] == '!':
        sql_lines = sql_lines[1:].strip()

    if "The SAS System" in sql_lines:
        sql_lines_list = re.split(r"The SAS System.*? \d\d\, \d\d\d\d ", sql_lines)
        sql_lines = "".join(sql_lines_list)

    return sql_lines + ' quit;'


def get_input_table_from_sql(proc_sql):
    input_library = []
    input_table = []
    lib_table_list = []

    if 'connect to' in proc_sql or 'CONNECT TO' in proc_sql:
        return input_library, input_table

    if 'union' in proc_sql:
        sql_union_regex = re.compile(r"from (.*?) ")
        lib_table_list = sql_union_regex.findall(proc_sql)

    if 'join' in proc_sql:
        # part 1: from ~
        sql_from_regex = re.compile(r"from (.*?) ")
        sql_from_list = sql_from_regex.findall(proc_sql)
        lib_table_list.append(sql_from_list[0])
        # part 2: xxx join ~

        if 'join (' in proc_sql:
            sql_join_regex = re.compile(r"join \(.* from (.*?\..*?)\) ")
            sql_join_list = sql_join_regex.findall(proc_sql)

        else:
            sql_join_regex = re.compile(r"join (.*?) ")
            sql_join_list = sql_join_regex.findall(proc_sql)

        lib_table_list += sql_join_list

    sql_from_where_regex = re.compile(r"from (.*?) where ", re.IGNORECASE)
    sql_from_where_list = sql_from_where_regex.findall(proc_sql)

    sql_from_order_regex = re.compile(r"from (.*?) order", re.IGNORECASE)
    sql_from_order_list = sql_from_order_regex.findall(proc_sql)

    sql_from_semi_regex = re.compile(r"from (.*?)(;| )", re.IGNORECASE)
    sql_from_semi_list = sql_from_semi_regex.findall(proc_sql)

    sql_from_quit_regex = re.compile(r"from (.*?) quit;", re.IGNORECASE)
    sql_from_quit_list = sql_from_quit_regex.findall(proc_sql)

    # case 1: "from (.*?) where "
    if len(sql_from_where_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in values
        is_from_in_bracket_regex = re.compile(r'(.*?)from ', re.IGNORECASE)
        from_in_bracket_list = is_from_in_bracket_regex.findall(proc_sql)

        prior_from = from_in_bracket_list[0]
        sql_from_where_list_filtered = []

        if prior_from.count('(') == prior_from.count(')'):
            sql_from_where_list_filtered.append(sql_from_where_list[0])

        if len(sql_from_where_list_filtered) != 0:
            lib_table_list += sql_from_where_list_filtered

            # lib_table_list += sql_from_where_list[0].split(',')

    # case 2: "from (.*?) order"
    elif len(sql_from_order_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in brackets
        is_from_in_values_regex = re.compile(r'\(.*from.*\)', re.IGNORECASE)
        if re.search(is_from_in_values_regex, proc_sql) is not None:
            sql_from_order_list = []

        if len(sql_from_order_list) != 0:
            lib_table_list += sql_from_order_list[0].split(',')

    # case 3: "from (.*?)(;| )"
    elif len(sql_from_semi_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in values
        is_from_in_values_regex = re.compile(r' values\(.*? from .*?\)', re.IGNORECASE)
        if re.search(is_from_in_values_regex, proc_sql) is not None:
            sql_from_semi_list = []

        lib_table_list += sql_from_semi_list
        lib_table_list = [element[0] for element in lib_table_list if element[0] != ""]

    # case4: "from (.*?) quit;"
    elif len(sql_from_quit_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in values
        is_from_in_values_regex = re.compile(r' values\(.*? from .*?\)', re.IGNORECASE)
        if re.search(is_from_in_values_regex, proc_sql) is not None:
            sql_from_quit_list = []

        lib_table_list += sql_from_quit_list

    # print(lib_table_list)
    # print("**********")
    if len(lib_table_list) != 0:
        each_lib_table_list = []
        for lib_table in lib_table_list:
            each_lib_table_list += lib_table.split(',')

        seen = set()
        seen_add = seen.add
        each_lib_table_list = [x for x in each_lib_table_list if not (x in seen or seen_add(x))]

        for table in each_lib_table_list:
            if len(table) != 0:
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')

            if len(table) == 1 and table[0] not in input_table:
                input_library.append('work')
                input_table.append(table[0])
            elif table[1] not in input_table:
                input_library.append(table[0])
                input_table.append(table[1])

    # print(proc_sql)
    # print(input_library)
    # print(input_table)
    # print("******")

    return input_library, input_table


def get_output_table_from_sql(proc_sql):
    output_library = []
    output_table = []

    sql_view_regex = re.compile(r"create view (.*?) ")
    lib_table_list = sql_view_regex.findall(proc_sql)

    sql_table_regex = re.compile(r"create table (.*?) ")
    lib_table_list += sql_table_regex.findall(proc_sql)

    if len(lib_table_list) != 0:
        # print(lib_table_list)

        for table in lib_table_list:
            if len(table) != 0:
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')
            if len(table) == 1 and table[0] not in output_table:
                output_library.append('work')
                output_table.append(table[0])
            elif table[1] not in output_table:
                output_library.append(table[0])
                output_table.append(table[1])

    return output_library, output_table


def data_step_parsing(record_content):
    data_step_regex = re.compile(r"(.* INFO .*data)(.+?)((?:\n.+)+)(run)", re.IGNORECASE)
    data_step_regex_list = data_step_regex.findall(record_content)

    input_library = []
    input_table = []
    output_library = []
    output_table = []

    if len(data_step_regex_list) != 0:
        sql_block = data_step_regex_list[0][0] + data_step_regex_list[0][1] + data_step_regex_list[0][2] + \
                    data_step_regex_list[0][3] + ';'

        data_step_sql = get_data_step_sql(sql_block)

        # print(data_step_sql)

        input_library, input_table = get_input_table_from_data_sql(data_step_sql)
        output_library, output_table = get_output_table_from_data_sql(data_step_sql)

    return input_library, input_table, output_library, output_table


def get_data_step_sql(sql_block):
    sql_lines = ""

    # MPRINT proc sql case: :hxdhiraj - MPRINT(ETLS_LOADER):   data
    if sql_lines == "":
        # print(sql_block)
        data_step_sql_mprint_regex = re.compile(r"(.*MPRINT\(.*\)\:\s+data )(.+?)((?:\n.+)+)( run)", re.IGNORECASE)
        data_step_sql_mprint_regex_list = data_step_sql_mprint_regex.findall(sql_block)
        if len(data_step_sql_mprint_regex_list) >= 1:
            sql_lines = "data " + data_step_sql_mprint_regex_list[0][1].strip() + " "

            mprint_regex = re.compile(r".* INFO .* - MPRINT\(.*\)\:\s+(.*)")
            general_regex = re.compile(r".* INFO .* - (.*)")

            mprint_block = data_step_sql_mprint_regex_list[0][2]
            for mprint_block_line in mprint_block.splitlines():

                # if 'connect to' in mprint_block_line:
                #     sql_lines = 'pass through'
                #     break
                if 'The SAS System' in mprint_block_line or '/*' in mprint_block_line or 'NOTE' in mprint_block_line:
                    continue

                if re.match(mprint_regex, mprint_block_line) is not None:
                    mprint_block_line_list = mprint_regex.findall(mprint_block_line)
                else:
                    mprint_block_line_list = general_regex.findall(mprint_block_line)

                if len(mprint_block_line_list) == 1 and mprint_block_line_list != '' and \
                        mprint_block_line_list[0][:4] != 'SYMB':
                    sql_lines += mprint_block_line_list[0]
            sql_lines += ' run;'
    # number + case :  - 1354      +set DmdMgt.GEOBRANDSUPADDS(where=(country_code='US'));
    if sql_lines == "":

        plus_data_step_regex = re.compile(r"(.*\+\s*data)(.+?)((?:\n.*)*)(run)", re.IGNORECASE)
        plus_data_step_regex_list = plus_data_step_regex.findall(sql_block)

        if len(plus_data_step_regex_list) != 0:
            plus_sql_block = plus_data_step_regex_list[0][0] + plus_data_step_regex_list[0][1] + \
                             plus_data_step_regex_list[0][2] + \
                             plus_data_step_regex_list[0][3]

            sql_block_regex = re.compile(r"(.* INFO .* - \d+ \s+\+)(.*)")
            for sql_block_line in plus_sql_block.splitlines():
                # if 'connect to' in sql_block_line:
                #     sql_lines = 'pass through'
                #     break
                if 'The SAS System' in sql_block_line or '/*' in sql_block_line or 'NOTE' in sql_block_line or \
                        'value(s) will be set' in sql_block_line:
                    continue
                filtered_line = sql_block_regex.findall(sql_block_line)
                if len(filtered_line) == 1 and len(filtered_line[0]) == 2 and filtered_line[0][1] != '':
                    sql_lines += filtered_line[0][1].strip() + " "

    # number data step sql case: :hxdhiraj - 673        data
    if sql_lines == "":

        num_data_step_regex = re.compile(r"(.*  data)(.+?)((?:\n.+)+)(run)", re.MULTILINE)
        num_data_step_regex_list = num_data_step_regex.findall(sql_block)

        if len(num_data_step_regex_list) != 0:
            num_sql_block = num_data_step_regex_list[0][0] + num_data_step_regex_list[0][1] + \
                            num_data_step_regex_list[0][2] + \
                            num_data_step_regex_list[0][3]

            data_step_sql_num_regex = re.compile(r".* INFO .* - \d+\s+(.*)")
            for sql_block_line in num_sql_block.splitlines():
                # if 'connect to' in sql_block_line:
                #     sql_lines = 'pass through'
                #     break
                if 'The SAS System' in sql_block_line or '/*' in sql_block_line or 'NOTE' in sql_block_line:
                    continue

                filtered_line = data_step_sql_num_regex.findall(sql_block_line)

                if len(filtered_line) == 1 and filtered_line[0] != '':
                    sql_lines += filtered_line[0].strip() + " "

            splited_sql = sql_lines.split("!")
            if len(splited_sql) == 2:
                sql_lines = splited_sql[1].strip()
            else:
                sql_lines = splited_sql[0]

    return sql_lines


def get_input_table_from_data_sql(data_step_sql):
    input_lib = []
    input_table = []

    set_lib_table_list = []
    merge_lib_table_list = []
    update_lib_table_list = []

    # get input library and table from set
    set_between_quote_regex = re.compile(r"\".*? set .*\"")

    if re.search(set_between_quote_regex, data_step_sql) is None:
        set_regex = re.compile(r"[;| ]set (.*?)(;|\(| )")
        set_lib_table_list = set_regex.findall(data_step_sql)

        set_lib_table_list = [element[0] for element in set_lib_table_list if element[0] != ""]

    # get input library and table from merge
    merge_regex = re.compile(r"merge (.*?);")
    if re.search(merge_regex, data_step_sql) is not None:
        merge_regex_list = merge_regex.findall(data_step_sql)
        merge_lib_table_regex = re.compile(r"(.*?)(\(.*\) | \(.*\)| )")
        merge_lib_table_list = merge_lib_table_regex.findall(merge_regex_list[0])
        merge_lib_table_list = [element[0] for element in merge_lib_table_list if element[0] != ""]

        # exception case 1 : if merge is between quotes
        merge_between_quote_regex = re.compile(r"\".*?merge .*?\"")
        if re.search(merge_between_quote_regex, data_step_sql) is not None:
            merge_lib_table_list = []

    # need to work with 'UPDATE'
    update_regex = re.compile(r"update (.*?);")
    if re.search(update_regex, data_step_sql) is not None:
        update_regex_list = update_regex.findall(data_step_sql)
        update_lib_table_regex = re.compile(r"(.*?)(\(.*\) | \(.*\)| )")
        update_lib_table_list = update_lib_table_regex.findall(update_regex_list[0])
        update_lib_table_list = [element[0] for element in update_lib_table_list if element[0] != ""]

        # exception case 1 : if update is between quotes
        update_between_quote_regex = re.compile(r"\".*?update .*?\"")
        if re.search(update_between_quote_regex, data_step_sql) is not None:
            update_lib_table_list = []

    input_regex_list = set_lib_table_list + merge_lib_table_list + update_lib_table_list

    if len(input_regex_list) != 0:

        for table in input_regex_list:
            if table != "":
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')
            if len(table) == 1 and table[0] not in input_table:
                input_lib.append('work')
                input_table.append(table[0])
            elif len(table) == 1 and table[0] in input_table:
                continue
            elif table[1] not in input_table:
                input_lib.append(table[0])
                input_table.append(table[1])

    return input_lib, input_table


def get_output_table_from_data_sql(data_step_sql):
    output_lib = []
    output_table = []

    data_out_tbl_regex = re.compile(r"data (.*?);")
    data_out_tbl_list = data_out_tbl_regex.findall(data_step_sql)
    data_out_bracket_list = []
    data_out_space_list = []
    data_out_view_list = []

    if len(data_out_tbl_list) != 0:

        if '_null_' in data_out_tbl_list[0]:
            data_out_tbl_list = []
        else:
            data_out_string = data_out_tbl_list[0]
            data_out_tbl_list = []

            if " " not in data_out_string:
                data_out_tbl_list.append(data_out_string)

            if '(' in data_out_string:
                data_out_tbl_regex = re.compile(r"(.*?)(\(.*?\)| )")
                data_out_bracket_list = data_out_tbl_regex.findall(data_out_string)
                if len(data_out_bracket_list) != 0:
                    data_out_bracket_list = [element[0] for element in data_out_bracket_list if '.' in element[0]]

            elif ' ' in data_out_string and '/view' not in data_out_string:
                data_out_space_list = data_out_string.split(" ")

            elif ' ' in data_out_string and '/view' in data_out_string:
                data_out_space_list = [data_out_string.split(" ")[0]]

            if '/view' in data_out_string:
                data_out_view_list = [data_out_string.split("=")[-1]]

            # print(data_out_string)
            # print(data_out_bracket_list)
            # print(data_out_space_list)
            # print(data_out_view_list)
            # print("*****")
    data_out_tbl_list = data_out_tbl_list + data_out_bracket_list + data_out_space_list + data_out_view_list

    if len(data_out_tbl_list) != 0:

        for table in data_out_tbl_list:

            if table == "":
                continue
            # print(table)
            if len(table) != 0:
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')

                if len(table) == 1 and table[0] not in output_table:
                    output_lib.append('work')
                    output_table.append(table[0])
                elif len(table) == 1 and table[0] in output_table:
                    continue
                elif table[1] not in output_table:
                    output_lib.append(table[0])
                    output_table.append(table[1])
                # print(output_lib)
                # print(output_table)

    return output_lib, output_table


def lib_table_write_to_variable(library, table, FILE_SAS_LIB, FILE_SAS_TBL):
    if table and len(table) != 0:

        # filter out exceptional cases such as table name ended with ()
        filtered_table = []
        for table_name in table:
            if table_name[-2:] == '()':
                filtered_table.append(table_name[:-2])
            else:
                filtered_table.append(table_name)

        if FILE_SAS_TBL == "":
            FILE_SAS_LIB = ';'.join(library)
            FILE_SAS_TBL = ';'.join(filtered_table)
        else:
            for lib, tbl in zip(library, filtered_table):
                if tbl.lower() not in FILE_SAS_TBL and tbl.upper() not in FILE_SAS_TBL:
                    FILE_SAS_LIB += ";" + lib
                    FILE_SAS_TBL += ";" + tbl

    return FILE_SAS_LIB, FILE_SAS_TBL


def get_macro_flag(FILE_SAS_INP_LIB, FILE_SAS_INP_TBL, FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL):
    lib_tbl_str = FILE_SAS_INP_LIB + ';' + FILE_SAS_INP_TBL + ';' + FILE_SAS_OUT_LIB + ';' + FILE_SAS_OUT_TBL
    lib_tbl_list = lib_tbl_str.split(';')

    for lib_or_tbl in lib_tbl_list:

        if "&" in lib_or_tbl:
            return 1

    return 0


# 1. check the record_contest has a libname ABC oracle/db2/hadoop/etc
# 2. if the database type is not base or V9 save it to ext_db_lib_ref_list
# 3.     ext_db_ref_list is created based on each file as empty list
#        return the name of the database name
# 4. on main function, check proc sql in / out part before save it to pandas.
def get_ext_db(record_content):
    ext_db_name_list = []
    # Check with proc sql statement
    proc_sql_regex = re.compile(r"(.* INFO .*proc sql)(.+)((?:\n.+)+)(quit?|run?)", re.IGNORECASE)
    proc_sql_regex_list = proc_sql_regex.findall(record_content)
    if len(proc_sql_regex_list) != 0:
        sql_block = proc_sql_regex_list[0][0] + proc_sql_regex_list[0][2] + proc_sql_regex_list[0][3]
        proc_sql = get_proc_sql(sql_block)
        # print(proc_sql)
        if "connect to" in proc_sql:
            ext_db_regex = re.compile(r"connect to (.*?)(\(| )")
            ext_db_obj = ext_db_regex.search(proc_sql)
            ext_db_name = ext_db_obj.group(1)
            ext_db_name_list.append(ext_db_name.lower())

    lib_name_list, db_name_list = ext_db_checker(record_content)

    ext_db_name_list += db_name_list
    ext_db_name_list = list(set(ext_db_name_list))

    # print(ext_db_name_list)

    return ext_db_name_list


def ext_db_checker(record_content):
    external_database_tuple = (
        'redshift', 'aster', 'db2' 'bigquery', 'greenplm', 'hadoop', 'hawq', 'impala', 'informix', 'jdbc', 'sqlsvr',
        'mysql', 'netezza', 'odbc', 'oledb', 'oracle', 'postgres', 'sapase', 'saphana', 'sapiq', 'snow', 'spark',
        'teradata', 'vertica', 'ybrick', 'mongo', 'sforce'
    )
    library_name_list = []
    database_name_list = []

    libname_regex = re.compile(r"libname (\w+?) (\w+?)(;| )", re.IGNORECASE)
    libname_list = libname_regex.findall(record_content)

    if libname_list:
        for lib_db in libname_list:

            temp_library_name = lib_db[0]
            temp_database_name = lib_db[1].lower()

            if temp_database_name in external_database_tuple:
                library_name_list.append(temp_library_name)
                database_name_list.append(temp_database_name)

    # print(library_name_list)
    # print(database_name_list)

    return library_name_list, database_name_list


def get_migration_disp(FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM, FILE_SAS_STP, FILE_SAS_STP_NM, record_content):
    RULE_ID = ""
    REC_ACT = ""
    recommendation = "Lift and Shift"

    # cpu_time_list = str(FILE_SAS_EXC_CPU_TM).split(':')
    # if len(cpu_time_list) == 2:
    #     FILE_SAS_EXC_CPU_TM = float(cpu_time_list[0] * 60) + float(cpu_time_list[1])
    # else:
    #     FILE_SAS_EXC_CPU_TM = float(FILE_SAS_EXC_CPU_TM)
    #
    # real_time_list = FILE_SAS_EXC_RL_TM.split(':')
    # if len(real_time_list) == 2:
    #     FILE_SAS_EXC_RL_TM = float(real_time_list[0] * 60) + float(real_time_list[1])
    # else:
    #     FILE_SAS_EXC_RL_TM = float(FILE_SAS_EXC_RL_TM)

    data_statement = ""

    data_step_regex = re.compile(r"(.* INFO .* data)(.+?)((?:\n.+)+)(run)", re.IGNORECASE)
    data_step_regex_list = data_step_regex.findall(record_content)

    if len(data_step_regex_list) != 0:
        sql_block = data_step_regex_list[0][0] + data_step_regex_list[0][1] + data_step_regex_list[0][2] + \
                    data_step_regex_list[0][3]
        data_statement = get_data_step_sql(sql_block)

    proc_sql = ""
    proc_sql_regex = re.compile(r"(.* INFO .*proc sql)(.+)((?:\n.+)+)(quit?|run?)", re.IGNORECASE)
    proc_sql_regex_list = proc_sql_regex.findall(record_content)

    if len(proc_sql_regex_list) != 0:
        sql_block = proc_sql_regex_list[0][0] + proc_sql_regex_list[0][2] + proc_sql_regex_list[0][3]
        proc_sql = get_proc_sql(sql_block)

    if FILE_SAS_EXC_CPU_TM >= 30.00:
        recommendation = "Code Change"
        RULE_ID = '1'
        REC_ACT = 'Consider reducing real time'
    elif FILE_SAS_EXC_CPU_TM >= FILE_SAS_EXC_RL_TM and FILE_SAS_EXC_CPU_TM != 0:
        recommendation = "Code Change"
        RULE_ID = '2'
        REC_ACT = 'Consider reducing cpu time so that it is less then real time'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'LOGISTIC':
        recommendation = "Code Change"
        RULE_ID = '4'
        REC_ACT = 'Consider using PROC LOGSELECT (CAS) instead of Logistic'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'MIXED':
        recommendation = "Code Change"
        RULE_ID = '5'
        REC_ACT = 'Consider using PROC LMIXED (CAS) instead of Mixed'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'REG':
        recommendation = "Code Change"
        RULE_ID = '6'
        REC_ACT = 'Consider using PROC REGSELECT (CAS) instead of Reg'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'SQL':
        recommendation = "Code Change"
        RULE_ID = '9'
        REC_ACT = 'Push Down whenever possible.'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'SORT':
        recommendation = "Code Change"
        RULE_ID = '10'
        REC_ACT = 'Push Down whenever possible. (To save memory use partioning)'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'TRANSPOSE':
        recommendation = "Code Change"
        RULE_ID = '11'
        REC_ACT = 'Depending on ther data source stays as DB2 or moves to native cloud data base.'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'FORMAT':
        recommendation = "Code Change"
        RULE_ID = '12'
        REC_ACT = 'Depending on ther data source stays as DB2 or moves to native cloud data base.'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'FEDSQL':
        recommendation = "Code Change"
        RULE_ID = '13'
        REC_ACT = 'Code Change because PROC FedSQL is ANSI 99 SQL compliant'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'APPEND':
        recommendation = "Code Change"
        RULE_ID = '14'
        REC_ACT = 'Neglect if target CAS table exists prior to the PROC APPEND.'
    elif FILE_SAS_STP == 'DATA statement' and 'index' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '15'
        REC_ACT = 'Neglect INDEX in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'firstobs' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '16'
        REC_ACT = 'Neglect FIRSTOBS in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'obs' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '17'
        REC_ACT = 'Neglect OBS in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'pointobs' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '18'
        REC_ACT = 'Neglect POINTOBS in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'infile' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '19'
        REC_ACT = 'Replace with SET statements, with the new SET statements pointing to the correct in-memory tables.'
    elif FILE_SAS_STP == 'DATA statement' and 'input' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '20'
        REC_ACT = 'Replace with SET statements, with the new SET statements pointing to the correct in-memory tables.'
    elif FILE_SAS_STP == 'DATA statement' and 'datalines' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '21'
        REC_ACT = 'Replace with SET statements, with the new SET statements pointing to the correct in-memory tables.'
    elif FILE_SAS_STP == 'DATA statement' and 'varfmt' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '22'
        REC_ACT = ''
    elif FILE_SAS_STP == 'PROCEDURE Statement' and 'varfmt' in proc_sql.lower():
        recommendation = "Code Change"
        RULE_ID = '22'
        REC_ACT = 'Neglect VARFMT function because it is Obsolete.'
    elif FILE_SAS_EXC_CPU_TM >= FILE_SAS_EXC_RL_TM and FILE_SAS_EXC_CPU_TM >= 10:
        recommendation = "Code Change"
        RULE_ID = '23'
        REC_ACT = 'new rule: Consider reducing cpu time so that it is less then real time'

    return REC_ACT, RULE_ID, recommendation


def get_migr_rule(FILE_SAS_MIGR_RUL_ID):
    if FILE_SAS_MIGR_RUL_ID == "":
        return ""

    migr_rule_dict = {
        "1": "Real_Time >=30",
        "2": "CPU Time >= Real Time",
        "3": "volume of table > 50GB",
        "4": "SAS Step == PROC LOGISTIC",
        "5": "SAS Step == PROC MIXED",
        "6": "SAS Step == PROC REG",
        "7": "no_of_functon_used > 20",
        "8": "Reporting Proc Real Time >  1 hr",
        "9": "Procedure == PROC SQL",
        "10": "Procedure == PROC SORT",
        "11": "Procedure == PROC TRANSPOSE",
        "12": "Procedure == PROC FORMAT",
        "13": "Procedure == PROC FedSQL",
        "14": "Procedure == PROC APPEND",
        "15": "INDEX  used in DATA statement",
        "16": "FIRSTOBS used in DATA statement",
        "17": "OBS used in DATA statement",
        "18": "POINTOBS used in DATA statement",
        "19": "INFILE in Data statement",
        "20": "INPUT in Data statement",
        "21": "DATALINES in Data statement",
        "22": "VARFMT function present",
        "23": "CPU Time >= Real Time AND CPU TIME >= 10"
    }
    migration_rule = migr_rule_dict.get(FILE_SAS_MIGR_RUL_ID)
    return migration_rule


#
def get_proc_inmem(record_content, FILE_SAS_STP, FILE_SAS_STP_NM):
    inmem_tuple = ('SAS_INSTALL_EP',
                   '%INDTD_PUBLISH_MODEL',
                   '%INDAC_PUBLISH_MODEL',
                   '%INDB2_PUBLISH_MODEL ',
                   '%INDGP_PUBLISH_MODEL ',
                   '%INDHD_PUBLISH_MODEL',
                   '%INDNZ_PUBLISH_MODEL ',
                   '%INDOR_PUBLISH_MODEL ',
                   '%INDHN_PUBLISH_MODEL ',
                   '%INDHN_RUN_MODEL ',
                   '%INDHD_RUN_MODEL',
                   'SQLGENERATION ',
                   'DSACCEL',
                   'HADOOPPLATFORM',
                   'SQLGENERATION',
                   'SQLMAPPUTTO',
                   'SQLREDUCEPUT',
                   'SAS_EP ',
                   'SAS_EP_ENABLE_EPCS',
                   'SAS_SCORE_EP ',
                   'SAS_EP_JOB_MANAGEMENT_URL ',
                   'SASEPFUNC',
                   'DSACCEL',
                   '%INDTD_CREATE_MODELTABLE ',
                   '%INDB2_CREATE_MODELTABLE',
                   '%INDNZ_CREATE_MODELTABLE',
                   '%INDOR_CREATE_MODELTABLE ',
                   'SAS_SCORE_EP',
                   'SAS_SYSFNLIB',
                   'HPSVM',
                   'HPFOREST ',
                   'SAS_SCORE',
                   'INDCONN ',
                   'EM_PREDICTION',
                   'DS2ACCEL=YES',
                   'SQLGENERATION',
                   'DSACCEL',
                   'HADOOPPLATFORM',
                   'SQLGENERATION',
                   'SQLMAPPUTTO',
                   'SQLREDUCEPUT',
                   'EM_PROBABILITY',
                   'EM_DECISION')

    for keyword in inmem_tuple:
        if keyword in record_content.upper():
            return 1

    if FILE_SAS_STP == "PROCEDURE Statement" and (FILE_SAS_STP_NM == 'LASR' or FILE_SAS_STP_NM == 'IAMSTAT'):
        return 1
    else:
        return 0


def get_proc_etl(FILE_SAS_PROC_CAT, FILE_SAS_STP, FILE_SAS_STP_NM):
    if FILE_SAS_PROC_CAT == 'Data Management' and FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM in [
        "APPEND", "CONTESTS", "DATASETS", "SORT", "SQL", "IMPORT"]:
        return 1
    else:
        return 0


def get_proc_grid(record_content):
    grid_keyword = ('GRIDOPTSET',
                    'GRIDWAITTIMEOUT',
                    'GRIDWAITRESULTS',
                    'GRIDRUNSASLM',
                    'GRIDRUNSASDMS',
                    'GRIDRUNCMDINT',
                    'GRIDWATCHOUTPUT',
                    'GRIDWAITLOGLIST',
                    'GRIDWAITNORESULTS',
                    'GRIDWAITNORESULTSNOLOG',
                    'GRIDRUNPGM',
                    'GRDSVC_HOSTLIST',
                    'GRDSVC_OPTSETS',
                    'GRIDAPPSERVER',
                    'GRIDFILESIN',
                    'GRIDFORCECLEAN',
                    'GRIDGETRESULTS',
                    'GRIDGETSTATUS',
                    'GRIDJOBNAME',
                    'GRIDJOBOPTS',
                    'GRIDKILLJOB',
                    'GRIDLICENSEFILE',
                    'GRIDLRESTARTOK',
                    'GRIDOPTSET',
                    'GRIDPASSWORD',
                    'GRIDPASS',
                    'GRIDPWD',
                    'GRIDPLUGINPATH',
                    'GRIDRESTARTOK',
                    'GRIDRESULTSDIR',
                    'GRIDRUNCMD',
                    'GRIDRUNCMDINT',
                    'GRIDRUNPGM',
                    'GRIDRUNSASDMS',
                    'GRIDRUNSASLM',
                    'GRIDSASOPTS',
                    'GRIDSETPERMS',
                    'GRIDSTAGECMD',
                    'GRIDSTAGEHOST',
                    'GRIDSUBMITPGM',
                    'GRIDWAIT',
                    'GRIDWAITLOGLIST',
                    'GRIDWAITNORESULTS',
                    'GRIDWAITRESULTS',
                    'GRIDWAITRESULTSNOLOG',
                    'GRIDWAITTIMEOUT',
                    'GRIDWATCHOUTPUT',
                    'GRIDWORKLOAD',
                    'GRDSVC_ENABLE ',
                    'GRDSVC_GETADDR ',
                    'GRDSVC_GETINFO ',
                    'GRDSVC_GETNAME ',
                    'GRDSVC_HOSTLIST ',
                    'GRDSVC_NNODES ',
                    'GRDSVC_OPTSETS',
                    'SASGSUB',
                    'GRIDSUBMITPGM ',
                    'GRIDLRESTART',
                    'GRIDSASOPTS ',
                    'GRIDRUNPGM',
                    'GRIDRUNSASLM',
                    'GRIDRUNSASDMS',
                    'GRIDWAITTIMEOUT ',
                    'GRIDRUNCMD ',
                    'GRIDRUNCMDINT ',
                    'GRIDWAITTIMEOUT',
                    'GRIDKILLJOB ',
                    'GRIDGETSTATUS ',
                    'GRIDGETRESULTS ',
                    'GRIDRESULTSDIR ',
                    'GRIDFORCECLEAN',
                    'GRIDAPPSERVER ',
                    'CLEANGRIDWORK ',
                    'GRIDWORK',
                    'GRIDWORKREM ',
                    'GRIDFILESIN ',
                    'GRIDSTAGECMD',
                    'GRIDSTAGEHOST',
                    'GRIDWAIT',
                    'GRIDWAITTIMEOUTGRIDWAITRESULTS',
                    'GRIDWAITLOGLIST',
                    'GRIDWAITNORESULTS',
                    'GRIDWAITRESULTSNOLOG',
                    'GRIDWATCHOUTPUT',
                    'GRIDJOBNAME ',
                    'GRIDJOBOPTS',
                    'GRIDOPTSET',
                    'GRIDWORKLOAD',
                    'GRDSVC_ENABLE',
                    'SASGSUB ',
                    'GRIDSUBMITPGM ',
                    'GRIDRESTARTOK',
                    'GRIDLRESTARTOK',
                    'GRIDSASOPTS')

    for keyword in grid_keyword:
        if keyword in record_content.upper():
            return 1

    return 0


def get_indb(record_content):
    external_database_tuple = (
        'redshift', 'aster', 'db2' 'bigquery', 'greenplm', 'hadoop', 'hawq', 'impala', 'informix', 'jdbc', 'sqlsvr',
        'mysql', 'netezza', 'odbc', 'oledb', 'oracle', 'postgres', 'sapase', 'saphana', 'sapiq', 'snow', 'spark',
        'teradata', 'vertica', 'ybrick', 'mongo', 'sforce'
    )

    connect_db_regex = re.compile(r"connect to (.*?)[ |\(]", re.IGNORECASE)
    connect_db_list = connect_db_regex.findall(record_content)

    disconnect_db_regex = re.compile(r"disconnect from (.*?)[;| ]", re.IGNORECASE)
    disconnect_db_list = disconnect_db_regex.findall(record_content)

    if len(connect_db_list) != 0:

        for conn_db, disconn_db in zip(connect_db_list, disconnect_db_list):

            if conn_db == disconn_db and conn_db in external_database_tuple:
                return 1

    return 0


# update a row of record to the given dataframe 'log_df'
def save_record_to_df(log_df, extracted_record):
    updated_log_df = log_df.append(pd.Series(extracted_record, index=log_df.columns), ignore_index=True)

    return updated_log_df


# save the dataframe to an excel file
def save_df_to_xlsx(log_df):
    # check "\output" folder and make it if it is not exist

    # print(log_df.iloc[2])

    if platform.system() == 'Windows':
        if not os.path.isdir('..\\Data_Model\\Extracted_Files'):
            os.makedirs('..\\Data_Model\\Extracted_Files')

        log_df.to_excel("..\\Data_Model\\Extracted_Files\\D_CLDASST_DISC_LOG_O.xlsx", float_format="%0.2f", index=False)
        log_df.to_csv("..\\Data_Model\\Extracted_Files\\D_CLDASST_DISC_LOG_O.csv", float_format="%0.2f", index=False,
                  date_format='%Y-%m-%d %H:%M:%S')
    else:

        if not os.path.isdir('../Data_Model/Extracted_Files'):
            os.makedirs('../Data_Model/Extracted_Files')

        log_df.to_excel("../Data_Model/Extracted_Files/D_CLDASST_DISC_LOG_O.xlsx", float_format="%0.2f", index=False)
        log_df.to_csv("../Data_Model/Extracted_Files/D_CLDASST_DISC_LOG_O.csv", float_format="%0.2f", index=False,
                      date_format='%Y-%m-%d %H:%M:%S')

# main function
if __name__ == "__main__":

    FILE_ID = ""
    FILE_PTH = ""
    FILE_NM = ""
    FILE_USR_NM = ""
    FILE_SAS_F_ID = ""
    FILE_SAS_F_LOC = ""
    FILE_SAS_F_NM = ""
    FILE_SAS_STP = ""
    FILE_SAS_STP_NM = ""
    FILE_LN_NUM = ""
    FILE_SAS_INP_LIB = ""
    FILE_SAS_INP_TBL = ""
    FILE_SAS_INP_FIL_NM = ""
    FILE_SAS_INP_ROW_RD = ""
    FILE_SAS_OUT_LIB = ""
    FILE_SAS_OUT_TBL = ""
    FILE_SAS_ROW_WRT = ""

    FILE_SAS_INP_MUL_FLG = ""
    FILE_SAS_INP_MUL_TBLS = ""
    FILE_SAS_MACRO_FLG = ""
    FILE_SAS_EXT_DB = ""
    FILE_EXC_DT = ""
    FILE_SAS_EXC_TM = ""
    FILE_SAS_EXC_CPU_TM = ""
    FILE_SAS_EXC_RL_TM = ""
    # ==========================
    FILE_SAS_PROC_CAT = ""
    FILE_SAS_PROC_PROD = ""
    FILE_SAS_MIGR_DISP = ""
    FILE_SAS_MIGR_RUL_ID = ""
    FILE_SAS_MIGR_RUL = ""
    FILE_SAS_MIGR_REC_ACT = ""
    FILE_SAS_PROC_INMEM_FLG = 0
    FILE_SAS_PROC_ELT_FLG = 0
    FILE_SAS_PROC_GRID_FLG = 0
    FILE_SAS_PROC_INDB_FLG = 0
    FILE_SAS_SRC_TYP = "SAS"
    FILE_SAS_ENV_NAME = "SAS GRID PROD"

    log_df = pd.DataFrame(columns=['FILE_ID', 'FILE_PTH', 'FILE_NM', 'FILE_USR_NM', 'FILE_SAS_F_ID',
                                   'FILE_SAS_F_LOC', 'FILE_SAS_F_NM', 'FILE_SAS_STP',
                                   'FILE_SAS_STP_NM', 'FILE_LN_NUM', 'FILE_SAS_INP_LIB',
                                   'FILE_SAS_INP_TBL', 'FILE_SAS_INP_FIL_NM', 'FILE_SAS_INP_ROW_RD',
                                   'FILE_SAS_OUT_LIB', 'FILE_SAS_OUT_TBL', 'FILE_SAS_ROW_WRT',
                                   'FILE_SAS_INP_MUL_FLG', 'FILE_SAS_INP_MUL_TBLS', 'FILE_SAS_MACRO_FLG',
                                   'FILE_SAS_EXT_DB', 'FILE_EXC_DT',
                                   'FILE_SAS_EXC_TM', 'FILE_SAS_EXC_CPU_TM', 'FILE_SAS_EXC_RL_TM',
                                   'FILE_SAS_PROC_CAT', 'FILE_SAS_PROC_PROD', 'FILE_SAS_MIGR_DISP',
                                   'FILE_SAS_MIGR_RUL_ID', 'FILE_SAS_MIGR_RUL', 'FILE_SAS_MIGR_REC_ACT',
                                   'FILE_SAS_PROC_INMEM_FLG', 'FILE_SAS_PROC_ELT_FLG', 'FILE_SAS_PROC_GRID_FLG',
                                   'FILE_SAS_PROC_INDB_FLG', 'FILE_SAS_SRC_TYP', 'FILE_SAS_ENV_NAME'])

    current_path = os.getcwd()
    current_folder = 'logs'
    visited = dict()
    file_list = []
    cat_prod_dict = dict()
    cat_prod_dict = init_proc_cat_prod(cat_prod_dict)
    getInventory(current_path, current_folder, visited, file_list)

    #    log_file_path_list = get_log_file_list()

    file_id_counter = 1
    sas_file_id_counter = 1
    file_list = []
    sas_file_dict = get_sas_file_id(current_path, current_folder, visited,
                                    file_list)  # key: sas_file_abs_path, value: FILE_SAS_F_ID

    for file_path, file_name in file_list:

        ext_db_lib_name_list = []

        if platform.system() == 'Windows':
            file_full_path = file_path + '\\' + file_name
        else:
            file_full_path = file_path + '/' + file_name

        log_content = get_log_content(file_full_path)
        FILE_PTH = file_full_path
        FILE_NM = file_name

        sas_file_content_list = get_sas_files(log_content)
        for sas_file_abs_path, sas_file_content in sas_file_content_list:

            temp_num = 1

            if re.search(r"cpu time .*? seconds\n.*? - \d+\s+The SAS System.*? \d\d\d\d", sas_file_content):
                sas_file_content = re.sub(r' \d+\s+The SAS System.*? \d\d\d\d', '       ', sas_file_content)
            else:
                sas_file_content = re.sub(r' \d+\s+The SAS System.*? \d\d\d\d', '              ', sas_file_content)

            record_content_list = re.split(r"seconds\n.*? -       \n", sas_file_content)

            for record_content in record_content_list:
                if record_content[-25:-17] != 'cpu time':
                    continue

                # print("record content num:" + str(temp_num))
                # temp_num+=1
                # print(record_content)
                # print("********************")

                # update sas file id and sas file name and path if it is updated.
                if sas_file_abs_path != '':
                    sas_file_norm_path = os.path.normpath(sas_file_abs_path)
                    FILE_SAS_F_NM = sas_file_norm_path.split(os.sep)[-1]
                    if sas_file_dict.get(FILE_SAS_F_NM) is None:
                        sas_file_dict[FILE_SAS_F_NM] = 'SF_' + str(sas_file_id_counter)
                        sas_file_id_counter += 1
                    FILE_SAS_F_ID = sas_file_dict.get(FILE_SAS_F_NM)


                FILE_USR_NM = get_user_name(record_content)
                FILE_SAS_F_LOC = sas_file_abs_path
                if FILE_SAS_F_LOC == "":
                    FILE_SAS_F_NM = ""
                    FILE_SAS_F_ID = ""
                FILE_SAS_INP_ROW_RD, FILE_SAS_INP_FIL_NM = get_input_file_name(record_content)
                if FILE_SAS_INP_FIL_NM != "":
                    FILE_SAS_INP_TBL = FILE_SAS_INP_FIL_NM.split('/')[-1]
                    FILE_SAS_INP_LIB = 'Ext'
                else:
                    FILE_SAS_INP_LIB, FILE_SAS_INP_TBL = get_input_library_table(record_content)

                FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL = get_output_library_table(record_content)

                # FILE_SAS_INP_ROW_RD  # Need to get some example to implement
                if FILE_SAS_F_LOC == "":
                    FILE_LN_NUM = ""
                else:
                    FILE_LN_NUM = get_sas_file_line_number(record_content)

                FILE_SAS_STP, FILE_SAS_STP_NM = get_sas_step_name(record_content)
                if FILE_SAS_STP == 'SAS Initialization' or FILE_SAS_STP == 'SAS System':
                    continue

                # Check if the FILE_SAS_STP is DATA and if it is not, initialize FILE_SAS_INP_ROW_RD and Input file
                if FILE_SAS_STP == 'PROCEDURE Statement':
                    FILE_SAS_INP_ROW_RD = FILE_SAS_INP_FIL_NM = ""

                FILE_EXC_DT, FILE_SAS_EXC_TM = get_time_info(record_content)

                # print(FILE_EXC_DT)
                # print(FILE_SAS_EXC_TM)

                FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM = get_process_time(record_content)

                rows, libs, tbls = get_sas_row_write(record_content)
                if rows is not None:
                    FILE_SAS_ROW_WRT = rows
                    if FILE_SAS_OUT_LIB == "":
                        FILE_SAS_OUT_LIB = libs
                    else:
                        FILE_SAS_OUT_LIB = ';'.join([FILE_SAS_OUT_LIB, libs])
                    if FILE_SAS_OUT_TBL == "":
                        FILE_SAS_OUT_TBL = tbls
                    else:
                        FILE_SAS_OUT_TBL = ';'.join([FILE_SAS_OUT_TBL, tbls])

                # more data extractions needed to be here

                if FILE_SAS_STP == "PROCEDURE Statement":
                    input_lib, input_table, output_lib, output_table = proc_sql_parsing(record_content)
                else:
                    input_lib, input_table, output_lib, output_table = data_step_parsing(record_content)

                FILE_SAS_INP_LIB, FILE_SAS_INP_TBL = lib_table_write_to_variable(input_lib, input_table,
                                                                                 FILE_SAS_INP_LIB,
                                                                                 FILE_SAS_INP_TBL)

                FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL = lib_table_write_to_variable(output_lib, output_table,
                                                                                 FILE_SAS_OUT_LIB,
                                                                                 FILE_SAS_OUT_TBL)

                FILE_SAS_MACRO_FLG = get_macro_flag(FILE_SAS_INP_LIB, FILE_SAS_INP_TBL, FILE_SAS_OUT_LIB,
                                                    FILE_SAS_OUT_TBL)

                ext_db_list = get_ext_db(record_content)
                FILE_SAS_EXT_DB = ';'.join(ext_db_list)
                # if FILE_SAS_EXT_DB != "":
                #     FILE_SAS_OUT_LIB = FILE_SAS_OUT_TBL = FILE_SAS_INP_LIB = FILE_SAS_INP_TBL = FILE_SAS_ROW_WRT = ""
                #     FILE_SAS_INP_MUL_TBLS = FILE_SAS_INP_MUL_FLG = 0

                if FILE_SAS_STP_NM == 'DATA':
                    FILE_SAS_PROC_PROD, FILE_SAS_PROC_CAT = 'Base SAS', 'Data Management'
                elif FILE_SAS_STP_NM == '':
                    pass
                else:
                    FILE_SAS_PROC_PROD, FILE_SAS_PROC_CAT = cat_prod_dict[FILE_SAS_STP_NM.upper()]

                if len(FILE_SAS_INP_LIB.split(';')) > 1:
                    FILE_SAS_INP_MUL_FLG = 1
                    FILE_SAS_INP_MUL_TBLS = 1
                else:
                    FILE_SAS_INP_MUL_FLG = 0
                    FILE_SAS_INP_MUL_TBLS = 0

                FILE_SAS_MIGR_REC_ACT, FILE_SAS_MIGR_RUL_ID, FILE_SAS_MIGR_DISP = get_migration_disp(
                    FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM,
                    FILE_SAS_STP, FILE_SAS_STP_NM,
                    record_content)

                FILE_SAS_MIGR_RUL = get_migr_rule(FILE_SAS_MIGR_RUL_ID)

                FILE_SAS_PROC_INMEM_FLG = get_proc_inmem(record_content, FILE_SAS_STP, FILE_SAS_STP_NM)

                FILE_SAS_PROC_ELT_FLG = get_proc_etl(FILE_SAS_PROC_CAT, FILE_SAS_STP, FILE_SAS_STP_NM)

                FILE_SAS_PROC_GRID_FLG = get_proc_grid(record_content)

                FILE_SAS_PROC_INDB_FLG = get_indb(record_content)

                FILE_ID = 'LOG_' + str(file_id_counter)
                file_id_counter += 1
                extracted_record = [FILE_ID, FILE_PTH, FILE_NM, FILE_USR_NM, FILE_SAS_F_ID, FILE_SAS_F_LOC,
                                    FILE_SAS_F_NM, FILE_SAS_STP, FILE_SAS_STP_NM, FILE_LN_NUM, FILE_SAS_INP_LIB,
                                    FILE_SAS_INP_TBL, FILE_SAS_INP_FIL_NM, FILE_SAS_INP_ROW_RD, FILE_SAS_OUT_LIB,
                                    FILE_SAS_OUT_TBL, FILE_SAS_ROW_WRT, FILE_SAS_INP_MUL_FLG, FILE_SAS_INP_MUL_TBLS,
                                    FILE_SAS_MACRO_FLG, FILE_SAS_EXT_DB, FILE_EXC_DT, FILE_SAS_EXC_TM,
                                    FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM, FILE_SAS_PROC_CAT, FILE_SAS_PROC_PROD,
                                    FILE_SAS_MIGR_DISP, FILE_SAS_MIGR_RUL_ID, FILE_SAS_MIGR_RUL, FILE_SAS_MIGR_REC_ACT,
                                    FILE_SAS_PROC_INMEM_FLG,
                                    FILE_SAS_PROC_ELT_FLG, FILE_SAS_PROC_GRID_FLG, FILE_SAS_PROC_INDB_FLG,
                                    FILE_SAS_SRC_TYP, FILE_SAS_ENV_NAME]

                log_df = save_record_to_df(log_df, extracted_record)

                # Data initialization
                FILE_SAS_ROW_WRT = FILE_SAS_OUT_LIB = FILE_SAS_OUT_TBL = ""
                FILE_SAS_INP_ROW_RD = FILE_SAS_INP_LIB = FILE_SAS_INP_TBL = ""

    save_df_to_xlsx(log_df)

logging.info('end of the program')
