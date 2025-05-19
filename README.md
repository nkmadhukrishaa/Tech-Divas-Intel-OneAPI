## TITLE:  

Vrksha - An ML based tool to assist the Farmers of India in Crop Disease Detection 

 

## REQUIREMENTS: 

- Intel; onednn-cpu-gomp,Jupyter Notebook 

- Flask-Python's web framework 

- Internet connection 

- Tensorflow-keras 

- Matplotlib-to plot the data assessed 

 

## PURPOSE: 

Farming is one of the major sources of livelihood in India and a major population consist of farmers. Just as populous farmers are, crop diseases are so too among crops.
Crops being affected by disease can prove fatal to the crop as well as lead to monetary loss. If left undetected, it can spread to many crops and prove fatal to them as well. To provide a solution, we have 
developed a crop disease detection app which detects the disease when a photo of the affected leaf is uploaded and provides remedies to immediately treat and safeguard the crop. 

 

## BENEFITS OF THE PROJECT: 
<b>Patiala, Punjab: </b>  

The tomato farmers in the villages of Sanaur block of Patiala district are awaiting compensation for the damage to their crop due to blight disease even as the district administration officials claimed that 
assessment reports were compiled and being sent to the government. 
(Times of India: Jan 6, 2024) 

 
The late blight disease has severely affected tomato crop planted on nearly 500 acres of farmland in Patiala, it has been learnt from officials who have carried out an assessment of the crop. In addition to this,
the disease has affected another 505 acres of tomato crop in varying degrees. Horticulture officials have submitted the assessment report to the district administration for further action. 
(Times of India: Dec 22, 2023) 

<b>Rajkot, Gujarat: </b> 

Farmers in Saurashtra are staring at a major loss of groundnut crop this year because of delayed rain and the menace of white grubs. Though the recent rain came as relief, still farmers say that the damage has 
already been done as the rain did not come when it should have come. Crop damage, coupled with the high MSP declared by the Union government this year, is expected to keep groundnut oil price high this year. 
(Times of India: Sep 21, 2023) 

<b>Chandigarh, Punjab and Haryana: </b>

The ordeal of flood-affected paddy farmers continues as basmati crop has now been hit by 'foot rot', a seed-borne fungal disease, in some areas, necessitating the need to seek out elusive labour for plucking the
affected plants before going for a third round of cultivation. According to agriculture experts, since this time there was a scramble for saplings after paddy transplanted in July was damaged by floods, farmers 
had no choice but to go for leftover seeds donated by volunteers, some of which could be infected. 
(Times of India: Aug 10, 2023)  

 
When we see all the above problems faced by our farmers, it has become the need of the hour to bring in the solutions to them. While the Government of India has brought up so many steps to aid the farmers, it 
still takes some time to reach the farmers. So, this tool can be used by the farmers themselves to take steps to treat their crops. 

 
Vrksha is a tool that aids farmers at the initial level itself to solve these issues. 

- The farmers will be able to know what kind of disease is caused. 

- Knowing the causes for the disease will help the farmers to make changes to their environment for the betterment of plantation of crops. 

- The solution also suggests the farmers what kind of fertilizers can be used (in terms of mineral) to improve the health of the plant. It also suggests the fertilizers that can be avoided (in terms of minerals).  

- The specific solution helps them to improve the plant’s health and so, they can buy only the required fertilizers. 

- In future, they will have an idea of what minerals and environment conditions are required for a good plantation. 


## USER MANUAL: 

- For easy access, a login page has not been provided. 

- Firstly, the image of the disease is required. So, a photo of the infected crop is to be taken. An image of the leaf would be appreciated. 

- The Vrksha tool is opened and the ‘Predict’ button is to be clicked. Our webpage will be directed to the ‘Predict’ page. 

- The ‘Insert Image’ button is to be clicked to insert the image. 

- The diseases are detected using the ML tools. 

- The results of the detections will be displayed in the ‘Results’ page. 

- If the ‘Diseases detected’ button is clicked, the disease which has infected the crop is displayed. 

- If the ‘Remedies’ button is clicked, the remedies that can be undertaken to improve the health of the crop is displayed. 

 

## TECHNICAL WORKING: 

- The entire project works on the data set of 25027 image files belonging to 19 classes of crop diseases. 

- The data set of 783 images is split into 626 train files, 78 validation files and 79 test files. 

- The image uploaded by the user is compared with the images and accurate predictions are made using TensorFlow keras to help detect the Crop Disease. 

- This web application works on Webpages designed using HTML, CSS and JavaScript. 

- The web framework behind this web application is Python’s Flask. 


## SCREENSHOTS OF WEB APPLICATION:

<b>Home page: </b>

![home](https://github.com/C-V-Malavika/Tech-Divas/assets/34850110/6d41644c-9e14-49e8-aff1-e6ee241a99d3)

<b>Inserting an image: </b>

![insert](https://github.com/C-V-Malavika/Tech-Divas/assets/34850110/55de2046-b22f-42d1-a337-49c23537b946)

<b>Uploading image from directory: </b>

![openimg](https://github.com/C-V-Malavika/Tech-Divas/assets/34850110/b1fb42d5-060e-4b1f-bf84-8156fe134d1e)

<b>Results page-Choosing the Disease option: </b>

![results](https://github.com/C-V-Malavika/Tech-Divas/assets/34850110/99cfcd79-abc2-4c46-8357-3eef4b9c3e46)

<b>Disease detected: </b>

![disease](https://github.com/C-V-Malavika/Tech-Divas/assets/34850110/67b51dbe-7d93-4b1f-9beb-88e0cef81d5d)

<b>Results page-Choosing the Remedies option: </b>

![results2](https://github.com/C-V-Malavika/Tech-Divas/assets/34850110/f9edef46-d69a-4bba-9faa-69adfdd506b2)

<b>Remedies and Tips: </b>

![remedies](https://github.com/C-V-Malavika/Tech-Divas/assets/34850110/e7a669a1-cb1e-476c-87f4-63556aa95b39)

## TECH TEAM:

- C V Malavika
- V Chinmaiyee
- N K Madhukrishaa

Sophomores at Sri Sivasubramaniya Nadar College of Engineering
