---
title: "RouteProgressListener constructor"
slug: "sdk-for-flutter-navigate-navigation-routeprogresslistener-routeprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteProgressListener.html -->


<div>
<h1>RouteProgressListener constructor</h1></div>

RouteProgressListener(<ol class="parameter-list single-line"> <li>void onRouteProgressUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive notifications
about the route progress from <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RouteProgressListener(
  void Function(RouteProgress) onRouteProgressUpdatedLambda,

) =&gt; RouteProgressListener$Lambdas(
  onRouteProgressUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
