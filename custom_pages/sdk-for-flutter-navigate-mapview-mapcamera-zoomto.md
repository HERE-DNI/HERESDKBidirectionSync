---
title: "zoomTo abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-zoomto"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomTo.html -->


<div>
<h1>zoomTo abstract method</h1></div>

void
zoomTo(<ol class="parameter-list single-line"> <li>double zoomLevel</li>
</ol>)

      

    

<p>Zooms to the specified zoom level.</p>
<p>The supplied value will be clamped to the range
of [0, 22], where 0 is a view of whole globe and 22 is street level.</p>
<p>This effectively changes the distance from the camera to the target.
The zooming occurs around the current target point.</p>
<ul>
<li><code>zoomLevel</code> The zoom level to set, clamped to the range of [0, 22].</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void zoomTo(double zoomLevel);</code></pre>

 



</div>
`
}</HTMLBlock>
