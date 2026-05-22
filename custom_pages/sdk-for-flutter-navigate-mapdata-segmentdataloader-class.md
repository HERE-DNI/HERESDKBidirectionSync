---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentDataLoader-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">SegmentDataLoader class</li>
</ol>
<div class="self-name">SegmentDataLoader</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentDataLoader-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SegmentDataLoader class abstract</h1></div>
<section class="desc markdown">
<p>Provides the abstract class for the access to the
segments data available in the local OCM map.</p>
<p>Please be aware that the methods within this class
load map data synchronously. In the event of absent data in the disk cache, the data will be
retrieved from the remote server. To mitigate the potential freezing of the calling thread,
it is advisable to proactively prefetch map data around the working area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SegmentDataLoader">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-segmentdataloader()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="SegmentDataLoader.withEngine">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-segmentdataloader-withengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-runtimetype
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
<dt class="callable" id="downloadFile">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-downloadfile(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-filereference-class&gt; fileReferences, /sdk-for-flutter-navigate-mapdata-downloadingfileoptions-class downloadingOptions)
    → List&lt;<wbr/>Uint8List&gt;

</dt>
<dd>
  Synchronously load the optional image providing guidance of a directed or non directed segment.
  

</dd>
<dt class="callable" id="getSegmentsAroundCoordinates">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-getsegmentsaroundcoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, double radiusInMeters)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-ocmsegmentid-class&gt;

</dt>
<dd>
  Loads the segments around a certain coordinates.
  

</dd>
<dt class="callable" id="loadData">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata(<wbr/>/sdk-for-flutter-navigate-mapdata-ocmsegmentid-class segment, /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class options)
    → /sdk-for-flutter-navigate-mapdata-segmentdata-class

</dt>
<dd>
  Synchronously load the data for the given map segment.
  

</dd>
<dt class="callable" id="loadDirectedSegmentData">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata(<wbr/>/sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class segment, /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class options)
    → /sdk-for-flutter-navigate-mapdata-segmentdata-class

</dt>
<dd>
  Synchronously load the data for the given map directed segment.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-segmentdataloader-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">SegmentDataLoader class</li>
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



</div>
`
}</HTMLBlock>
