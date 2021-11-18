



  <h3 align="center">Table tenis movement dection dataset and creation of ML models</h3>

  <p align="center">
    Dataset used in a master thesis 
  </p>




<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
          <a href="#datasets">Datasets</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

This project contains 2 main datasets acquired using a robot in table tennis and allows the creation of 3 ML Models.

The ML models are the following:
* Create ML - Apple's Machine learning tool
* CNN-LSTM - one-dimensional Convolutional Neural Network LSTM - `CNN-LSTM.py`
* ConvLSTM - one-dimensional Convolutional LSTM - `convLSTM.py`

## Datasets
On the datasets folders its possible to find the following specifications:
* Raw
* Pre-processed

###Raw
The raw folder is where the files have not been touched or altered in anyway.
This folder contains the two types of dataset adquired.
One fast dataset where a robot would send a ball every 1.166 seconds and a 
slow dataset where the robot would send a ball every 1.74 seconds.
Each of this types has 6 classes representing each movement (rest, right top spin, left top spin, 
block, right flip, left flip.)
Each file represents a session with an athlete where it was asked to do thepip install --pre -i https://pypi.anaconda.org/scipy-wheels-nightly/simple scipy respective 
movement until the robot had no more balls to shoot.


###Pre-processed
On this folder is possible to find 2 raw datasets plus 3 pre-processed created from the raw dataset ready to copy and paste on createML

####D1-fast
* Composed by data from the fast dataset from RAW
* unnecessary data removed
* renamed columns  
* timestamp column was converted as starting from zero
* train and test data randomly separated

#####D2-slow
* Same features as the fast dataset but instead using the slow dataset from raw data.

#####D3-fast-cut
This dataset contains the data from D1-fast dataset. Then a stroke detection algorithm 
was applied (if forces on any axis were greater then 1m/s then create a prediction windows) and a windows prediction
of size 46 was cut for every possible movement detected.
This dataset contains a folder for each type of movement and each movement folder contains multiple files in which a file
represents the corresponding movement.

For the rest class, samples were obtained from the stroke algorithm for each time no stroke was being detected.


* Same data as D1-fast
* Movement detection algorithm applied.
* Renamed columns  
* Timestamp column converted as starting from zero

slow_&_fast_dataset_with_cut_movements_separated

#####D4-slow-cut
This dataset contains the data from D2-slow dataset. The same stroke detection algorithm was applied

* Same data as D2-slow
* Movement detection algorithm applied.
* Renamed columns  
* Timestamp column converted as starting from zero



#####D5-fast-slow-cut
This dataset merges both D3-fast-cut and D4-slow-cut. 
* D3-fast-cut and D4-slow-cut from raw data merged together
* Movement detection algorithm applied.
* Renamed columns  
* Timestamp column converted as starting from zero


Dataset where files are separated into train and test folders (80%, 20%) using `train_test_sep_data.py`
which sorts all the files by class randomly. 


## ML Models
### CreateML
On this folder is possible to find the 5 pre-processed datasets created from the raw dataset ready to copy and paste on createML.


### CNN-LSTM
This folder contains only D3-fast, D4-slow and D5-fast-slow-cut were used. These datasets were used to generate the CNN-LSTM model
Then for each dataset, a further pre-processing was applied to fit the model requirements.
For each dataset folder, the folder contains a file for every axis represented on an accelerometer and gyroscope sensor.
Each file has multiple rows with 47 columns where the first 46 represents sensor data of the 
respective axxis and sensor and the last class represents the movement id corresponding to sensor data
   * "right_top_spin" = 0 
   * "left_top_spin" = 1, 
   * "block" = 2, 
   * "right_flip" = 3, 
   * "left_flip" = 4, 
   * "rest" = 5
   
###ConvLSTM
The same folder structure as CNN-LSTM. 


 The code for the algorithm applied to the raw dataset can be seen here: 
 Github link:
 TO-DO
<!--* [R](https://www.r-project.org/)-->




<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

* Python 3
  ```sh
  https://www.python.org/downloads/
  ```
* Jupyter-notebook
  ```
  https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html#
  ```

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Create a virtual environment
   ```sh
   python3 -m venv /path/to/new/virtual/environment
   ```
3. Install the requirements on the virtual using  `requirements.txt`
   ```JS
   pip3 install -r requirements.txt;
   ```



<!-- USAGE EXAMPLES -->
## Usage
Run the any of the ML Models
   ```JS
   jupyter notebook
   python3 LSTM.py
   python3 CNN-LSTM.py
   python3 convLSTM.py
   ```

To change the dataset for the CNN-LSTM and convLSTM models, just change the directory on function
```
def load_dataset_group():
```
<!-- CONTRIBUTING -->
## Contributing

At the time of writting this readme no contributions are allowed




<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Nuno Ferreira  - 35053@ufp.edu.pt

Project Link: [https://github.com/MikaPower/ai_ping_pong](https://github.com/MikaPower/ai_ping_pong)









<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png