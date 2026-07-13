---
title: "electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronic_horizon-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- electronic_horizon-library.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html">

<div>

# <span class="kind-library">electronic_horizon</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizon-class">ElectronicHorizon</a></span>  
A class containing the full set of available paths predicted for the current vehicle state.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a></span>  
Loads map data for segments that belong to the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a> paths.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderresult-class">ElectronicHorizonDataLoaderResult</a></span>  
Represents the result of a data loading operation performed by <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderstatuslistener-class">ElectronicHorizonDataLoaderStatusListener</a></span>  
Provides a listener for status updates from the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-loaddata">ElectronicHorizonDataLoader.loadData</a> method.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a></span>  
Provides an electronic horizon engine that continuously predicts the road network ahead of the vehicle by using detailed map data, including road topography that is currently out of sight.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a></span>  
Provides a listener for receiving updates during execution of the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-update">ElectronicHorizonEngine.update</a> method.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-class">ElectronicHorizonOptions</a></span>  
Provides options to configure <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a>.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-class">ElectronicHorizonPath</a></span>  
Represents a single electronic horizon path.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonposition-class">ElectronicHorizonPosition</a></span>  
Provides a position on an electronic horizon path with a reference to the current item in the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizon-class">ElectronicHorizon</a>.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonsegment-class">ElectronicHorizonSegment</a></span>  
Represents a segment in an <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-class">ElectronicHorizonPath</a>.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonsegmentchanges-class">ElectronicHorizonSegmentChanges</a></span>  
A class describing the set of changes in horizon segments between two consecutive updates.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonsegmentid-class">ElectronicHorizonSegmentId</a></span>  
Identifies a segment in an <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-class">ElectronicHorizonPath</a>.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a></span>  
A class representing a full update delivered via <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a> notifications.

## Enums

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a></span>  
Represents the status of data that was loaded by <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloadererrorcode">ElectronicHorizonDataLoaderErrorCode</a></span>  
Represents error codes that describe the result of the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-getsegment">ElectronicHorizonDataLoader.getSegment</a> method.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonerrorcode">ElectronicHorizonErrorCode</a></span>  
Represents error codes that describe the result of the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-update">ElectronicHorizonEngine.update</a> method.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
