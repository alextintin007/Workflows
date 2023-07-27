# cd /home/cmsusr
echo "Setting up ${CMSSW_VERSION}"
source ${CMS_INSTALL_DIR}/cmsset_default.sh
scramv1 project CMSSW ${CMSSW_VERSION}
cmsrel ${CMSSW_VERSION}
cd ${CMSSW_VERSION}/src
cmsenv
echo "CMSSW should now be available."
curl https://raw.githubusercontent.com/cms-sw/genproductions/master/Utilities/calculateXSectionAndFilterEfficiency/genXsec_cfg.py -o ana.py
# cp $REANA_WORKSPACE/code/doubleeg_nanoaod_eg.root .
cmsRun ana.py inputFiles="file:root://eospublic.cern.ch//eos/opendata/cms/mc/RunIIFall15MiniAODv2/ADDGravToGG_MS-3000_NED-2_KK-1_M-1000To2000_13TeV-sherpa/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/3AE9F9CF-09B8-E511-AB84-00237DF29430.root" maxEvents=-1 > xsec.log 2>&1
echo "here5"
ls
wget https://raw.githubusercontent.com/Ari-mu-l/genproductions/master/Utilities/calculateXSectionAndFilterEfficiency/output_to_numpy.py -O output_to_numpy.py
python output_to_numpy.py
ls
cp xsec.npy $REANA_WORKSPACE/results/production_output/
echo "done"