---
title: "LocationEngine class"
slug: "sdk-for-flutter-navigate-location-locationengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="location/LocationEngine-class.html#constructors">Constructors</a></li>
<li><a href="location/LocationEngine/LocationEngine.html">LocationEngine</a></li>
<li><a href="location/LocationEngine/LocationEngine.withSdkEngine.html">withSdkEngine</a></li>
<li class="section-title">
<a href="location/LocationEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="location/LocationEngineBase/hashCode.html">hashCode</a></li>
<li><a href="location/LocationEngine/isStarted.html">isStarted</a></li>
<li><a href="location/LocationEngine/lastKnownLocation.html">lastKnownLocation</a></li>
<li class="inherited"><a href="location/LocationEngineBase/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="location/LocationEngine-class.html#instance-methods">Methods</a></li>
<li><a href="location/LocationEngine/addLocationIssueListener.html">addLocationIssueListener</a></li>
<li><a href="location/LocationEngine/addLocationListener.html">addLocationListener</a></li>
<li><a href="location/LocationEngine/addLocationStatusListener.html">addLocationStatusListener</a></li>
<li><a href="location/LocationEngine/confirmHEREPrivacyNoticeException.html">confirmHEREPrivacyNoticeException</a></li>
<li><a href="location/LocationEngine/confirmHEREPrivacyNoticeInclusion.html">confirmHEREPrivacyNoticeInclusion</a></li>
<li><a href="location/LocationEngine/getBackgroundLocationAllowed.html">getBackgroundLocationAllowed</a></li>
<li><a href="location/LocationEngine/getBackgroundLocationIndicatorVisible.html">getBackgroundLocationIndicatorVisible</a></li>
<li><a href="location/LocationEngine/getPauseLocationUpdatesAutomatically.html">getPauseLocationUpdatesAutomatically</a></li>
<li><a href="location/LocationEngine/internalsetCallListenerFromMainThreadEnabled.html">internalsetCallListenerFromMainThreadEnabled</a></li>
<li class="inherited"><a href="location/LocationEngineBase/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="location/LocationEngine/removeLocationIssueListener.html">removeLocationIssueListener</a></li>
<li><a href="location/LocationEngine/removeLocationListener.html">removeLocationListener</a></li>
<li><a href="location/LocationEngine/removeLocationStatusListener.html">removeLocationStatusListener</a></li>
<li><a href="location/LocationEngine/setBackgroundLocationAllowed.html">setBackgroundLocationAllowed</a></li>
<li><a href="location/LocationEngine/setBackgroundLocationIndicatorVisible.html">setBackgroundLocationIndicatorVisible</a></li>
<li><a href="location/LocationEngine/setLastKnownLocationPersistent.html">setLastKnownLocationPersistent</a></li>
<li><a href="location/LocationEngine/setPauseLocationUpdatesAutomatically.html">setPauseLocationUpdatesAutomatically</a></li>
<li><a href="location/LocationEngine/startWithLocationAccuracy.html">startWithLocationAccuracy</a></li>
<li><a href="location/LocationEngine/startWithLocationOptions.html">startWithLocationOptions</a></li>
<li><a href="location/LocationEngine/stop.html">stop</a></li>
<li class="inherited"><a href="location/LocationEngineBase/toString.html">toString</a></li>
<li><a href="location/LocationEngine/updateLocationAccuracy.html">updateLocationAccuracy</a></li>
<li><a href="location/LocationEngine/updateLocationOptions.html">updateLocationOptions</a></li>
<li class="section-title inherited"><a href="location/LocationEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="location/LocationEngineBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li class="self-crumb">LocationEngine class</li>
</ol>
<div class="self-name">LocationEngine</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LocationEngine class</h1></div>
<section class="desc markdown">
<p>Handles location updates received according to the desired /sdk-for-flutter-navigate-location-locationaccuracy or /sdk-for-flutter-navigate-location-locationoptions-class.</p>
<p>Each instance of this class will be using internally the same client providing the actual
location updates. For that reason, only one /sdk-for-flutter-navigate-location-locationengine-class can be started at a time.
Multiple listeners can be attached, either to receive location updates, see /sdk-for-flutter-navigate-core-locationlistener-class,
status updates, see /sdk-for-flutter-navigate-location-locationstatuslistener-class or location issue has occurred, see LocationIssueListener].
When a different /sdk-for-flutter-navigate-location-locationaccuracy or /sdk-for-flutter-navigate-location-locationoptions-class is
desired, the /sdk-for-flutter-navigate-location-locationengine-class needs to be stopped and started again.
Note: starting the /sdk-for-flutter-navigate-location-locationengine-class with /sdk-for-flutter-navigate-location-locationoptions-class is only supported in Android platforms.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LocationEngine">
/sdk-for-flutter-navigate-location-locationengine-locationengine()
</dt>
<dd>
</dd>
<dt class="callable" id="LocationEngine.withSdkEngine">
/sdk-for-flutter-navigate-location-locationengine-locationengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-location-locationenginebase-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isStarted">
/sdk-for-flutter-navigate-location-locationengine-isstarted
→ bool
</dt>
<dd>
  Checks if the engine is in started state.
Checks if the engine is in started state.
  <div class="features">no setteroverride</div>
</dd>
<dt class="property" id="lastKnownLocation">
/sdk-for-flutter-navigate-location-locationengine-lastknownlocation
→ /sdk-for-flutter-navigate-core-location-class?
</dt>
<dd>
  The last known location obtained by the engine.
/sdk-for-flutter-navigate-core-location-class is returned synchronously. /sdk-for-flutter-navigate-core-location-class object has a timestamp attribute,
which reflects when data was obtained. If location was never obtained - null is returned.
  <div class="features">no setteroverride</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-location-locationenginebase-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addLocationIssueListener">
/sdk-for-flutter-navigate-location-locationengine-addlocationissuelistener(<wbr/>/sdk-for-flutter-navigate-location-locationissuelistener-class listener)
    → void

</dt>
<dd>
  Adds a /sdk-for-flutter-navigate-location-locationissuelistener-class to the engine to get notified when a location issue has occurred
Supports more than one listener, instance is added only once.
  <div class="features">override</div>
</dd>
<dt class="callable" id="addLocationListener">
/sdk-for-flutter-navigate-location-locationengine-addlocationlistener(<wbr/>/sdk-for-flutter-navigate-core-locationlistener-class listener)
    → void

</dt>
<dd>
  Adds a /sdk-for-flutter-navigate-core-locationlistener-class to the engine to get notified when there is a new location update available.
Supports more than one listener, instance is added only once.
  <div class="features">override</div>
</dd>
<dt class="callable" id="addLocationStatusListener">
/sdk-for-flutter-navigate-location-locationengine-addlocationstatuslistener(<wbr/>/sdk-for-flutter-navigate-location-locationstatuslistener-class listener)
    → void

</dt>
<dd>
  Adds a /sdk-for-flutter-navigate-location-locationstatuslistener-class to the engine to get notified when there is a an important status change.
Supports more than one listener, instance is added only once.
  <div class="features">override</div>
</dd>
<dt class="callable" id="confirmHEREPrivacyNoticeException">
/sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception(<wbr/>)
    → /sdk-for-flutter-navigate-location-confirmationstatus

</dt>
<dd>
  On Android devices by calling this method, the application developer confirms that they have received an
exceptional permission from HERE in written form to <strong>not</strong> include a reference to the HERE
Privacy Notice. As a result, the <code>LocationEngine</code> will not collect characteristic
information about the nearby mobile and Wi-Fi network signals. However, the engine will still
be fully functional and will deliver location updates when the exception can be confirmed.
  <div class="features">override</div>
</dd>
<dt class="callable" id="confirmHEREPrivacyNoticeInclusion">
/sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion(<wbr/>)
    → /sdk-for-flutter-navigate-location-confirmationstatus

</dt>
<dd>
  On Android devices it is the responsibility of the application developer to ensure that
the application user is informed about the collection of characteristic information
regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related
<a href="https://legal.here.com/here-network-positioning-via-sdk">HERE Privacy Notice</a>
must be made available to the user.
  <div class="features">override</div>
</dd>
<dt class="callable" id="getBackgroundLocationAllowed">
/sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationallowed(<wbr/>)
    → bool

</dt>
<dd>
  On iOS devices this checks if application's background location updates are enabled.
Returns true if background location updates are allowed, false otherwise.
  <div class="features">override</div>
</dd>
<dt class="callable" id="getBackgroundLocationIndicatorVisible">
/sdk-for-flutter-navigate-location-locationengine-getbackgroundlocationindicatorvisible(<wbr/>)
    → bool

</dt>
<dd>
  On iOS devices this checks if application's background location indicator is visible.
Returns true if background location indicator is visible, false otherwise.
  <div class="features">override</div>
</dd>
<dt class="callable" id="getPauseLocationUpdatesAutomatically">
/sdk-for-flutter-navigate-location-locationengine-getpauselocationupdatesautomatically(<wbr/>)
    → bool

</dt>
<dd>
  On iOS devices this checks if automatic pausing of location updates is enabled.
Returns true if automatic pausing of location updates is enabled, false otherwise.
  <div class="features">override</div>
</dd>
<dt class="callable" id="internalsetCallListenerFromMainThreadEnabled">
/sdk-for-flutter-navigate-location-locationengine-internalsetcalllistenerfrommainthreadenabled(<wbr/>bool enabled)
    → void

</dt>
<dd>
  Enables or disables forcing listener calls to originate from main thread.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-location-locationenginebase-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeLocationIssueListener">
/sdk-for-flutter-navigate-location-locationengine-removelocationissuelistener(<wbr/>/sdk-for-flutter-navigate-location-locationissuelistener-class listener)
    → void

</dt>
<dd>
  Removes a /sdk-for-flutter-navigate-location-locationissuelistener-class from the engine.
  <div class="features">override</div>
</dd>
<dt class="callable" id="removeLocationListener">
/sdk-for-flutter-navigate-location-locationengine-removelocationlistener(<wbr/>/sdk-for-flutter-navigate-core-locationlistener-class listener)
    → void

</dt>
<dd>
  Removes a /sdk-for-flutter-navigate-core-locationlistener-class from the engine.
  <div class="features">override</div>
</dd>
<dt class="callable" id="removeLocationStatusListener">
/sdk-for-flutter-navigate-location-locationengine-removelocationstatuslistener(<wbr/>/sdk-for-flutter-navigate-location-locationstatuslistener-class listener)
    → void

</dt>
<dd>
  Removes a /sdk-for-flutter-navigate-location-locationstatuslistener-class from the engine.
  <div class="features">override</div>
</dd>
<dt class="callable" id="setBackgroundLocationAllowed">
/sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationallowed(<wbr/>bool allowed)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  On iOS devices this enables or disables application's background location updates.
By default background location updates
are enabled if application has background location capabilities.
Set <code>allowed</code> to true to allow background location updates, or false to disable them.
Returns /sdk-for-flutter-navigate-location-locationenginestatus if call succeeds. /sdk-for-flutter-navigate-location-locationenginestatus if the application
does not have background location capabilities enabled.
  <div class="features">override</div>
</dd>
<dt class="callable" id="setBackgroundLocationIndicatorVisible">
/sdk-for-flutter-navigate-location-locationengine-setbackgroundlocationindicatorvisible(<wbr/>bool visible)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  On iOS devices this controls visibility of application's background location indicator.
By default background location indicator
is visible, if application has background location capabilities.
Set <code>visible</code> to true to show background location indicator, or false to hide it.
Returns /sdk-for-flutter-navigate-location-locationenginestatus if call succeeds and /sdk-for-flutter-navigate-location-locationenginestatus if the application
does not have background location capabilities enabled.
  <div class="features">override</div>
</dd>
<dt class="callable" id="setLastKnownLocationPersistent">
/sdk-for-flutter-navigate-location-locationengine-setlastknownlocationpersistent(<wbr/>bool persistent)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  On Android devices this enables or disables saving of last known location so
that it persists across application sessions.
By default persistent saving across sessions is enabled.
Set <code>persistent</code> to true to enable last known location to persist across application sessions, or false to disable it.
When calling this method then /sdk-for-flutter-navigate-location-locationenginestatus is returned.
  <div class="features">override</div>
</dd>
<dt class="callable" id="setPauseLocationUpdatesAutomatically">
/sdk-for-flutter-navigate-location-locationengine-setpauselocationupdatesautomatically(<wbr/>bool allowed)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  On iOS devices this controls automatic pausing of location updates e.g.
for improving device's battery life at times when
location data is unlikely to change.
By default automatic pausing of location updates is allowed.
Set <code>allowed</code> to true to allow automatic pausing of location updates, or false to disable them.
When calling this method then /sdk-for-flutter-navigate-location-locationenginestatus is returned.
  <div class="features">override</div>
</dd>
<dt class="callable" id="startWithLocationAccuracy">
/sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy(<wbr/>/sdk-for-flutter-navigate-location-locationaccuracy locationAccuracy)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Starts the location engine with desired /sdk-for-flutter-navigate-location-locationaccuracy.
Make sure to call either /sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion or
/sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception beforehand.
Returns /sdk-for-flutter-navigate-location-locationenginestatus if /sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy or
/sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions is called again without calling /sdk-for-flutter-navigate-location-locationengine-stop in between.
See /sdk-for-flutter-navigate-location-locationenginestatus for other possible return values.
  <div class="features">override</div>
</dd>
<dt class="callable" id="startWithLocationOptions">
/sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions(<wbr/>/sdk-for-flutter-navigate-location-locationoptions-class locationOptions)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  On Android devices starts the location engine with desired /sdk-for-flutter-navigate-location-locationoptions-class.
Make sure to call either /sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion or
/sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception beforehand.
Returns /sdk-for-flutter-navigate-location-locationenginestatus if /sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy or
/sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions is called again without calling /sdk-for-flutter-navigate-location-locationengine-stop in between.
See /sdk-for-flutter-navigate-location-locationenginestatus for other possible return values.
  <div class="features">override</div>
</dd>
<dt class="callable" id="stop">
/sdk-for-flutter-navigate-location-locationengine-stop(<wbr/>)
    → void

</dt>
<dd>
  Stops the location engine.
  <div class="features">override</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-location-locationenginebase-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="updateLocationAccuracy">
/sdk-for-flutter-navigate-location-locationengine-updatelocationaccuracy(<wbr/>/sdk-for-flutter-navigate-location-locationaccuracy locationAccuracy)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Reconfigures the location engine with desired LocationAccuracy.
  <div class="features">override</div>
</dd>
<dt class="callable" id="updateLocationOptions">
/sdk-for-flutter-navigate-location-locationengine-updatelocationoptions(<wbr/>/sdk-for-flutter-navigate-location-locationoptions-class locationOptions)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Reconfigures the location engine with desired LocationOptions.
  <div class="features">override</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-location-locationenginebase-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li class="self-crumb">LocationEngine class</li>
</ol>
<h5>location library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
