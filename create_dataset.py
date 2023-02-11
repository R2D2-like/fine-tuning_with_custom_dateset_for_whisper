import csv
from datasets import load_dataset, DatasetDict, Dataset, Audio
mp3 = []
text = []
with open("/storage/home/robot_dev5/TRAIL-INTEGRATION/weblab_hsr_tidyup_rcj2023_2/catkin_ws/src/weblab_wrs_v2/scripts/data_set/data_set.csv", "r") as f:
    #reader = csv.reader(f)
    reader = f.readlines()
    print(reader)
    for lines in reader:
        lines = str(lines)
        print(lines)
        line = lines.split(',')
        print(line)
        mp3.append(line[0].replace('/root/HSR','/home/robot_dev5/TRAIL-INTEGRATION/weblab_hsr_tidyup_rcj2023_2'))
        text.append(line[1].replace('\n',''))
                
# mp3 = ["/home/robot_dev5/TRAIL-INTEGRATION/weblab_hsr_tidyup_rcj2023_2/catkin_ws/src/weblab_wrs_v2/scripts/saved_audio/mic_2023_2_9_2_35_39.mp3",\
#     "/home/robot_dev5/TRAIL-INTEGRATION/weblab_hsr_tidyup_rcj2023_2/catkin_ws/src/weblab_wrs_v2/scripts/saved_audio/mic_2023_2_9_2_35_29.mp3"]
#text = ["I would like to have a lemon and chocolate milk.",\
#             "I would like to have an apple and coak."]
print(mp3)
print(text)
#mp3 = ['/home/robot_dev5/TRAIL-INTEGRATION/weblab_hsr_tidyup_rcj2023_2/catkin_ws/src/weblab_wrs_v2/scripts/collected_data/mic_2023_2_11_11_33_8.mp3', '/home/robot_dev5/TRAIL-INTEGRATION/weblab_hsr_tidyup_rcj2023_2/catkin_ws/src/weblab_wrs_v2/scripts/collected_data/mic_2023_2_11_13_56_35.mp3']
audio_dataset_train = Dataset.from_dict({"audio": mp3,\
                                   "sentence": text},\
                                 ).cast_column("audio", Audio())
audio_dataset_test = Dataset.from_dict({"audio": mp3,\
                                   "sentence": text},\
                                 ).cast_column("audio", Audio())

audio_dataset = DatasetDict({'train': audio_dataset_train, 'test': audio_dataset_test})
print(audio_dataset['train'])
                              
print(audio_dataset['train'][0]["audio"])
print(audio_dataset)
print(type(audio_dataset['train'][0]["sentence"]))
# print(audio_dataset["sentence"])
# audio_dataset.push_to_hub("figfig/restaurant_order_local_test",'train') 
audio_dataset.push_to_hub("figfig/restaurant_order_HSR_test") 
