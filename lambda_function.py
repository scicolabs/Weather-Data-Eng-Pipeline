from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
import pyart.graph
import pyart.io
import boto3

print('Loading function')

s3c = boto3.client('s3')

def lambda_handler(event, context):
    
    # Get NEXRAD data from it's S3 bucket
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    keyFile = key.replace("/","_")[:-3]
    fig_name = keyFile + ".png"
    
    try:
        response = s3c.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])

        download_path = keyFile
        upload_path = keyFile
        s3c.download_file(bucket, key, download_path)

        radar = pyart.io.read_nexrad_archive(download_path)

        # display the lowest elevation scan data
        display = pyart.graph.RadarDisplay(radar)
        fig = plt.figure(figsize=(9, 12))

        plots = [
            # variable-name in pyart, display-name that we want, sweep-number of radar (0=lowest ref, 1=lowest velocity)
            ['reflectivity', 'Reflectivity (dBZ)', 0],
            ['differential_reflectivity', 'Zdr (dB)', 0],
            ['differential_phase', 'Phi_DP (deg)', 0],
            ['cross_correlation_ratio', 'Rho_HV', 0],
            ['velocity', 'Velocity (m/s)', 1],
            ['spectrum_width', 'Spectrum Width', 1]
        ]

        def plot_radar_images(plots):
            ncols = 2
            nrows = len(plots)/2
            for plotno, plot in enumerate(plots, start=1):
                ax = fig.add_subplot(nrows, ncols, plotno)
                display.plot(plot[0], plot[2], ax=ax, title=plot[1],
                     colorbar_label='',
                     axislabels=('East-West distance from radar (km)' if plotno == 6 else '', 
                                 'North-South distance from radar (km)' if plotno == 1 else ''))
                display.set_limits((-300, 300), (-300, 300), ax=ax)
                display.set_aspect_ratio('equal', ax=ax)
                display.plot_range_rings(range(100, 350, 100), lw=0.5, col='black', ax=ax)
            fig.savefig(fig_name, dpi=fig.dpi)

        plot_radar_images(plots)
        s3c.upload_file(fig_name, 'data-eng-project', 'stream/' + fig_name)

        return response['ContentType']
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(key, bucket))
        raise e
        
    # s3c.download_file("data-eng-project", "fig1.png", "fig1.png")
    
    # data = open('fig.png', 'rb')
    
    # s3r = session.resource('s3')
    # s3r.Bucket('data-eng-project').put_object(Key='stream/fig.png', Body=data)

    #s3.Object('data-eng-project', 'hello.txt').put(Body=data)
    #s3.Bucket('data-eng-project').put_object(Key='stream/bar.txt', Body=message)
    