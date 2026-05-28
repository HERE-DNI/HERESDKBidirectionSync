---
title: "SegmentData class abstract"
slug: "sdk-for-flutter-navigate-mapdata-segmentdata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentData-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/SegmentData-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/SegmentData/SegmentData.html">SegmentData</a></li>
<li class="section-title">
<a href="mapdata/SegmentData-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapdata/SegmentData/hashCode.html">hashCode</a></li>
<li><a href="mapdata/SegmentData/lengthInMeters.html">lengthInMeters</a></li>
<li><a href="mapdata/SegmentData/ocmSegmentId.html">ocmSegmentId</a></li>
<li><a href="mapdata/SegmentData/polyline.html">polyline</a></li>
<li><a href="mapdata/SegmentData/railwayCrossings.html">railwayCrossings</a></li>
<li><a href="mapdata/SegmentData/roadSigns.html">roadSigns</a></li>
<li class="inherited"><a href="mapdata/SegmentData/runtimeType.html">runtimeType</a></li>
<li><a href="mapdata/SegmentData/segmentReference.html">segmentReference</a></li>
<li><a href="mapdata/SegmentData/spans.html">spans</a></li>
<li><a href="mapdata/SegmentData/tollPoints.html">tollPoints</a></li>
<li><a href="mapdata/SegmentData/trafficSignals.html">trafficSignals</a></li>
<li class="section-title inherited"><a href="mapdata/SegmentData-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/SegmentData/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/SegmentData/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapdata/SegmentData-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapdata/SegmentData/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">SegmentData class</li>
</ol>
<div class="self-name">SegmentData</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentData-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SegmentData class abstract</h1></div>
<section class="desc markdown">
<p>Contains the requested information for a segment</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.</p>
<p>Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SegmentData">
/sdk-for-flutter-navigate-mapdata-segmentdata-segmentdata()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapdata-segmentdata-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="lengthInMeters">
/sdk-for-flutter-navigate-mapdata-segmentdata-lengthinmeters
→ int
</dt>
<dd>
  The length of this segment in meters. This information is based on map data.
It can differ from the length of /sdk-for-flutter-navigate-mapdata-segmentdata-polyline due to
approximations of the polyline.
Gets the length of this segment in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="ocmSegmentId">
/sdk-for-flutter-navigate-mapdata-segmentdata-ocmsegmentid
→ /sdk-for-flutter-navigate-mapdata-ocmsegmentid-class
</dt>
<dd>
  The /sdk-for-flutter-navigate-mapdata-ocmsegmentid-class object representing the segment
Gets the /sdk-for-flutter-navigate-mapdata-ocmsegmentid-class object representing the the segment.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="polyline">
/sdk-for-flutter-navigate-mapdata-segmentdata-polyline
→ /sdk-for-flutter-navigate-core-geopolyline-class
</dt>
<dd>
  The /sdk-for-flutter-navigate-core-geopolyline-class object representing the polyline of this segment.
Gets the /sdk-for-flutter-navigate-core-geopolyline-class object representing the polyline of this segment.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="railwayCrossings">
/sdk-for-flutter-navigate-mapdata-segmentdata-railwaycrossings
→ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-railwaycrossing-class&gt;?
</dt>
<dd>
  The list of /sdk-for-flutter-navigate-mapdata-railwaycrossing-class of the given segment.
Returns an empty list if no data is found.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadrailwaycrossings is set to <code>false</code>.
Gets the list of /sdk-for-flutter-navigate-mapdata-railwaycrossing-class.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadSigns">
/sdk-for-flutter-navigate-mapdata-segmentdata-roadsigns
→ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-roadsign-class&gt;?
</dt>
<dd>
  The list of /sdk-for-flutter-navigate-navigation-roadsign-class of the given segment.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadsigns is set to <code>false</code>.
Gets the list of /sdk-for-flutter-navigate-navigation-roadsign-class.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-segmentdata-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentReference">
/sdk-for-flutter-navigate-mapdata-segmentdata-segmentreference
→ /sdk-for-flutter-navigate-routing-segmentreference-class
</dt>
<dd>
  The /sdk-for-flutter-navigate-routing-segmentreference-class object representing the segment
Gets the /sdk-for-flutter-navigate-routing-segmentreference-class object representing the the segment.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="spans">
/sdk-for-flutter-navigate-mapdata-segmentdata-spans
→ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-segmentspandata-class&gt;
</dt>
<dd>
  The list of /sdk-for-flutter-navigate-mapdata-segmentspandata-class of the given segment for the
requested attributes
<strong>Note:</strong> If no span attributes is requested, the list will be empty.
Gets the list of /sdk-for-flutter-navigate-mapdata-segmentspandata-class.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="tollPoints">
/sdk-for-flutter-navigate-mapdata-segmentdata-tollpoints
→ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-tollpoint-class&gt;?
</dt>
<dd>
  The list of /sdk-for-flutter-navigate-mapdata-tollpoint-class of the given segment.
Returns an empty list if no data is found.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtollpoints is set to <code>false</code>
or the /sdk-for-flutter-navigate-mapdata-segmentdata-class is not initialized using /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata.
Gets the list of /sdk-for-flutter-navigate-mapdata-tollpoint-class.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="trafficSignals">
/sdk-for-flutter-navigate-mapdata-segmentdata-trafficsignals
→ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-trafficsignal-class&gt;?
</dt>
<dd>
  The list of /sdk-for-flutter-navigate-mapdata-trafficsignal-class of the given segment.
Returns an empty list if no data is found.
Returns <code>null</code> if /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtrafficsignals is set to <code>false</code>.
The /sdk-for-flutter-navigate-mapdata-trafficsignallocation indicates the location of a single traffic signal, which can be any combination of left, right and overhead.
The /sdk-for-flutter-navigate-mapdata-trafficsignal-offsetinmeters is the location along the segment,
while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.
Gets the list of /sdk-for-flutter-navigate-mapdata-trafficsignal-class.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-segmentdata-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-segmentdata-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-segmentdata-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">SegmentData class</li>
</ol>
<h5>mapdata library</h5>
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
