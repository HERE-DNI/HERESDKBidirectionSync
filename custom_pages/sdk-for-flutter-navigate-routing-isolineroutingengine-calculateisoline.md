---
title: "calculateIsoline abstract method"
slug: "sdk-for-flutter-navigate-routing-isolineroutingengine-calculateisoline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateIsoline.html -->


<div>
<h1>calculateIsoline abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
calculateIsoline(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a> center, </li>
<li><a href="sdk-for-flutter-navigate-routing-isolineoptions-class">IsolineOptions</a> isolineOptions, </li>
<li><a href="sdk-for-flutter-navigate-routing-calculateisolinecallback">CalculateIsolineCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously calculates isolines to indicate the reachable area from a center point.</p>
<p>This finds all destinations that can be reached in a specific amount of time,
a maximum travel distance, or even the charge level available in an electric vehicle.
The result is a polygon area where each point is reachable within the provided limit.</p>
<ul>
<li>
<p><code>center</code> Center point from which isolines are calculated.
At minimum, the waypoint must contain the coordinates as point of origin.</p>
</li>
<li>
<p><code>isolineOptions</code> Options for isoline calculation.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after isoline calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateIsoline(Waypoint center, IsolineOptions isolineOptions, CalculateIsolineCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
