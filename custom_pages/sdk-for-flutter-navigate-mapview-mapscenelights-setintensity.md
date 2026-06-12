---
title: "setIntensity abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscenelights-setintensity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setIntensity.html -->


<div>
<h1>setIntensity abstract method</h1></div>

void
setIntensity(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a> category, </li>
<li>double intensity, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>? callback</li>
</ol>)

      

    

<p>Set a new intensity for the light based on its category.</p>
<ul>
<li>
<p><code>category</code> The category of light for which the intensity is set.</p>
</li>
<li>
<p><code>intensity</code> The light intensity value must be inside the range [0, 10].
The intensity value is clamped to this range.
If the value falls outside its supported range, it will be adjusted to stay within the range.
Note: When the intensity value is big,
3D objects might turn completely white because all the color channels could go over the limit of 1.0.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setIntensity(MapSceneLightsCategory category, double intensity, MapSceneLightsAttributeSettingCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
