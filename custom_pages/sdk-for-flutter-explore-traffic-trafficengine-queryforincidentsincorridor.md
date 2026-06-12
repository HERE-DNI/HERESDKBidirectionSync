---
title: "queryForIncidentsInCorridor abstract method"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForIncidentsInCorridor.html -->


<div>
<h1>queryForIncidentsInCorridor abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
queryForIncidentsInCorridor(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a> corridorArea, </li>
<li><a href="/sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a> queryOptions, </li>
<li><a href="/sdk-for-flutter-explore-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously queries for traffic incidents by a corridor as a filter.</p>
<ul>
<li><code>corridorArea</code> The corridor box to search for traffic incidents.
The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters.
If the number of points in corridor is greater than 300 then request is split into smaller ones and results are
aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.</li>
</ul>
<p>To reduce number of points in the corridor use <a href="/sdk-for-flutter-explore-core-polylinesimplifier-class">PolylineSimplifier</a>.</p>
<p>If no <code>GeoCorridor.half_width_in_meters</code> is specified, the default value is used. The default value is 30 meters.</p>
<ul>
<li>
<p><code>queryOptions</code> The options which are specific for incidents query.</p>
</li>
<li>
<p><code>callback</code> It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle queryForIncidentsInCorridor(GeoCorridor corridorArea, TrafficIncidentsQueryOptions queryOptions, TrafficIncidentsQueryCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
