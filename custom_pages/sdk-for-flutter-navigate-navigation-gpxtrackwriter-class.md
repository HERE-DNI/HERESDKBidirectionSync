---
title: "GPXTrackWriter class abstract"
slug: "sdk-for-flutter-navigate-navigation-gpxtrackwriter-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GPXTrackWriter-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/GPXTrackWriter-class.html#constructors">Constructors</a></li>
<li><a href="navigation/GPXTrackWriter/GPXTrackWriter.html">GPXTrackWriter</a></li>
<li><a href="navigation/GPXTrackWriter/GPXTrackWriter.withTrack.html">withTrack</a></li>
<li class="section-title">
<a href="navigation/GPXTrackWriter-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core/LocationListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core/LocationListener/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/GPXTrackWriter/track.html">track</a></li>
<li class="section-title inherited"><a href="navigation/GPXTrackWriter-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/LocationListener/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/LocationListener/onLocationUpdated.html">onLocationUpdated</a></li>
<li class="inherited"><a href="core/LocationListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/GPXTrackWriter-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core/LocationListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">GPXTrackWriter class</li>
</ol>
<div class="self-name">GPXTrackWriter</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/GPXTrackWriter-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GPXTrackWriter class abstract</h1></div>
<section class="desc markdown">
<p>Writes GPX track points to /sdk-for-flutter-navigate-navigation-gpxtrack-class.</p>
<p>The instance of the class should be added as a listener to the
<code>LocationEngine</code> for GPX track recording.
Appends the new location to the back segment of the track whenever the listener is called.
The following data (if provided) can be recorded and inserted into the resulting /sdk-for-flutter-navigate-navigation-gpxtrack-class: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>pitchInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code>, <code>bearingAccuracyInDegrees</code>, <code>speedAccuracyInMetersPerSecond</code> and <code>locationTechnology</code>.</p>
<p>Use case examples:</p>
<p>A user wants to create and save a new /sdk-for-flutter-navigate-navigation-gpxdocument-class with one /sdk-for-flutter-navigate-navigation-gpxtrack-class:</p>
<ul>
<li>create /sdk-for-flutter-navigate-navigation-gpxtrackwriter-class and add it as a location listener to <code>LocationEngine</code>.</li>
<li>set user parameters to /sdk-for-flutter-navigate-navigation-gpxtrackwriter-track (e.g. /sdk-for-flutter-navigate-navigation-gpxtrack-name or /sdk-for-flutter-navigate-navigation-gpxtrack-description).</li>
<li>when writing is completed, create a new /sdk-for-flutter-navigate-navigation-gpxdocument-class with a list of one /sdk-for-flutter-navigate-navigation-gpxtrack-class and save the document via /sdk-for-flutter-navigate-navigation-gpxdocument-save.</li>
</ul>
<p>A user wants to modify and save /sdk-for-flutter-navigate-navigation-gpxtrack-class in the existing /sdk-for-flutter-navigate-navigation-gpxdocument-class:</p>
<ul>
<li>load /sdk-for-flutter-navigate-navigation-gpxdocument-class from a file by the relevant constructor.</li>
<li>create /sdk-for-flutter-navigate-navigation-gpxtrackwriter-class with the required track in the list /sdk-for-flutter-navigate-navigation-gpxdocument-tracks,
add the created instance as a location listener to <code>LocationEngine</code>.</li>
<li>when writing is completed, save the document via /sdk-for-flutter-navigate-navigation-gpxdocument-save.</li>
</ul>
<p>The <code>GPXDocument</code> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-core-locationlistener-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="GPXTrackWriter">
/sdk-for-flutter-navigate-navigation-gpxtrackwriter-gpxtrackwriter()
</dt>
<dd>
          Creates a new instance of GPXTrackWriter with an empty track inside.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GPXTrackWriter.withTrack">
/sdk-for-flutter-navigate-navigation-gpxtrackwriter-gpxtrackwriter-withtrack(/sdk-for-flutter-navigate-navigation-gpxtrack-class track)
</dt>
<dd>
          Creates a new instance of /sdk-for-flutter-navigate-navigation-gpxtrackwriter-class with /sdk-for-flutter-navigate-navigation-gpxtrack-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-core-locationlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-locationlistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="track">
/sdk-for-flutter-navigate-navigation-gpxtrackwriter-track
→ /sdk-for-flutter-navigate-navigation-gpxtrack-class
</dt>
<dd>
  GPX track into which GPX track points are written.
Gets the GPX track into which GPX track points are written.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-locationlistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="onLocationUpdated">
/sdk-for-flutter-navigate-core-locationlistener-onlocationupdated(<wbr/>/sdk-for-flutter-navigate-core-location-class location)
    → void

</dt>
<dd class="inherited">
  Called each time a new location is available.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-locationlistener-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-core-locationlistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">GPXTrackWriter class</li>
</ol>
<h5>navigation library</h5>
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
