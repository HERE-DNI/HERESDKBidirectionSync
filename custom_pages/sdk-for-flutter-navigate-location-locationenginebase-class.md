---
title: "LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngineBase-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationEngineBase-class-sidebar.html">

<div>

# <span class="kind-class">LocationEngineBase</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Public abstract class that describes the behaviour of `LocationEngine`.

Implementation is platform-specific.

</div>

<div class="section">

Implementers  
- <a href="sdk-for-flutter-navigate-location-locationengine-class">LocationEngine</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-locationenginebase">LocationEngineBase</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-startWithLocationAccuracyLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">startWithLocationAccuracyLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-startWithLocationOptionsLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">startWithLocationOptionsLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-updateLocationAccuracyLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">updateLocationAccuracyLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-updateLocationOptionsLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">updateLocationOptionsLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-stopLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">stopLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-confirmHEREPrivacyNoticeInclusionLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> <span class="parameter-name">confirmHEREPrivacyNoticeInclusionLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-confirmHEREPrivacyNoticeExceptionLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> <span class="parameter-name">confirmHEREPrivacyNoticeExceptionLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-addLocationListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">addLocationListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-removeLocationListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">removeLocationListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-addLocationStatusListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">addLocationStatusListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-removeLocationStatusListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">removeLocationStatusListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-addLocationIssueListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">addLocationIssueListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-removeLocationIssueListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">removeLocationIssueListenerLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-setBackgroundLocationAllowedLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">setBackgroundLocationAllowedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>), </span><span id="sdk-for-flutter-navigate-param-getBackgroundLocationAllowedLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">getBackgroundLocationAllowedLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-setBackgroundLocationIndicatorVisibleLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">setBackgroundLocationIndicatorVisibleLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>), </span><span id="sdk-for-flutter-navigate-param-getBackgroundLocationIndicatorVisibleLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">getBackgroundLocationIndicatorVisibleLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-setPauseLocationUpdatesAutomaticallyLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">setPauseLocationUpdatesAutomaticallyLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>), </span><span id="sdk-for-flutter-navigate-param-getPauseLocationUpdatesAutomaticallyLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">getPauseLocationUpdatesAutomaticallyLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-setLastKnownLocationPersistentLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">setLastKnownLocationPersistentLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>), </span><span id="sdk-for-flutter-navigate-param-internalsetCallListenerFromMainThreadEnabledLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">internalsetCallListenerFromMainThreadEnabledLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>), </span><span id="sdk-for-flutter-navigate-param-lastKnownLocationGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a>?</span> <span class="parameter-name">lastKnownLocationGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-isStartedGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isStartedGetLambda</span>()</span>)</span>  
Public abstract class that describes the behaviour of `LocationEngine`.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-isstarted">isStarted</a></span> <span class="signature">→ bool</span>  
Checks if the engine is in started state. Checks if the engine is in started state.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-lastknownlocation">lastKnownLocation</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-location-class">Location</a>?</span>  
The last known location obtained by the `LocationEngine`. It is persisted throughout the app's lifecycle. This property can be obtained without starting the `LocationEngine`. However, the initial value might be `null` if no location has ever been obtained by the `LocationEngine`. The time attribute of the `Location` object indicates when the last location was obtained. Note: In order to receive continuous location updates, add a `LocationListener`. Gets the last known location obtained by the `LocationEngine`. It is persisted throughout the app's lifecycle.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-addlocationissuelistener">addLocationIssueListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLocationIssueListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a <a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> to the engine to get notified when a location issue has occurred.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-addlocationlistener">addLocationListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLocationListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a `LocationListener` to the engine to get notified when there is a new location update available.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-addlocationstatuslistener">addLocationStatusListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLocationStatusListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a `LocationStatusListener` to the engine to get notified when there is an important status change.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception">confirmHEREPrivacyNoticeException</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> </span>  
By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to **not** include a reference to the HERE Privacy Notice.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion">confirmHEREPrivacyNoticeInclusion</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> </span>  
It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-getbackgroundlocationallowed">getBackgroundLocationAllowed</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Check if application's background location updates are enabled.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-getbackgroundlocationindicatorvisible">getBackgroundLocationIndicatorVisible</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Check if application's background location indicator is visible.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-getpauselocationupdatesautomatically">getPauseLocationUpdatesAutomatically</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Check if automatic pausing of location updates are enabled.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-removelocationissuelistener">removeLocationIssueListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLocationIssueListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-location-locationissuelistener-class">LocationIssueListener</a> from the engine.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-removelocationlistener">removeLocationListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLocationListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a `LocationListener` from the engine.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-removelocationstatuslistener">removeLocationStatusListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLocationStatusListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-class">LocationStatusListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a `LocationStatusListener` from the engine.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationallowed">setBackgroundLocationAllowed</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setBackgroundLocationAllowed-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Enables or disables background location updates for an application.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationindicatorvisible">setBackgroundLocationIndicatorVisible</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setBackgroundLocationIndicatorVisible-param-visible" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">visible</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Controls visibility of application's background location indicator.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-setlastknownlocationpersistent">setLastKnownLocationPersistent</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setLastKnownLocationPersistent-param-persistent" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">persistent</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Enables or disables saving of last known location so that it persists between application sessions.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-setpauselocationupdatesautomatically">setPauseLocationUpdatesAutomatically</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setPauseLocationUpdatesAutomatically-param-allowed" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">allowed</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Controls automatic pausing of location updates e.g.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-startwithlocationaccuracy">startWithLocationAccuracy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startWithLocationAccuracy-param-locationAccuracy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span> <span class="parameter-name">locationAccuracy</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions">startWithLocationOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startWithLocationOptions-param-locationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span> <span class="parameter-name">locationOptions</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Starts the location engine with desired <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-stop">stop</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops the location engine.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-updatelocationaccuracy">updateLocationAccuracy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateLocationAccuracy-param-locationAccuracy" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a></span> <span class="parameter-name">locationAccuracy</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Reconfigures the location engine with desired <a href="sdk-for-flutter-navigate-location-locationaccuracy">LocationAccuracy</a>.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-updatelocationoptions">updateLocationOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-updateLocationOptions-param-locationOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a></span> <span class="parameter-name">locationOptions</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> </span>  
Reconfigures the location engine with desired <a href="sdk-for-flutter-navigate-location-locationoptions-class">LocationOptions</a>.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-makelocationengine">makeLocationEngine</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-makeLocationEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginebase-class">LocationEngineBase</a></span> </span>  
Creates instance of `LocationEngine` using factory, registered on platform side

<span class="name"><a href="sdk-for-flutter-navigate-location-locationenginebase-makelocationenginefromsharedsdknativeengine">makeLocationEngineFromSharedSdkNativeEngine</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-location-locationenginebase-class">LocationEngineBase</a></span> </span>  
Creates instance of `LocationEngine` using factory, registered on platform side

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
