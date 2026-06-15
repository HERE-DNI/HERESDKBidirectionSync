---
title: "drawOrderType property"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-drawordertype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- drawOrderType.html -->


<div>
<h1>drawOrderType property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType</a>
drawOrderType


<p>The draw order type of the polyline.
Gets the draw order type of the polyline.</p>
<p>The default value is <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">DrawOrderType get drawOrderType;</code></pre>

</section>
<section id="setter">

void
drawOrderType=(<a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType</a> value)


<p>The draw order type of the polyline.
Sets the draw order type of the polyline.</p>
<p>For <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a>, map polylines with outlines having
the same draw order are drawn as a whole in the order of addition to a map scene. There
is no possibility that parts of another polyline, regardless of its draw order value,
are drawn between outline and mainline of another polyline.</p>
<p>With <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderDependent</a>, polylines are rendered one by one.</p>
<p>For <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderIndependent</a>, for multiple polylines with
outlines having the same draw order, all outlines are rendered first in an arbitrary order
and then all mainlines are drawn on top of those polylines in an arbitrary order.</p>
<p><a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType.mapSceneAdditionOrderIndependent</a> allows speeding up the rendering
process and keeping high frame rates when many similar polylines (with same styling
attributes and <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>) are present in a map scene.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set drawOrderType(DrawOrderType value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
