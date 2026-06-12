---
title: "getIntensity abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-getintensity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getIntensity.html -->


<div>
<h1>getIntensity abstract method</h1></div>

double?
getIntensity(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-mapscenelightscategory">MapSceneLightsCategory</a> category</li>
</ol>)

      

    

<p>Retrieves the current intensity of the light based on its category.</p>
<ul>
<li><code>category</code> The category of light from which the intensity is retrieved.</li>
</ul>
<p>Returns <code>double?</code>. The current intensity of the light, or <code>null</code> if the light is missing from the loaded scene
or MapScene is not intitialized.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? getIntensity(MapSceneLightsCategory category);</code></pre>

 



</div>
`
}</HTMLBlock>
