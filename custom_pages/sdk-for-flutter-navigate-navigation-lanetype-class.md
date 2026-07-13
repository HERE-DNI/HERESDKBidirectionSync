---
title: "LaneType class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lanetype-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LaneType-class-sidebar.html">

<div>

# <span class="kind-class">LaneType</span> class

</div>

<div class="section desc markdown">

A class that provides information on the available lane properties.

The lane type values can be combined as follows:

- High Occupancy Vehicle, Reversible
- High Occupancy Vehicle and Express
- Reversible and Express
- High Occupancy Vehicle, Reversible and Express
- High Occupancy Vehicle and Acceleration
- Reversible, Acceleration Lane
- High Occupancy Vehicle, Reversible, Acceleration Lane
- Express and Acceleration
- High Occupancy Vehicle and Deceleration
- Reversible, Deceleration Lane
- High Occupancy Vehicle, Reversible, Deceleration Lane
- Express and Deceleration

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-lanetype">LaneType</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-isRegular" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isRegular</span>, </span><span id="sdk-for-flutter-navigate-param-isHighOccupancyVehicle" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isHighOccupancyVehicle</span>, </span><span id="sdk-for-flutter-navigate-param-isReversible" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isReversible</span>, </span><span id="sdk-for-flutter-navigate-param-isExpress" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isExpress</span>, </span><span id="sdk-for-flutter-navigate-param-isAcceleration" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isAcceleration</span>, </span><span id="sdk-for-flutter-navigate-param-isDeceleration" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isDeceleration</span>, </span><span id="sdk-for-flutter-navigate-param-isAuxiliary" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isAuxiliary</span>, </span><span id="sdk-for-flutter-navigate-param-isSlow" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isSlow</span>, </span><span id="sdk-for-flutter-navigate-param-isPassing" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isPassing</span>, </span><span id="sdk-for-flutter-navigate-param-isShoulder" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isShoulder</span>, </span><span id="sdk-for-flutter-navigate-param-isRegulatedAccess" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isRegulatedAccess</span>, </span><span id="sdk-for-flutter-navigate-param-isTurn" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isTurn</span>, </span><span id="sdk-for-flutter-navigate-param-isCenterTurn" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isCenterTurn</span>, </span><span id="sdk-for-flutter-navigate-param-isTruckParking" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isTruckParking</span>, </span><span id="sdk-for-flutter-navigate-param-isParking" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isParking</span>, </span><span id="sdk-for-flutter-navigate-param-isVariableDriving" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isVariableDriving</span>, </span><span id="sdk-for-flutter-navigate-param-isBicycle" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isBicycle</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isacceleration">isAcceleration</a></span> <span class="signature">↔ bool</span>  
An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle increase its speed to where it can safely merge with ongoing traffic. These lanes can be accessed from ramps, rest areas, or weigh stations.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isauxiliary">isAuxiliary</a></span> <span class="signature">↔ bool</span>  
An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next interchange.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isbicycle">isBicycle</a></span> <span class="signature">↔ bool</span>  
Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by lane markings, signs, buffers or barriers.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-iscenterturn">isCenterTurn</a></span> <span class="signature">↔ bool</span>  
Center turn lane is a bidirectional turn lane located in the middle of a road that allows traffic in both directions to turn left (right for left side driving countries).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isdeceleration">isDeceleration</a></span> <span class="signature">↔ bool</span>  
A deceleration lane is the same as an acceleration lane but used for the opposite scenario.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isexpress">isExpress</a></span> <span class="signature">↔ bool</span>  
Express lane is a lane or set of lanes usually physically separated from the major roadway with limited entry and exit points to quickly move traffic in and out of a major metropolitan city. An express lane can be reversible, bidirectional, or one-way.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-ishighoccupancyvehicle">isHighOccupancyVehicle</a></span> <span class="signature">↔ bool</span>  
A lane which is restricted for high occupancy vehicles. Note: High occupancy vehicles are vehicles with a driver and one or more passengers.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isparking">isParking</a></span> <span class="signature">↔ bool</span>  
Parking lanes are portions of the road bed that may be used for parking legally. They may allow vehicles to use them as driving lanes at times, though.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-ispassing">isPassing</a></span> <span class="signature">↔ bool</span>  
A passing lane is a lane that can occur on steep mountain grades or other roads where overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass slow moving vehicles.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isregular">isRegular</a></span> <span class="signature">↔ bool</span>  
Regular lane is a lane that does not have a specific use.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isregulatedaccess">isRegulatedAccess</a></span> <span class="signature">↔ bool</span>  
A regulated lane access is a lane designated as a holding zone, used to regulate traffic using time intervals. Regulated lane access is only coded for truck holding zones that are used to regulate truck access into tunnels and over bridges using time intervals (e.g., some tunnel accesses in Switzerland).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isreversible">isReversible</a></span> <span class="signature">↔ bool</span>  
A lane in which traffic may travel in either direction, depending on certain conditions such as the time of the day to improve traffic flow during rush hours.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isshoulder">isShoulder</a></span> <span class="signature">↔ bool</span>  
A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is not generally used for driving, although it is possible under certain circumstances.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isslow">isSlow</a></span> <span class="signature">↔ bool</span>  
A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-istruckparking">isTruckParking</a></span> <span class="signature">↔ bool</span>  
Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for emergency.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isturn">isTurn</a></span> <span class="signature">↔ bool</span>  
Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-isvariabledriving">isVariableDriving</a></span> <span class="signature">↔ bool</span>  
Variable driving lanes are lanes added to a road that open and close to accommodate traffic volume and flow using variable indicators.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

