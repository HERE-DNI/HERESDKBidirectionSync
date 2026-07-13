---
title: "VenueEngine class - venue library - Dart API"
slug: "sdk-for-flutter-navigate-venue-venueengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue/venue-library-sidebar.html" data-below-sidebar="venue/VenueEngine-class-sidebar.html">

<div>

# <span class="kind-class">VenueEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

VenueEngine is an add-on to the base map functionality with its own content loading and cache.

VenueEngine gives access to the venue functionality, which allows you to load and visualize venues on the map, search content inside venues etc.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-venueengine">VenueEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-venueengineinitcallback">VenueEngineInitCallback</a>?</span> <span class="parameter-name">callback</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-venueengine-withsdkengine">VenueEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-withSdkEngine-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-venueengineinitcallback">VenueEngineInitCallback</a>?</span> <span class="parameter-name">callback</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-venuemap">venueMap</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a></span>  
The venue map. Gets a venue map to visualize venues and control the state of the venues on the map. You need to start the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a> to be able to load venues. Gets a venue map to visualize venues.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-venueservice">venueService</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a></span>  
The venue service. Gets the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>. This service can be used to load the <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> objects. Gets the venue service. This service can be used to load the venue model objects.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-destroy">destroy</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Releases all internally used resources.

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-start">start</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-start-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-authenticationcallback">AuthenticationCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Authenticates asynchronously using HERE SDK credentials and uses a result token to start the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-startwithtoken">startWithToken</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startWithToken-param-token" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">token</span></span>) <span class="returntype parameter">→ void</span> </span>  
Authenticates asynchronously using HERE SDK credentials using a token to start the <a href="sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-venueengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
