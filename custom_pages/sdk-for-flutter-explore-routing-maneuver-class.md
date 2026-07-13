---
title: "Maneuver class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-maneuver-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Maneuver-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Maneuver-class-sidebar.html">

<div>

# <span class="kind-class">Maneuver</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This class provides all the information for a maneuver.

The directional information (e.g. road names, road numbers and signpost direction) is stored in <a href="sdk-for-flutter-explore-routing-maneuver-roadtexts">Maneuver.roadTexts</a> and <a href="sdk-for-flutter-explore-routing-maneuver-nextroadtexts">Maneuver.nextRoadTexts</a> attributes. As for the motorway exit information, it can be obtained from <a href="sdk-for-flutter-explore-routing-maneuver-exitsigntexts">Maneuver.exitSignTexts</a> attribute.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-maneuver">Maneuver</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-action">action</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Indicates the maneuver action. Gets the maneuver action.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-coordinates">coordinates</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>  
Geographic coordinates where the maneuver is located. Gets the geographic coordinates where the maneuver is located.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-countrycode">countryCode</a></span> <span class="signature">→ String?</span>  
The country code of the maneuver position. The value is `null` when no data is available. Gets the country code of the maneuver position. The value is `null` when no data is available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-duration">duration</a></span> <span class="signature">→ Duration</span>  
The estimated time in seconds needed to perform the maneuver. Gets the estimated time in seconds needed to perform the maneuver.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-exitsigntexts">exitSignTexts</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-localizedtexts-class">LocalizedTexts</a></span>  
The textual attributes of the exit sign. These might contain exit number(s) and/or name(s). These attributes are only available for the Navigate license. Otherwise, the attributes are always empty. Gets the textual attributes of the exit sign. These might contain exit number(s) and/or name(s).

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-intersectionnames">intersectionNames</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-localizedtexts-class">LocalizedTexts</a></span>  
The textual attributes of the intersection. These attributes are only available for the Navigate license. Otherwise, the attributes are always empty. **Note:** Routes calculated with OfflineRoutingEngine are not supported. Gets the textual attributes of the intersection.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-lengthinmeters">lengthInMeters</a></span> <span class="signature">→ int</span>  
The length of the maneuver in meters. Gets the length of the maneuver in meters.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-nextroadtexts">nextRoadTexts</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-roadtexts-class">RoadTexts</a></span>  
The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point. These attributes are only available for the Navigate license. Otherwise, the attributes are always empty. Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-offset">offset</a></span> <span class="signature">→ int</span>  
Index over <a href="sdk-for-flutter-explore-routing-section-geometry">Section.geometry</a> where the maneuver is located. Gets the index over <a href="sdk-for-flutter-explore-routing-section-geometry">Section.geometry</a> where the maneuver is located.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-roadtexts">roadTexts</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-roadtexts-class">RoadTexts</a></span>  
The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information. **Note:** These attributes are only available for the Navigate license. Otherwise, the attributes are always empty. Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-roundaboutangleindegrees">roundaboutAngleInDegrees</a></span> <span class="signature">→ double?</span>  
The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout. This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive in right-hand side driving country, and negative in left-hand side countries. Note that the value is available for both the enter roundabout actions and the exit roundabout actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the roundabout itself is not representing a perfect circle, then the accuracy of the angle may be compromised. **Note:** These attributes are only available for the Navigate license. The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-sectionindex">sectionIndex</a></span> <span class="signature">→ int</span>  
Index over <a href="sdk-for-flutter-explore-routing-route-sections">Route.sections</a> indicating the section to which the maneuver belongs to. Gets the index over <a href="sdk-for-flutter-explore-routing-route-sections">Route.sections</a> indicating the section to which the maneuver belongs to.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-signpost">signpost</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-signpost-class">Signpost</a>?</span>  
Gets the <a href="sdk-for-flutter-explore-routing-signpost-class">Signpost</a> object. Gets <a href="sdk-for-flutter-explore-routing-signpost-class">Signpost</a> object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-spanindex">spanIndex</a></span> <span class="signature">→ int</span>  
Index over <a href="sdk-for-flutter-explore-routing-section-spans">Section.spans</a> indicating the first span after the maneuver point. **Note:** The span index for the last maneuvers (those maneuvers with maneuver action set to <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction.arrive</a>) cannot be used, since these maneuvers are placed after the last span of the route and the span index for them would be greater than the span list size. Gets the index over <a href="sdk-for-flutter-explore-routing-section-spans">Section.spans</a> indicating the first span after the maneuver point.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-text">text</a></span> <span class="signature">→ String</span>  
The maneuver instruction. The text is formatted and localized as specified via <a href="sdk-for-flutter-explore-routing-routetextoptions-class">RouteTextOptions</a>. **Note for users of the Navigate license:** This text is meant to be displayed in a preview context, whereas real-time `EventTextListener` texts are meant to be used for spoken voice announcements during a trip. Gets the maneuver instruction. The text is formatted and localized as specified via <a href="sdk-for-flutter-explore-routing-routetextoptions-class">RouteTextOptions</a>.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-turnangleindegrees">turnAngleInDegrees</a></span> <span class="signature">→ double?</span>  
The angle of the turn component of the maneuver. The angle increases clockwise and small values are used for going straight, i.e. a positive number means there is a right turn and a negative number is a left turn. Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value is omitted. **Note:** These attributes are only available for the Navigate license. Gets the angle of the turn component of the maneuver. The value is in degrees and from -180 to 180.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuver-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
