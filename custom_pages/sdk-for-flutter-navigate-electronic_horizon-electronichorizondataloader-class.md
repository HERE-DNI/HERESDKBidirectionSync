---
title: "ElectronicHorizonDataLoader class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonDataLoader-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonDataLoader-class-sidebar.html">

<div>

# <span class="kind-class">ElectronicHorizonDataLoader</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Loads map data for segments that belong to the <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a> paths.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

Offline availability: This property is available online and offline.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-electronichorizondataloader">ElectronicHorizonDataLoader</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-param-segmentDataCacheSize" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">segmentDataCacheSize</span></span>)</span>  
Creates a new instance of <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-addelectronichorizondataloaderstatuslistener">addElectronicHorizonDataLoaderStatusListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addElectronicHorizonDataLoaderStatusListener-param-electronicHorizonListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderstatuslistener-class">ElectronicHorizonDataLoaderStatusListener</a></span> <span class="parameter-name">electronicHorizonListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds an <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderstatuslistener-class">ElectronicHorizonDataLoaderStatusListener</a> to the subscription list.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-getsegment">getSegment</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getSegment-param-segmentId" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class">DirectedOCMSegmentId</a></span> <span class="parameter-name">segmentId</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderresult-class">ElectronicHorizonDataLoaderResult</a></span> </span>  
Returns loaded data for the given segment identifier.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-loaddata">loadData</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-loadData-param-electronicHorizonUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a></span> <span class="parameter-name">electronicHorizonUpdate</span></span>) <span class="returntype parameter">→ void</span> </span>  
Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-removeelectronichorizondataloaderstatuslistener">removeElectronicHorizonDataLoaderStatusListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeElectronicHorizonDataLoaderStatusListener-param-electronicHorizonListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderstatuslistener-class">ElectronicHorizonDataLoaderStatusListener</a></span> <span class="parameter-name">electronicHorizonListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes an <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloaderstatuslistener-class">ElectronicHorizonDataLoaderStatusListener</a> from the subscription list.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizondataloader-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
