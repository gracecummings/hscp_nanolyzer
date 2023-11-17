# HSCP Studies with NanoAOD content

This is a repo with some code to allow for basic studies for the HSCP analyses. These analyses normally happen at the AOD level, but for trigger studies and the similar, it is easier (and quicker) to do them at the nanoAOD level.

## Setting up the environment

We want to use cvmfs and stuff so this works seemlessly whereever that is mounted. To this end, we will use the predefined LCG environments, and those alone. To find the list of all of the possible LCG environments, please check out:

https://lcginfo.cern.ch/

To setup the environment, run

```
source /cvmfs/sft.cern.ch/lcg/views/LCG_104/x86_64-centos7-gcc11-opt/setup.sh
```

In order to access remote files, you will have to have a grid certifcate. To authenticate, run

```
voms-proxy-init --rfc --voms cms -valid 192:00
```

and enter your grid certificate.

## Finding Samples

In this repo, CMS files are accessed via xrootd. The names and paths of the files are stored in .txt files. If one wants to run over additional samples, one must make new .txt files.

To find the HSCP datasets (after making sure your grid proxy is valid), run

```
dasgoclient --query='dataset dataset=/HSCP*/RunII*/NANOAODSIM'
```

The above command will print every dataset, which is good if you want to find everything! For most of these studies, just a few sets will suffice. As an example, we will look at the 1800 GeV Gluino sample. To list all of the files in that dataset, and to make a text file with them, one would execute

```
dasgoclient --query='file dataset=/HSCPgluino_M-1800_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM > HSCPgluino_M-1800_TuneCP5_13TeV-pythia8_nanoFiles.txt'
```