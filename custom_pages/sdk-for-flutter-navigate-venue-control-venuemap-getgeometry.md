---
title: "getGeometry abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venuemap-getgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getGeometry.html -->


<div>
<h1>getGeometry abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?
getGeometry(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> position</li>
</ol>)

      

    

<p>Tries to find a <a href="/sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a> at the specified geographic coordinates
in the selected <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> in the currently selected <a href="/sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.</p>
<ul>
<li><code>position</code> Geographic coordinates where the geometry is located.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry?</a>. Geometry or <code>null</code> if there is no geometry at the specified geographic coordinates.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">VenueGeometry? getGeometry(GeoCoordinates position);</code></pre>

 



</div>
`
}</HTMLBlock>
