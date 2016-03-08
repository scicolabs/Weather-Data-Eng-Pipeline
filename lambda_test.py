from __future__ import print_function

import urllib
import boto3

import matplotlib.pyplot as plt
import pyart

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + str(event))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)

        #############################
		# open the file, create the displays and figure
		filename = str(response)
		radar = pyart.io.read_nexrad_archive(filename)
		display = pyart.graph.RadarDisplay(radar)
		fig1 = plt.figure(figsize=(6, 5))

		# plot super resolution reflectivity
		ax = fig1.add_subplot(111)
		display.plot('reflectivity', 0, title='NEXRAD Reflectivity',
		             vmin=-32, vmax=64, colorbar_label='', ax=ax)
		display.plot_range_ring(radar.range['data'][-1]/1000., ax=ax)
		display.set_limits(xlim=(-500, 500), ylim=(-500, 500), ax=ax)
		#plt.show()
		fig1.savefig('fig1.png', dpi=fig1.dpi)

		#########################
		fig2 = plt.figure(figsize=(10, 10))

		ax = fig2.add_subplot(221)
		display.plot('velocity', 1, ax=ax, title='Doppler Velocity',
		             colorbar_label='',
		             axislabels=('', 'North South distance from radar (km)'))
		display.set_limits((-300, 300), (-300, 300), ax=ax)

		ax = fig2.add_subplot(222)
		display.plot('differential_reflectivity', 0, ax=ax,
		             title='Differential Reflectivity', colorbar_label='',
		             axislabels=('', ''))
		display.set_limits((-300, 300), (-300, 300), ax=ax)

		ax = fig2.add_subplot(223)
		display.plot('differential_phase', 0, ax=ax,
		             title='Differential Phase', colorbar_label='')
		display.set_limits((-300, 300), (-300, 300), ax=ax)

		ax = fig2.add_subplot(224)
		display.plot('cross_correlation_ratio', 0, ax=ax,
		             title='Correlation Coefficient', colorbar_label='',
		             axislabels=('East West distance from radar (km)', ''))
		display.set_limits((-300, 300), (-300, 300), ax=ax)


		#plt.show()
		fig2.savefig('fig2.png', dpi=fig2.dpi)

        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e