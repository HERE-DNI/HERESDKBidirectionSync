---
title: "getTopology abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venuemap-gettopology"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getTopology.html -->


<div>
<h1>getTopology abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-venue-data-venuetopology-class">VenueTopology</a>?
getTopology(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> position</li>
</ol>)

      

    

<p>Tries to find a <a href="/sdk-for-flutter-navigate-venue-data-venuetopology-class">VenueTopology</a> at the specified geographic coordinates
in the selected <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> in the currently selected <a href="/sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.</p>
<ul>
<li><code>position</code> Geographic coordinates where the topology is located.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-venue-data-venuetopology-class">VenueTopology?</a>. Topology or <code>null</code> if there is no topology at the specified geographic coordinates.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">VenueTopology? getTopology(GeoCoordinates position);</code></pre>

 



</div>
`
}</HTMLBlock>
