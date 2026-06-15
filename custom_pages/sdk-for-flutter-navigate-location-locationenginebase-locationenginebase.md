---
title: "LocationEngineBase constructor"
slug: "sdk-for-flutter-navigate-location-locationenginebase-locationenginebase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngineBase.html -->


<div>
<h1>LocationEngineBase constructor</h1></div>

LocationEngineBase(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> startWithLocationAccuracyLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> startWithLocationOptionsLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> updateLocationAccuracyLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> updateLocationOptionsLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></li>
</ol>), </li>
<li>void stopLambda(), </li>
<li><a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a> confirmHEREPrivacyNoticeInclusionLambda(), </li>
<li><a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a> confirmHEREPrivacyNoticeExceptionLambda(), </li>
<li>void addLocationListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></li>
</ol>), </li>
<li>void removeLocationListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></li>
</ol>), </li>
<li>void addLocationStatusListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></li>
</ol>), </li>
<li>void removeLocationStatusListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></li>
</ol>), </li>
<li>void addLocationIssueListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></li>
</ol>), </li>
<li>void removeLocationIssueListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> setBackgroundLocationAllowedLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool getBackgroundLocationAllowedLambda(), </li>
<li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> setBackgroundLocationIndicatorVisibleLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool getBackgroundLocationIndicatorVisibleLambda(), </li>
<li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> setPauseLocationUpdatesAutomaticallyLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool getPauseLocationUpdatesAutomaticallyLambda(), </li>
<li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> setLastKnownLocationPersistentLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>void internalsetCallListenerFromMainThreadEnabledLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-core-location-class">Location</a>? lastKnownLocationGetLambda(), </li>
<li>bool isStartedGetLambda(), </li>
</ol>)
    

<p>Public abstract class that describes the behaviour of <code>LocationEngine</code>.</p>
<p>Implementation is platform-specific.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LocationEngineBase(
  LocationEngineStatus Function(LocationAccuracy) startWithLocationAccuracyLambda,
  LocationEngineStatus Function(LocationOptions) startWithLocationOptionsLambda,
  LocationEngineStatus Function(LocationAccuracy) updateLocationAccuracyLambda,
  LocationEngineStatus Function(LocationOptions) updateLocationOptionsLambda,
  void Function() stopLambda,
  ConfirmationStatus Function() confirmHEREPrivacyNoticeInclusionLambda,
  ConfirmationStatus Function() confirmHEREPrivacyNoticeExceptionLambda,
  void Function(LocationListener) addLocationListenerLambda,
  void Function(LocationListener) removeLocationListenerLambda,
  void Function(LocationStatusListener) addLocationStatusListenerLambda,
  void Function(LocationStatusListener) removeLocationStatusListenerLambda,
  void Function(LocationIssueListener) addLocationIssueListenerLambda,
  void Function(LocationIssueListener) removeLocationIssueListenerLambda,
  LocationEngineStatus Function(bool) setBackgroundLocationAllowedLambda,
  bool Function() getBackgroundLocationAllowedLambda,
  LocationEngineStatus Function(bool) setBackgroundLocationIndicatorVisibleLambda,
  bool Function() getBackgroundLocationIndicatorVisibleLambda,
  LocationEngineStatus Function(bool) setPauseLocationUpdatesAutomaticallyLambda,
  bool Function() getPauseLocationUpdatesAutomaticallyLambda,
  LocationEngineStatus Function(bool) setLastKnownLocationPersistentLambda,
  void Function(bool) internalsetCallListenerFromMainThreadEnabledLambda,
  Location? Function() lastKnownLocationGetLambda,
  bool Function() isStartedGetLambda
) =&gt; LocationEngineBase$Lambdas(
  startWithLocationAccuracyLambda,
  startWithLocationOptionsLambda,
  updateLocationAccuracyLambda,
  updateLocationOptionsLambda,
  stopLambda,
  confirmHEREPrivacyNoticeInclusionLambda,
  confirmHEREPrivacyNoticeExceptionLambda,
  addLocationListenerLambda,
  removeLocationListenerLambda,
  addLocationStatusListenerLambda,
  removeLocationStatusListenerLambda,
  addLocationIssueListenerLambda,
  removeLocationIssueListenerLambda,
  setBackgroundLocationAllowedLambda,
  getBackgroundLocationAllowedLambda,
  setBackgroundLocationIndicatorVisibleLambda,
  getBackgroundLocationIndicatorVisibleLambda,
  setPauseLocationUpdatesAutomaticallyLambda,
  getPauseLocationUpdatesAutomaticallyLambda,
  setLastKnownLocationPersistentLambda,
  internalsetCallListenerFromMainThreadEnabledLambda,
  lastKnownLocationGetLambda,
  isStartedGetLambda
);</code></pre>

 



</div>
`
}</HTMLBlock>
