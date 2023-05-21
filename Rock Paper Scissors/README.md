<h2> Clarification: This project was created using Replit, you can check it on https://replit.com/@LautaroOchotore/Rockpaper-and-scissors</h2>
<h1> Rock Paper Scissors </h1>
<div><section id="instructions">
<p>In the file <code>RPS.py</code> you are provided with a function called <code>player</code>. The function takes an argument that is a string describing the last move of the opponent ("R", "P", or "S"). The function should return a string representing the next move for it to play ("R", "P", or "S").</p>
<p>A player function will receive an empty string as an argument for the first game in a match since there is no previous play.</p>
<p>The file <code>RPS.py</code> shows an example function that you will need to update. The example function is defined with two arguments (<code>player(prev_play, opponent_history = [])</code>). The function is never called with a second argument so that one is completely optional. The reason why the example function contains a second argument (<code>opponent_history = []</code>) is because that is the only way to save state between consecutive calls of the <code>player</code> function. You only need the <code>opponent_history</code> argument if you want to keep track of the opponent_history.</p>
<p><em>Hint: To defeat all four opponents, your program may need to have multiple strategies that change depending on the plays of the opponent.</em></p>
<h2>Development</h2>
<p>Do not modify <code>RPS_game.py</code>. Write all your code in <code>RPS.py</code>. For development, you can use <code>main.py</code> to test your code.</p>
<p><code>main.py</code> imports the game function and bots from <code>RPS_game.py</code>.</p>
<p>To test your code, play a game with the <code>play</code> function. The <code>play</code> function takes four arguments:</p>
<ul>
<li>two players to play against each other (the players are actually functions)</li>
<li>the number of games to play in the match</li>
<li>an optional argument to see a log of each game. Set it to <code>True</code> to see these messages.</li>
</ul>
<pre class="language-py" tabindex="0" role="region" aria-label="ejemplo de código de python"><code class="language-py">play<span class="token punctuation">(</span>player1<span class="token punctuation">,</span> player2<span class="token punctuation">,</span> num_games<span class="token punctuation">[</span><span class="token punctuation">,</span> verbose<span class="token punctuation">]</span><span class="token punctuation">)</span>
</code></pre>
<p>For example, here is how you would call the function if you want <code>player</code> and <code>quincy</code> to play 1000 games against each other and you want to see the results of each game:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="ejemplo de código de python"><code class="language-py">play<span class="token punctuation">(</span>player<span class="token punctuation">,</span> quincy<span class="token punctuation">,</span> <span class="token number">1000</span><span class="token punctuation">,</span> verbose<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span>
</code></pre>
<p>Click the "run" button and <code>main.py</code> will run.</p>
<h2>Testing</h2>
<p>The unit tests for this project are in <code>test_module.py</code>. We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. If you uncomment the last line in <code>main.py</code>, the tests will run automatically whenever you hit the "run" button.</p>
<h2>Submitting</h2>
<p>Copy your project's URL and submit it below.</p>
</section></div>
<h2> This one can be run on https://replit.com/@LautaroOchotore/Rockpaper-and-scissors</h2>
