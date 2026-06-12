---
title: "drawOrder property"
slug: "sdk-for-flutter-navigate-mapview-mappolygon-draworder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- drawOrder.html -->


<div>
<h1>drawOrder property</h1></div>
<section id="getter">

int
drawOrder


<p>The draw order of this map polygon relative to other map polygons.
Gets the draw order of this map polygon relative to other map polygons. Default value is 0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get drawOrder;</code></pre>

</section>
<section id="setter">

void
drawOrder=(int value)


<p>The draw order of this map polygon relative to other map polygons.
Sets the draw order of this map polygon relative to other map polygons.</p>
<p>Polygon with higher draw order value are drawn
on top of polygons with lower draw order.</p>
<p>In case multiple polygons have the same draw order value
then the order in which they were added to the scene matters. Last added polygon is drawn on top.</p>
<p>Allowed range is 0-1023. Values outside this range will be clamped.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set drawOrder(int value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
