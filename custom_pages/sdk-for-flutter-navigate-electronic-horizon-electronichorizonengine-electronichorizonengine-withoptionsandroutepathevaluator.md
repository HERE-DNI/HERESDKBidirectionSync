---
title: "ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-electronichorizonengine-withoptionsandroutepathevaluator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator.html -->


<div>
<h1>ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator constructor</h1></div>

ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> sdkEngine, </li>
<li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class">ElectronicHorizonOptions</a> options, </li>
<li><a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode</a> transportMode, </li>
<li><a href="/sdk-for-flutter-navigate-routing-route-class">Route</a>? route, </li>
</ol>)
    

<p>Creates a new instance of <a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class">ElectronicHorizonEngine</a>.</p>
<ul>
<li>
<p><code>sdkEngine</code> The <a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> instance that provides shared services, such as networking and map data.</p>
</li>
<li>
<p><code>options</code> The <a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class">ElectronicHorizonOptions</a> instance that configures how the electronic horizon is calculated, including look-ahead distances.</p>
</li>
<li>
<p><code>transportMode</code> The <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode</a> that is used when building the electronic horizon paths.</p>
</li>
<li>
<p><code>route</code> The <a href="/sdk-for-flutter-navigate-routing-route-class">Route</a> that improves the calculation of the most-preferred path (MPP).
If <code>null</code> is passed, the most-preferred path can deviate from the route.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="/sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> If the electronic horizon engine cannot be created.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator(SDKNativeEngine sdkEngine, ElectronicHorizonOptions options, TransportMode transportMode, Route? route) =&gt; $prototype.WithOptionsAndRoutePathEvaluator(sdkEngine, options, transportMode, route);</code></pre>

 



</div>
`
}</HTMLBlock>
