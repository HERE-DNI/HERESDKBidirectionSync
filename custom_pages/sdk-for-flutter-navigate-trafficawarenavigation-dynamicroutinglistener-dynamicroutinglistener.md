---
title: "DynamicRoutingListener constructor"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-dynamicroutinglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DynamicRoutingListener.html -->


<div>
<h1>DynamicRoutingListener constructor</h1></div>

DynamicRoutingListener(<ol class="parameter-list single-line"> <li>void onBetterRouteFoundLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>, </li>
<li>int, </li>
<li>int</li>
</ol>), </li>
<li>void onRoutingErrorLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to
receive notifications about the new route via the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DynamicRoutingListener(
  void Function(Route, int, int) onBetterRouteFoundLambda,
  void Function(RoutingError) onRoutingErrorLambda,

) =&gt; DynamicRoutingListener$Lambdas(
  onBetterRouteFoundLambda,
  onRoutingErrorLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
