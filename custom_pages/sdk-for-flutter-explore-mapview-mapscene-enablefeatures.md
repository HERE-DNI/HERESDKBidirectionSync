---
title: "enableFeatures abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscene-enablefeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableFeatures.html -->


<div>
<h1>enableFeatures abstract method</h1></div>

void
enableFeatures(<ol class="parameter-list single-line"> <li>Map&lt;String, String&gt; features</li>
</ol>)

      

    

<p>Enables specified map features.</p>
<p>Those will become active
after next map redraw, meaning that <a href="sdk-for-flutter-explore-mapview-mapscene-getactivefeatures">MapScene.getActiveFeatures</a> will
return updated list of active features only after the redraw happens.</p>
<p>Does not affect features that were not specified.
Unsupported features are ignored.</p>
<p>May cause the current map configuration to be reloaded.</p>
<p>See <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a> for feature names and <a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-class">MapFeatureModes</a> for
feature mode names.</p>
<ul>
<li><code>features</code> The list of features to enable, key is the name of the feature
(see <a href="sdk-for-flutter-explore-mapview-mapfeatures-class">MapFeatures</a>), value specifies its mode (see <a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-class">MapFeatureModes</a>).</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void enableFeatures(Map&lt;String, String&gt; features);</code></pre>

 



</div>
`
}</HTMLBlock>
