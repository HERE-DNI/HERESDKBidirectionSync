---
title: "LocationEngine class"
slug: "sdk-for-flutter-navigate-location-locationengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngine-class.html -->


<div>
<h1>LocationEngine class</h1></div>

<p>Handles location updates received according to the desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.</p>
<p>Each instance of this class will be using internally the same client providing the actual
location updates. For that reason, only one <a href="sdk-for-flutter-navigate-location-locationengine-class">LocationEngine</a> can be started at a time.
Multiple listeners can be attached, either to receive location updates, see <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>,
status updates, see <a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> or location issue has occurred, see LocationIssueListener].
When a different <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a> is
desired, the <a href="sdk-for-flutter-navigate-location-locationengine-class">LocationEngine</a> needs to be stopped and started again.
Note: starting the <a href="sdk-for-flutter-navigate-location-locationengine-class">LocationEngine</a> with <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a> is only supported in Android platforms.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-location-locationengine-locationengine">LocationEngine</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-locationengine-withsdkengine">LocationEngine.withSdkEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-location-locationenginebase-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-isstarted">isStarted</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-lastknownlocation">lastKnownLocation</a></li><li><a href="sdk-for-flutter-navigate-location-locationenginebase-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-location-locationengine-addlocationissuelistener">addLocationIssueListener</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-addlocationlistener">addLocationListener</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-addlocationstatuslistener">addLocationStatusListener</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">confirmHEREPrivacyNoticeException</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">confirmHEREPrivacyNoticeInclusion</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationallowed">getBackgroundLocationAllowed</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationindicatorvisible">getBackgroundLocationIndicatorVisible</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-getpauselocationupdatesautomatically">getPauseLocationUpdatesAutomatically</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-internalsetcalllistenerfrommainthreadenabled">internalsetCallListenerFromMainThreadEnabled</a></li><li><a href="sdk-for-flutter-navigate-location-locationenginebase-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-removelocationissuelistener">removeLocationIssueListener</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-removelocationlistener">removeLocationListener</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-removelocationstatuslistener">removeLocationStatusListener</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationallowed">setBackgroundLocationAllowed</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationindicatorvisible">setBackgroundLocationIndicatorVisible</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-setlastknownlocationpersistent">setLastKnownLocationPersistent</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-setpauselocationupdatesautomatically">setPauseLocationUpdatesAutomatically</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">startWithLocationAccuracy</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">startWithLocationOptions</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-stop">stop</a></li><li><a href="sdk-for-flutter-navigate-location-locationenginebase-tostring">toString</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-updatelocationaccuracy">updateLocationAccuracy</a></li><li><a href="sdk-for-flutter-navigate-location-locationengine-updatelocationoptions">updateLocationOptions</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-location-locationenginebase-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
