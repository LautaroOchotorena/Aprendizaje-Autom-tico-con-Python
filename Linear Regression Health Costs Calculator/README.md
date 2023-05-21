<h1> Linear Regression Health Costs Calculator </h1>
<div><section id="instructions">
<p>In this challenge, you will predict healthcare costs using a regression algorithm.</p>
<p>You are given a dataset that contains information about different people including their healthcare costs. Use the data to predict healthcare costs based on new data.</p>
<p>The first two cells of this notebook import libraries and the data.</p>
<p>Make sure to convert categorical data to numbers. Use 80% of the data as the <code>train_dataset</code> and 20% of the data as the <code>test_dataset</code>.</p>
<p><code>pop</code> off the "expenses" column from these datasets to create new datasets called <code>train_labels</code> and <code>test_labels</code>. Use these labels when training your model.</p>
<p>Create a model and train it with the <code>train_dataset</code>. Run the final cell in this notebook to check your model. The final cell will use the unseen <code>test_dataset</code> to check how well the model generalizes.</p>
<p>To pass the challenge, <code>model.evaluate</code> must return a Mean Absolute Error of under 3500. This means it predicts health care costs correctly within $3500.</p>
<p>The final cell will also predict expenses using the <code>test_dataset</code> and graph the results.</p>
</section></div>
