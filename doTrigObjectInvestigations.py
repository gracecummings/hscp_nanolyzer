import uproot
import argparse
import mplhep
import numpy as np
import awkward as ak
import matplotlib.pyplot as plt
from coffea.nanoevents import NanoEventsFactory

mplhep.style.use(mplhep.style.CMS)

def makeXrootDFilenames(files,redirect):
    fs = [x.split('\n')[0] for x in files]
    fxrd = [redirect+x for x in fs]
    return fxrd

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--sample", type=str,help = "sample name, ie HSCPgluino_M-1800_TuneCP5_13TeV-pythia8")
    args = parser.parse_args()
    
    #Open the files
    f = open('samples/'+args.sample+'_nanoFiles.txt')
    fs = f.readlines()
    redirector = 'root://cmsxrootd.fnal.gov/'
    samples = makeXrootDFilenames(fs,redirector)
    events = NanoEventsFactory.from_root(samples[0]).events()
    print(samples[0])

    #Trigger parameters
    #Ideally want to access a bunch of branches by name
    #not sure how to use string to access it
    hltpaths = ['PFMET120_PFMHT120_IDTight']
    #l1seeds  = []
    #hltpaths = events.HLT.fields


    hltdecs = events.HLT.PFMET120_PFMHT120_IDTight
    numtot  = len(hltdecs)
    passtrg = np.array(hltdecs).sum()

    print("Total number of events: ",numtot)
    print("Passing {0} HLT Path: {1}".format(hltpaths[0],passtrg))

    #Some analysis
    trgdevnts = events[events.HLT.PFMET120_PFMHT120_IDTight & ~events.HLT.Mu50]
    print(len(trgdevnts))

    #trigpt = ak.flatten(events.TrigObj.pt)
    #print("trig pt max: ",max(trigpt))
    #print("some trig pts: ",trigpt[:6])
    #print("some trig pts: ",trigpt[6:12])
    #print("some trig pts: ",trigpt[12:18])
    #print("some trig pts: ",trigpt[18:24])
    #print("some trig pts: ",trigpt[24:30])
    #print("some trig pts: ",trigpt[30:36])

    #Make some plots
    fig0, (ax01,ax02) = plt.subplots(nrows=2,ncols=3,figsize=(30,15))
    ax01[0].set_xlabel('All TrgObj pT, no trig req')
    ax01[0].set_yscale('log')
    ax01[0].set_ylim([0.1,100000])
    ax01[1].set_xlabel('All TrgObj Eta, no trig req')
    ax01[2].set_xlabel('All TrgObj Phi, no trig req')
    
    ax02[0].set_xlabel('All TrgObj pT, mettrg no mutrg')
    ax02[0].set_yscale('log')
    ax02[0].set_ylim([0.1,100000])
    ax02[1].set_xlabel('All TrgObj Eta, mettrg no mutrg')
    ax02[2].set_xlabel('All TrgObj Phi, mettrg no mutrg')
    

    fig1, (ax11,ax12) = plt.subplots(nrows=2,ncols=2,figsize=(20,15))
    ax11[0].set_xlabel('All TrgObj ID, no trig req')
    ax12[0].set_xlabel('All TrgObj ID, mettrg no mutrg')
    ax11[1].set_xlabel('nTrgObj, no trig req')
    ax12[1].set_xlabel('nTrgObj, mettrg no mutrg')

    alltrighists = []
    trigdhists   = []
    alltrighists.append(ax01[0].hist(ak.flatten(events.TrigObj.pt),bins=np.linspace(0,25000,100)))
    alltrighists.append(ax01[1].hist(ak.flatten(events.TrigObj.eta),bins=np.linspace(-5,5,100)))
    alltrighists.append(ax01[2].hist(ak.flatten(events.TrigObj.phi),bins=np.linspace(-3.14,3.14,100)))
    alltrighists.append(ax11[0].hist(ak.flatten(events.TrigObj.id),bins=np.linspace(0,23,24)))
    alltrighists.append(ax11[1].hist(ak.num(events.TrigObj.id),bins=np.linspace(0,30,31)))

    trigdhists.append(ax02[0].hist(ak.flatten(trgdevnts.TrigObj.pt),bins=np.linspace(0,25000,100)))
    trigdhists.append(ax02[1].hist(ak.flatten(trgdevnts.TrigObj.eta),bins=np.linspace(-5,5,100)))
    trigdhists.append(ax02[2].hist(ak.flatten(trgdevnts.TrigObj.phi),bins=np.linspace(-3.14,3.14,100)))
    trigdhists.append(ax12[0].hist(ak.flatten(trgdevnts.TrigObj.id),bins=np.linspace(0,23,24)))
    trigdhists.append(ax12[1].hist(ak.num(trgdevnts.TrigObj.id),bins=np.linspace(0,30,31)))

    #divs = []
    #bins = []
    #for i,hist in enmuerate(alltrighists):
    #    divs.append(trigdhists[i][0]/hist[0])
    #    bins.append(hist[1])
        
    #fig2, (ax21,ax22) = plt.subplots(nrows=2,ncols=2,figsize=(20,11.25),height_ratios=2)
    

    fig0.savefig('trig_obj_comp_kinematics.png')
    fig1.savefig('trig_obj_comp_gendescrip.png')
    


