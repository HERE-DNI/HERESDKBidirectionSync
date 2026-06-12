---
title: "InterpolatedLocationListener constructor"
slug: "sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-interpolatedlocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- InterpolatedLocationListener.html -->


<div>
<h1>InterpolatedLocationListener constructor</h1></div>

InterpolatedLocationListener(<ol class="parameter-list single-line"> <li>void onInterpolatedLocationUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-location-class">Location</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented
in order to receive interpolated locations.</p>
<p>The interpolated locations are only provided between
<a href="/sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">VisualNavigator.startRendering</a> and <a href="/sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering">VisualNavigator.stopRendering</a> calls and the application
is not running in the background.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory InterpolatedLocationListener(
  void Function(Location) onInterpolatedLocationUpdatedLambda,

) =&gt; InterpolatedLocationListener$Lambdas(
  onInterpolatedLocationUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
