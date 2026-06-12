---
title: "accessPoints property"
slug: "sdk-for-flutter-navigate-search-place-accesspoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- accessPoints.html -->


<div>
<h1>accessPoints property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>&gt;
accessPoints


<p>The access points to the place, such as the points on a road or in a parking lot.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.
A place can have multiple access points. For example, a large warehouse can have
multiple entrances, while the center of the warehouse may not be directly reachable.
Note that access points are meant to be reachable by vehicles.
For routes it is recommended to navigate to one of the available access points (if any),
whereas the <code>sideOfStreetHint</code> should be set to the geographic coordinates of the place.
The list is empty when no access points are known or when the place is directly reachable.
Gets the access points to the place, such as the points on a road or in a parking lot.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;GeoCoordinates&gt; get accessPoints;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
