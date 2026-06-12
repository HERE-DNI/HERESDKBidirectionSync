---
title: "setDirection abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-setdirection"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setDirection.html -->


<div>
<h1>setDirection abstract method</h1></div>

void
setDirection(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-mapscenelightscategory">MapSceneLightsCategory</a> category, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapscenelightsdirection-class">MapSceneLightsDirection</a> direction, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>? callback</li>
</ol>)

      

    

<p>Set a new direction for the light based on its category.</p>
<ul>
<li>
<p><code>category</code> The category of light for which the direction is set.</p>
</li>
<li>
<p><code>direction</code> The Direction contains azimuth and altitude angles in degrees.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setDirection(MapSceneLightsCategory category, MapSceneLightsDirection direction, MapSceneLightsAttributeSettingCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
