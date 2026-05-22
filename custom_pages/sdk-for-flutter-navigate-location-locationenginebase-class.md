---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-locationenginebase-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngineBase-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li class="self-crumb">LocationEngineBase class</li>
</ol>
<div class="self-name">LocationEngineBase</div>
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
<div class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationEngineBase-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LocationEngineBase class abstract</h1></div>
<section class="desc markdown">
<p>Public abstract class that describes the behaviour of <code>LocationEngine</code>.</p>
<p>Implementation is platform-specific.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LocationEngineBase">
/sdk-for-flutter-navigate-location-locationenginebase-locationenginebase(/sdk-for-flutter-navigate-location-locationenginestatus startWithLocationAccuracyLambda(/sdk-for-flutter-navigate-location-locationaccuracy), /sdk-for-flutter-navigate-location-locationenginestatus startWithLocationOptionsLambda(/sdk-for-flutter-navigate-location-locationoptions-class), /sdk-for-flutter-navigate-location-locationenginestatus updateLocationAccuracyLambda(/sdk-for-flutter-navigate-location-locationaccuracy), /sdk-for-flutter-navigate-location-locationenginestatus updateLocationOptionsLambda(/sdk-for-flutter-navigate-location-locationoptions-class), void stopLambda(), /sdk-for-flutter-navigate-location-confirmationstatus confirmHEREPrivacyNoticeInclusionLambda(), /sdk-for-flutter-navigate-location-confirmationstatus confirmHEREPrivacyNoticeExceptionLambda(), void addLocationListenerLambda(/sdk-for-flutter-navigate-core-locationlistener-class), void removeLocationListenerLambda(/sdk-for-flutter-navigate-core-locationlistener-class), void addLocationStatusListenerLambda(/sdk-for-flutter-navigate-location-locationstatuslistener-class), void removeLocationStatusListenerLambda(/sdk-for-flutter-navigate-location-locationstatuslistener-class), void addLocationIssueListenerLambda(/sdk-for-flutter-navigate-location-locationissuelistener-class), void removeLocationIssueListenerLambda(/sdk-for-flutter-navigate-location-locationissuelistener-class), /sdk-for-flutter-navigate-location-locationenginestatus setBackgroundLocationAllowedLambda(bool), bool getBackgroundLocationAllowedLambda(), /sdk-for-flutter-navigate-location-locationenginestatus setBackgroundLocationIndicatorVisibleLambda(bool), bool getBackgroundLocationIndicatorVisibleLambda(), /sdk-for-flutter-navigate-location-locationenginestatus setPauseLocationUpdatesAutomaticallyLambda(bool), bool getPauseLocationUpdatesAutomaticallyLambda(), /sdk-for-flutter-navigate-location-locationenginestatus setLastKnownLocationPersistentLambda(bool), void internalsetCallListenerFromMainThreadEnabledLambda(bool), /sdk-for-flutter-navigate-core-location-class? lastKnownLocationGetLambda(), bool isStartedGetLambda())
</dt>
<dd>
          Public abstract class that describes the behaviour of <code>LocationEngine</code>.
            <div class="constructor-modifier features">factory</div>
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
/sdk-for-flutter-navigate-location-locationenginebase-isstarted
→ bool
</dt>
<dd>
  Checks if the engine is in started state.
Checks if the engine is in started state.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastKnownLocation">
/sdk-for-flutter-navigate-location-locationenginebase-lastknownlocation
→ /sdk-for-flutter-navigate-core-location-class?
</dt>
<dd>
  The last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.
This property can be obtained without starting the <code>LocationEngine</code>. However, the initial value might be <code>null</code>
if no location has ever been obtained by the <code>LocationEngine</code>.
The time attribute of the <code>Location</code> object indicates when the last location was obtained.
Note: In order to receive continuous location updates, add a <code>LocationListener</code>.
Gets the last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.
  <div class="features">no setter</div>
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
/sdk-for-flutter-navigate-location-locationenginebase-addlocationissuelistener(<wbr/>/sdk-for-flutter-navigate-location-locationissuelistener-class listener)
    → void

</dt>
<dd>
  Adds a /sdk-for-flutter-navigate-location-locationissuelistener-class to the engine to get notified when a location issue has occurred.
  

</dd>
<dt class="callable" id="addLocationListener">
/sdk-for-flutter-navigate-location-locationenginebase-addlocationlistener(<wbr/>/sdk-for-flutter-navigate-core-locationlistener-class listener)
    → void

</dt>
<dd>
  Adds a <code>LocationListener</code> to the engine to get notified when there is a new location
update available.
  

</dd>
<dt class="callable" id="addLocationStatusListener">
/sdk-for-flutter-navigate-location-locationenginebase-addlocationstatuslistener(<wbr/>/sdk-for-flutter-navigate-location-locationstatuslistener-class listener)
    → void

</dt>
<dd>
  Adds a <code>LocationStatusListener</code> to the engine to get notified when there is an important
status change.
  

</dd>
<dt class="callable" id="confirmHEREPrivacyNoticeException">
/sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception(<wbr/>)
    → /sdk-for-flutter-navigate-location-confirmationstatus

</dt>
<dd>
  By calling this method, the application developer confirms that they have received an exceptional permission
from HERE in written form to <strong>not</strong> include a reference to the HERE Privacy Notice.
  

</dd>
<dt class="callable" id="confirmHEREPrivacyNoticeInclusion">
/sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion(<wbr/>)
    → /sdk-for-flutter-navigate-location-confirmationstatus

</dt>
<dd>
  It is the responsibility of the application developer to ensure that
the application user is informed about the collection of characteristic information
regarding nearby mobile and Wi-Fi network signals.
  

</dd>
<dt class="callable" id="getBackgroundLocationAllowed">
/sdk-for-flutter-navigate-location-locationenginebase-getbackgroundlocationallowed(<wbr/>)
    → bool

</dt>
<dd>
  Check if application's background location updates are enabled.
  

</dd>
<dt class="callable" id="getBackgroundLocationIndicatorVisible">
/sdk-for-flutter-navigate-location-locationenginebase-getbackgroundlocationindicatorvisible(<wbr/>)
    → bool

</dt>
<dd>
  Check if application's background location indicator is visible.
  

</dd>
<dt class="callable" id="getPauseLocationUpdatesAutomatically">
/sdk-for-flutter-navigate-location-locationenginebase-getpauselocationupdatesautomatically(<wbr/>)
    → bool

</dt>
<dd>
  Check if automatic pausing of location updates are enabled.
  

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
/sdk-for-flutter-navigate-location-locationenginebase-removelocationissuelistener(<wbr/>/sdk-for-flutter-navigate-location-locationissuelistener-class listener)
    → void

</dt>
<dd>
  Removes a /sdk-for-flutter-navigate-location-locationissuelistener-class from the engine.
  

</dd>
<dt class="callable" id="removeLocationListener">
/sdk-for-flutter-navigate-location-locationenginebase-removelocationlistener(<wbr/>/sdk-for-flutter-navigate-core-locationlistener-class listener)
    → void

</dt>
<dd>
  Removes a <code>LocationListener</code> from the engine.
  

</dd>
<dt class="callable" id="removeLocationStatusListener">
/sdk-for-flutter-navigate-location-locationenginebase-removelocationstatuslistener(<wbr/>/sdk-for-flutter-navigate-location-locationstatuslistener-class listener)
    → void

</dt>
<dd>
  Removes a <code>LocationStatusListener</code> from the engine.
  

</dd>
<dt class="callable" id="setBackgroundLocationAllowed">
/sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationallowed(<wbr/>bool allowed)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Enables or disables background location updates for an application.
  

</dd>
<dt class="callable" id="setBackgroundLocationIndicatorVisible">
/sdk-for-flutter-navigate-location-locationenginebase-setbackgroundlocationindicatorvisible(<wbr/>bool visible)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Controls visibility of application's background location indicator.
  

</dd>
<dt class="callable" id="setLastKnownLocationPersistent">
/sdk-for-flutter-navigate-location-locationenginebase-setlastknownlocationpersistent(<wbr/>bool persistent)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Enables or disables saving of last known location so that it persists between application sessions.
  

</dd>
<dt class="callable" id="setPauseLocationUpdatesAutomatically">
/sdk-for-flutter-navigate-location-locationenginebase-setpauselocationupdatesautomatically(<wbr/>bool allowed)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Controls automatic pausing of location updates e.g.
  

</dd>
<dt class="callable" id="startWithLocationAccuracy">
/sdk-for-flutter-navigate-location-locationenginebase-startwithlocationaccuracy(<wbr/>/sdk-for-flutter-navigate-location-locationaccuracy locationAccuracy)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Starts the location engine with desired /sdk-for-flutter-navigate-location-locationaccuracy.
  

</dd>
<dt class="callable" id="startWithLocationOptions">
/sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions(<wbr/>/sdk-for-flutter-navigate-location-locationoptions-class locationOptions)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Starts the location engine with desired /sdk-for-flutter-navigate-location-locationoptions-class.
  

</dd>
<dt class="callable" id="stop">
/sdk-for-flutter-navigate-location-locationenginebase-stop(<wbr/>)
    → void

</dt>
<dd>
  Stops the location engine.
  

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
/sdk-for-flutter-navigate-location-locationenginebase-updatelocationaccuracy(<wbr/>/sdk-for-flutter-navigate-location-locationaccuracy locationAccuracy)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Reconfigures the location engine with desired /sdk-for-flutter-navigate-location-locationaccuracy.
  

</dd>
<dt class="callable" id="updateLocationOptions">
/sdk-for-flutter-navigate-location-locationenginebase-updatelocationoptions(<wbr/>/sdk-for-flutter-navigate-location-locationoptions-class locationOptions)
    → /sdk-for-flutter-navigate-location-locationenginestatus

</dt>
<dd>
  Reconfigures the location engine with desired /sdk-for-flutter-navigate-location-locationoptions-class.
  

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
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="makeLocationEngine">
/sdk-for-flutter-navigate-location-locationenginebase-makelocationengine(<wbr/>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
    → /sdk-for-flutter-navigate-location-locationenginebase-class

</dt>
<dd>
  Creates instance of <code>LocationEngine</code> using factory, registered on platform side
  

</dd>
<dt class="callable" id="makeLocationEngineFromSharedSdkNativeEngine">
/sdk-for-flutter-navigate-location-locationenginebase-makelocationenginefromsharedsdknativeengine(<wbr/>)
    → /sdk-for-flutter-navigate-location-locationenginebase-class

</dt>
<dd>
  Creates instance of <code>LocationEngine</code> using factory, registered on platform side
  

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
<li class="self-crumb">LocationEngineBase class</li>
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



</div>
`
}</HTMLBlock>
