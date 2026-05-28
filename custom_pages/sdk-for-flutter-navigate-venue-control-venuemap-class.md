---
title: "VenueMap class abstract"
slug: "sdk-for-flutter-navigate-venue-control-venuemap-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueMap-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.control/VenueMap-class.html#constructors">Constructors</a></li>
<li><a href="venue.control/VenueMap/VenueMap.html">VenueMap</a></li>
<li class="section-title">
<a href="venue.control/VenueMap-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="venue.control/VenueMap/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="venue.control/VenueMap/runtimeType.html">runtimeType</a></li>
<li><a href="venue.control/VenueMap/selectedVenue.html">selectedVenue</a></li>
<li><a href="venue.control/VenueMap/venueService.html">venueService</a></li>
<li class="section-title"><a href="venue.control/VenueMap-class.html#instance-methods">Methods</a></li>
<li><a href="venue.control/VenueMap/addDrawingSelectionListener.html">addDrawingSelectionListener</a></li>
<li><a href="venue.control/VenueMap/addLevelSelectionListener.html">addLevelSelectionListener</a></li>
<li><a href="venue.control/VenueMap/addVenueAsync.html">addVenueAsync</a></li>
<li><a href="venue.control/VenueMap/addVenueAsyncStr.html">addVenueAsyncStr</a></li>
<li><a href="venue.control/VenueMap/addVenueAsyncWithErrors.html">addVenueAsyncWithErrors</a></li>
<li><a href="venue.control/VenueMap/addVenueAsyncWithErrorsStr.html">addVenueAsyncWithErrorsStr</a></li>
<li><a href="venue.control/VenueMap/addVenueInfoListListener.html">addVenueInfoListListener</a></li>
<li><a href="venue.control/VenueMap/addVenueLifecycleListener.html">addVenueLifecycleListener</a></li>
<li><a href="venue.control/VenueMap/addVenueMapLifecycleListener.html">addVenueMapLifecycleListener</a></li>
<li><a href="venue.control/VenueMap/addVenueSelectionListener.html">addVenueSelectionListener</a></li>
<li><a href="venue.control/VenueMap/cancelVenueSelection.html">cancelVenueSelection</a></li>
<li><a href="venue.control/VenueMap/getCrosswalk.html">getCrosswalk</a></li>
<li><a href="venue.control/VenueMap/getGeometry.html">getGeometry</a></li>
<li><a href="venue.control/VenueMap/getTopology.html">getTopology</a></li>
<li><a href="venue.control/VenueMap/getVenue.html">getVenue</a></li>
<li><a href="venue.control/VenueMap/getVenueInfoList.html">getVenueInfoList</a></li>
<li><a href="venue.control/VenueMap/getVenueInfoListAsync.html">getVenueInfoListAsync</a></li>
<li><a href="venue.control/VenueMap/getVenueInfoListAsyncWithErrors.html">getVenueInfoListAsyncWithErrors</a></li>
<li><a href="venue.control/VenueMap/getVenueInfoListWithErrors.html">getVenueInfoListWithErrors</a></li>
<li class="inherited"><a href="venue.control/VenueMap/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="venue.control/VenueMap/removeDrawingSelectionListener.html">removeDrawingSelectionListener</a></li>
<li><a href="venue.control/VenueMap/removeLevelSelectionListener.html">removeLevelSelectionListener</a></li>
<li><a href="venue.control/VenueMap/removeVenue.html">removeVenue</a></li>
<li><a href="venue.control/VenueMap/removeVenueInfoListListener.html">removeVenueInfoListListener</a></li>
<li><a href="venue.control/VenueMap/removeVenueLifecycleListener.html">removeVenueLifecycleListener</a></li>
<li><a href="venue.control/VenueMap/removeVenueMapLifecycleListener.html">removeVenueMapLifecycleListener</a></li>
<li><a href="venue.control/VenueMap/removeVenueSelectionListener.html">removeVenueSelectionListener</a></li>
<li><a href="venue.control/VenueMap/selectVenueAsync.html">selectVenueAsync</a></li>
<li><a href="venue.control/VenueMap/selectVenueAsyncStr.html">selectVenueAsyncStr</a></li>
<li><a href="venue.control/VenueMap/selectVenueAsyncWithErrors.html">selectVenueAsyncWithErrors</a></li>
<li><a href="venue.control/VenueMap/selectVenueAsyncWithErrorsStr.html">selectVenueAsyncWithErrorsStr</a></li>
<li class="inherited"><a href="venue.control/VenueMap/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.control/VenueMap-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.control/VenueMap/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li class="self-crumb">VenueMap class</li>
</ol>
<div class="self-name">VenueMap</div>
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
<div class="main-content" data-above-sidebar="venue.control/venue.control-library-sidebar.html" data-below-sidebar="venue.control/VenueMap-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueMap class abstract</h1></div>
<section class="desc markdown">
<p>Connects a map with venues.</p>
<p>When the /sdk-for-flutter-navigate-venue-control-venuemap-class is started,
venues can be seen on the map as interactive models. The user can switch drawings and levels,
change a visual style of geometries and related labels inside the venue etc.
After constructing the /sdk-for-flutter-navigate-venue-control-venuemap-class,
for relevant events should be added to the object. /sdk-for-flutter-navigate-venue-control-venuemap-class is an add-on to
the base map functionality with its own content loading and cache. For this reason, in certain
situations there may be a small delay before the venue is visible.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueMap">
/sdk-for-flutter-navigate-venue-control-venuemap-venuemap()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-control-venuemap-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-control-venuemap-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="selectedVenue">
/sdk-for-flutter-navigate-venue-control-venuemap-selectedvenue
↔ /sdk-for-flutter-navigate-venue-control-venue-class?
</dt>
<dd>
  The selected venue or <code>null</code> if no venue is selected.
Use <code>null</code> to deselect the venue.
Gets the currently selected /sdk-for-flutter-navigate-venue-control-venue-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="venueService">
/sdk-for-flutter-navigate-venue-control-venuemap-venueservice
→ /sdk-for-flutter-navigate-venue-service-venueservice-class
</dt>
<dd>
  The <code>VenueService</code> object.
It can be used to search and get the /sdk-for-flutter-navigate-venue-data-venuemodel-class objects.
Gets the venue service.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addDrawingSelectionListener">
/sdk-for-flutter-navigate-venue-control-venuemap-adddrawingselectionlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class listener)
    → void

</dt>
<dd>
  Adds a drawing selection .
  

</dd>
<dt class="callable" id="addLevelSelectionListener">
/sdk-for-flutter-navigate-venue-control-venuemap-addlevelselectionlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-class listener)
    → void

</dt>
<dd>
  Adds a level selection .
  

</dd>
<dt class="callable" id="addVenueAsync">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenueasync(<wbr/>int venueId)
    → void

</dt>
<dd>
  Downloads and adds a /sdk-for-flutter-navigate-venue-control-venue-class to the /sdk-for-flutter-navigate-venue-control-venuemap-class.
  

</dd>
<dt class="callable" id="addVenueAsyncStr">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncstr(<wbr/>String venueIdentifier)
    → void

</dt>
<dd>
  Downloads and adds a /sdk-for-flutter-navigate-venue-control-venue-class to the /sdk-for-flutter-navigate-venue-control-venuemap-class.
  

</dd>
<dt class="callable" id="addVenueAsyncWithErrors">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrors(<wbr/>int venueId, /sdk-for-flutter-navigate-venue-control-venueloaderrorcallback callback)
    → void

</dt>
<dd>
  Downloads and adds a /sdk-for-flutter-navigate-venue-control-venue-class to the /sdk-for-flutter-navigate-venue-control-venuemap-class.
  

</dd>
<dt class="callable" id="addVenueAsyncWithErrorsStr">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrorsstr(<wbr/>String venueIdentifier, /sdk-for-flutter-navigate-venue-control-venueloaderrorcallback callback)
    → void

</dt>
<dd>
  Downloads and adds a /sdk-for-flutter-navigate-venue-control-venue-class to the /sdk-for-flutter-navigate-venue-control-venuemap-class.
  

</dd>
<dt class="callable" id="addVenueInfoListListener">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenueinfolistlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venueinfolistlistener-class listener)
    → void

</dt>
<dd>
  Adds a listener to handle the completion of the asynchronous venue info list retrieval.
  

</dd>
<dt class="callable" id="addVenueLifecycleListener">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenuelifecyclelistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class listener)
    → void

</dt>
<dd>
  Adds a venue lifecycle .
  

</dd>
<dt class="callable" id="addVenueMapLifecycleListener">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenuemaplifecyclelistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-class listener)
    → void

</dt>
<dd>
  Adds a venue map lifecycle .
  

</dd>
<dt class="callable" id="addVenueSelectionListener">
/sdk-for-flutter-navigate-venue-control-venuemap-addvenueselectionlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venueselectionlistener-class listener)
    → void

</dt>
<dd>
  Adds a venue selection .
  

</dd>
<dt class="callable" id="cancelVenueSelection">
/sdk-for-flutter-navigate-venue-control-venuemap-cancelvenueselection(<wbr/>)
    → bool

</dt>
<dd>
  Attempts to cancel venue loading and selection
that may currently be in progress.
  

</dd>
<dt class="callable" id="getCrosswalk">
/sdk-for-flutter-navigate-venue-control-venuemap-getcrosswalk(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class position)
    → /sdk-for-flutter-navigate-venue-data-crosswalk-class?

</dt>
<dd>
  Tries to find a /sdk-for-flutter-navigate-venue-data-crosswalk-class at the specified geographic coordinates
in the selected /sdk-for-flutter-navigate-venue-control-venue-class in the currently selected /sdk-for-flutter-navigate-venue-data-venuelevel-class.
  

</dd>
<dt class="callable" id="getGeometry">
/sdk-for-flutter-navigate-venue-control-venuemap-getgeometry(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class position)
    → /sdk-for-flutter-navigate-venue-data-venuegeometry-class?

</dt>
<dd>
  Tries to find a /sdk-for-flutter-navigate-venue-data-venuegeometry-class at the specified geographic coordinates
in the selected /sdk-for-flutter-navigate-venue-control-venue-class in the currently selected /sdk-for-flutter-navigate-venue-data-venuelevel-class.
  

</dd>
<dt class="callable" id="getTopology">
/sdk-for-flutter-navigate-venue-control-venuemap-gettopology(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class position)
    → /sdk-for-flutter-navigate-venue-data-venuetopology-class?

</dt>
<dd>
  Tries to find a /sdk-for-flutter-navigate-venue-data-venuetopology-class at the specified geographic coordinates
in the selected /sdk-for-flutter-navigate-venue-control-venue-class in the currently selected /sdk-for-flutter-navigate-venue-data-venuelevel-class.
  

</dd>
<dt class="callable" id="getVenue">
/sdk-for-flutter-navigate-venue-control-venuemap-getvenue(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class position)
    → /sdk-for-flutter-navigate-venue-control-venue-class?

</dt>
<dd>
  Tries to find a /sdk-for-flutter-navigate-venue-control-venue-class at the specified geographic coordinates.
  

</dd>
<dt class="callable" id="getVenueInfoList">
/sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolist(<wbr/>)
    → /sdk-for-flutter-navigate-venue-control-venuemapvenueinfolist

</dt>
<dd>
  The list of /sdk-for-flutter-navigate-venue-data-venueinfo-class contains venue id and name.
  

</dd>
<dt class="callable" id="getVenueInfoListAsync">
/sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolistasync(<wbr/>)
    → void

</dt>
<dd>
  The list of /sdk-for-flutter-navigate-venue-data-venueinfo-class contains venue id and name.
  

</dd>
<dt class="callable" id="getVenueInfoListAsyncWithErrors">
/sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolistasyncwitherrors(<wbr/>/sdk-for-flutter-navigate-venue-control-venueloaderrorcallback callback)
    → void

</dt>
<dd>
  The list of /sdk-for-flutter-navigate-venue-data-venueinfo-class contains venue id and name.
  

</dd>
<dt class="callable" id="getVenueInfoListWithErrors">
/sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolistwitherrors(<wbr/>/sdk-for-flutter-navigate-venue-control-venueloaderrorcallback callback)
    → /sdk-for-flutter-navigate-venue-control-venuemapvenueinfolist

</dt>
<dd>
  The list of /sdk-for-flutter-navigate-venue-data-venueinfo-class contains venue id and name.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-control-venuemap-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeDrawingSelectionListener">
/sdk-for-flutter-navigate-venue-control-venuemap-removedrawingselectionlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class listener)
    → void

</dt>
<dd>
  Removes a drawing selection .
  

</dd>
<dt class="callable" id="removeLevelSelectionListener">
/sdk-for-flutter-navigate-venue-control-venuemap-removelevelselectionlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-class listener)
    → void

</dt>
<dd>
  Removes a level selection .
  

</dd>
<dt class="callable" id="removeVenue">
/sdk-for-flutter-navigate-venue-control-venuemap-removevenue(<wbr/>/sdk-for-flutter-navigate-venue-control-venue-class venue)
    → void

</dt>
<dd>
  Removes a /sdk-for-flutter-navigate-venue-control-venue-class from the /sdk-for-flutter-navigate-venue-control-venuemap-class.
  

</dd>
<dt class="callable" id="removeVenueInfoListListener">
/sdk-for-flutter-navigate-venue-control-venuemap-removevenueinfolistlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venueinfolistlistener-class listener)
    → void

</dt>
<dd>
  Removes a listener for the asynchronous venue info list retrieval.
  

</dd>
<dt class="callable" id="removeVenueLifecycleListener">
/sdk-for-flutter-navigate-venue-control-venuemap-removevenuelifecyclelistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class listener)
    → void

</dt>
<dd>
  Removes a venue lifecycle .
  

</dd>
<dt class="callable" id="removeVenueMapLifecycleListener">
/sdk-for-flutter-navigate-venue-control-venuemap-removevenuemaplifecyclelistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-class listener)
    → void

</dt>
<dd>
  Removes a venue map lifecycle .
  

</dd>
<dt class="callable" id="removeVenueSelectionListener">
/sdk-for-flutter-navigate-venue-control-venuemap-removevenueselectionlistener(<wbr/>/sdk-for-flutter-navigate-venue-control-venueselectionlistener-class listener)
    → void

</dt>
<dd>
  Removes a venue selection .
  

</dd>
<dt class="callable" id="selectVenueAsync">
/sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasync(<wbr/>int venueId)
    → void

</dt>
<dd>
  Downloads a /sdk-for-flutter-navigate-venue-data-venuemodel-class if needed and selects a /sdk-for-flutter-navigate-venue-control-venue-class.
  

</dd>
<dt class="callable" id="selectVenueAsyncStr">
/sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncstr(<wbr/>String venueIdentifier)
    → void

</dt>
<dd>
  Downloads a /sdk-for-flutter-navigate-venue-data-venuemodel-class if needed and selects a /sdk-for-flutter-navigate-venue-control-venue-class.
  

</dd>
<dt class="callable" id="selectVenueAsyncWithErrors">
/sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrors(<wbr/>int venueId, /sdk-for-flutter-navigate-venue-control-venueloaderrorcallback callback)
    → void

</dt>
<dd>
  Downloads a /sdk-for-flutter-navigate-venue-data-venuemodel-class if needed and selects a /sdk-for-flutter-navigate-venue-control-venue-class.
  

</dd>
<dt class="callable" id="selectVenueAsyncWithErrorsStr">
/sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrorsstr(<wbr/>String venueIdentifier, /sdk-for-flutter-navigate-venue-control-venueloaderrorcallback callback)
    → void

</dt>
<dd>
  Downloads a /sdk-for-flutter-navigate-venue-data-venuemodel-class if needed and selects a /sdk-for-flutter-navigate-venue-control-venue-class.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-control-venuemap-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-control-venuemap-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li class="self-crumb">VenueMap class</li>
</ol>
<h5>venue.control library</h5>
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
