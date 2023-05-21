<h1> Book Recommendation Engine using KNN </h1>
<div><section id="instructions">
<p>In this challenge, you will create a book recommendation algorithm using <strong>K-Nearest Neighbors</strong>.</p>
<p>You will use the <a href="http://www2.informatik.uni-freiburg.de/~cziegler/BX/" target="_blank" rel="noopener noreferrer nofollow">Book-Crossings dataset</a>. This dataset contains 1.1 million ratings (scale of 1-10) of 270,000 books by 90,000 users.</p>
<p>After importing and cleaning the data, use <code>NearestNeighbors</code> from <code>sklearn.neighbors</code> to develop a model that shows books that are similar to a given book. The Nearest Neighbors algorithm measures the distance to determine the “closeness” of instances.</p>
<p>Create a function named <code>get_recommends</code> that takes a book title (from the dataset) as an argument and returns a list of 5 similar books with their distances from the book argument.</p>
<p>This code:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="ejemplo de código de python"><code class="language-py">get_recommends<span class="token punctuation">(</span><span class="token string">"The Queen of the Damned (Vampire Chronicles (Paperback))"</span><span class="token punctuation">)</span>
</code></pre>
<p>should return:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="ejemplo de código de python"><code class="language-py"><span class="token punctuation">[</span>
  <span class="token string">'The Queen of the Damned (Vampire Chronicles (Paperback))'</span><span class="token punctuation">,</span>
  <span class="token punctuation">[</span>
    <span class="token punctuation">[</span><span class="token string">'Catch 22'</span><span class="token punctuation">,</span> <span class="token number">0.793983519077301</span><span class="token punctuation">]</span><span class="token punctuation">,</span> 
    <span class="token punctuation">[</span><span class="token string">'The Witching Hour (Lives of the Mayfair Witches)'</span><span class="token punctuation">,</span> <span class="token number">0.7448656558990479</span><span class="token punctuation">]</span><span class="token punctuation">,</span> 
    <span class="token punctuation">[</span><span class="token string">'Interview with the Vampire'</span><span class="token punctuation">,</span> <span class="token number">0.7345068454742432</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
    <span class="token punctuation">[</span><span class="token string">'The Tale of the Body Thief (Vampire Chronicles (Paperback))'</span><span class="token punctuation">,</span> <span class="token number">0.5376338362693787</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
    <span class="token punctuation">[</span><span class="token string">'The Vampire Lestat (Vampire Chronicles, Book II)'</span><span class="token punctuation">,</span> <span class="token number">0.5178412199020386</span><span class="token punctuation">]</span>
  <span class="token punctuation">]</span>
<span class="token punctuation">]</span>
</code></pre>
<p>Notice that the data returned from <code>get_recommends()</code> is a list. The first element in the list is the book title passed into the function. The second element in the list is a list of five more lists. Each of the five lists contains a recommended book and the distance from the recommended book to the book passed into the function.</p>
<p>If you graph the dataset (optional), you will notice that most books are not rated frequently. To ensure statistical significance, remove from the dataset users with less than 200 ratings and books with less than 100 ratings.</p>
<p>The first three cells import libraries you may need and the data to use. The final cell is for testing. Write all your code in between those cells.</p>
</section></div>
