---
title: "LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationEngine-class-sidebar.html">

<div>

# <span class="kind-class">LocationEngine</span> class

</div>

<div class="section desc markdown">

Handles location updates received according to the desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.

Each instance of this class will be using internally the same client providing the actual location updates. For that reason, only one <a href="sdk-for-flutter-navigate-location-locationengine-class">LocationEngine</a> can be started at a time. Multiple listeners can be attached, either to receive location updates, see <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>, status updates, see <a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> or location issue has occurred, see LocationIssueListener\]. When a different <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a> is desired, the <a href="sdk-for-flutter-navigate-location-locationengine-class">LocationEngine</a> needs to be stopped and started again. Note: starting the <a href="sdk-for-flutter-navigate-location-locationengine-class">LocationEngine</a> with <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a> is only supported in Android platforms.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-location-locationenginebase-class">LocationEngineBase</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-locationengine">LocationEngine</a></span><span class="signature">()</span>  

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-locationengine-withsdkengine">LocationEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-isstarted">isStarted</a></span> <span class="signature">→ bool</span>  
Checks if the engine is in started state. Checks if the engine is in started state.

<div class="features">

<span class="feature">no setter</span><span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-lastknownlocation">lastKnownLocation</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-location-class">Location</a>?</span>  
The last known location obtained by the engine. <a href="sdk-for-flutter-navigate-core-location-class">Location</a> is returned synchronously. <a href="sdk-for-flutter-navigate-core-location-class">Location</a> object has a timestamp attribute, which reflects when data was obtained. If location was never obtained - null is returned.

<div class="features">

<span class="feature">no setter</span><span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-addlocationissuelistener">addLocationIssueListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLocationIssueListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a <a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> to the engine to get notified when a location issue has occurred Supports more than one listener, instance is added only once.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-addlocationlistener">addLocationListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLocationListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> to the engine to get notified when there is a new location update available. Supports more than one listener, instance is added only once.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-addlocationstatuslistener">addLocationStatusListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLocationStatusListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a <a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> to the engine to get notified when there is a an important status change. Supports more than one listener, instance is added only once.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">confirmHEREPrivacyNoticeException</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> </span>  
On Android devices by calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to **not** include a reference to the HERE Privacy Notice. As a result, the `LocationEngine` will not collect characteristic information about the nearby mobile and Wi-Fi network signals. However, the engine will still be fully functional and will deliver location updates when the exception can be confirmed.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">confirmHEREPrivacyNoticeInclusion</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> </span>  
On Android devices it is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related <a href="https://legal.here.com/here-network-positioning-via-sdk">HERE Privacy Notice</a> must be made available to the user.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationallowed">getBackgroundLocationAllowed</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
On iOS devices this checks if application's background location updates are enabled. Returns true if background location updates are allowed, false otherwise.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationindicatorvisible">getBackgroundLocationIndicatorVisible</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
On iOS devices this checks if application's background location indicator is visible. Returns true if background location indicator is visible, false otherwise.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-getpauselocationupdatesautomatically">getPauseLocationUpdatesAutomatically</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
On iOS devices this checks if automatic pausing of location updates is enabled. Returns true if automatic pausing of location updates is enabled, false otherwise.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-internalsetcalllistenerfrommainthreadenabled">internalsetCallListenerFromMainThreadEnabled</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-internalsetCallListenerFromMainThreadEnabled-param-enabled" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enabled</span></span>) <span class="returntype parameter">→ void</span> </span>  
Enables or disables forcing listener calls to originate from main thread.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-removelocationissuelistener">removeLocationIssueListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLocationIssueListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> from the engine.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-removelocationlistener">removeLocationListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLocationListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a> from the engine.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-removelocationstatuslistener">removeLocationStatusListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLocationStatusListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a> from the engine.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationallowed">setBackgroundLocationAllowed</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setBackgroundLocationAllowed-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
On iOS devices this enables or disables application's background location updates. By default background location updates are enabled if application has background location capabilities. Set `allowed` to true to allow background location updates, or false to disable them. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds. <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application does not have background location capabilities enabled.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationindicatorvisible">setBackgroundLocationIndicatorVisible</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setBackgroundLocationIndicatorVisible-param-visible" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">visible</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
On iOS devices this controls visibility of application's background location indicator. By default background location indicator is visible, if application has background location capabilities. Set `visible` to true to show background location indicator, or false to hide it. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> if call succeeds and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.notAllowed</a> if the application does not have background location capabilities enabled.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-setlastknownlocationpersistent">setLastKnownLocationPersistent</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setLastKnownLocationPersistent-param-persistent" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">persistent</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
On Android devices this enables or disables saving of last known location so that it persists across application sessions. By default persistent saving across sessions is enabled. Set `persistent` to true to enable last known location to persist across application sessions, or false to disable it. When calling this method then <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> is returned.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-setpauselocationupdatesautomatically">setPauseLocationUpdatesAutomatically</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setPauseLocationUpdatesAutomatically-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
On iOS devices this controls automatic pausing of location updates e.g. for improving device's battery life at times when location data is unlikely to change. By default automatic pausing of location updates is allowed. Set `allowed` to true to allow automatic pausing of location updates, or false to disable them. When calling this method then <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.ok</a> is returned.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">startWithLocationAccuracy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startWithLocationAccuracy-param-locationAccuracy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span> <span class="parameter-name">locationAccuracy</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>. Make sure to call either <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">LocationEngine.confirmHEREPrivacyNoticeInclusion</a> or <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">LocationEngine.confirmHEREPrivacyNoticeException</a> beforehand. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a> if <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">LocationEngine.startWithLocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">LocationEngine.startWithLocationOptions</a> is called again without calling <a href="sdk-for-flutter-navigate-location-locationengine-stop">LocationEngine.stop</a> in between. See <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> for other possible return values.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">startWithLocationOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startWithLocationOptions-param-locationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span> <span class="parameter-name">locationOptions</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
On Android devices starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>. Make sure to call either <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion">LocationEngine.confirmHEREPrivacyNoticeInclusion</a> or <a href="sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception">LocationEngine.confirmHEREPrivacyNoticeException</a> beforehand. Returns <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.alreadyStarted</a> if <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy">LocationEngine.startWithLocationAccuracy</a> or <a href="sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions">LocationEngine.startWithLocationOptions</a> is called again without calling <a href="sdk-for-flutter-navigate-location-locationengine-stop">LocationEngine.stop</a> in between. See <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a> for other possible return values.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-stop">stop</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops the location engine.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-updatelocationaccuracy">updateLocationAccuracy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateLocationAccuracy-param-locationAccuracy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span> <span class="parameter-name">locationAccuracy</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Reconfigures the location engine with desired LocationAccuracy.

<div class="features">

<span class="feature">override</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationengine-updatelocationoptions">updateLocationOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateLocationOptions-param-locationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span> <span class="parameter-name">locationOptions</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Reconfigures the location engine with desired LocationOptions.

<div class="features">

<span class="feature">override</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
