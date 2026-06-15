---
title: "RouteDeviationListener constructor"
slug: "sdk-for-flutter-navigate-navigation-routedeviationlistener-routedeviationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteDeviationListener.html -->


<div>
<h1>RouteDeviationListener constructor</h1></div>

RouteDeviationListener(<ol class="parameter-list single-line"> <li>void onRouteDeviationLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-routedeviation-class">RouteDeviation</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to
receive notifications
about route deviations from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RouteDeviationListener(
  void Function(RouteDeviation) onRouteDeviationLambda,

) =&gt; RouteDeviationListener$Lambdas(
  onRouteDeviationLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
