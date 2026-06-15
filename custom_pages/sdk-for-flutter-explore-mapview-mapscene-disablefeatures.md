---
title: "disableFeatures abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscene-disablefeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- disableFeatures.html -->


<div>
<h1>disableFeatures abstract method</h1></div>

void
disableFeatures(<ol class="parameter-list single-line"> <li>List&lt;String&gt; features</li>
</ol>)

      

    

<p>Disables specified map features.</p>
<p>Those will become inactive
after next map redraw, meaning that <a href="sdk-for-flutter-explore-mapview-mapscene-getactivefeatures">MapScene.getActiveFeatures</a> will
return updated list of active features only after the redraw happens.</p>
<p>Does not affect features that were not specified.
Unsupported features are ignored.</p>
<p>May cause the current map configuration to be reloaded.</p>
<p>See <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a> for feature names.</p>
<ul>
<li><code>features</code> The names of features to disable (see <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a>).</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void disableFeatures(List&lt;String&gt; features);</code></pre>

 



</div>
`
}</HTMLBlock>
