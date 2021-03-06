import os,sys,datetime,time
from ROOT import *
execfile("/uscms_data/d3/jmanagan/EOSSafeUtils.py")

start_time = time.time()

#IO directories must be full paths
input  = sys.argv[1]
output = sys.argv[2]
shift = sys.argv[3]

inputDir='/eos/uscms/store/user/lpcljm/2018/'+input+'/'+shift
outputDir='/eos/uscms/store/user/lpcljm/2018/'+output+'/'+shift

inDir=inputDir[10:]
outDir=outputDir[10:]

os.system('eos root://cmseos.fnal.gov/ mkdir -p '+outDir)

signalList = [
    #'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8',
    'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8'
    ]

signalOutList = ['BWBW','TZBW','THBW','TZTH','TZTZ','THTH']

for sample in signalList:
    for outlabel in signalOutList:

        rootfiles = EOSlist_root_files(inputDir+'/'+sample+'_'+outlabel)
#       print 'N root files in',sample,'=',len(rootfiles)
        haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+sample+'_'+outlabel+'_hadd.root '

        print '##########'*15
        print 'HADDING:', sample,'_',outlabel
        print '##########'*15

        for file in rootfiles:
           
            haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'_'+outlabel+'/'+file

        os.system(haddcommand)

        if bool(EOSisfile(outDir+'/'+sample+'_'+outlabel+'_hadd.root')) != True:
            print haddcommand


# signalList = [
# #    'BprimeBprime_M-700_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-900_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1100_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1300_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1500_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1600_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1700_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     'BprimeBprime_M-1800_TuneCUETP8M1_13TeV-madgraph-pythia8',
#     ]

# signalOutList = ['TWTW','BZTW','BHTW','BZBH','BZBZ','BHBH']

# for sample in signalList:
#     for outlabel in signalOutList:

#         rootfiles = EOSlist_root_files(inputDir+'/'+sample+'_'+outlabel)
# #        print 'N root files in',sample,'=',len(rootfiles)
#         haddcommand = 'hadd root://cmseos.fnal.gov/'+outDir+'/'+sample+'_'+outlabel+'_hadd.root '

#         print '##########'*15
#         print 'HADDING:', sample,'_',outlabel
#         print '##########'*15

#         for file in rootfiles:
           
#             haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'_'+outlabel+'/'+file

#         os.system(haddcommand)
# #        print haddcommand

dirList = [
    'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8',
    'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8',
    'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
    'TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8',
    'TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8',
    'TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8',
    'ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
    'ST_t-channel_antitop_5f_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8_vtd_vts_prod',
    'ST_t-channel_top_5f_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8_vtd_vts_prod',
    'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',    
]
if shift == 'nominal':
    dirList.append('SingleElectron_Mar2018')
    dirList.append('SingleMuon_Mar2018')

for sample in dirList:
    
    rootfiles = EOSlist_root_files(inputDir+'/'+sample)
    haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+sample+'_hadd.root '
    
    print '##########'*15
    print 'HADDING:', sample
    print 'N root files in',sample,'=',len(rootfiles)
    print '##########'*15

    nFilesPerHadd = 999

    if len(rootfiles) < nFilesPerHadd:
        #print 'Done'
        haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+sample+'_hadd.root '
        for file in rootfiles:
            haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'/'+file
        os.system(haddcommand)
        if bool(EOSisfile(outDir+'/'+sample+'_hadd.root')) != True:
                print haddcommand

    else:
        for i in range(int(len(rootfiles)/nFilesPerHadd)+1):
            haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+sample+'_'+str(i+1)+'_hadd.root '

            begin=i*nFilesPerHadd
            end=begin+nFilesPerHadd
            if end > len(rootfiles): end=len(rootfiles)
            print 'begin:',begin,'end:',end

            for j in range(begin,end):
                haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'/'+rootfiles[j]
            os.system(haddcommand)

            if bool(EOSisfile(outDir+'/'+sample+'_'+str(i+1)+'_hadd.root')) != True:
                    print haddcommand



# bool(needed yet in 80X, waiting for high mass samples to finish

dirList = [
    'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
    'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8'
    ]
TTOutList = ['Mtt0to700','Mtt700to1000','Mtt1000toInf']

for sample in dirList:
    for outlabel in TTOutList:

        rootfiles = EOSlist_root_files(inputDir+'/'+sample+'_'+outlabel)
        print 'N root files in',sample,'=',len(rootfiles)
        haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+sample+'_'+outlabel+'_hadd.root '
    
        print '##########'*15
        print 'HADDING:', sample,'_',outlabel
        print '##########'*15

        nFilesPerHadd = 999
    
        if len(rootfiles) < nFilesPerHadd:
            haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+sample+'_'+outlabel+'_hadd.root '
            for file in rootfiles:
                haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'_'+outlabel+'/'+file
            os.system(haddcommand)
            if bool(EOSisfile(outDir+'/'+sample+'_'+outlabel+'_hadd.root')) != True:
                    print haddcommand
        else:
            for i in range(int(len(rootfiles)/nFilesPerHadd)+1):
                if i == 0: continue
                haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+sample+'_'+outlabel+'_'+str(i+1)+'_hadd.root '

                begin=i*nFilesPerHadd
                end=begin+nFilesPerHadd
                if end > len(rootfiles): end=len(rootfiles)
                print 'begin:',begin,'end:',end

                for j in range(begin,end):
                    haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'_'+outlabel+'/'+rootfiles[j]
                os.system(haddcommand)

                if bool(EOSisfile(outDir+'/'+sample+'_'+outlabel+'_'+str(i+1)+'_hadd.root')) != True:
                    print haddcommand

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))



