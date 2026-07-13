---
title: "VenueService class - venue.service library - Dart API"
slug: "sdk-for-flutter-navigate-venue.service-venueservice-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.service/venue.service-library-sidebar.html" data-below-sidebar="venue.service/VenueService-class-sidebar.html">

<div>

# <span class="kind-class">VenueService</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Offers methods to download venues.

Use of this object does not necessitate Map involvement.

Before loading the venues, initialize the venue service with one of the start methods.

The venue service is online only. Even if there is a cached venue on the device, the venue service requires an online connection to check if the venue is available for the user.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-venueservice">VenueService</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-language">language</a></span> <span class="signature">↔ String</span>  
The active language. The venue service will try to load a venue with a translation in the active language. If such translation doesn't exist, a venue will be loaded in its default language. Gets an active language in the venue service.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-languages">languages</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-venue-service-venueservicestringarray">VenueServiceStringArray</a></span>  
The languages available in the venue service. Gets the languages available in the venue service.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-addservicelistener">addServiceListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addServiceListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venueservicelistener-class">VenueServiceListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a service .

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-addvenuelistener">addVenueListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venuelistener-class">VenueListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a venue .

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-addvenuemaplistener">addVenueMapListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueMapListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venuemaplistener-class">VenueMapListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a venue map .

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-addvenuetoload">addVenueToLoad</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueToLoad-param-venueId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">venueId</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a venue to the loading queue.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-addvenuetoloadstr">addVenueToLoadStr</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addVenueToLoadStr-param-venueIdentifier" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">venueIdentifier</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a venue to the loading queue.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-getinitstatus">getInitStatus</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-venue-service-venueserviceinitstatus">VenueServiceInitStatus</a></span> </span>  
Gets an initialization status.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-isinitialized">isInitialized</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Checks if the venue service is initialized.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-loadoptionalfeatures">loadOptionalFeatures</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-loadOptionalFeatures-param-optionalFeatureList" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venueservicevenueoptionalfeaturelist">VenueServiceVenueOptionalFeatureList</a></span> <span class="parameter-name">optionalFeatureList</span></span>) <span class="returntype parameter">→ void</span> </span>  
Lets user load optional features for current session.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-loadtopologies">loadTopologies</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Lets user load topologies for current session

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-removeservicelistener">removeServiceListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeServiceListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venueservicelistener-class">VenueServiceListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a service .

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-removevenuelistener">removeVenueListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeVenueListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venuelistener-class">VenueListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a venue .

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-removevenuemaplistener">removeVenueMapListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeVenueMapListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-venue-service-venuemaplistener-class">VenueMapListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a venue map .

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-sethrn">setHrn</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setHrn-param-hrn" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">hrn</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets HRN of platform catalog.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-setlabeltextpreference">setLabeltextPreference</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setLabeltextPreference-param-labelTextPref" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">labelTextPref</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets override labelTextPreference for labels.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-stop">stop</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Stops the venue service.

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-service-venueservice-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

