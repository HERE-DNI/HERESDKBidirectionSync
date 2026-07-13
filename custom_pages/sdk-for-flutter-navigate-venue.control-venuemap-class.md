---
title: "VenueMap class - venue.control library - Dart API"
slug: "sdk-for-flutter-navigate-venue.control-venuemap-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueMap-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.control/venue.control-library-sidebar.html" data-below-sidebar="venue.control/VenueMap-class-sidebar.html">

<div>

# <span class="kind-class">VenueMap</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Connects a map with venues.

When the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a> is started, venues can be seen on the map as interactive models. The user can switch drawings and levels, change a visual style of geometries and related labels inside the venue etc. After constructing the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>, for relevant events should be added to the object. <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a> is an add-on to the base map functionality with its own content loading and cache. For this reason, in certain situations there may be a small delay before the venue is visible.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-venuemap">VenueMap</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-selectedvenue">selectedVenue</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>?</span>  
The selected venue or `null` if no venue is selected. Use `null` to deselect the venue. Gets the currently selected <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-venueservice">venueService</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a></span>  
The `VenueService` object. It can be used to search and get the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> objects. Gets the venue service.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-adddrawingselectionlistener">addDrawingSelectionListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addDrawingSelectionListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class">VenueDrawingSelectionListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a drawing selection .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addlevelselectionlistener">addLevelSelectionListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addLevelSelectionListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-class">VenueLevelSelectionListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a level selection .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenueasync">addVenueAsync</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueAsync-param-venueId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">venueId</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads and adds a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> to the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncstr">addVenueAsyncStr</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueAsyncStr-param-venueIdentifier" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">venueIdentifier</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads and adds a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> to the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrors">addVenueAsyncWithErrors</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueAsyncWithErrors-param-venueId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">venueId</span>, </span><span id="sdk-for-flutter-navigate-addVenueAsyncWithErrors-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads and adds a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> to the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrorsstr">addVenueAsyncWithErrorsStr</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueAsyncWithErrorsStr-param-venueIdentifier" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">venueIdentifier</span>, </span><span id="sdk-for-flutter-navigate-addVenueAsyncWithErrorsStr-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads and adds a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> to the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenueinfolistlistener">addVenueInfoListListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueInfoListListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueinfolistlistener-class">VenueInfoListListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a listener to handle the completion of the asynchronous venue info list retrieval.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenuelifecyclelistener">addVenueLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueLifecycleListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class">VenueLifecycleListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a venue lifecycle .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenuemaplifecyclelistener">addVenueMapLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueMapLifecycleListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-class">VenueMapLifecycleListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a venue map lifecycle .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-addvenueselectionlistener">addVenueSelectionListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueSelectionListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueselectionlistener-class">VenueSelectionListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a venue selection .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-cancelvenueselection">cancelVenueSelection</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Attempts to cancel venue loading and selection that may currently be in progress.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-getcrosswalk">getCrosswalk</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getCrosswalk-param-position" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">position</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-crosswalk-class">Crosswalk</a>?</span> </span>  
Tries to find a <a href="sdk-for-flutter-navigate-venue-data-crosswalk-class">Crosswalk</a> at the specified geographic coordinates in the selected <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> in the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-getgeometry">getGeometry</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getGeometry-param-position" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">position</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>?</span> </span>  
Tries to find a <a href="sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a> at the specified geographic coordinates in the selected <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> in the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-gettopology">getTopology</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getTopology-param-position" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">position</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-data-venuetopology-class">VenueTopology</a>?</span> </span>  
Tries to find a <a href="sdk-for-flutter-navigate-venue-data-venuetopology-class">VenueTopology</a> at the specified geographic coordinates in the selected <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> in the currently selected <a href="sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-getvenue">getVenue</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getVenue-param-position" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">position</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>?</span> </span>  
Tries to find a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> at the specified geographic coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolist">getVenueInfoList</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-control-venuemapvenueinfolist">VenueMapVenueInfoList</a></span> </span>  
The list of <a href="sdk-for-flutter-navigate-venue-data-venueinfo-class">VenueInfo</a> contains venue id and name.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolistasync">getVenueInfoListAsync</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
The list of <a href="sdk-for-flutter-navigate-venue-data-venueinfo-class">VenueInfo</a> contains venue id and name.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolistasyncwitherrors">getVenueInfoListAsyncWithErrors</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getVenueInfoListAsyncWithErrors-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
The list of <a href="sdk-for-flutter-navigate-venue-data-venueinfo-class">VenueInfo</a> contains venue id and name.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-getvenueinfolistwitherrors">getVenueInfoListWithErrors</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getVenueInfoListWithErrors-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-control-venuemapvenueinfolist">VenueMapVenueInfoList</a></span> </span>  
The list of <a href="sdk-for-flutter-navigate-venue-data-venueinfo-class">VenueInfo</a> contains venue id and name.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-removedrawingselectionlistener">removeDrawingSelectionListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeDrawingSelectionListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class">VenueDrawingSelectionListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a drawing selection .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-removelevelselectionlistener">removeLevelSelectionListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeLevelSelectionListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-class">VenueLevelSelectionListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a level selection .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-removevenue">removeVenue</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeVenue-param-venue" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></span> <span class="parameter-name">venue</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> from the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-removevenueinfolistlistener">removeVenueInfoListListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeVenueInfoListListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueinfolistlistener-class">VenueInfoListListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a listener for the asynchronous venue info list retrieval.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-removevenuelifecyclelistener">removeVenueLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeVenueLifecycleListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class">VenueLifecycleListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a venue lifecycle .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-removevenuemaplifecyclelistener">removeVenueMapLifecycleListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeVenueMapLifecycleListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-class">VenueMapLifecycleListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a venue map lifecycle .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-removevenueselectionlistener">removeVenueSelectionListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeVenueSelectionListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueselectionlistener-class">VenueSelectionListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a venue selection .

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasync">selectVenueAsync</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-selectVenueAsync-param-venueId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">venueId</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads a <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> if needed and selects a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncstr">selectVenueAsyncStr</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-selectVenueAsyncStr-param-venueIdentifier" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">venueIdentifier</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads a <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> if needed and selects a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrors">selectVenueAsyncWithErrors</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-selectVenueAsyncWithErrors-param-venueId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">venueId</span>, </span><span id="sdk-for-flutter-navigate-selectVenueAsyncWithErrors-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads a <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> if needed and selects a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrorsstr">selectVenueAsyncWithErrorsStr</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-selectVenueAsyncWithErrorsStr-param-venueIdentifier" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">venueIdentifier</span>, </span><span id="sdk-for-flutter-navigate-selectVenueAsyncWithErrorsStr-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Downloads a <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> if needed and selects a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-control-venuemap-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
