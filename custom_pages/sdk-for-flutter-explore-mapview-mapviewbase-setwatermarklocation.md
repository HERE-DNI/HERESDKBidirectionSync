---
title: "setWatermarkLocation abstract method"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-setwatermarklocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setWatermarkLocation.html -->


<div>
<h1>setWatermarkLocation abstract method</h1></div>

void
setWatermarkLocation(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> anchor, </li>
<li><a href="/sdk-for-flutter-explore-core-point2d-class">Point2D</a> offset</li>
</ol>)

      

    

<p>Sets the position of the HERE logo watermark within the map view.</p>
<p>By default, the watermark is aligned to the bottom-right corner of the view:
Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2).
It is recommended to change the default position only if necessary to avoid overlapping UI elements.
The watermark should always be fully visible within the view.
The anchor point on the watermark is its center (width/2, height/2), around which it will be placed
in the map view.
For map views smaller than 250 dip in both width and height, the watermark will not be shown.</p>
<ul>
<li>
<p><code>anchor</code> Anchor point in normalized view coordinates [0, 1]. Map view's origin at (0, 0) indicates
a top-left corner of the map view.
Out of boundary anchor point values will be clamped to the [0, 1] range.</p>
</li>
<li>
<p><code>offset</code> A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that
allows shifting the watermark from the anchor point position in one or the other
direction.
For the quadrant of values expressing visible part of the map view negative offset shifts
the watermark to the direction of the origin, positive - away from it.
For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to
the bottom.
If specified offset will result in watermark being completely or partially out-of-view
the offset will be adjusted internally so that watermark is fully visible.
Offset is not being scaled when the map view size changes.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setWatermarkLocation(Anchor2D anchor, Point2D offset);</code></pre>

 



</div>
`
}</HTMLBlock>
