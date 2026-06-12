---
title: "RoadSignWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarninglistener-roadsignwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSignWarningListener.html -->


<div>
<h1>RoadSignWarningListener constructor</h1></div>

RoadSignWarningListener(<ol class="parameter-list single-line"> <li>void onRoadSignWarningUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive road sign warnings.</p>
<p><strong>Note:</strong> The road sign warner is a point warner, which means that for a road sign there will <em>always</em> be
2 warnings emitted, with the <a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-distancetype">RoadSignWarning.distanceType</a> set to <a href="/sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> and <a href="/sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a>
which is given when the location of the road sign is reached.
A <a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> will not be given until the previous warning of that type has been passed.
For example, a route with <a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 120 meters and <a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 160 meters ahead,
the first <a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is 120 meters
and the next <a href="/sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RoadSignWarningListener(
  void Function(RoadSignWarning) onRoadSignWarningUpdatedLambda,

) =&gt; RoadSignWarningListener$Lambdas(
  onRoadSignWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
