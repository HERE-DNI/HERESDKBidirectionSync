---
title: "LaneAccess class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-laneaccess-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LaneAccess-class-sidebar.html">

<div>

# <span class="kind-class">LaneAccess</span> class

</div>

<div class="section desc markdown">

A class which identifies the vehicle type(s) allowed to access a lane.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-laneaccess">LaneAccess</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-automobiles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">automobiles</span>, </span><span id="sdk-for-flutter-navigate-param-buses" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">buses</span>, </span><span id="sdk-for-flutter-navigate-param-taxis" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">taxis</span>, </span><span id="sdk-for-flutter-navigate-param-carpools" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">carpools</span>, </span><span id="sdk-for-flutter-navigate-param-pedestrians" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">pedestrians</span>, </span><span id="sdk-for-flutter-navigate-param-trucks" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">trucks</span>, </span><span id="sdk-for-flutter-navigate-param-throughTraffic" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">throughTraffic</span>, </span><span id="sdk-for-flutter-navigate-param-deliveryVehicles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">deliveryVehicles</span>, </span><span id="sdk-for-flutter-navigate-param-emergencyVehicles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">emergencyVehicles</span>, </span><span id="sdk-for-flutter-navigate-param-motorcycles" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">motorcycles</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-automobiles">automobiles</a></span> <span class="signature">↔ bool</span>  
Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-buses">buses</a></span> <span class="signature">↔ bool</span>  
Buses that are used for public transportation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-carpools">carpools</a></span> <span class="signature">↔ bool</span>  
Represents the sharing of car journeys so that more than one person travels in a car, and prevents the need for others to have to drive to a location themselves.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-deliveryvehicles">deliveryVehicles</a></span> <span class="signature">↔ bool</span>  
Delivery <a href="sdk-for-flutter-navigate-navigation-laneaccess-trucks">LaneAccess.trucks</a> that are permitted to enter the city proper to unload goods at businesses.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-emergencyvehicles">emergencyVehicles</a></span> <span class="signature">↔ bool</span>  
Any vehicle that is designated and authorized to respond to an emergency in a life-threatening situation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-motorcycles">motorcycles</a></span> <span class="signature">↔ bool</span>  
Motorized two-wheeled passenger vehicles. Generally, mopeds are considered motorcycles.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-pedestrians">pedestrians</a></span> <span class="signature">↔ bool</span>  
Persons traveling on foot, whether walking or running.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-taxis">taxis</a></span> <span class="signature">↔ bool</span>  
Four-wheel vehicles that are usually fitted with a taximeter, that may be hired, along with their driver, to carry passengers to any specified destination.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-throughtraffic">throughTraffic</a></span> <span class="signature">↔ bool</span>  
Passenger vehicles (i.e., those defined as passenger car/automobiles) that are allowed to access roads that have traffic restrictions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-trucks">trucks</a></span> <span class="signature">↔ bool</span>  
Large vehicles that range from medium to heavy duty trucks.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

