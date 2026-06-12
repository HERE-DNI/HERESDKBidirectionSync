---
title: "getActiveFeatures abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscene-getactivefeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getActiveFeatures.html -->


<div>
<h1>getActiveFeatures abstract method</h1></div>

Map&lt;String, String&gt;
getActiveFeatures()

      

    

<p>Gets map features that are currently active.</p>
<p>Active features are features that are either
enabled via a call to <a href="/sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> or that are enabled by default in the scene.</p>
<p>The key to the resulting map is the name of the feature
and the value is the active mode.</p>
<p>Result is empty if scene has not been loaded.</p>
<p>Returns <code>Map&lt;String, String&gt;</code>. The map of active features.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;String, String&gt; getActiveFeatures();</code></pre>

 



</div>
`
}</HTMLBlock>
