## FruitAI by GitAI



## Projet description

This project is an app with several features aroud fruit using computer vision. It can detect and recognize the fruits present on a picture, whether they are rotten, and how much all the fruits cost.



## Installation

Python version recommended : 3.10
Run the code below to install the required modules.
```
pip install -r requirements.txt
```


## Usage

List of fruits which can be classified with v1:

- Green apple
- Red apple
- Apricot
- Banana
- Clementine
- Fig
- Red onion
- White onion
- Pear
- Kiwi
- Avocado
- Red pepper
- Potato
- Strawberry
- Watermelon


List of fruits which can be classified with v2:
- Grape
- Apple
- Mango
- Strawberry
- Banana
- Peach
- Orange
- Pear



How to use with CLI: 

- Manuel mode : Classify the fruit you cropped manually 
    Run the code below in the terminal after replacing [image] with the path to the image you want to use, then select the fruit you want to classify with your mouse and press enter.
```
python fruit_detection_main.py -i [image] -p fruit_type_manual
```

- Auto mode : Detects all the fruit present and classify them
    Run the code below in the terminal after replacing [image] with the path to the image you want to use   
    
```
python fruit_detection_main.py -i [image] -p fruit_type_auto
```                 
- Cost mode : Detects all the fruit present and computes the total price
```
python fruit_detection_main.py -i [image] -p cost
```                 


## Support

alexis.chapelant@student-cs.fr
erwin.deng@student-cs.fr

## The GitAI Team
+ Member A : Alexis Chapelant
+ Member B : Hung
+ Member C : Je suis Yi
+ Member D : Xavier Mc Court
+ Member E : Erwin DENG


### Documentation

Resnet50: https://arxiv.org/abs/1512.03385
Yolo:
