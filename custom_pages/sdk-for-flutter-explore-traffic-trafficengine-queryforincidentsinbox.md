---
title: "queryForIncidentsInBox abstract method"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsinbox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForIncidentsInBox.html -->


<div>
<h1>queryForIncidentsInBox abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
queryForIncidentsInBox(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a> boxArea, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a> queryOptions, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously queries for traffic incidents using a bounding box as a filter.</p>
<ul>
<li>
<p><code>boxArea</code> The bounding box area to search for traffic incidents.
The maximum width and height for a bounding box filter is 1 degree.</p>
</li>
<li>
<p><code>queryOptions</code> The options which are specific for incidents query.</p>
</li>
<li>
<p><code>callback</code> It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle queryForIncidentsInBox(GeoBox boxArea, TrafficIncidentsQueryOptions queryOptions, TrafficIncidentsQueryCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
