---
title: "zoomBy static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-zoomby"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomBy.html -->


<div>
<h1>zoomBy static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
zoomBy(<ol class="parameter-list single-line"> <li>double factor, </li>
<li><a href="/sdk-for-flutter-explore-core-point2d-class">Point2D</a> origin</li>
</ol>)

      

    

<p>Creates an update to zoom map camera by a given factor preserving a given focus point.</p>
<p>Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out,
which moves map camera further.</p>
<p>If factor is zero, negative or not finite, no update will be applied to the map camera.</p>
<p>If the focusPoint is not inside the viewport bounds, then the current principal point will be used.</p>
<ul>
<li>
<p><code>factor</code> Zooming factor.</p>
</li>
<li>
<p><code>origin</code> Pixel location on the screen to use as zoom origin.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate zoomBy(double factor, Point2D origin) =&gt; $prototype.zoomBy(factor, origin);</code></pre>

 



</div>
`
}</HTMLBlock>
