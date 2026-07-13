---
title: "LaneType constructor - LaneType - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lanetype-lanetype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneType.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/LaneType-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LaneType</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LaneType</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-isRegular" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isRegular</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-isHighOccupancyVehicle" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isHighOccupancyVehicle</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-isReversible" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isReversible</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-isExpress" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isExpress</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-isAcceleration" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isAcceleration</span>, </span>
6.  <span id="sdk-for-flutter-navigate-param-isDeceleration" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isDeceleration</span>, </span>
7.  <span id="sdk-for-flutter-navigate-param-isAuxiliary" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isAuxiliary</span>, </span>
8.  <span id="sdk-for-flutter-navigate-param-isSlow" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isSlow</span>, </span>
9.  <span id="sdk-for-flutter-navigate-param-isPassing" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isPassing</span>, </span>
10. <span id="sdk-for-flutter-navigate-param-isShoulder" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isShoulder</span>, </span>
11. <span id="sdk-for-flutter-navigate-param-isRegulatedAccess" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isRegulatedAccess</span>, </span>
12. <span id="sdk-for-flutter-navigate-param-isTurn" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isTurn</span>, </span>
13. <span id="sdk-for-flutter-navigate-param-isCenterTurn" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isCenterTurn</span>, </span>
14. <span id="sdk-for-flutter-navigate-param-isTruckParking" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isTruckParking</span>, </span>
15. <span id="sdk-for-flutter-navigate-param-isParking" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isParking</span>, </span>
16. <span id="sdk-for-flutter-navigate-param-isVariableDriving" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isVariableDriving</span>, </span>
17. <span id="sdk-for-flutter-navigate-param-isBicycle" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isBicycle</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `isRegular` Regular lane is a lane that does not have a specific use.
- `isHighOccupancyVehicle` A lane which is restricted for high occupancy vehicles. Note: High occupancy vehicles are vehicles with a driver and one or more passengers.
- `isReversible` A lane in which traffic may travel in either direction, depending on certain conditions such as the time of the day to improve traffic flow during rush hours.
- `isExpress` Express lane is a lane or set of lanes usually physically separated from the major roadway with limited entry and exit points to quickly move traffic in and out of a major metropolitan city. An express lane can be reversible, bidirectional, or one-way.
- `isAcceleration` An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle increase its speed to where it can safely merge with ongoing traffic. These lanes can be accessed from ramps, rest areas, or weigh stations.
- `isDeceleration` A deceleration lane is the same as an acceleration lane but used for the opposite scenario.
- `isAuxiliary` An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next interchange.
- `isSlow` A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.
- `isPassing` A passing lane is a lane that can occur on steep mountain grades or other roads where overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass slow moving vehicles.
- `isShoulder` A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is not generally used for driving, although it is possible under certain circumstances.
- `isRegulatedAccess` A regulated lane access is a lane designated as a holding zone, used to regulate traffic using time intervals. Regulated lane access is only coded for truck holding zones that are used to regulate truck access into tunnels and over bridges using time intervals (e.g., some tunnel accesses in Switzerland).
- `isTurn` Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing traffic.
- `isCenterTurn` Center turn lane is a bidirectional turn lane located in the middle of a road that allows traffic in both directions to turn left (right for left side driving countries).
- `isTruckParking` Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for emergency.
- `isParking` Parking lanes are portions of the road bed that may be used for parking legally. They may allow vehicles to use them as driving lanes at times, though.
- `isVariableDriving` Variable driving lanes are lanes added to a road that open and close to accommodate traffic volume and flow using variable indicators.
- `isBicycle` Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by lane markings, signs, buffers or barriers.

</div>

## Implementation

``` dart
LaneType(this.isRegular, this.isHighOccupancyVehicle, this.isReversible, this.isExpress, this.isAcceleration, this.isDeceleration, this.isAuxiliary, this.isSlow, this.isPassing, this.isShoulder, this.isRegulatedAccess, this.isTurn, this.isCenterTurn, this.isTruckParking, this.isParking, this.isVariableDriving, this.isBicycle);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
