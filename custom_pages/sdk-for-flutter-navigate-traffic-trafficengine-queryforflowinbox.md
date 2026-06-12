---
title: "queryForFlowInBox abstract method"
slug: "sdk-for-flutter-navigate-traffic-trafficengine-queryforflowinbox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForFlowInBox.html -->


<div>
<h1>queryForFlowInBox abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
queryForFlowInBox(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> boxArea, </li>
<li><a href="/sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a> queryOptions, </li>
<li><a href="/sdk-for-flutter-navigate-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously queries for traffic flow using a bounding box as a filter.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>boxArea</code> The bounding box area to search for traffic flow.</p>
</li>
<li>
<p><code>queryOptions</code> The options which are specific for flow query.</p>
</li>
<li>
<p><code>callback</code> It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle queryForFlowInBox(GeoBox boxArea, TrafficFlowQueryOptions queryOptions, TrafficFlowQueryCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
