# $Id: flac2txt.py,v 0.2 2018-03-02 14:28:24-08 fran abriz $
import argparse
import os.path, sys
from googleapiclient.discovery import build

# Take a list of files with FLAC encoding; run them through the Google Cloud
# Speech API to transcribe them into text; and put the text in a similarly
# named .txt output in a named directory.

def main(args, inputs):

    print(args)
    #print(sys.argv)
    print(inputs)
    APIKEY = args["key"]
    b = args["b"]
    o = args["o"]
    sservice = build('speech', 'v1', developerKey=APIKEY)
    stdout_orig = sys.stdout
    fbody = {
	"config": {
	    "languageCode": "en-US"
	    },
	"audio": {
	    "uri": uri
	    }
	}
#		"encoding": 'FLAC',
#		"sampleRateHertz": 22050

    for a in inputs:
        uri = "gs://"+b+'/'+a
        output = o+"/"+os.path.splitext(os.path.basename(uri))[0]+".txt"
	# splitext() splits off extension e.g. .flac
        # write stdout to file output
        sys.stdout = open(output, 'w')
        response = ssservice.speech().recognize(body=fbody).execute()
	print(response)
	print('============')
        print(response['results'][0]['alternatives'][0]['transcript'])
        sys.stdout.flush()
    sys.exit(0)

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('-b', help='bucket', default='audio')
   parser.add_argument('-key', help='API key', required=True)
   parser.add_argument('-o', help='output file in ~', default='out')
   args, inputs = parser.parse_known_args()
   arguments = args.__dict__
   main(arguments, inputs)
