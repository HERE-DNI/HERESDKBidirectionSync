---
title: "LocationSimulator class abstract"
slug: "sdk-for-flutter-navigate-navigation-locationsimulator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationSimulator-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/LocationSimulator-class.html#constructors">Constructors</a></li>
<li><a href="navigation/LocationSimulator/LocationSimulator.withRoute.html">withRoute</a></li>
<li><a href="navigation/LocationSimulator/LocationSimulator.withTrack.html">withTrack</a></li>
<li class="section-title">
<a href="navigation/LocationSimulator-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="navigation/LocationSimulator/hashCode.html">hashCode</a></li>
<li><a href="navigation/LocationSimulator/listener.html">listener</a></li>
<li class="inherited"><a href="navigation/LocationSimulator/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="navigation/LocationSimulator-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/LocationSimulator/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/LocationSimulator/pause.html">pause</a></li>
<li><a href="navigation/LocationSimulator/resume.html">resume</a></li>
<li><a href="navigation/LocationSimulator/start.html">start</a></li>
<li><a href="navigation/LocationSimulator/stop.html">stop</a></li>
<li class="inherited"><a href="navigation/LocationSimulator/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/LocationSimulator-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/LocationSimulator/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">LocationSimulator class</li>
</ol>
<div class="self-name">LocationSimulator</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LocationSimulator-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LocationSimulator class abstract</h1></div>
<section class="desc markdown">
<p>Use the <code>LocationSimulator</code> to generate locations along a route or a GPX document.</p>
<p>It notifies
the registered object about the current location at a fixed interval. In order to customize
the interval, see /sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class.
The locations are closely matched to the shape and proceeded from the start to the
destination as found in the provided route or the GPX document.
When providing a route, the <code>LocationSimulator</code> uses a base speed taken from each span
found in the provided route object. This base speed can be multiplied upfront
with a custom <code>speedFactor</code> for simulation purposes.
Effectively, this means that traffic-related information is not considered
to adjust the speed of the simulation.
For the <code>GPXTrack</code>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <code>GPXTrack</code> and inserted into the provided <code>Location</code> object: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code> and <code>locationTechnology</code>.</p>
<p>Note that simulation works offline and independent from any map data</p>
<ul>
<li>only the information found in the provided route or GPX document is considered.</li>
<li>When initializing the <code>LocationSimulator</code> with a route, then interpolations take place between the vertices of the route's
polyline. The distance between interpolated locations is a function of the current span's speed and the set notification interval.</li>
<li>When initializing the <code>LocationSimulator</code> with a GPX file, the <code>LocationSimulator</code> does not apply
any interpolation on the provided location data as this would shadow the recorded GPX data.</li>
</ul>
<p>Notifications will stop after the entire route has been traveled.</p>
<p><strong>Note:</strong>
Map-matched locations are only accessible from /sdk-for-flutter-navigate-navigation-routeprogress-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LocationSimulator.withRoute">
/sdk-for-flutter-navigate-navigation-locationsimulator-locationsimulator-withroute(/sdk-for-flutter-navigate-routing-route-class route, /sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class options)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="LocationSimulator.withTrack">
/sdk-for-flutter-navigate-navigation-locationsimulator-locationsimulator-withtrack(/sdk-for-flutter-navigate-navigation-gpxtrack-class gpxTrack, /sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class options)
</dt>
<dd>
          Create a location simulator
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-locationsimulator-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="listener">
/sdk-for-flutter-navigate-navigation-locationsimulator-listener
↔ /sdk-for-flutter-navigate-core-locationlistener-class?
</dt>
<dd>
  The object that notifies on location updates.
Gets a <code>LocationListener</code> that notifies on location updates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-locationsimulator-runtimetype
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
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-locationsimulator-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="pause">
/sdk-for-flutter-navigate-navigation-locationsimulator-pause(<wbr/>)
    → void

</dt>
<dd>
  Pauses sending notifications to the subscribers.
  

</dd>
<dt class="callable" id="resume">
/sdk-for-flutter-navigate-navigation-locationsimulator-resume(<wbr/>)
    → void

</dt>
<dd>
  Resumes sending notifications to the subscribers.
  

</dd>
<dt class="callable" id="start">
/sdk-for-flutter-navigate-navigation-locationsimulator-start(<wbr/>)
    → void

</dt>
<dd>
  Starts the location provider to send notifications to the subscribers.
  

</dd>
<dt class="callable" id="stop">
/sdk-for-flutter-navigate-navigation-locationsimulator-stop(<wbr/>)
    → void

</dt>
<dd>
  Stops the location provider from sending notifications to the subscribers.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-locationsimulator-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-locationsimulator-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">LocationSimulator class</li>
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
