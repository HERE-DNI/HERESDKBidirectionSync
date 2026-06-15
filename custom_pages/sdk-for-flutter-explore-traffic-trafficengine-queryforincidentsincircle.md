---
title: "queryForIncidentsInCircle abstract method"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincircle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForIncidentsInCircle.html -->


<div>
<h1>queryForIncidentsInCircle abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
queryForIncidentsInCircle(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a> circleArea, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a> queryOptions, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously queries for traffic incidents using a circle as a filter.</p>
<ul>
<li>
<p><code>circleArea</code> The circle area to search for traffic incidents.
The maximum radius of the circle filter is 50000 meters.</p>
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
<pre class="language-dart"><code class="language-dart">TaskHandle queryForIncidentsInCircle(GeoCircle circleArea, TrafficIncidentsQueryOptions queryOptions, TrafficIncidentsQueryCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
