---
title: "isCoordinatesInterpolated property"
slug: "sdk-for-flutter-navigate-search-place-iscoordinatesinterpolated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isCoordinatesInterpolated.html -->


<div>
<h1>isCoordinatesInterpolated property</h1></div>
<section id="getter">

bool
isCoordinatesInterpolated


<p>A property that says whether the coordinates of the house number were interpolated or not.
This property is valid only for house number results retrieved using online search.
When false, it means <a href="/sdk-for-flutter-navigate-search-place-geocoordinates">Place.geoCoordinates</a> point to an accurate position of the house. Otherwise
coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm.
Gets the flag saying whether the coordinates of the house number were interpolated or not.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isCoordinatesInterpolated;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
