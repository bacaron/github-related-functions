#!/usr/bin/env python3

import json

def create_brainlife_readme(bl_app_number,bl_app_doi,app_title,app_description,Authors,Contributors,References,json_structure,app_output,dependencies,output_dir):
	line1="[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)"
	line2="\n[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.%s-blue.svg)](https://doi.org/%s)\n" %(str(bl_app_number),bl_app_doi)
	line3="\n# %s \n" %app_title
	line4="\nThis app will %s \n" %app_description
	line5="\n### Authors \n"
	line6="\n- %s \n" %Authors
	line7="\n### Contributors \n"
	line8="\n- %s \n" %Contributors
	line9="\n### Funding Acknowledgement\n"
	line10="\nbrainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code. \n"
	line11="\n[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)"
	line12="\n[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)"
	line13="\n[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)"
	line14="\n[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)"
	line15="\n[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)\n"
	line16="\n### Citations \n"
	line17="\nWe kindly ask that you cite the following articles when publishing papers and code using this code. \n"
	line18="\n1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y \n"
	line19="\n%s \n" %References
	line20="\n#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University \n"
	line21="\n## Running the App \n"
	line22="\n### On Brainlife.io \n"
	line23="\nYou can submit this App online at [https://doi.org/%s](https://doi.org/%s) via the 'Execute' tab. \n" %(bl_app_doi,bl_app_doi)
	line24="\n### Running Locally (on your machine) \n"
	line25="\n1. git clone this repo \n"
	line26="\n2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files. \n"
	line27="\n```json \n"
	line28="%s \n" %json.dumps(json_structure,indent=4)
	line29="``` \n"
	line30="\n### Sample Datasets \n"
	line31="\nYou can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli). \n"
	line32="\n```"
	line33="\nnpm install -g brainlife \n"
	line34="bl login \n"
	line35="mkdir input \n"
	line36="bl dataset download \n"
	line37="``` \n"
	line38="\n3. Launch the App by executing 'main' \n"
	line39="\n```bash \n"
	line40="./main \n"
	line41="``` \n"
	line42="\n## Output \n"
	line43="\nThe main output of this App is %s \n" %app_output
	line44="\n#### Product.json \n"
	line45="\nThe secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing. \n"
	line46="\n### Dependencies \n"
	line47="\nThis App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.   \n"
	line48="\n- %s" %dependencies
	line49="\n"
	line50="\n#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University"

	filename='%s/README.md' %output_dir
	with open(filename,'w') as out:
	    out.writelines([line1, line2, line3, line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23,line24,line25,line26,line27,line28,line29,line30,line31,line32,line33,line34,line35,line36,line37,line38,line39,line40,line41,line42,line43,line44,line45,line46,line47,line48,line49,line50])

def extract_app_info(app_config):

    bl_app_doi = app_config['doi']
    bl_app_number = bl_app_doi.split('.app.')[1]
    app_title = app_config['name']
    config_json_structure = {}
    for i in app_config['config']:
        config_json_structure[i] = "/input/%s/%s.nii.gz" %(app_config['config'][i]['input_id'],app_config['config'][i]['file_id'])

    return bl_app_number, bl_app_doi, app_title, config_json_structure

def generate_bl_readme():

    with open('config.json','r') as config_f:
        app_config = json.load(config_f)[0]

    output_dir = './'

    [bl_app_number, bl_app_doi, app_title, config_json_structure] = extract_app_info(app_config)

    ## need to ask for user input for following variables:
    ## app_description, Authors, Contributors, References, app_output, Dependencies
    app_description = input("What is the app description? ")
    Authors = input("Who are the app authors? ")
    Contributors = input("Who are the app contributors? ")
    References = input("What are the citations for the app? ")
    app_output = input("What is the app output? ")
    Dependencies = input("What are the app dependencies? ")

    create_brainlife_readme(bl_app_number,bl_app_doi,app_title,app_description,Authors,Contributors,References,config_json_structure,app_output,Dependencies,output_dir)
