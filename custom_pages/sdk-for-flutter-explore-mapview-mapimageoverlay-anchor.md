---
title: "anchor property"
slug: "sdk-for-flutter-explore-mapview-mapimageoverlay-anchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- anchor.html -->


<div>
<h1>anchor property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a>
anchor


<p>The anchor point for the overlay image which specifies the position offset relative
to the overlay's view coordinates.
Gets current anchor point for the overlay image.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Anchor2D get anchor;</code></pre>

</section>
<section id="setter">

void
anchor=(<a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> value)


<p>The anchor point for the overlay image which specifies the position offset relative
to the overlay's view coordinates.
Sets anchor point of the overlay image which specifies the position offset relative
to the overlay's view coordinates.</p>
<p>For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates.
(1, 1) would place the bottom-right corner of the image at the overlay's view coordinates.
(0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.</p>
<p>Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the overlay's view coordinates at the distance
in pixels that is equal to the height of the image.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set anchor(Anchor2D value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
