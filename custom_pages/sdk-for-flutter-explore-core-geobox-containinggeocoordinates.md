---
title: "containingGeoCoordinates static method"
slug: "sdk-for-flutter-explore-core-geobox-containinggeocoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- containingGeoCoordinates.html -->


<div>
<h1>containingGeoCoordinates static method</h1></div>

<a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>?
containingGeoCoordinates(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>&gt; geoCoordinates</li>
</ol>)

      

    

<p>Creates a <code>GeoBox</code> which encompases all coordinates from the list.</p>
<p>The provided list must contain at least two points.
The altitude values of the input coordinates are not considered for the result.</p>
<ul>
<li><code>geoCoordinates</code> List of coordinates to encompass inside bounding box.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox?</a>. <code>GeoBox</code> containing all supplied coordinates, or <code>null</code> if less than two coordinates were provided.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static GeoBox? containingGeoCoordinates(List&lt;GeoCoordinates&gt; geoCoordinates) =&gt; $prototype.containingGeoCoordinates(geoCoordinates);</code></pre>

 



</div>
`
}</HTMLBlock>
