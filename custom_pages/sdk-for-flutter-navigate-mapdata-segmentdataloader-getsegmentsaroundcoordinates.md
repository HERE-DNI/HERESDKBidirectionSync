---
title: "getSegmentsAroundCoordinates abstract method"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-getsegmentsaroundcoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getSegmentsAroundCoordinates.html -->


<div>
<h1>getSegmentsAroundCoordinates abstract method</h1></div>

List&lt;<a href="/sdk-for-flutter-navigate-mapdata-ocmsegmentid-class">OCMSegmentId</a>&gt;
getSegmentsAroundCoordinates(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li>double radiusInMeters</li>
</ol>)

      

    

<p>Loads the segments around a certain coordinates.</p>
<p>Returns an empty list in case no segments could be found around the coordinates.</p>
<ul>
<li>
<p><code>coordinates</code> The location to explore</p>
</li>
<li>
<p><code>radiusInMeters</code> The radius of the search. Only values between 1m and 5000m are accepted.</p>
</li>
</ul>
<p>Returns <code>List&lt;OCMSegmentId&gt;</code>. The list of segments around the given position.</p>
<p>The segments are sorted by distance
from the point.
Throws if it's not possible to return list of a list of segments.</p>
<p>Throws <a href="/sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why list of a list of segments is not returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;OCMSegmentId&gt; getSegmentsAroundCoordinates(GeoCoordinates coordinates, double radiusInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
