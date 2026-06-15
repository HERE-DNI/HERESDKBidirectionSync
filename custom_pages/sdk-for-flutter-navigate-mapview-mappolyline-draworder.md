---
title: "drawOrder property"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-draworder"
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


<p>The draw order of the polyline.
Gets the draw order of the polyline.</p>
<p>The default draw order is 0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get drawOrder;</code></pre>

</section>
<section id="setter">

void
drawOrder=(int value)


<p>The draw order of the polyline.
Sets the draw order of the polyline.</p>
<p>Polylines with a higher draw order are drawn on top
of polylines with a lower draw order.</p>
<p>In case multiple polylines have the same draw
order, they can be rendered in different ways depending on the <a href="sdk-for-flutter-navigate-mapview-mappolyline-drawordertype">MapPolyline.drawOrderType</a> set.</p>
<p>Supplied value is clamped to the range [0; 1023].</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set drawOrder(int value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
