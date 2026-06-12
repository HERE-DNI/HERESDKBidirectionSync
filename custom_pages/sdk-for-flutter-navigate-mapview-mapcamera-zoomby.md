---
title: "zoomBy abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-zoomby"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- zoomBy.html -->


<div>
<h1>zoomBy abstract method</h1></div>

void
zoomBy(<ol class="parameter-list single-line"> <li>double factor, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a> origin</li>
</ol>)

      

    

<p>Zooms in or out by a specified factor.</p>
<p>This effectively changes the distance from the camera to the <a href="/sdk-for-flutter-navigate-mapview-mapcamerastate-targetcoordinates">MapCameraState.targetCoordinates</a>
by the specified factor, which changes <a href="/sdk-for-flutter-navigate-mapview-mapcamerastate-zoomlevel">MapCameraState.zoomLevel</a> as well.</p>
<p>Values above 1.0 will zoom in and values below will zoom out.</p>
<p>The relation with <a href="/sdk-for-flutter-navigate-mapview-mapcamerastate-distancetotargetinmeters">MapCameraState.distanceToTargetInMeters</a> is inversely linear,
meaning that zooming by 4 will decrease distance to target by 4 while zooming by 0.5
will increase distance to target by 2.</p>
<p>The relation with zoom level is logarithmic. Meaning that zooming by a factor of 4 will
increase zoom level by 2 (because log2(4) == 2). So to zoom in by X zoom levels, the zoom
factor needs to be 2^X. To zoom out by X zoom levels, zoom factor needs to be 1/(2^X).</p>
<p>The zooming occurs around the specified origin inside the view.</p>
<ul>
<li>
<p><code>factor</code> The zoom factor. Values above 1.0 will zoom in and values below will zoom out.</p>
</li>
<li>
<p><code>origin</code> Pixel point in view coordinates around which zooming occurs.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void zoomBy(double factor, Point2D origin);</code></pre>

 



</div>
`
}</HTMLBlock>
