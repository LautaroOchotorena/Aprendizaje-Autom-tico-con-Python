### This is a course taken in Freecodecamp, to complete it I had to make 5 proyects which are the ones that are in the folders. <br>
### The 'Rock, Paper, Scissors' project can also be checked without downloading anything, just check https://replit.com/@LautaroOchotore<br>

<div id="content-start" tabindex="-1"><div tabindex="-1"><main id="learn-app-wrapper"><div class="container"><div class="row"><div class="col-md-8 col-md-offset-2 col-sm-10 col-sm-offset-1 col-xs-12"><div class="spacer" style="padding: 15px 0px; height: 1px;"></div><div class="challenge-title-wrap"><a href="https://contribute.freecodecamp.org/#/i18n/espanol/how-to-translate-files" class="title-translation-cta" rel="noopener noreferrer" target="_blank">Ayúdanos a traducir</a><div class="challenge-title"><div class="title-text"><h1>Rock Paper Scissors</h1><svg aria-label="Aprobado" height="15" viewBox="0 0 200 200" width="15" xmlns="http://www.w3.org/2000/svg"><g aria-hidden="true"><title>Aprobado</title><circle cx="100" cy="99" fill="var(--primary-color)" r="95" stroke="var(--primary-color)" stroke-dasharray="null"></circle><rect fill="var(--primary-background)" height="30" stroke="var(--primary-background)" stroke-dasharray="null" transform="rotate(-45, 120, 106.321)" width="128.85878" x="55.57059" y="91.32089"></rect><rect fill="var(--primary-background)" height="30" stroke="var(--primary-background)" stroke-dasharray="null" transform="rotate(45, 66.75, 123.75)" width="80.66548" x="26.41726" y="108.75"></rect></g></svg></div></div></div><div class="challenge-instructions  "><div><section id="description">
<p>For this challenge, you will create a program to play Rock, Paper, Scissors. A program that picks at random will usually win 50% of the time. To pass this challenge your program must play matches against four different bots, winning at least 60% of the games in each match.</p>
<p>You will be <a href="https://replit.com/github/freeCodeCamp/boilerplate-rock-paper-scissors" target="_blank" rel="noopener noreferrer nofollow">working on this project with our Replit starter code</a>.</p>
<ul>
<li>Start by importing the project on Replit.</li>
<li>Next, you will see a <code>.replit</code> window.</li>
<li>Select <code>Use run command</code> and click the <code>Done</code> button.</li>
</ul>
<p>We are still developing the interactive instructional part of the machine learning curriculum. For now, you will have to use other resources to learn how to pass this challenge.</p>
</section></div><hr><div><section id="instructions">
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
</section></div><hr></div><form id="dynamic-front-end-form" style="width: 100%;"><div class="form-group"><label for="solution" class="control-label">Enlace a la solución</label><input name="solution" placeholder="ex: https://replit.com/@camperbot/hello" required="" rows="4" type="url" id="solution" class="form-control" value=""></div><button type="submit" disabled="" class="btn btn-primary btn-block">He completado este desafío</button></form><a href="https://forum.freecodecamp.org/t/462376" target="_blank" class="btn-invert btn btn-primary btn-block">Obtén un consejo</a><button type="button" class="btn-invert btn btn-primary btn-block">Solicitar ayuda</button><br><div class="spacer" style="padding: 15px 0px; height: 1px;"></div></div></div></div></main></div></div>
