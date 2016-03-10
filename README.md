# Lambda Architecture (Batch & Streaming) Pipeline with NEXRAD Radar Data

The [NEXRAD data](https://aws.amazon.com/noaa-big-data/nexrad/) is a public dataset hosted on amazon.

**Dataset Information:**
- Stands for Next Generation Weather Radar
- Network of 160 high-resolution Doppler radar sites that detects precipitation and atmospheric movement
- Historical archives from June 1991 to present
- Real-time streaming (5 minute intervals from each site)
- Both streams are available on aws S3 buckets
- Enables Storm Prediction
- Study of weather's impact on various sectors


**Notebooks rendered on nbviewer (recommended for animated plots):**

- [PART1 - Introduction to NEXRAD Dataset](http://nbviewer.jupyter.org/github/MarvinBertin/Weather-Data-Eng-Pipeline/blob/master/PART1-NEXRAD_Data_Intro.ipynb)
- [PART2 - Mapping and Visualizing Hurricanes](http://nbviewer.jupyter.org/github/MarvinBertin/Weather-Data-Eng-Pipeline/blob/master/PART2-Weather_Data_Batch_Mapping_Visualization.ipynb)
- [PART3 - Batch Analysis with Hadoop MapReduce](http://nbviewer.jupyter.org/github/MarvinBertin/Weather-Data-Eng-Pipeline/blob/master/PART3-HadoopMapReduce.ipynb)
- [PART4 - Stream and Visualize Daily Weather](http://nbviewer.jupyter.org/github/MarvinBertin/Weather-Data-Eng-Pipeline/blob/master/PART4-Daily_Weather_Data_Stream.ipynb)
- [PART5 - Serverless Architecture with Amazon Lambda](http://nbviewer.jupyter.org/github/MarvinBertin/Weather-Data-Eng-Pipeline/blob/master/PART5-Streaming_AWS_Lambda.ipynb)
