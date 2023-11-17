import uproot
from coffea.nanoevents import NanoEventsFactory

def makeXrootDFilenames(files,redirect):
    #remove trailing linebreak
    fs = [x.split('\n')[0] for x in files]
    #add redirect
    fxrd = [redirect+x for x in fs]
    return fxrd

if __name__=="__main__":
    f = open('samples/HSCPgluino_M-1800_TuneCP5_13TeV-pythia8_nanoFiles.txt')
    fs = f.readlines()
    redirector = 'root://cmsxrootd.fnal.gov/'#This can be changed!https://xrootd.slac.stanford.edu/index.html 
    samples = makeXrootDFilenames(fs,redirector)
    
    #Let's look at the first file
    #file = uproot.open(samples[0])
    #tree = file['Events']
    #tree.show()#This is the very large print out! All of the details of what is in here is found
    #https://cms-nanoaod-integration.web.cern.ch/integration/cms-swCMSSW_10_6_X/mc106Xul18_doc.html
    
    #Okay, let's use coffea
    print("Using Coffea to do something a bit more usable - only plotting electron info")
    events = NanoEventsFactory.from_root(samples[0]).events()
    print(events.Electron.fields)
