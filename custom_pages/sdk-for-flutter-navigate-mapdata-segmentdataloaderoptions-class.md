---
title: "SegmentDataLoaderOptions class"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentDataLoaderOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/SegmentDataLoaderOptions-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/SegmentDataLoaderOptions.html">SegmentDataLoaderOptions</a></li>
<li class="section-title">
<a href="mapdata/SegmentDataLoaderOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/SegmentDataLoaderOptions/hashCode.html">hashCode</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadAdministrativeRules.html">loadAdministrativeRules</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadBaseSpeeds.html">loadBaseSpeeds</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadFunctionalRoadClass.html">loadFunctionalRoadClass</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadLocalRoadCharacteristics.html">loadLocalRoadCharacteristics</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadRailwayCrossings.html">loadRailwayCrossings</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadRoadAttributes.html">loadRoadAttributes</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadRoadSigns.html">loadRoadSigns</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadSpecialSpeedSituations.html">loadSpecialSpeedSituations</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadSpeedLimits.html">loadSpeedLimits</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadStreetNamesAndRoadNumbers.html">loadStreetNamesAndRoadNumbers</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadTollPoints.html">loadTollPoints</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadTrafficSignals.html">loadTrafficSignals</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadTransportModesAccess.html">loadTransportModesAccess</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadTravelDirection.html">loadTravelDirection</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/loadUrban.html">loadUrban</a></li>
<li class="inherited"><a href="mapdata/SegmentDataLoaderOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapdata/SegmentDataLoaderOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/SegmentDataLoaderOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/SegmentDataLoaderOptions/toString.html">toString</a></li>
<li class="section-title"><a href="mapdata/SegmentDataLoaderOptions-class.html#operators">Operators</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">SegmentDataLoaderOptions class</li>
</ol>
<div class="self-name">SegmentDataLoaderOptions</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentDataLoaderOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SegmentDataLoaderOptions class</h1></div>
<section class="desc markdown">
<p>Specifies which data should be loaded by the /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata function.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SegmentDataLoaderOptions">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-segmentdataloaderoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="loadAdministrativeRules">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadadministrativerules
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-administrativerules will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadBaseSpeeds">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadbasespeeds
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionbasespeedinmeterspersecond,
/sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionbasespeedinmeterspersecond and /sdk-for-flutter-navigate-mapdata-segmentspandata-basespeedinmeterspersecond will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadFunctionalRoadClass">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadfunctionalroadclass
↔ bool
</dt>
<dd>
  If it is true, the /sdk-for-flutter-navigate-mapdata-segmentspandata-functionalroadclass will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadLocalRoadCharacteristics">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadlocalroadcharacteristics
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-localroadcharacteristics will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadRailwayCrossings">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadrailwaycrossings
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentdata-railwaycrossings will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadRoadAttributes">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadattributes
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-physicalattributes and
/sdk-for-flutter-navigate-mapdata-segmentspandata-roadusages will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadRoadSigns">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadroadsigns
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentdata-roadsigns will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadSpecialSpeedSituations">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspecialspeedsituations
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-specialspeedsituations will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata is called.
<strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, <code>sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules</code> must also be set to <code>true</code>.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadSpeedLimits">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadspeedlimits
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-positivedirectionspeedlimit,
/sdk-for-flutter-navigate-mapdata-segmentspandata-negativedirectionspeedlimit and /sdk-for-flutter-navigate-mapdata-segmentspandata-speedlimit will be loaded
when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadStreetNamesAndRoadNumbers">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadstreetnamesandroadnumbers
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-streetnames and /sdk-for-flutter-navigate-mapdata-segmentspandata-roadnumbers and will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadTollPoints">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtollpoints
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentdata-tollpoints will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadTrafficSignals">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtrafficsignals
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentdata-trafficsignals will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadTransportModesAccess">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtransportmodesaccess
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-allowedtransportmodes will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadTravelDirection">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtraveldirection
↔ bool
</dt>
<dd>
  If it is true, the /sdk-for-flutter-navigate-mapdata-segmentspandata-traveldirection will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata is called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="loadUrban">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadurban
↔ bool
</dt>
<dd>
  If it is true, /sdk-for-flutter-navigate-mapdata-segmentspandata-isurban will be loaded when /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata is called.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">SegmentDataLoaderOptions class</li>
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
