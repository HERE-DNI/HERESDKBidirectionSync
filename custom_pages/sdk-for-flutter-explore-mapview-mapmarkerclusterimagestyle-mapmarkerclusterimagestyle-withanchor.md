---
title: "MapMarkerClusterImageStyle.withAnchor constructor"
slug: "sdk-for-flutter-explore-mapview-mapmarkerclusterimagestyle-mapmarkerclusterimagestyle-withanchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerClusterImageStyle.withAnchor.html -->


<div>
<h1>MapMarkerClusterImageStyle.withAnchor constructor</h1></div>

MapMarkerClusterImageStyle.withAnchor(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> image, </li>
<li><a href="/sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> anchor</li>
</ol>)
    

<p>Creates a cluster marker image style using a map image with anchor.</p>
<p>The anchor is a way of specifying position offset relative to image's dimensions on the
screen. For example, (0, 0) places the top-left corner of the image at the cluster's
position. (1, 1) would place the bottom-right corner of the image at the cluster's
position.</p>
<ul>
<li>
<p><code>image</code> The map image for the cluster marker.</p>
</li>
<li>
<p><code>anchor</code> The anchor point for the marker image which specifies the position offset relative
to the cluster's position.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarkerClusterImageStyle.withAnchor(MapImage image, Anchor2D anchor) =&gt; $prototype.withAnchor(image, anchor);</code></pre>

 



</div>
`
}</HTMLBlock>
