---
title: "getColor abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscenelights-getcolor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getColor.html -->


<div>
<h1>getColor abstract method</h1></div>

Color?
getColor(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a> category</li>
</ol>)

      

    

<p>Retrieves the current color of the light based on its category.</p>
<ul>
<li><code>category</code> The category of light from which the color is retrieved.</li>
</ul>
<p>Returns <code>ui.Color?</code>. The current color of the light, or <code>null</code> if the light is missing from the loaded scene
or MapScene is not intitialized.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ui.Color? getColor(MapSceneLightsCategory category);</code></pre>

 



</div>
`
}</HTMLBlock>
