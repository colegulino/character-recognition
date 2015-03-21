# character-recognition
<h3>Simple Pseudoinverse Algorithm for Recognizing Single Characters</h3>
Designed to recognize single symbols. <br>
Weight Matrix is designed to be be trained by images where the symbol is black with a white or colored uniform background<br>
<h3>Steps to run the program: </h3>
<ol>
  <li>Use pickle to store a list in a text file of the image names you want to train the weight matrix with</li>
  <li>Run weightMatrixGeneration.py specifying the text file that holds the list of image names</li>
  <ol><li>The weight matrix and dictionary holding bipolar vectors for each symbol with the key being the name of the image</li></ol>
  <li>Run characterRecognition.py specifying the image you want to test for recognition</li>
  <ol><li>The output of the program will be the character from the dictionary that the test character most resembles with the percentage of accuracy</li></ol>
  
