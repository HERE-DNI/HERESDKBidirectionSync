---
title: "LocationEngineBase constructor"
slug: "sdk-for-flutter-navigate-location-locationenginebase-locationenginebase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationEngineBase.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">LocationEngineBase factory constructor</li>
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
<div class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LocationEngineBase constructor</h1></div>
<section class="multi-line-signature">
LocationEngineBase(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-location-locationenginestatus startWithLocationAccuracyLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationaccuracy</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-location-locationenginestatus startWithLocationOptionsLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-location-locationenginestatus updateLocationAccuracyLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationaccuracy</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-location-locationenginestatus updateLocationOptionsLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationoptions-class</li>
</ol>), </li>
<li>void stopLambda(), </li>
<li>/sdk-for-flutter-navigate-location-confirmationstatus confirmHEREPrivacyNoticeInclusionLambda(), </li>
<li>/sdk-for-flutter-navigate-location-confirmationstatus confirmHEREPrivacyNoticeExceptionLambda(), </li>
<li>void addLocationListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-locationlistener-class</li>
</ol>), </li>
<li>void removeLocationListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-locationlistener-class</li>
</ol>), </li>
<li>void addLocationStatusListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationstatuslistener-class</li>
</ol>), </li>
<li>void removeLocationStatusListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationstatuslistener-class</li>
</ol>), </li>
<li>void addLocationIssueListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationissuelistener-class</li>
</ol>), </li>
<li>void removeLocationIssueListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationissuelistener-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-location-locationenginestatus setBackgroundLocationAllowedLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool getBackgroundLocationAllowedLambda(), </li>
<li>/sdk-for-flutter-navigate-location-locationenginestatus setBackgroundLocationIndicatorVisibleLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool getBackgroundLocationIndicatorVisibleLambda(), </li>
<li>/sdk-for-flutter-navigate-location-locationenginestatus setPauseLocationUpdatesAutomaticallyLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool getPauseLocationUpdatesAutomaticallyLambda(), </li>
<li>/sdk-for-flutter-navigate-location-locationenginestatus setLastKnownLocationPersistentLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>void internalsetCallListenerFromMainThreadEnabledLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-location-class? lastKnownLocationGetLambda(), </li>
<li>bool isStartedGetLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Public abstract class that describes the behaviour of <code>LocationEngine</code>.</p>
<p>Implementation is platform-specific.</p>
</section>
<section class="summary source-code" id="source">
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
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">LocationEngineBase factory constructor</li>
</ol>
<h5>LocationEngineBase class</h5>
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
