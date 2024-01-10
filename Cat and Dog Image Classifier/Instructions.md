<h1> Cat and Dog Image Classifier </h1>
<div><section id="instructions">
<p>For this challenge, you will complete the code  to classify images of dogs and cats. You will use TensorFlow 2.0 and Keras to create a convolutional neural network that correctly classifies images of cats and dogs at least 63% of the time. (Extra credit if you get it to 70% accuracy!)</p>
<p>Some of the code is given to you but some code you must fill in to complete this challenge. Read the instruction in each text cell so you will know what you have to do in each code cell.</p>
<p>The first code cell imports the required libraries. The second code cell downloads the data and sets key variables. The third cell is the first place you will write your own code.</p>
<p>The structure of the dataset files that are downloaded looks like this (You will notice that the test directory has no subdirectories and the images are not labeled):</p>
<pre class="language-py" tabindex="0" role="region" aria-label="ejemplo de código de python"><code class="language-py">cats_and_dogs
<span class="token operator">|</span>__ train<span class="token punctuation">:</span>
    <span class="token operator">|</span>______ cats<span class="token punctuation">:</span> <span class="token punctuation">[</span>cat<span class="token punctuation">.</span><span class="token number">0</span><span class="token punctuation">.</span>jpg<span class="token punctuation">,</span> cat<span class="token punctuation">.</span><span class="token number">1</span><span class="token punctuation">.</span>jpg <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span>
    <span class="token operator">|</span>______ dogs<span class="token punctuation">:</span> <span class="token punctuation">[</span>dog<span class="token punctuation">.</span><span class="token number">0</span><span class="token punctuation">.</span>jpg<span class="token punctuation">,</span> dog<span class="token punctuation">.</span><span class="token number">1</span><span class="token punctuation">.</span>jpg <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span>
<span class="token operator">|</span>__ validation<span class="token punctuation">:</span>
    <span class="token operator">|</span>______ cats<span class="token punctuation">:</span> <span class="token punctuation">[</span>cat<span class="token punctuation">.</span><span class="token number">2000</span><span class="token punctuation">.</span>jpg<span class="token punctuation">,</span> cat<span class="token punctuation">.</span><span class="token number">2001</span><span class="token punctuation">.</span>jpg <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span>
    <span class="token operator">|</span>______ dogs<span class="token punctuation">:</span> <span class="token punctuation">[</span>dog<span class="token punctuation">.</span><span class="token number">2000</span><span class="token punctuation">.</span>jpg<span class="token punctuation">,</span> dog<span class="token punctuation">.</span><span class="token number">2001</span><span class="token punctuation">.</span>jpg <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span>
<span class="token operator">|</span>__ test<span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">.</span>jpg<span class="token punctuation">,</span> <span class="token number">2</span><span class="token punctuation">.</span>jpg <span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">.</span><span class="token punctuation">]</span>
</code></pre>
<p>You can tweak epochs and batch size if you like, but it is not required.</p>
<p>The following instructions correspond to specific cell numbers, indicated with a comment at the top of the cell (such as <code># 3</code>).</p>
<h2>Cell 3</h2>
<p>Now it is your turn! Set each of the variables in this cell correctly. (They should no longer equal <code>None</code>.)</p>
<p>Create image generators for each of the three image data sets (train, validation, test). Use <code>ImageDataGenerator</code> to read / decode the images and convert them into floating point tensors. Use the <code>rescale</code> argument (and no other arguments for now) to rescale the tensors from values between 0 and 255 to values between 0 and 1.</p>
<p>For the <code>*_data_gen</code> variables, use the <code>flow_from_directory</code> method. Pass in the batch size, directory, target size (<code>(IMG_HEIGHT, IMG_WIDTH)</code>), class mode, and anything else required. <code>test_data_gen</code> will be the trickiest one. For <code>test_data_gen</code>, make sure to pass in <code>shuffle=False</code> to the <code>flow_from_directory</code> method. This will make sure the final predictions stay is in the order that our test expects. For <code>test_data_gen</code> it will also be helpful to observe the directory structure.</p>
<p>After you run the code, the output should look like this:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="ejemplo de código de python"><code class="language-py">Found <span class="token number">2000</span> images belonging to <span class="token number">2</span> classes<span class="token punctuation">.</span>
Found <span class="token number">1000</span> images belonging to <span class="token number">2</span> classes<span class="token punctuation">.</span>
Found <span class="token number">50</span> images belonging to <span class="token number">1</span> <span class="token keyword">class</span><span class="token punctuation">.</span>
</code></pre>
<h2>Cell 4</h2>
<p>The <code>plotImages</code> function will be used a few times to plot images. It takes an array of images and a probabilities list, although the probabilities list is optional. This code is given to you. If you created the <code>train_data_gen</code> variable correctly, then running this cell will plot five random training images.</p>
<h2>Cell 5</h2>
<p>Recreate the <code>train_image_generator</code> using <code>ImageDataGenerator</code>.</p>
<p>Since there are a small number of training examples, there is a risk of overfitting. One way to fix this problem is by creating more training data from existing training examples by using random transformations.</p>
<p>Add 4-6 random transformations as arguments to&nbsp;<code>ImageDataGenerator</code>. Make sure to rescale the same as before.</p>
<h2>Cell 6</h2>
<p>You don't have to do anything for this cell. <code>train_data_gen</code> is created just like before but with the new <code>train_image_generator</code>. Then, a single image is plotted five different times using different variations.</p>
<h2>Cell 7</h2>
<p>In this cell, create a model for the neural network that outputs class probabilities. It should use the Keras Sequential model. It will probably involve a stack of Conv2D and MaxPooling2D layers and then a fully connected layer on top that is activated by a ReLU activation function.</p>
<p>Compile the model passing the arguments to set the optimizer and loss. Also pass in <code>metrics=['accuracy']</code> to view training and validation accuracy for each training epoch.</p>
<h2>Cell 8</h2>
<p>Use the <code>fit</code> method on your <code>model</code> to train the network. Make sure to pass in arguments for <code>x</code>, <code>steps_per_epoch</code>, <code>epochs</code>, <code>validation_data</code>, and <code>validation_steps</code>.</p>
<h2>Cell 9</h2>
<p>Run this cell to visualize the accuracy and loss of the model.</p>
<h2>Cell 10</h2>
<p>Now it is time to use your model to predict whether a brand new image is a cat or a dog.</p>
<p>In this cell, get the probability that each test image (from <code>test_data_gen</code>) is a dog or a cat. <code>probabilities</code> should be a list of integers.</p>
<p>Call the <code>plotImages</code> function and pass in the test images and the probabilities corresponding to each test image.</p>
<p>After you run the cell, you should see all 50 test images with a label showing the percentage of "sure" that the image is a cat or a dog. The accuracy will correspond to the accuracy shown in the graph above (after running the previous cell). More training images could lead to a higher accuracy.</p>
<h2>Cell 11</h2>
<p>Run this final cell to see if you passed the challenge or if you need to keep trying.</p>
</section></div>
