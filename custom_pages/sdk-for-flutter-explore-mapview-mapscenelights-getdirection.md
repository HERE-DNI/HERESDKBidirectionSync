---
title: "getDirection abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-getdirection"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getDirection.html -->


<div>
<h1>getDirection abstract method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapscenelightsdirection-class">MapSceneLightsDirection</a>?
getDirection(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapscenelightscategory">MapSceneLightsCategory</a> category</li>
</ol>)

      

    

<p>Retrieves the current direction of the light based on its category.</p>
<ul>
<li><code>category</code> The category of light from which the direction is retrieved.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapscenelightsdirection-class">MapSceneLightsDirection?</a>. The current direction of the light, or <code>null</code> if the light is missing from the loaded scene
or MapScene is not intitialized.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapSceneLightsDirection? getDirection(MapSceneLightsCategory category);</code></pre>

 



</div>
`
}</HTMLBlock>
