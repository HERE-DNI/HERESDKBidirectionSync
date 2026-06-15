---
title: "setColor abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-setcolor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setColor.html -->


<div>
<h1>setColor abstract method</h1></div>

void
setColor(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapscenelightscategory">MapSceneLightsCategory</a> category, </li>
<li>Color color, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>? callback</li>
</ol>)

      

    

<p>Set a new color for the light based on its category.</p>
<ul>
<li>
<p><code>category</code> The category of light for which the color is set.</p>
</li>
<li>
<p><code>color</code> The Color type includes red, green, blue, and alpha components.
The value of these components must be inside the range [0, 1].</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setColor(MapSceneLightsCategory category, ui.Color color, MapSceneLightsAttributeSettingCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
