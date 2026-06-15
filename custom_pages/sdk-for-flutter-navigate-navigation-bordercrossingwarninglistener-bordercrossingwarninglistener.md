---
title: "BorderCrossingWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-bordercrossingwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- BorderCrossingWarningListener.html -->


<div>
<h1>BorderCrossingWarningListener constructor</h1></div>

BorderCrossingWarningListener(<ol class="parameter-list single-line"> <li>void onBorderCrossingWarningUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive border crossing warnings for country and state borders.</p>
<p><strong>Note:</strong> The border crossing warner is a point warner, which means that for a border crossing there will <em>always</em> be
2 warnings emitted, with the <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetype">BorderCrossingWarning.distanceType</a> set to <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> and <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a>
which is given when the location of the border crossing is reached.
A <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a> will not be given until the previous warning of that type has been passed.
For example, a route with <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a> 160 meters ahead,
the first <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters">BorderCrossingWarning.distanceToBorderCrossingInMeters</a> is 120 meters
and the next <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters">BorderCrossingWarning.distanceToBorderCrossingInMeters</a> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory BorderCrossingWarningListener(
  void Function(BorderCrossingWarning) onBorderCrossingWarningUpdatedLambda,

) =&gt; BorderCrossingWarningListener$Lambdas(
  onBorderCrossingWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
