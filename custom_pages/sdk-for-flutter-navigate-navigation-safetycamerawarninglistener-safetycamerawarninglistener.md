---
title: "SafetyCameraWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-safetycamerawarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SafetyCameraWarningListener.html -->


<div>
<h1>SafetyCameraWarningListener constructor</h1></div>

SafetyCameraWarningListener(<ol class="parameter-list single-line"> <li>void onSafetyCameraWarningUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-class">SafetyCameraWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive notifications on safety cameras.</p>
<p>A <code>SafetyCameraWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>SafetyCameraWarning</code> 120 meters and <code>SafetyCameraWarning</code> 160 meters ahead,
the first <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters
and the next <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<p>When <code>SafetyCameraWarningListener</code> is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled.
The updates for the same safety camera appear in order of the initial <code>DistanceType.AHEAD</code> event.
That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SafetyCameraWarningListener(
  void Function(SafetyCameraWarning) onSafetyCameraWarningUpdatedLambda,

) =&gt; SafetyCameraWarningListener$Lambdas(
  onSafetyCameraWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
